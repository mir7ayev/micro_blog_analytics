from django.contrib import admin
from .models import (
    PostView, PostViewByUser, PostViewByGender, PostViewByAge,
    PostViewByCountry,
)


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'count')
    list_display_links = ('id', 'post_id')


@admin.register(PostViewByUser)
class PostViewByUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'user_id', 'count')
    list_display_links = ('id', 'post_id')


@admin.register(PostViewByGender)
class PostViewByGenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'gender', 'count')
    list_display_links = ('id', 'post_id')


@admin.register(PostViewByAge)
class PostViewByAgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'age', 'count')
    list_display_links = ('id', 'post_id')


@admin.register(PostViewByCountry)
class PostViewByCountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'country', 'count')
    list_display_links = ('id', 'post_id')
