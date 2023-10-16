from django.contrib import admin
from django.urls import path, include

from nails.Views.specialization import *
from nails.Views.Master.SettingServeces import *
from nails.Views.Master.DatePlan import *
from nails.Views.schedule import *




urlpatterns = [

    # 31    SettingMaster
    # 311   Настройка специализаций
    path('get-specialization-master', GetSpecializationMasterView.as_view()),           # Получить специализации мастера
    path('chenge-specialization-master', ChengeSpecializationMasterView.as_view()),     # Изменить специализацию мастера
   
    # 312   Настройка услуг
    path('get-data-for-setting-serveces-master', GetDataForSettingSerecesView.as_view()),   # Получить данные для настройки услуг
    path('send-data-add-serveces-master', MasterAddServecesView.as_view()),                 # Добавить в список выбранных
    path('send-data-del-serveces-master', MasterDelServecesView.as_view()),                 # Удалить из списка выбранных
    

    # 33    DataPlan
    path('transfer-time', TransferTimeView.as_view()),                              # Создание свободного времени для записи
    path('get-data-form-date-plan-master', GetDataFormDatePlanView.as_view()),      # Получить данные для формы
    path('get-data-date-master', GetDataDateView.as_view()),                        # Получаем данные из расписания за указанную дату
    path('del-data-date', DelDataDateView.as_view()), 
]
