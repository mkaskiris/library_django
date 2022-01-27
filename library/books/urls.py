from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books-index'),
    #path('about/', views.about, name='books-about'),
    path('<int:id>/', views.show, name='books-show')
]
