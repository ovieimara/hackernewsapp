from django.urls import path
from .views import latestView, newsDetailView


urlpatterns = [
    path('', latestView, name='news'),
    path('news', latestView, name='news'),
    path('news/<int:id>', newsDetailView, name='app-news-detail'),

]