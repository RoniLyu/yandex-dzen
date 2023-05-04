from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views

from . import views

urlpatterns = [
    path('register/', views.AuthorRegisterAPIView.as_view()),
    path('<str:user__username>/', views.AuthorRetrieveUpdateDestroy.as_view({'get': 'retrieve', 'put': 'update',
                                                                             'delete': 'destroy'})),
    path('token/', obtain_auth_token),
    #path('login/', views.LoginView.as_view()),
    #path('logout', views.LogoutView.as_view()),

]
