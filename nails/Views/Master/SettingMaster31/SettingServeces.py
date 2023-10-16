from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, Specializations, UserToSpecialization, UserToServices, Services


# Получить данные для настройки услуг
class GetDataForSettingSerecesView(APIView):
# 1 найти специализации которые выбрал пользователь
# 2 найти услуги каждой специализации которые выбрал пользователь
# 3 найти все услуги каждой специализации и исключить из них выбранные
# 4 вернуть все одним массивом

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            # Будет хранить конечные данные
            arrData = []
            # Ищем пользователя
            master = Session.objects.get(sid=sid).user
            # Ищем специализации которые выбрал пользователь
            arrSpec = UserToSpecialization.objects.filter(user=master).values()
            # Перебираем полученные массив
            for el in arrSpec:
                
                # id специализации
                specId = el['specialization_id']
                specTitle = Specializations.objects.get(id=el['specialization_id']).title
                # Выбранные услуги
                arrSelectServeces = []
                # Доступные для выбора услуги
                arrAvailabelServeces = []

                # Получаем массив выбранных услуг
                arrSelectServecesSPEC = UserToServices.objects.filter(user=master, specialization=el['specialization_id']).values()
                # Перебираем этот массив
                for n in arrSelectServecesSPEC:

                    # Достаем данные
                    userToServID = n['id']
                    service_id = n['service_id']
                    price = n['price']
                    service_title = Services.objects.get(id=n['service_id']).title
                    # Формируем объект и добавляем в массив
                    arrSelectServeces.append({'id':userToServID,'service_id':service_id,'price':price,'service_title':service_title,})
                    
                # Получаем все возможные для специализации услуги
                arrAllServices = Services.objects.filter(specialization=el['specialization_id']).values()
                # Перебираем их
                for n in arrAllServices:
                    # Флаг попадет ли услуга в массив
                    flag = True
                    # Перебираем массив уже выбранных услуг
                    for a in arrSelectServeces:
                        # Если услуга уже выбрана
                        if n['id'] == a['service_id']:
                            flag = False
                            break
                    
                    # Если продолжение не одобренно
                    if flag == False:
                        continue

                    arrAvailabelServeces.append(n)
                    
                #print(arrAvailabelServeces)


                # Формируем объект и добавляем в массив
                arrData.append({
                    'id':specId,
                    'title': specTitle,
                    'arrSelectServeces':arrSelectServeces,
                    'arrAvailabelServeces':arrAvailabelServeces
                })

            # Возвращаем данные
            return Response({'data' : arrData})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Добавить в список выбранных
class MasterAddServecesView(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            id = request.data['id']
            price = request.data['price']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name != 'client':
                
                # Достаем услугу из базы
                servece = Services.objects.filter(id=id).values()
                # Получаем специализацию
                specializations = Specializations.objects.get(id=servece[0]['specialization_id'])
                
                # Создаем новую запись в базе выбранных услуг
                UserToServices.objects.create(
                    user=user,
                    specialization = specializations,
                    service = Services.objects.get(id=id),
                    price=price
                )
                #print(servece[0]['specialization_id'])


            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Удалить из списка выбранных
class MasterDelServecesView(APIView):

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

            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name != 'client':
                
                # Ищем запись по id
                masterServece = UserToServices.objects.get(id=id)
                # Удаляем
                masterServece.delete()

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})







