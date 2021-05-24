from django.contrib import admin
from books.models import GenreModel, AuthorModel, BookModel


@admin.register(GenreModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'page_count', 'created_at']
    list_filter = ['author', 'genres', 'created_at']
    search_fields = ['title', 'summary', 'isbn']
    autocomplete_fields = ['author', 'genres']
