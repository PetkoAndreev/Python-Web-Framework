from django.urls import path

from . import views
# from pythons.pythons_app.views import index, create

urlpatterns = [
    # path('', index, name="index"),
    path('', views.IndexView.as_view(), name="index"),
    # path('create/', create, name="create"),
    path('create/', views.PythonCreateView.as_view(), name="create"),
]
