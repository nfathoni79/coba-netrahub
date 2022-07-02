from django.urls import path
from main import views

urlpatterns = [
    path('outbox', views.outbox),
    path('inbox', views.inbox),
    path('data/fromDevice', views.from_dev),
    path('data/toDevice', views.to_dev),
]
