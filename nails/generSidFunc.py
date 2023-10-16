# Функция генерирует сессию и возвращает рандомную строку

import random
import string



def generate_session_key(min_size):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(min_size))
    return rand_string