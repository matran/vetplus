from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('checkup', views.checkup, name='checkup'),
    path('animal', views.animal, name='animal'),
    path('cowinterview/<str:animal>/<str:step>/<str:choice>/',views.cowinterview,name='interview'),
    path('goatinterview/<str:animal>/<str:step>/<str:choice>/',views.goatinterview,name='interview'),
    path('sheepinterview/<str:animal>/<str:step>/<str:choice>/',views.sheepinterview,name='interview'),
    path('chickeninterview/<str:animal>/<str:step>/<str:choice>/',views.chickeninterview,name='interview'),
    path('rabbitinterview/<str:animal>/<str:step>/<str:choice>/',views.rabbitinterview,name='interview'),
    path('turkeyinterview/<str:animal>/<str:step>/<str:choice>/',views.turkeyinterview,name='interview')
]
