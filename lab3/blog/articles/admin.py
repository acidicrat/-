from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date') 

admin.site.register(Article, ArticleAdmin)




#Register your models here.
