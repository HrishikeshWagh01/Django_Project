from django.db import models
from  django.contrib.auth.models  import  Group
from django.contrib import admin
from .models import Category, Publisher ,Details, Author

class  categoryAdmin(admin.ModelAdmin):
    pass

class  publisherAdmin(admin.ModelAdmin):
    pass


class  detailsAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'category', 'Author', 'pages', 'publisher')

class  authorAdmin(admin.ModelAdmin):
    list_display=['name','image_tag']

admin.site.register(Category, categoryAdmin)
admin.site.register(Publisher, publisherAdmin)
admin.site.register(Details, detailsAdmin)
admin.site.register(Author, authorAdmin)

admin.site.unregister(Group)

