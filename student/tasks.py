from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
import time
from .models import *
from .codechef import codechef
from .codeforces import codeforces
from .hackerearth import hackerearth
from .github import github
from .spoj import spoj
import requests
import mechanicalsoup
import sys
import re
import getpass
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
browser = mechanicalsoup.StatefulBrowser()


@task(name="update database")
def delete_notifications():
    details = StudentData.objects.all()
    for i in details:
        if(len(i.er_no) > 0):

            # User objects
            obj = StudentData.objects.get(er_no=i.er_no)
            print(obj)
            cc_user = obj.codechef
            spoj_user = obj.spoj
            cf_user = obj.codeforces
            he_user = obj.hackerearth
            github_user = obj.github

            # Problems/Projects Solved/done
            codechef1 = []
            codechef1 = codechef(headers, browser, cc_user)
            print(codechef1)
            if(len(spoj_user) != 0):
                spoj_count = spoj(headers, browser, spoj_user)
            else:
                spoj_count = 0
            if(len(cf_user) != 0):
                codeforces1 = codeforces(headers, browser, cf_user)
            else:
                codeforces1 = 0
            if(len(he_user) != 0):
                hackerearth1 = hackerearth(headers, browser, he_user)
            else:
                hackerearth1 = 0

            if(len(github_user) != 0):
                github1 = github(headers, browser, github_user)
            else:
                github1 = 0

            particularstudent = StudentDetails(
                er_no=i, codeforces=codeforces1, codechef=codechef1, spoj=spoj_count, hackerearth=hackerearth1, github=github1)
            particularstudent.save()
