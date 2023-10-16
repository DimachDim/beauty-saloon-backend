from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import Users, Session, Status



# Получение списка пользователей
class GetUsersView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Получаем всех пользователей из базы
            users = Users.objects.all().values('id', 'name', 'lastName', 'phone', 'status')

            # Получаем существующие статусы из базы
            statuses = Status.objects.all().values()
           
            # Возвращаем данные
            return Response({'users' : list(users), 'statuses' : list(statuses)})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})


# Назначение мастером
class MasterUserView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            user_id = request.data['id']

            # Ищем пользователя который отправил запрос
            user = Session.objects.get(sid=sid).user

            # Проверяем отправил админ или бос
            if user.status.status_name == 'admin' or user.status.status_name == 'boss':
                
                # Ищем пользователя по id
                master_user = Users.objects.get(id=user_id)

                # Если статус клиента
                if master_user.status.status_name == 'client':

                    # Меняем на мастера
                    master_user.status_id=3
                    master_user.save()

                # Если другой статус
                else:

                    # Меняем на клиента
                    master_user.status_id=2
                    master_user.save()
           
            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})


# Удаление пользователя
class DelUserView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data['SID']
            user_id = request.data['id']

            # Ищем пользователя который отправил запрос
            user = Session.objects.get(sid=sid).user

            # Проверяем отправил админ или бос
            if user.status.status_name == 'admin' or user.status.status_name == 'boss':
                
                # Ищем пользователя по id
                del_user = Users.objects.get(id=user_id)
                # Удаляем пользователя
                del_user.delete()
           
            # Возвращаем данные
            return Response({})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})

