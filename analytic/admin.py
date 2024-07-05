from django.contrib import admin
from .models import (
    PostView, UserVisit
)


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id')


@admin.register(UserVisit)
class UserVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'post_id')
