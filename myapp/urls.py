from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup-new/', views.signup, name='signup'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('demo/', views.secret_page, name='secret'),
    path('demo1/', views.SecretPage.as_view(), name='secret2'),
    path('post/', views.PostView.as_view(),name='post'),
]