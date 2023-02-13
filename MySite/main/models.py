from django.db import models

# Create your models here.
# Define Attributes
class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
#to associate items with todolist we define with the FK on Todolist object when we create an item
class Item(models.Model):
	todolist =models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	complete = models.BooleanField()

	def __str__(self):
		return self.text


