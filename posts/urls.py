from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
]