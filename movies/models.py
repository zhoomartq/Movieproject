from django.db import models


from account.models import User


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')

