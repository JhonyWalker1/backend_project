from django.urls import path

from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('region',views.RegionView.as_view()),
]