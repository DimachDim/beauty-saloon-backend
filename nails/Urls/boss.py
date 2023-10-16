from django.contrib import admin
from django.urls import path, include

from nails.Views.Boss.SettingsBoss21.specialization import *
from nails.Views.Boss.SettingsBoss21.services import *



urlpatterns = [

    # 21    SettingsBoss  
    # 211   Специализации
    path('get-specialization', GetSpecializationView.as_view()),            # Получить специализации
    path('add-specialization', AddSpecializationView.as_view()),            # Создать специализацию
    path('del-specialization', DelSpecializationView.as_view()),            # Удаление специализацию

    # 212   Услуги
    path('get-services', GetServicesView.as_view()),                        # Получить услуги
    path('add-service', AddServiceView.as_view()),                          # Создать услуги
    path('del-service', DelServiceView.as_view()),                          # Удаление услуги

]
