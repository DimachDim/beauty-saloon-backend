import datetime
import os



# Генерирует путь до файла изображения и назначет имя
def get_upload_path(instance, filename):
    # Получаем текущее время
    now = datetime.datetime.now()
    return os.path.join('media', instance.phone, 'avatar', now.strftime("%d-%m-%Y %H-%M-%S.jpg"))