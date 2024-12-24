from django.http import JsonResponse
from core.models import TestInsert

async def hello(request):
    print("FROM DJANGO")
    return JsonResponse({'msg': 'hello from django'})

async def fetch(request):
    print(await TestInsert.objects.acount(), "FROM DJANGO")
    return JsonResponse({'msg': 'complete'})