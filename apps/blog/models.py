from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title=models.CharField(max_length=100)
    content = models.TextField()
    author=models.ForeignKey(Author, null=True, related_name="autor", on_delete=models.CASCADE)
    publication_date=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, related_name="category", on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title
