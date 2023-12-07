from django.urls import path
from . import views


urlpatterns = [
   path('api/v2/', views.GetAllProgramas.as_view(), name='all-programs'),
   path('api/v2/post', views.PostProgramasApi.as_view(), name='post-programs'),
]