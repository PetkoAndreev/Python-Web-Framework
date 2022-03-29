from django.urls import path

from articles.web.views import ArticlesListView, ArticleCreateView, SourceCreateView, SourceDetailsView, SourceListView

urlpatterns = (
    path('', ArticlesListView.as_view(), name='index'),
    path('articles/create', ArticleCreateView.as_view(), name='create article'),
    path('sources', SourceListView.as_view(), name='list sources'),
    path('sources/<int:pk>', SourceDetailsView.as_view(), name='details source'),
    path('sources/create', SourceCreateView.as_view(), name='create source'),

)
