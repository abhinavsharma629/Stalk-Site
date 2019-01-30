from bs4 import BeautifulSoup
def spoj(headers,browser,spoj_user):
	url2="https://www.spoj.com/users/"
	url2+=spoj_user
	cont=browser.get(url2,headers=headers)
	r1=BeautifulSoup(cont.content,'lxml')
	r2=r1.find('table',class_="table table-condensed")
	spoj_count=0
	s=""
	for problems in r2.find_all('td'):
		st=problems.get_text()
		if(len(st)==0):
			continue
		else:
			spoj_count=spoj_count+1;
	return spoj_count