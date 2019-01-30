from bs4 import BeautifulSoup


def codeforces(headers, browser, cf_user):
    page_no = 1
    count = 0
    urlcf = "https://codeforces.com/profile/"
    urlcf += cf_user
    url3 = "https://codeforces.com/submissions/"+cf_user+"/page/"+str(page_no)
    cont = browser.get(url3, headers=headers)
    r1 = BeautifulSoup(cont.content, 'lxml')
    data = r1.find('table', class_="status-frame-datatable")
    a = []
    cou = 0
    a1 = []

    for r2 in r1.find_all('div', class_='pagination'):
        cou = cou+1
        if(cou == 2):
            for r3 in r2.find_all('span', class_='page-index'):
                a1.append(r3.get_text())
    end_page = (int)(a1[(len(a1))-1])

    while(page_no <= end_page):
        for r2 in data.find_all('tr'):
            r3 = r2.find_all('td', class_='status-small')
            for r4 in r3:
                r5 = r4.find_all('a')
                for r6 in r5:
                    ll = ""
                    text = "".join(
                        [ll.rstrip() for ll in r6.get_text().splitlines() if ll.strip()])
                    a.append(text.strip())

        page_no = page_no+1
        url_new = ""
        url_new = "https://codeforces.com/submissions/" + \
            cf_user+"/page/"+str(page_no)
        cont = browser.get(url_new, headers=headers)
        r1 = BeautifulSoup(cont.content, 'lxml')
        data = r1.find('table', class_="status-frame-datatable")

    a = list(set(a))
    return len(a)
