from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='portfolio/images/')
    git_hub_link = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=20, blank=True, choices=(
        ('cat', 'jobs'),
        ('cat2', 'achievements')
    ))


