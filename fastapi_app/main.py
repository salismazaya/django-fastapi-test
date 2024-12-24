import os, django as _django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
_django.setup()


from fastapi import FastAPI
from core.models import TestInsert

app = FastAPI()

@app.get("/hello")
async def hello():
    print("FROM FASTAPI")
    return {'msg': 'hello from fastapi'}

@app.get("/fetch")
async def fetch():
    print(await TestInsert.objects.acount(), "FROM FASTAPI")
    return {'msg': 'complete'}