  
from django.contrib import admin
from .models import Article,Author,Category,Comment
# Register your models here.

class ArticleModel(admin.ModelAdmin):
    list_display = ['__str__','posted_on','updated_on']
    search_fields = ['__str__']
    class Meta:
        model = Article
admin.site.register(Article,ArticleModel)


class AuthorModel(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__']
    class Meta:
        model = Author
admin.site.register(Author,AuthorModel)

admin.site.register(Category)
admin.site.register(Comment)