from django.contrib import admin
from Ins.models import Post, InsUser, Comment, Like, UserConnection

# Register your models here.
class CommentInline(admin.StackedInline):
	model = Comment

class LikeInline(admin.StackedInline):
	model = Like

class PostAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
		LikeInline
	]

class FollowingInline(admin.StackedInline):
	model = UserConnection
	fk_name = 'creator'

class FollowerInline(admin.StackedInline):
	model = UserConnection
	fk_name = 'following'

class UserAdmin(admin.ModelAdmin):
	inlines = [
		FollowingInline,
		FollowerInline
	]

admin.site.register(Post, PostAdmin)
admin.site.register(InsUser, UserAdmin)
admin.site.register(Comment)
admin.site.register(Like)