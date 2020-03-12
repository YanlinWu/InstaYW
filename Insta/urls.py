from django.contrib import admin
from django.urls import include, path

from Insta.views import HelloWorld, PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, addLike,\
UserProfile, EditProfile, addComment, toggleFollow, ExploreView




urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name = 'helloworld'),
    path('', PostListView.as_view(), name = 'home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post'),
    path('post/new/', PostCreateView.as_view(), name ='make_post'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name = 'edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'delete_post'),
    path('like', addLike, name = 'addLike'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('comment', addComment, name='addComment'),
    path('togglefollow', toggleFollow, name = 'toggleFollow'),
    path('explore', ExploreView.as_view(), name = 'explore'),
]