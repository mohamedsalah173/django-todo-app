from django.contrib import admin

from main.models import TODO,todoItems

# Register your models here.
admin.site.register(TODO)
admin.site.register(todoItems)