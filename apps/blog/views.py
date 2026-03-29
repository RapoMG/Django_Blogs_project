from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Author, Category
from  django.db.models import Q

# Create your views here.

# authors = Author.objects.annotate(posts_count=Count("post")).order_by("-posts_count")

def posts_by_category(request, category_id: int):
    category = get_object_or_404(Category, pk=category_id)
    posts = (
        Post.objects
        .filter(category=category)
        .prefetch_related("author", "category")
        .order_by("-publication_date")
    )

    # for base.html -> _sections.html
    sections = Category.objects.order_by("name")

    context = {
        'posts':posts,
        "category": category,
        "sections": sections,  # for base.html -> _sections.html
    }

    return render(request, 'post_list.html', context)

def last_posts(request):
    posts = Post.objects.all().order_by("-publication_date")[:5]

    context = {
            'posts':posts
        }

    return render(request, 'last_posts.html', context)


def search_view(request):
    query = (request.GET.get('q') or "").strip()
    posts = Post.objects.none()

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    
    context = {
        'posts':posts,
        'query':query
    }

    return render(request, 'search.html', context)