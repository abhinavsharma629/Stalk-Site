from django.db import models


class StudentData(models.Model):
    er_no = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150)
    college_name = models.CharField(max_length=250)
    codeforces = models.CharField(max_length=100)
    codechef = models.CharField(max_length=100)
    spoj = models.CharField(max_length=100)
    hackerrank = models.CharField(max_length=100)
    hackerearth = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    '''def __str__(self):
		return self.er_no+'-'+self.name+'-'+self.college_name'''


class StudentDetails(models.Model):
    er_no = models.OneToOneField(
        StudentData, on_delete=models.CASCADE, primary_key=True)
    codeforces = models.CharField(max_length=100, default=0)
    codechef = models.CharField(max_length=100, default=0)
    spoj = models.CharField(max_length=100, default=0)
    hackerearth = models.CharField(max_length=100, default=0)
    github = models.CharField(max_length=100, default=0)
