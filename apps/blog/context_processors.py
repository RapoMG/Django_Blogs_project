from .models import Category

def sections_context(request):
    return {
        "sections": Category.objects.order_by("name")
    }
