from django.contrib import admin


from .models import Book,RoleInfo

# Register your models here.
admin.site.register(Book)
admin.site.register(RoleInfo)