from django.contrib import admin
from .models import Post, Author

# Register your models here.

#admin.site.register(Post)
admin.site.register(Author)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ai_import = True  # Enable AI-driven form filling
    list_display =('title', 'category', 'author',)