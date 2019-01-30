from django.shortcuts import render, redirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q
from .codechef import codechef
from .spoj import spoj
from .codeforces import codeforces
from .hackerearth import hackerearth
from .github import github
import requests
import mechanicalsoup
import sys
import re
import getpass
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
browser = mechanicalsoup.StatefulBrowser()


def index(request):
    return render(request, 'student/combined.html',)


# Registration
def register(request):
    if(request.method == 'POST'):
        form = StudentSubmit(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = StudentSubmit()

    return render(request, 'student/index.html', {'form': form})


# Success Page
def success(request):
    args = {}
    return render(request, 'student/success.html', args)


# Search
def search(request):
    query = request.GET.get('q')
    details = StudentData.objects.all()
    for i in details:
        print(i)
    if(query):
        match = StudentData.objects.filter(Q(er_no__iexact=query)).values()
        if(match):
            args = {'match': match}
            return render(request, 'student/details.html', args)
        else:
            return HttpResponseRedirect('search')
    args = {}
    return render(request, 'student/search.html', args)


# Stalk
def number(request):
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

				#Extracting from the dict stored in the column
                code = []
                s = ""
                for i in codedict:
                    if(i != "'" and i != '[' and i != ']'):
                        s = s+i
                    else:
                        code.append(s)
                        s = ""
                print(code[4])
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

    return HttpResponseRedirect('search')
