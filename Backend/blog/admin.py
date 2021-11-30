from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','id','status','slug','author') #editar display
    prepopulated_fields={'slug':('title',),}             #slug para poder acceder


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','email','publish','status') 
    list_filter=('status','publish')
    search_fields=('name','email','content')


admin.site.register(models.Category)




# Register your models here.
