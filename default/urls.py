from django.urls import path
from . import views

urlpatters = [
    path('poll', views.Poll_list.as_view()),
    path('poll/<int:pk>/', views.PollView.as_view()),
] 
