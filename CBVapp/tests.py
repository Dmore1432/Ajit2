from django.test import TestCase
import requests
# Create your tests here.
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='IntructorListView'
r=requests.get(BASE_URL+ENDPOINT)
data=r.json()
print(data)