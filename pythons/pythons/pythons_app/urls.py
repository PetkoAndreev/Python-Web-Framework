from django.urls import path

from . import views
from pythons.pythons_app.views import index, create

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
]
