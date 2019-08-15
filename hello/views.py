from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_409_CONFLICT
)
from rest_framework.response import Response

from .models import IPStore

# Create your views here.
@api_view(["GET"])
@permission_classes((AllowAny,))
def index(request):
    # return HttpResponse('Hello from Python!')
    ip = None

    try:
        ip = IPStore.objects.get().ip
    except IPStore.DoesNotExist:
        ip = None
    return Response({'ip':ip})




def updip(request):
    store = None
    if IPStore.objects.exists():
        store = IPStore.objects.get()
    else:
        store = IPStore()
    store.ip = request.META['HTTP_X_FORWARDED_FOR']['origin'][-1]
    store.save()
    return Response({'status':'ok'})
