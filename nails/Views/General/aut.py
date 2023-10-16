from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import Users, Session, Status

from nails.generSidFunc import generate_session_key

#LOGIN
class loginView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            phone = request.data['phone']
            password = request.data['password']

            arrUser = Users.objects.filter(phone=phone)

            # Если такого номера нет в базе
            if len(arrUser) == 0:
                return Response({'textError' : 'user does not exist'})
            
            # ЕСЛИ такой номер есть в базе
            else:
                # Смотрим пароль найденного пользователя
                password_from_db = arrUser[0].password

                # ЕСЛИ ПАРОЛИ СОВПАДАЮТ
                if password_from_db == password:
                    # Вычленяем пользователя
                    user = arrUser[0]
                    # Генерируем сессию
                    sid = generate_session_key(50)
                    # Создаем запись в базе сессий
                    Session.objects.create(
                        sid = sid,
                        user = user
                    )
                    # Возвращаем сессию
                    return Response({'SID' : sid})
                
                # ЕСЛИ пароли не совпадают
                else:
                    # Возвращаем текст ошибки
                    return Response({'textError' : 'incorrect password'})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})


#REG
class RegView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            name = request.data['name']
            lastName = request.data['lastName']
            phone = request.data['phone']
            password = request.data['password']

            # Ищем пользователя по номеру телефона
            arrUsers = Users.objects.filter(phone = phone)

            # ЕСЛИ такого пользователя нет
            if len(arrUsers) == 0:

                # Создаем пользователя
                user = Users.objects.create(
                    name=name,
                    lastName=lastName,
                    phone=phone,
                    password=password,
                    status=Status.objects.get(status_name='client')
                )

                # Генерируем сессию
                sid = generate_session_key(50)

                # Создаем запись в базе сессий
                Session.objects.create(
                    sid = sid,
                    user=user
                )

                # Возвращаем сессию
                return Response({'SID' : sid})

            # ЕСЛИ такой пользователь уже есть
            else:
                return Response({'textError' : 'number is busy'})
            

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})

#LOGOUT
class logoutView(APIView):
    
    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Вытаскиваем данные
            sid = request.data

            # Изем запись
            record = Session.objects.get(sid=sid)
            # Удаляем
            record.delete()

            # Возвращаем текст ошибки
            return Response({'answer' : 'ok'})

        # Если возникнет непредвиденая ошибка
        except:
            return Response({'textError' : 'unknown error'})