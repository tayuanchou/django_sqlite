from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # this is automatically created
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,
                            db_index=True)  # harry-potter-1

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = self.title.replace(" ", "-").lower()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
