from django.urls import path
from game.views.views import index

urlpatterns=[
    path("",index,name="index"),
]