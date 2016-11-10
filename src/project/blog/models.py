from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    labels = models.ManyToManyField('Label')

    # Article publishing date/time - articles ordering is made by this field.
    # Also if it's blank - the article will be hidden.
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'blog_article'

    def __str__(self):
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, unique=True)

    class Meta:
        db_table = 'blog_label'

    def __str__(self):
        return self.title
