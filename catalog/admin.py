from django.contrib import admin
from . models import Book, Author, Genre, BookInstance, Language


# admin.register decorator registers argument and decorates function beneath

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'due_back', 'status', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back')
            }),
    )


admin.site.register(Genre)
admin.site.register(Language)
