from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import Users, Session, Schedule, ServicesToShedule, Services, SheduleStatus, UserToServices

# =========== МАСТЕР =========
# Создание свободного времени для записи
class TransferTimeView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            time = request.data['time']
            dateLocal = request.data['dateLocal']
            month = request.data['month']
            year = request.data['year']
            arrIdServices = request.data['arrIdServices']
            
            

            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Если статус не клинта
            if user.status.status_name != 'client':
                # Создаем запись в расписании
                entry = Schedule.objects.create(
                    master = user,
                    year = year,
                    month = month,
                    date = dateLocal,
                    time = time,
                    status = SheduleStatus.objects.get(id=1)
                )

                # Проходимся по присланному массиву
                for el in arrIdServices:

                    # Достаем услугу 
                    service = Services.objects.get(id=int(el))

                    # Создаем запись в таблице отношений расписания к услугам
                    ServicesToShedule.objects.create(
                        shedule = entry,
                        service = service
                    )
                    
           
            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Получаем данные из расписания за указанную дату
class GetDataDateView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            dateLocal = request.data['dateLocal']
            month = request.data['month']
            year = request.data['year']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Ищем все записи мастера за указаную дату
            arrEntries = Schedule.objects.filter(
                master=user,
                year=year,
                month = month,
                date=dateLocal
            ).values()
            
            # Проходимся по массиву который получили
            for el in arrEntries:

                # ПОЛУЧЕНИЕ СТАТУСА
                # Ищем название статуса по его id
                statusTitle = SheduleStatus.objects.get(id=el['status_id']).title
                
                # Указывае статус записи
                el['statys'] = statusTitle


                # ЕСЛИ ЗАПИСЬ СВОБОДНА
                if el['client_id'] == None:
                    
                    # ИЩЕМ ВОЗМОЖНЫЕ УСЛУГИ
                    # Массив будет хранить указанные услуги
                    el['arrSrvices'] = []
                    # Получаем указанные услуги
                    arrIdSelectServ = ServicesToShedule.objects.filter(
                        shedule = el['id']
                    ).values('service_id')
                    # Перебираем полученый массив
                    for n in arrIdSelectServ:
                        # Вытаскиваем данные
                        serviceId = n['service_id']
                        serviceTitle = Services.objects.get(id=n['service_id']).title
                        servicePrice = UserToServices.objects.get(service=n['service_id'],user=user).price
                        # Добавляем данные в массив
                        el['arrSrvices'].append({'id':serviceId,'title':serviceTitle,'price':servicePrice,})

            
                
                # ЕСЛИ ЗАПИСЬ ЗАНЯТА
                if el['client_id'] != None:

                    # ИЩЕМ ИНФУ ОБ УСЛУГЕ
                    # Название услуги
                    serviceName = Services.objects.get(id=el['service_id']).title
                    # Цена услуги
                    servicePrice = UserToServices.objects.get(service=el['service_id'], user=user).price
                    # Добавляем информацию к услуге
                    el['service']={'title': serviceName,"price" : servicePrice}

                    # ИЩЕМ ИНФУ О КЛИЕНТЕ
                    # Ищем клиента
                    client = Users.objects.get(id=el['client_id'])
                    # Вытаскиваем данные
                    name = client.name
                    lastName = client.lastName
                    phone = client.phone
                    # Добавляем информацию в основной массив
                    el['client'] = {'name': name, 'lastName': lastName,'phone': phone,}

                # Удаляем ненужные данные
                del el['master_id']
                del el['client_id']
                del el['year']
                del el['month']
                del el['date']
                del el['service_id']
                del el['status_id']

                
            

            # Возвращаем данные
            return Response({'data' : arrEntries})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Удаляем данные из расписания за указанную дату
class DelDataDateView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            id = request.data['id']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Ищем запись
            data = Schedule.objects.get(id=id)

            # Если запросил этот мастер или админ или бос
            if data.master == user or user.status.status_name == 'admin' or user.status.status_name == 'boss' :

                # Удаляем запись
                data.delete()
                
            
            return Response({})
           
            

        # Если возникнет непредвиденая ошибка
        except:
            print('error')
            return Response({'textError' : 'unknown error'})


#=============== КЛИЕНТ ================


# Получаем данные из расписания за указанную дату
class GetDataDateClientView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            dateLocal = request.data['dateLocal']
            month = request.data['month']
            year = request.data['year']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Запрашиваем все записи за указанную дату
            data = Schedule.objects.filter(
                year = year,
                month = month, 
                date = dateLocal
            ).values()

            # Запускаем цикл для нахождения и указания мастера
            for obj in data:
                # Добавляем в объект новое значение. Ищем в базе мастера по id
                obj['master'] = Users.objects.get(id=obj['master_id']).name + ' ' + Users.objects.get(id=obj['master_id']).lastName
            
            
            # Возвращаем данные
            return Response({'data' : list(data)})

        # Если возникнет непредвиденая ошибка
        except:
            print('error')
            return Response({'textError' : 'unknown error'})
        

# Бронируем расписание
class SendToBookView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            id = request.data['id']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Ищем запись
            data = Schedule.objects.get(id=id)
            
            # Меняем запись. Указываем клиента
            data.client = user
            data.save()

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except:
            print('error')
            return Response({'textError' : 'unknown error'})


# Отменить запись
class SendCancelBookView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            id = request.data['id']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Ищем запись
            data = Schedule.objects.get(id=id)
            
            # Меняем запись. Указываем клиента
            data.client = None
            data.save()

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})













