
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'example/index.html')


def first_endpoint(request):
    return JsonResponse({'first': 'endpoint'})


def second_endpoint(request):
    return JsonResponse({'second': 'endpoint'})
