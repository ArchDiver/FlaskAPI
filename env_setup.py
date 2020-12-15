import hashlib
import string
import random

def add_to_env(length):
    with open('.env', 'w+') as file:
        database_url= 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='LittleZoeNugget3689',url='127.0.0.1:5433',db='api_test_db')
        data = file.read()
        file.seek(0)
        all_letters = string.ascii_lowercase
        letter_connect = ''.join(random.choice(all_letters) for i in range(length))