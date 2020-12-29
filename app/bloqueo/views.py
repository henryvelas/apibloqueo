
from django.shortcuts import render, redirect

import json
import psycopg2
import time
from socket import error as socket_error
from django.urls import reverse_lazy

from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from .models import Bloqueo

# Create your views here.

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


def conexionn():
    conect = psycopg2.connect(host="localhost", port="5432",
                              database="APIbloqueo", user="postgres", password="verim123.")

    return conect


class vista(View):

    def get(self, request):
        list2 = Bloqueo.objects.order_by('idd')
        return JsonResponse(list(list2.values()), safe=False)


class detalle(View):

    def get(self, request, pk):
        list2 = Bloqueo.objects.get(pk=pk)
        return JsonResponse(model_to_dict(list2))
