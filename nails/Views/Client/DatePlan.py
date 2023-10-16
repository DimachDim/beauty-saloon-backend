from django.shortcuts import render 
import os
import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, SheduleStatus, Schedule, Services, ServicesToShedule, Users, UserToServices, SheduleStatus


# Получить данные о специализациях и их услугах
class GetDataDateClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            year = request.data['year']
            month = request.data['month']
            date = request.data['date']
            idServece = request.data['id']
            sid = request.data['SID']
            
            # Будет хранить конечные данные
            arrData = []
            
            # Ищем услугу в отношении записи в раскиании к возможным услугам
            arrServToSched = ServicesToShedule.objects.filter(service=idServece).values('shedule_id')
            
            # Ищем все записи в расписании на дату
            arrSchedule = Schedule.objects.filter(year=year,month=month,date=date).values()
            
            
            
            # Перебираем полученный массив
            for el in arrSchedule:
                
                # =================== Проверка на включение услуги в окно ===============
                flagLeave = False       #Если истина то итерация продолжится

                # Перебираем массив отношений услуг к расписанию
                for n in arrServToSched:
                    
                    # Если id есть в массиве
                    if el['id'] == n['shedule_id']:
                        # Переключаем флаг и выходим из массива
                        flagLeave = True
                        break

                # Если нет команды на выход
                if flagLeave == False:
                    continue
                # =================== Проверка на включение услуги в окно end ===========

                # Id
                idSchedule = el['id']
                # Время 
                time = el['time']
                # Статус
                status = SheduleStatus.objects.get(id=el['status_id']).title
                # id записанного клиента
                client = None
                # Услуга
                serviceObj = {'id': idServece, 'title': None,'price': None}
                # Мастер
                masterObj = {'id': None,'name':None,'lastName':None,'phone':None,}

                # Вытаскиваем данные о мастере
                master = Users.objects.get(id=el['master_id'])
                masterObj['id'] = el['master_id']
                masterObj['name']=master.name
                masterObj['lastName']=master.lastName
                masterObj['phone']=master.phone
                
                # Вытаскиваем услугу
                service = Services.objects.get(id=idServece)
                # Заполняем нужные поля
                serviceObj['title']=service.title
                serviceObj['price']=UserToServices.objects.get(service=service, user=master).price
                
                # ЕСЛИ окно занято
                if el['client_id'] != None:
                    # Смотрим кто запрашивал информацию
                    user = Session.objects.get(sid=sid).user
                    # Если id того кто запросил информацию равен id в записи
                    if el['client_id'] == user.id:
                        # Говорим что он забронировал
                        client = 'you'
                    else:
                        client = 'not you'

                    
                            
                # Добавляем собранные данные в массив
                arrData.append({
                    'idSchedule':idSchedule,
                    'time':time,
                    'status':status,
                    'service':serviceObj,
                    'master':masterObj,
                    'client':client
                })

            

            # Возвращаем данные
            return Response({'data' : arrData})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Получить все окна мастера за указанную дату
class GetMasterDataDateClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            idMaster = request.data['id']
            year = request.data['year']
            month = request.data['month']
            date = request.data['date']
            sid = request.data['SID']
            
            user = Session.objects.get(sid=sid).user        # Пользователь который делает запрос
            master = Users.objects.get(id=idMaster)         # Мастер
            arrData = []                                    # Конечный массив с инф

            # Записи на указанную дату
            arrSchedules = Schedule.objects.filter(year=year, month=month,date=date,master=master).values()
            # Перебираем полученый массив
            for el in arrSchedules:
                id = el['id']
                time = el['time']
                status = SheduleStatus.objects.get(id=1).title
                selectService = None
                whoRegistred = None
                arrServices = []

                # Если ктото назначен
                if el['client_id'] != None:
                    # Ставим статус
                    status = SheduleStatus.objects.get(id=2).title
                    # Если клиент вы
                    if el['client_id'] == user.id:
                        # Указываем что записаны вы
                        whoRegistred = 'you'
                    else:
                        whoRegistred = 'not you'
                    # Ищем назначенную услугу
                    serviceid = el['service_id']
                    serviceTitle = Services.objects.get(id=serviceid).title
                    servicePrice = UserToServices.objects.get(user=master, service=serviceid).price
                    # Передаем данные
                    selectService = {'id':serviceid, 'title':serviceTitle, 'price': servicePrice}

                # Если никто не назначен
                else:
                    # Ищем возможные услуги
                    arrServicesSpec = ServicesToShedule.objects.filter(shedule=el['id']).values()
                    # Перебираем полученный массив
                    for n in arrServicesSpec:
                        servId = n['service_id']
                        servTitle = Services.objects.get(id=servId).title
                        servPrice = UserToServices.objects.get(user=master, service=servId).price
                        # Формируем объект и добавляе в подготовленный массив
                        arrServices.append({'id':servId,'title':servTitle,'price':servPrice})
                
                # Формируем объект и добавляем в конечный массив
                arrData.append({
                    'idSchedule': id,
                    'time': time,
                    'status':status,
                    'whoRegistred':whoRegistred,
                    'selectService':selectService,
                    'master':{
                        'id':master.id, 'name':master.name, 'lastName': master.lastName, 'phone':master.phone
                    },
                    'arrServices': arrServices
                })

                
            # Возвращаем данные
            return Response({'data' : arrData})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Записаться на прием 
class AppointmentClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            idSchedule = request.data['idSchedule']
            idService = request.data['idService']
            sid = request.data['SID']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user
            # Запись в расписании
            schedule = Schedule.objects.get(id=idSchedule)
            # Услуга
            service = Services.objects.get(id=idService)

            # Меняем запись в расписании
            schedule.client = user
            schedule.service = service
            schedule.status = SheduleStatus.objects.get(id=2)
            schedule.save()
            

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Отменить записаться на прием
class CancelAppointmentClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            idSchedule = request.data['idSchedule']
            sid = request.data['SID']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user
            # Запись в расписании
            schedule = Schedule.objects.get(id=idSchedule)


            # Меняем запись в расписании
            schedule.client = None
            schedule.service = None
            schedule.status = SheduleStatus.objects.get(id=1)
            schedule.save()
            

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


