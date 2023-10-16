from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, Specializations, Schedule, Services, ServicesToShedule


# Получить данные о специализациях и их услугах
class GetDataServicesClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user
            
            # Вытаскиваем все специализации
            arrSpecializations = Specializations.objects.all().values()
            # Перебираем полученый массив
            for el in arrSpecializations:

                # Достаем все услуги этой специализации
                arrServices = Services.objects.filter(specialization=el['id']).values()
                # Передаем данные главному массиву
                el['arrServices'] = arrServices

           

            # Возвращаем данные
            return Response({'data' : arrSpecializations})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Отправляем id выбранной услуги
class SendIdServeceClient(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            id = request.data

            # Массив будет хранить информацию с свободными датами
            arrDates = []
            
            # Находим записи в таблице отношения услуг к записи
            arrEntriesService = ServicesToShedule.objects.filter(service=id).values('shedule')

            # Перебираем полученый массив 
            for el in arrEntriesService:

                # Ищем запись по id
                entry = Schedule.objects.get(id=el['shedule'])
                # Формируем дату и добавляем ее в массив
                arrDates.append({
                    'year': entry.year,
                    'month': entry.month,
                    'date': entry.date
                })
                
            
                      
            # Возвращаем данные
            return Response({'data' : arrDates})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})




