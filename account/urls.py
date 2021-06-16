from django.urls import path
from . import views
from .views import *

# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('activate/<str:activation_code>/', ActivateView.as_view()),
# ]


urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view(), name='activate_account'),

]