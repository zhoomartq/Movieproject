from django.urls import path

from movies import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('movies/', views.PostView.as_view(), name='movie-lists'),
#     path('movies/<int:pk>/', views.PostDetailView.as_view(), name = 'movie-detail'),
#     path('movies-update/<int:pk>/', views.PostUpdateView.as_view()),
#     path('movies-delete/<int:pk>/', views.PostDeleteView.as_view()),
]

