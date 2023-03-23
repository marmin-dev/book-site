import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import requests
from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured
from booker.models import Books


BASE_DIR = Path(__file__).resolve().parent.parent.parent
secret_file = os.path.join(BASE_DIR, 'secret.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())
def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

API_KEY =get_secret('API_KEY')




def getBookData(n):
    r = requests.get(
        f'http://api.kcisa.kr/openapi/service/rest/meta4/getKCPG0506?serviceKey={API_KEY}&numOfRows=10&pageNo={n}',
        headers={'Accept': 'application/json'})
    return r.json()['response']['body']['items']['item']

def data_save(n):
    for i in range(n):
        for data in getBookData(i+1):
            book = Books()
            book.title = data['title']
            book.extent = data['extent']
            book.description = data['description']
            book.charge = data['charge']
            book.cover = data['referenceIdentifier']
            book.rights = data['rights']
            book.issued_at = data['issuedDate']
            try:
                book.save()
            except:
                pass

data_save(82)
# print(getBookData(1))