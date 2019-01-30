from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class TeacherProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	id_no=models.CharField(max_length=100, primary_key=True)
	name=models.CharField(max_length=150)
	college_name=models.CharField(max_length=250)
	password=models.CharField(max_length=50)

	'''def __str__(self):
		return self.er_no+'-'+self.name+'-'+self.college_name'''

def create_profile(sender, **kwargs):
	if(kwargs['created']):
		user_profile=TeacherProfile(user=kwargs['instance'])




post_save.connect(create_profile, sender=User)	
'''class Teacherdata(models.Model):
	id_no=models.CharField(max_length=100, primary_key=True)
	name=models.CharField(max_length=150)
	college_name=models.CharField(max_length=250)
	password=models.CharField(max_length=50)'''

