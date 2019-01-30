from bs4 import BeautifulSoup
def codechef(headers,browser,cc_user):
	head=[]
	dict1=[]
	urlc="https://www.codechef.com/users/"
	urlc+=cc_user
	cont=browser.get(urlc,headers=headers)
	html=cont.text
	html.encode('utf-8')
	st="Could not find page you requested for."
	if(st in html):
		dict1.append("None")
		dict1.append("None")
		return dict1
	else:
		cchome=BeautifulSoup(cont.content,'lxml')
		userofsameinstitute=cchome.find('section',class_="user-details")
		r2=cchome.find('section',class_="rating-data-section problems-solved")
		r3=r2.find('div',class_="content")
		for heading in r3.find_all('h5'):
			head.append(heading.get_text())

		dict1.append(head[0][14:((len(head[0]))-1)])
		dict1.append(head[1][18:((len(head[1]))-1)])
		return dict1