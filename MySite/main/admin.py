from django.contrib import admin
from .models import ToDoList, Item

# Register your mod ls here.
admin.site.register(ToDoList)
admin.site.register(Item)
