from bs4 import BeautifulSoup


def github(headers, browser, github_user):
    urlgit = "https://github.com/"
    urlgit += github_user+"?tab=repositories"
    cont = browser.get(urlgit, headers=headers)
    r1 = BeautifulSoup(cont.content, 'lxml')
    find_repo = r1.find('span', class_="Counter")
    find_repo_no = find_repo.get_text()
    find_repo_no = find_repo_no.replace(" ", "")
    if(len(find_repo_no) == 0):
        return "None"
    else:
        return find_repo_no
