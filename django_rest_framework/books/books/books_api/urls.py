from . import views
from django.urls import path

urlpatterns = (
    path('', views.BookListCreate.as_view()),
    path('<int:book_id>', views.BookGetUpdateDelete.as_view()),
)
