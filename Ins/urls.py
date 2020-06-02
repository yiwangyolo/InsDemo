from django.urls import path
from Ins.views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView, 
	SignUp, 
	UserProfile, 
	EditProfile,
	toggleFollow
)

urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('post/<int:pk>', PostDetailView.as_view(), name='post'),
	path('post/new', PostCreateView.as_view(), name='make_post'),
	path('post/edit/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
	path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
	path('auth/signup', SignUp.as_view(), name='sign_up'),
	path('user_profile/<int:pk>', UserProfile.as_view(), name='user_profile'),
	path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
	path('togglefollow', toggleFollow, name='togglefollow'),
]