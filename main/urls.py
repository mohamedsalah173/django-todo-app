from . import views
from django.urls import path

urlpatterns = [
    path('detailed/<str:id>/', views.detailed, name='detailed'),
    path('update/<str:id>',views.updateTodo, name = 'update'),
    path('delete/<str:id>',views.delete, name = 'delete'),
    path('create/' ,views.createTodo , name = 'create' ),
    path('',views.home , name='home')
]