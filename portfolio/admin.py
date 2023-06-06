from django.contrib import admin
from .models import Portfolio


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


admin.site.register(Portfolio, ArticleAdmin)

