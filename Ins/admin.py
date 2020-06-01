from django.contrib import admin
from Ins.models import Post, InsUser, Comment, Like

# Register your models here.
class CommentInLine(admin.StackedInline):
    model = Comment

class LikeInLine(admin.StackedInline):
    model = Like

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
        LikeInLine
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(InsUser)
admin.site.register(Comment)
admin.site.register(Like)