from django.contrib import admin
from django.urls import path, include


from nails.Views.General.aut import *
from nails.Views.General.profile import *
from nails.Views.General.users import *


urlpatterns = [

    # 1     Аутентификация   
    path('login', loginView.as_view()),                 # LOGIN
    path('reg', RegView.as_view()),                     # REG
    path('logout', logoutView.as_view()),               # logout

    # 12    Профиль
    path('profile-info', ProfileInfoView.as_view()),    # INFO PROFILE

    # 13    Пользователи
    path('get-users', GetUsersView.as_view()),          # Получение списка пользователей
    path('del-user', DelUserView.as_view()),            # Удаление пользователя
    path('master-user', MasterUserView.as_view()),      # Назначение мастером

]
