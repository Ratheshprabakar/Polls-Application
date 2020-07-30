from django.db import models

# Create your models here.
class question(models.Model):
	question_text=models.CharField(max_length= 200)
	published_data=models.DateTimeField('date published')

class options(models.Model):
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	question=models.ForeignKey(question,on_delete=models.CASCADE)
