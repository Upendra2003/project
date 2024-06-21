from django.urls import path
from .  import views
urlpatterns = [
    path('user-details/',views.user_details,name='user-details'),
    path('user/<str:user_name>/', views.user_detail, name='user_detail'),
]
