from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Session, Specializations, UserToSpecialization, UserToServices, Services


# Получить данные для формы
class GetDataFormDatePlanView(APIView):

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
                
                # Основной массив
                arrSpec = [] 

                # Ищем записи о том какие специализации выбрал пользователь
                specRecord = UserToSpecialization.objects.filter(user=user).values('specialization_id')
                # Перебираем записи
                for el in specRecord:
                    
                    # Ищем специализацию по id
                    spec = Specializations.objects.filter(id=el['specialization_id']).values()[0]
                    # Добавляем в объект дополнительные поля
                    spec['arrSelectServeces'] = []              #Место для выбранных услуг

                    # Добавляем в основной массив
                    arrSpec.append(spec)

                    # Ищем выбранные услуги
                    arrSelectServ = UserToServices.objects.filter(specialization=spec['id'],user=user).values('id', 'service_id', 'price')
                    # Перебираем найденые услуги
                    for il in arrSelectServ:
                    
                        # Добавляем к ней новое поле
                        il['service_title'] = Services.objects.filter(id=il['service_id']).values('title')[0]['title']
                        # Добваляе новый объект в подгатовленый массив
                        spec['arrSelectServeces'].append(il)

                    
                    
                      
                                     

            # Возвращаем данные
            return Response({'data' : arrSpec})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})






