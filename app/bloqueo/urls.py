from django.urls import path
from .views import *

urlpatterns = [
    path('vista/', vista.as_view(), name='vista'),
    path('detalle/<str:pk>/', detalle.as_view(), name='detalle')

]
