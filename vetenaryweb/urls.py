from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('checkup', views.checkup, name='checkup'),
    path('animal', views.animal, name='animal'),
    path('notification', views.notification, name='notification'),
    path('feedback', views.feedback, name='feedback'),
    path('cowinterview/',views.cowinterview,name='cowinterview'),
    path('goatinterview/',views.goatinterview,name='goatinterview'),
    path('sheepinterview/',views.sheepinterview,name='sheepinterview'),
    path('chickeninterview/',views.chickeninterview,name='chickeninterview'),
    path('turkeyinterview/',views.turkeyinterview,name='turkeyinterview')
]
