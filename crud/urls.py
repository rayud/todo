from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read_more/', views.read_more, name='read_more'),
    path('add', views.add, name='add'),
    path('more/<int:todo_id>', views.more, name="more" ),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('wipe/', views.wipe, name="wipe" ),
    path('update/<int:todo_id>/', views.update, name='update'),
]