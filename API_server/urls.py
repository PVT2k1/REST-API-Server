from django.urls import path

from API_server import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]