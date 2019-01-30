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

            #User objects
            obj = StudentData.objects.get(er_no=i.er_no)
            cc_user = obj.codechef
            spoj_user = obj.spoj
            cf_user = obj.codeforces
            he_user = obj.hackerearth
            github_user = obj.github

            # Problems/Projects Solved/done
            codechef1 = []
            codechef1 = codechef(headers, browser, cc_user)
            print(codechef1)
            spoj_count = spoj(headers, browser, spoj_user)
            codeforces1 = codeforces(headers, browser, cf_user)
            # hackerearth1='344'
            # hackerearth(headers,browser,he_user)
            github1 = github(headers, browser, github_user)

            particularstudent = StudentDetails(
                er_no=i, codeforces=codeforces1, codechef=codechef1, spoj=spoj_count, hackerearth="344", github=github1)
            particularstudent.save()
