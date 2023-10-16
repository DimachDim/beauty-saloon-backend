from django.contrib import admin
from django.urls import path, include

from nails.Views.Client.ChoiseServece import *
from nails.Views.Client.DatePlan import *
from nails.Views.Client.ChoiseMaster import *



urlpatterns = [
 
    # 411   Выбор услуги
    path('get-data-serveces-client', GetDataServicesClient.as_view()),      # Получить данные о специализациях и их услугах
    path('send-id-servece-client', SendIdServeceClient.as_view()),          # Отправляем id выбранной услуги

    # 4111  Дата план выбор услуг       '4121'
    path('get-data-date-client', GetDataDateClient.as_view()),                      # Получить данные за переданную дату
    path('send-data-appointment-client', AppointmentClient.as_view()),              # Записаться на прием
    path('send-data-cancel-appointment-client', CancelAppointmentClient.as_view()), # Отменить записаться на прием

    # 412   Выбор мастера
    path('get-list-masters', GetListMaster.as_view()),                  # Получить список всех мастеров
    path('get-data-for-calendar', GetDataForCalendar.as_view()),        # Получить данные для календаря

    # 4121
    path('get-master-data-date-client', GetMasterDataDateClient.as_view()),         # Получить все окна мастера за указанную дату

]