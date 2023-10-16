from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import Users, Session



#PROFILE INFO
class ProfileInfoView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data
            
            # Ищем пользователя
            user = Session.objects.get(sid=sid).user

            # Собираем данные пользователя
            id = user.id
            name = user.name
            lastName = user.lastName
            status = user.status.status_name

           
            # Возвращаем данные
            return Response({'id' : id, 'name' : name, 'lastName' : lastName, 'status' : status})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})



