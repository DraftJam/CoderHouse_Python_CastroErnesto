import profile
from django.contrib import admin
from posts.models import Post, Comment, Profile, Venue

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Venue)
