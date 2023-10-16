from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from nails.models import  Users, UserToSpecialization, Specializations, Schedule


# Получить список всех мастеров
class GetListMaster(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            # Массив с конечными данными
            arrData = []
            # Массив всех мастеров
            arrMasters = Users.objects.filter(status=3).values()

            # Перебираем массив мастеров
            for el in arrMasters:

                # Подготавливаем место для нужных данных
                id = el['id']
                name = el['name']
                lastName = el['lastName']
                arrSpecializations = []

                # Получаем все специализации мастера
                specializations = UserToSpecialization.objects.filter(user=id).values()
                # Перебираем их
                for n in specializations:
                    # Достаем нужные данные
                    idSpec = n['specialization_id']
                    titleSpec = Specializations.objects.get(id=n['specialization_id']).title

                    # Формируем словарь и добавляем его в массив
                    arrSpecializations.append({'id':idSpec, 'title':titleSpec})
                

                # Формируем объект и добавляем данные в массив
                arrData.append({'id':id,'name':name,'lastName':lastName,'arrSpecialization':arrSpecializations,})


            # Возвращаем данные
            return Response({'data' : arrData})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})


# Получить данные для календаря
class GetDataForCalendar(APIView):

    def get(self, request):
        return Response({'title': 'test'})

    def post(self, request):
        # Если все пойдет без ошибок
        try:
            idMaster = request.data['idMaster']
            # Дата с которой начинать поиск
            startYear = request.data['year']
            startMonth = request.data['month']
            startDate = request.data['date']
            
            arrData = []        # Конечный массив с данными
            arrUnsortedData =[] # Не сортированны массив


            # Мастер
            master = Users.objects.get(id=idMaster)
            # Получаем все записи мастера
            arrSchedules =  Schedule.objects.filter(master=master).values()
            # Проходимся по полученному массиву
            for el in arrSchedules:

                # Вытаскиваем дату
                year = el['year']
                month = el['month']
                date = el['date']
                statusFree = True

                # Если дата уже прошла
                if startYear >= year and startMonth>=month and startDate> date:
                    continue

                # Если кто то записан
                if el['client_id'] != None:
                    statusFree = False

                # Формируем словарь и добавляем в несартированный массив
                arrUnsortedData.append({'year':year,'month':month,'date':date,'statusFree':statusFree,})


            # Перебираем несартированный массив
            i=0
            while i<len(arrUnsortedData):
                # Если первый проход
                if i == 0:
                    # Добавляем элемент в конечный массив
                    arrData.append(arrUnsortedData[i])

                # Если не первый проход
                else:
                    # Если дата равна предыдущей
                    if arrUnsortedData[i]['year']==arrUnsortedData[i-1]['year'] and arrUnsortedData[i]['month']==arrUnsortedData[i-1]['month'] and arrUnsortedData[i]['date']==arrUnsortedData[i-1]['date']:
                        # Если статус прошлой лож а новой истина
                        if arrUnsortedData[i-1]['statusFree']==False and arrUnsortedData[i]['statusFree']==True:
                            # Удаляем последнюю запись из конечного массива
                            del arrData[len(arrData)-1]
                            # Добавляем элемент в конечный массив
                            arrData.append(arrUnsortedData[i])
                        i +=1
                        continue

                    # Если дата не равна предыдущей
                    else:
                        # Добавляем элемент в конечный массив
                        arrData.append(arrUnsortedData[i])
                        
                i+=1
            
            # Возвращаем данные
            return Response({'data' : arrData})

        # Если возникнет непредвиденая ошибка
        except Exception as e:
            print(e)
            return Response({'textError' : 'unknown error'})

