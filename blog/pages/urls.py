from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('post_form/', views.post_form, name='post_form'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/delete/', views.delete, name='delete')
]