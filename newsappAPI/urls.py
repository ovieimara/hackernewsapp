from django.urls import path
from .views import latest_news, ItemsView, ItemsManagerView


urlpatterns = [
    path('', latest_news, name='latest-news'),
    path('latest', latest_news, name='latest-news'),
    path('news', ItemsView.as_view(), name='news-list'),
    path('news/<int:pk>', ItemsManagerView.as_view(), name='news-detail'),
]