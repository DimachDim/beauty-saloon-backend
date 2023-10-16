from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, Specializations, Services, UserToSpecialization


# Получить все специализации и услуги
class GetServicesView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name != 'client':
                
                # Получаем из базы все специализации
                dataSpec = Specializations.objects.all().values()

                # Получаем из базы все услуги
                dataService = Services.objects.all().values()

                
                                

            # Возвращаем данные
            return Response({'dataSpec' : dataSpec, 'dataService': dataService })

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Создать услугу
class AddServiceView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            id = request.data['id']
            title = request.data['title']
            
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name == 'admin' or user.status.status_name == 'boss':
                
                # По id получаем специализацию
                spec = Specializations.objects.get(id=id)

                
                # Добавляем в базу услуг новоую запись
                Services.objects.create(
                    specialization = spec,
                    title = title
                )
                               
                                

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Удалить услугу
class DelServiceView(APIView):
    
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
            if user.status.status_name == 'admin' or user.status.status_name == 'boss':
                                              
                # Ищим и удаляем запись
                Services.objects.get(id=id).delete()                

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})




# ========== ДЛЯ МАСТЕРА ============
# Запрос всех услуг относящихся к указанной специализации
class GetSservicesForSpecView(APIView):
    
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
                
                # Ищем в базе все услуги для этой специализации
                services = Services.objects.filter(specialization=id).values()
                               
                                

            # Возвращаем данные
            return Response({'data' : services})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


