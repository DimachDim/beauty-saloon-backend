from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, Specializations, UserToSpecialization, UserToServices, Services


# Получить все специализации
class GetSpecializationView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            print(sid)
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user
            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name != 'client':
                
                # Получаем из базы все специализации
                data = Specializations.objects.all().values()
                                

            # Возвращаем данные
            return Response({'data' : data})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Добавить специализацию
class AddSpecializationView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            name = request.data['value']
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Проверяем. Пользователь должен быть админ или босс
            if user.status.status_name == 'admin' or user.status.status_name == 'boss':

                # Создаем запись в базе специализаций
                Specializations.objects.create(
                    title = name
                )

                

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Удалить специализацию
class DelSpecializationView(APIView):
    
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

                # Находим специализацию и удаляем
                Specializations.objects.get(id=id).delete()               
                

            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# ============= ДЛЯ МАСТЕРА ==============
# -----------Компанента 'Настройки специализации'---------------- 

# Получить специализации для мастера
class GetSpecializationMasterView(APIView):
    
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
            if user.status.status_name != 'client' :
                
                # Получаем из базы все специализации
                specAll = Specializations.objects.all().values()
                
                # Получаем все специализации которые выбрал пользователь
                specUser = UserToSpecialization.objects.filter(user=user).values()

                # Поеребираем массив всех специализаций
                for el in specAll:

                    # Перебираем массив специализаций пользователя
                    for il in specUser:

                        # Если id специализации совпадает с id спкц. мастера
                        if el['id'] == il['specialization_id']:
                            # Отмечаем что эта специализация выбрана
                           el['flag'] = True
                        
                
            # Возвращаем данные
            return Response({'data' : specAll})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Изменить специализацию для мастера
class ChengeSpecializationMasterView(APIView):
    
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

            # Проверяем. Пользователь должен быть клиентом
            if user.status.status_name != 'client' :
                
                # Получаем специализацию мастера (может быть пустой)
                specMaster = UserToSpecialization.objects.filter(user=user, specialization_id=id).values()

                # Если такая специализация не найдена
                if len(specMaster) == 0:

                    # Создаем новую специализацию для мастера
                    UserToSpecialization.objects.create(
                        user=user, 
                        specialization=Specializations.objects.get(id=id)
                    )
                    
                
                # Если такая специализация уже есть
                else:

                    # Удаляем ее
                    UserToSpecialization.objects.filter(user=user, specialization_id=id).delete()
                    
                    
                
            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})



# -----------Компанента 'Настройки услуг'----------------

# Получить специализации с выбранными для мастера массивом услуг
class GetSpecWithAddServView(APIView):
    
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
            if user.status.status_name != 'client' :
                
                # Вытаскиваем специализации которые выбрал мастер
                arrSpec = UserToSpecialization.objects.filter(user=user).values()
                # Вытаскиваем услуги которые выбрал мастер
                arrServices = UserToServices.objects.filter(user=user).values()

                # Перебираем массив специализаций
                for el in arrSpec:

                    # Создаем место в массиве где будет храниться массив услуг
                    el['arrServices'] = []
                    # Тут будет название специализации
                    el['specialization'] = Specializations.objects.filter(id=el['specialization_id']).values()


                    # Перебираем массив услуг
                    for il in arrServices:

                        # Если специализации совпадают 
                        if el['specialization_id'] == il['specialization_id']:

                            # Добавляем название услуги
                            il['service'] = Services.objects.filter(id=il['service_id']).values()
                            # То добавляем в массив специализаций
                            el['arrServices'].append(il)

                            il = None
                     
                
            
            # Возвращаем данные
            return Response({'data': arrSpec})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})







