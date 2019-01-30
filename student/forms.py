from django import forms
from .models import StudentData

class StudentSubmit(forms.ModelForm):
	er_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}),required=True,max_length=100)
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=150)
	college_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)
	codeforces=forms.CharField(widget=forms.TextInput(),required=False,max_length=100)
	codechef=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	spoj=forms.CharField(widget=forms.TextInput(),required=False,max_length=100)
	hackerrank=forms.CharField(widget=forms.TextInput(),required=False,max_length=100)
	hackerearth=forms.CharField(widget=forms.TextInput(),required=False,max_length=100)
	github=forms.CharField(widget=forms.TextInput(), required=False, max_length=100)
	class Meta:
		model= StudentData
		fields=['er_no','name','college_name','codeforces',	'codechef','spoj','hackerrank','hackerearth', 'github']
