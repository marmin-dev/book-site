from django.urls import path, include
from . import views

app_name='booker'

urlpatterns = [
    path('list', views.book_list, name='book-list'),
    path('detail/<int:book_id>/', views.book_detail, name='detail'),
    path('detail/like/<int:book_id>/', views.book_like, name='like'),
    path('detail/unlike/<int:book_id>/',views.book_unlike,name='unlike'),
    path('random/', views.book_reference, name='random'),
    path('profile/',views.book_profile, name='profile'),
    path('comment/delete/<int:comment_id>',views.comment_delete,name='comment-delete'),
    path('comment/update/<int:book_id>/<int:comment_id>', views.comment_update, name="comment-update"),
]
