from django.urls import path
from . import views

app_name='booker'

urlpatterns = [
    path('list',views.book_list, name='book-list'),
    path('detail/<int:book_id>/', views.book_detail, name='detail'),
    path('detail/like/<int:book_id>', views.book_like ,name='like')
]
