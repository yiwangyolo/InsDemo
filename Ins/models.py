from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InsUser(AbstractUser):
	profile_pic = ProcessedImageField(
		upload_to = 'static/images/profiles',
		format = 'JPEG',
		options = {'quality': 100},
		null = True,
		blank = True
	)

	def get_connections(self):
		connections = UserConnection.objects.filter(creator = self)
		return connections

	def get_followers(self):
		followers = UserConnection.objects.filter(following = self)
		return followers

	def is_followed_by(self, user):
		followers = UserConnection.objects.filter(following = self)
		return followers.filter(creator = user).exists()

	def __str__(self):
		return self.username

class UserConnection(models.Model):
	created = models.DateTimeField(
		auto_now_add = True,
		editable = False
	)
	creator = models.ForeignKey(
		InsUser,
		on_delete = models.CASCADE,
		related_name = 'friendship_creator_set'
	)
	following = models.ForeignKey(
		InsUser,
		on_delete = models.CASCADE,
		related_name = 'friend_set'
	)

	def __str__(self):
		return self.creator.username + ' follows ' + self.following.username

class Post(models.Model):
	author = models.ForeignKey(
		InsUser,
		blank = True,
		null = True,
		on_delete = models.CASCADE,
		related_name = 'ins_posts'
	)
	title = models.TextField(
		blank=True, 
		null=True
	)
	image = ProcessedImageField(
		upload_to = 'static/images/posts',
		format = 'JPEG',
		options = {'quality': 100},
		blank = True,
		null = True,
	)
	posted_on = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		blank = True,
		null = True,
	)

	def __str__(self):
		return self.title

	def get_like_count(self):
		return self.likes.count()

	def get_comment_count(self):
		return self.comments.count()

	def get_absolute_url(self):
		return reverse('post', args = [str(self.id)])

class Comment(models.Model):
	post = models.ForeignKey(
		Post, 
		on_delete=models.CASCADE, 
		related_name='comments'
	)
	user = models.ForeignKey(
		InsUser, 
		on_delete=models.CASCADE
	)
	comment = models.CharField(
		max_length=100
	)
	posted_on = models.DateTimeField(
		auto_now_add=True, 
		editable=False
	)

	def __str__(self):
		return self.comment

class Like(models.Model):
	post = models.ForeignKey(
		Post, 
		on_delete=models.CASCADE, 
		related_name='likes'
	)
	user = models.ForeignKey(
		InsUser, 
		on_delete=models.CASCADE
	)

	class Meta:
		unique_together = ('post', 'user')

	def __str__(self):
		return 'Like: ' + self.user.username + ' ' + self.post.title