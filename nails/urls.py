from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from nails.Views.aut import *
from nails.Views.profile import *
from nails.Views.users import *
from nails.Views.schedule import *
from nails.Views.specialization import *
from nails.Views.services import *
from nails.Views.Master.SettingServeces import *
from nails.Views.Master.DatePlan import *
from nails.Views.Client.ChoiseServece import *
from nails.Views.Client.DatePlan import *
from nails.Views.Client.ChoiseMaster import *

urlpatterns = [
    # Аутентификация
    path('api/login', loginView.as_view()),                 # LOGIN
    path('api/reg', RegView.as_view()),                     # REG
    path('api/logout', logoutView.as_view()),               # logout

    # Профиль
    path('api/profile-info', ProfileInfoView.as_view()),    # INFO PROFILE

    # Пользователи
    path('api/get-users', GetUsersView.as_view()),          # Получение списка пользователей
    path('api/del-user', DelUserView.as_view()),            # Удаление пользователя
    path('api/master-user', MasterUserView.as_view()),      # Назначение мастером

    # РАСШИРЕННЫЕ НАСТРОЙКИ
    path('api/get-specialization', GetSpecializationView.as_view()),            # Получить специализации
    path('api/add-specialization', AddSpecializationView.as_view()),            # Создать специализацию
    path('api/del-specialization', DelSpecializationView.as_view()),            # Удаление специализацию

    path('api/get-services', GetServicesView.as_view()),                        # Получить услуги
    path('api/add-service', AddServiceView.as_view()),                          # Создать услуги
    path('api/del-service', DelServiceView.as_view()),                          # Удаление услуги

    # =================== МАСТЕР ==========================
    # НАСТРОЙКИ МАСТЕРА
    # DatePlan для мастера
    path('api/transfer-time', TransferTimeView.as_view()),                              # Создание свободного времени для записи
    path('api/get-data-form-date-plan-master', GetDataFormDatePlanView.as_view()),      # Получить данные для формы
    path('api/get-data-date-master', GetDataDateView.as_view()),                        # Получаем данные из расписания за указанную дату
    path('api/del-data-date', DelDataDateView.as_view()),                               # Удаляем данные из расписания за указанную дату
    # специализация
    path('api/get-specialization-master', GetSpecializationMasterView.as_view()),           # Получить специализации мастера
    path('api/chenge-specialization-master', ChengeSpecializationMasterView.as_view()),     # Изменить специализацию мастера
    # настройка услуг
    path('api/get-data-for-setting-serveces-master', GetDataForSettingSerecesView.as_view()),   # Получить данные для настройки услуг
    path('api/send-data-add-serveces-master', MasterAddServecesView.as_view()),                 # Добавить в список выбранных
    path('api/send-data-del-serveces-master', MasterDelServecesView.as_view()),                 # Удалить из списка выбранных
    # =================== МАСТЕР end==========================
    

    # =================== КЛИЕНТ ==========================
    # ЗАПИСАТЬСЯ
    # Выбор услуги
    path('api/get-data-serveces-client', GetDataServicesClient.as_view()),      # Получить данные о специализациях и их услугах
    path('api/send-id-servece-client', SendIdServeceClient.as_view()),          # Отправляем id выбранной услуги
    # Выбор мастера
    path('api/get-list-masters', GetListMaster.as_view()),                  # Получить список всех мастеров
    path('api/get-data-for-calendar', GetDataForCalendar.as_view()),        # Получить данные для календаря
    # ПЛАН ДАТЫ
    # выбор услуги
    path('api/get-data-date-client', GetDataDateClient.as_view()),                      # Получить данные за переданную дату
    path('api/send-data-appointment-client', AppointmentClient.as_view()),              # Записаться на прием
    path('api/send-data-cancel-appointment-client', CancelAppointmentClient.as_view()), # Отменить записаться на прием
    # выбор мастера
    path('api/get-master-data-date-client', GetMasterDataDateClient.as_view()),         # Получить все окна мастера за указанную дату

    # =================== КЛИЕНТ end==========================
]



#urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)        # Для статичных файлов