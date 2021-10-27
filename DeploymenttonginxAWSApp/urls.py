from django.urls import path,include

from . import views

app_name="nginx"

urlpatterns = [

    path('', views.index_view, name="gunicorn"),
]
