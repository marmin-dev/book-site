from django.contrib import admin
from django.urls import path,include
from booker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booker/',include('booker.urls')),
    path('', views.index,name='index'),
    path('common/',include('common.urls')),
    path('pybo/',include('pybo.urls'))
]

handler404 = 'common.views.page_not_found'