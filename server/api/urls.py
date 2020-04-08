from django.urls import path
from .views import save,reset
urlpatterns = [
    path('save/',save, name='save'),
    path('reset/',reset, name='reset'),
]