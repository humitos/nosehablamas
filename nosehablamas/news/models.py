from django.db import models


class News(models.Model):

    title = models.CharField(max_length=512)

    posted_at = models.DateTimeField(auto_now_add=True)


class Article(models.Model):

    title = models.CharField(max_length=512)
    description = models.TextField()
    url = models.URLField(verify_exists=True)
    news = models.ForeignKey(News)
    views = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to='articles',
                              null=True, blank=True)

    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_at']
