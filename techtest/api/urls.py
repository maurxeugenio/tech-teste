from django.urls import path
from .views import ArticleListView, ArticleDetailView, AuthorListView, AuthorDetailView, RegionListView, RegionDetailView


urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('article/<id>/', ArticleDetailView.as_view()),
    path('article/', ArticleDetailView.as_view()),
    path('article/remove/author/', ArticleListView.as_view()),

    path('regions/', RegionListView.as_view()),
    path('region/<id>/', RegionDetailView.as_view()),
    path('region/', RegionDetailView.as_view()),

    path('authors/', AuthorListView.as_view()),
    path('author/<id>/', AuthorDetailView.as_view()),
    path('author/', AuthorDetailView.as_view()),
]
