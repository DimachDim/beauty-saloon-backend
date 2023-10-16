from django.db import models
import datetime
import os


# Пользователи
class Users(models.Model):
    name =  models.CharField(max_length=30)
    lastName =  models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=200)    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    
    #avatar = models.ImageField(upload_to=get_upload_path, default='', null=True)

# Сессии
class Session(models.Model):
    sid = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

# Статус
class Status(models.Model):
    status_name = models.CharField(max_length=20)


# Расписание
class Schedule(models.Model):
    master = models.ForeignKey(Users, related_name="master", on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Users, related_name="client", on_delete=models.SET_NULL, null=True)
    year = models.SmallIntegerField(null=True)
    month = models.SmallIntegerField(null=True)
    date = models.SmallIntegerField(null=True)
    time = models.TimeField(null=True)
    service = models.ForeignKey('Services', on_delete=models.CASCADE, null=True)                        # Выбранная услуга
    status = models.ForeignKey('SheduleStatus', on_delete=models.SET_NULL, null=True)                   # Статус выполнения записи


# ОТНОШЕНИЕ возможных услуг к записи в распиании
class ServicesToShedule(models.Model):
    shedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)    # Ссылка на одну запись в расписании
    service = models.ForeignKey('Services', on_delete=models.CASCADE)       # Cылка на возможную услугу


# Статус выполнения записи
class SheduleStatus(models.Model):
    title = models.CharField(max_length=50)     # Название статуса


# Специализации
class Specializations(models.Model):
    title = models.CharField(max_length=50)


# ОТНОШЕНИЕ пользователя к специализации
class UserToSpecialization(models.Model):
    user = models.ForeignKey(Users,  on_delete=models.CASCADE, null=True)
    specialization = models.ForeignKey('Specializations',  on_delete=models.CASCADE)


# Услуги
class Services(models.Model):
    specialization = models.ForeignKey(Specializations, related_name="specialization", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)


# ОТНОШЕНИЕ мастера к услугам
class UserToServices(models.Model):
    user = models.ForeignKey(Users,  on_delete=models.CASCADE, null=True)
    specialization = models.ForeignKey(Specializations,  on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Services,  on_delete=models.CASCADE, null=True)
    price = models.SmallIntegerField(null=True)


