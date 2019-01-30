from django import forms
from .models import TeacherProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
	#id_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	#name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)
	#college_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)

	class Meta:
		model= User
		#fields=['username','id_no','name','college_name','password1','password2']
		fields=['username','first_name','last_name','password1','password2']
	def save(self,commit=True):
		user=super(RegistrationForm, self).save(commit=False)
		#user.id_no=self.cleaned_data['id_no']
		#user.name=self.cleaned_data['name']
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		#user.college_name=self.cleaned_data['college_name']
		if(commit):
			user.save()

		return user





class LoginForm(AuthenticationForm):
	id_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=100)


'''class TeacherSubmit(forms.ModelForm):
	id_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)
	college_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)
	password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=50)

	class Meta:
		model= TeacherData
		fields=['id_no','name','college_name','password']'''

class ProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = TeacherProfile
		fields=['id_no','name','college_name','password']