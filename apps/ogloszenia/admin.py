from django.contrib import admin

# Register your models here.
from .models import Post

#@admin.register(Post)  # seme as "admin.site.register(Post, PostAdmin)"
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "published_date")
    

admin.site.register(Post, PostAdmin)