from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('list/',views.ProfileViewList.as_view(),name='profile-list'),
    path('profile/create/',views.profile_create,name='profile-create'),
    path('profile/detail/<int:profile_id>',views.profile_detail,name='detail'),
    path('profile/like/<int:profile_id>',views.profile_like,name='like'),
    path('profile/unlike/<int:profile_id>',views.profile_unlike,name='unlike'),
    path('profile/comment/delete/<int:comment_id>',views.comment_delete,name='comment-delete'),
    path('profile/comment/update/<int:profile_id>/<int:comment_id>',views.comment_update,name='comment-update'),
    path('profile/profile/delete/<int:profile_id>',views.delete_profile,name='profile-delete'),
    path('profile/profile/update/<int:profile_id>',views.update_profile,name='profile-update'),
    path('hello/<int:user_id>',views.UserProfileView.as_view(),name='profile')


]

