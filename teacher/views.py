from django.shortcuts import render, redirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from student.models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
import bcrypt
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
import hashlib
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def regisearch(request):
    return render(request, 'teacher/register.html')


def detail(request):
    if(request.method == 'POST'):
        query = request.POST.get('q')
        query1 = request.POST.get('q1')
        query2 = hashlib.md5(str.encode(query1))
        query2 = query2.digest()
        user = authenticate(id_no=query, password=query1)
        obj = TeacherData.objects.all()
        print(obj)
        if(query and query1):
            match = TeacherData.objects.filter(
                Q(id_no__iexact=query) and Q(password__iexact=query2)).values()
            if(match):
                print(match)
                obj = TeacherData.objects.get(id_no=query)
                # login(request,obj.id_no)
                print(obj.id_no)
                print(obj.college_name)
                obj1 = StudentData.objects.filter(
                    Q(college_name__icontains=obj.college_name)).values()
                print(obj1)
                args = {'obj1': obj1}
                return render(request, 'teacher/userdetails.html', args)
            else:
                return render(request, 'teacher/noaccount.html')

        else:
            return render(request, 'teacher/noaccount.html')
    else:
        return render(request, 'teacher/login.html')


def register(request):

    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'teacher/success.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'teacher/makeaccount.html', {'form': form})


def info(request):
    query = request.GET.get('q')
    details = StudentData.objects.all()
    if(query):
        match = StudentData.objects.filter(Q(er_no__iexact=query)).values()
        if(match):
            obj = StudentData.objects.get(er_no=query)
            if((obj.er_no) == ""):
                args = {}
                return render(request, 'student/stalk.html', args)
            else:

                # User Details
                obj1 = StudentDetails.objects.get(er_no=query)
                codedict = obj1.codechef

                # Extracting from the dict stored in the column
                code = []
                s = ""
                for i in codedict:
                    if(i != "'" and i != '[' and i != ']'):
                        s = s+i
                    else:
                        code.append(s)
                        s = ""

                spoj_count = obj1.spoj
                codeforces1 = obj1.codeforces
                hackerearth1 = obj1.hackerearth
                github1 = obj1.github

        # User Handles
                obj = StudentData.objects.get(er_no=query)
                cc_user = obj.codechef
                spoj_user = obj.spoj
                cf_user = obj.codeforces
                he_user = obj.hackerearth
                github_user = obj.github

        # Url's Of User's Profile
                urlcf = "https://codeforces.com/profile/"
                urlcf += cf_user
                url2 = "https://www.spoj.com/users/"
                url2 += spoj_user
                urlc = "https://www.codechef.com/users/"
                urlc += cc_user
                urlhe = "https://www.hackerearth.com/@"
                urlhe += he_user
                urlgit = "https://github.com/"
                urlgit += github_user+"?tab=repositories"

                args = {'urlc': urlc, 'urlhe': urlhe, 'url2': url2, 'urlcf': urlcf, 'urlgit': urlgit,
                        'fully': code[2], 'partial': code[4], 'spoj': spoj_count, 'codeforces': codeforces1, 'hackerearth': hackerearth1, 'github': github1}
                return render(request, 'student/stalk.html', args)
    return HttpResponseRedirect('detail')


@login_required(login_url='/teacher/login')
def profile(request):
    # print(request.user.first_name)
    # print(request.GET.get('request.user'))
    args = {'user': request.user}
    return render(request, 'teacher/search.html', args)


@login_required(login_url='/teacher/login')
def search(request):
    print(request)
    if(request.method == "GET"):
        args = {'details': request.user}
        return render(request, 'teacher/search.html', args)
    else:
        return HttpResponseRedirect('/teacher/login')


@login_required(login_url='/teacher/login')
def edit_profile(request):
    # print(request.user)
    if(request.method == 'POST'):
        form = UserChangeForm(request.POST, instance=request.user)

        if(form.is_valid()):
            form.save()
            return redirect('/teacher/profile')
    else:
        form = UserChangeForm(instance=request.user)
    args = {'form': form}
    return render(request, 'teacher/edit_profile.html', args)


@login_required(login_url='/teacher/login')
def all_info(request):
    if(request.method == 'GET'):
        query = request.GET.get('q')
        print(query)
        details = StudentData.objects.all()
        if(query):
            obj1 = StudentData.objects.filter(
                Q(college_name__icontains=query) or Q(er_no__iexact=query)).values()
            print(obj1)
            args = {'obj1': obj1}
            return render(request, 'teacher/userdetails.html', args)
        else:
            return HttpResponse("NO USERS AVAILABLE")

    return render(request, 'teacher/userdetails.html', args)
