from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request

from .models import Post, InsUser
from .forms import CustomUserCreationForm

# Create your views here.
class HomePage(TemplateView):
	template_name = 'home.html'

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	login_url = 'login'
	template_name = 'home.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class PostCreateView(CreateView):
	model = Post
	fields = '__all__'
	template_name = 'make_post.html'

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title']
	template_name = 'edit_post.html'

class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('home')
	template_name = 'delete_post.html'

class SignUp(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'sign_up.html'

class UserProfile(LoginRequiredMixin, DetailView):
	model = InsUser
	login_url = 'login'
	template_name = 'user_profile.html'

class EditProfile(LoginRequiredMixin, UpdateView):
	model = InsUser
	login_url = 'login'
	fields = ['profile_pic', 'username']
	success_url = reverse_lazy('home')
	template_name = 'edit_profile.html'

@ajax_request
def toggleFollow(request):
	current_user = InsUser.objects.get( pk = request.user.pk )
	follow_user_pk = request.POST.get('follow_user_pk')
	follow_user = InsUser.objects.get( pk = follow_user_pk )
	post_type = request.POST.get('type')

	try:
		if current_user != follow_user:
			if post_type == 'follow':
				connection = UserConnection( creator = current_user, following = follow_user )
				connection.save()
			elif post_type == 'unfollow':
				UserConnection.objects.filter( creator = current_user, following = follow_user ).delete()
			result = 200
		else:
			result = 500
	except Exception as e:
		print(e)
		result = 500

	return {
		'result': result,
		'type': post_type,
		'follow_user_pk': follow_user_pk,
	}