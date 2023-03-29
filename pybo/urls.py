from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('list/',views.ProfileViewList.as_view(),name='profile-list'),

]

