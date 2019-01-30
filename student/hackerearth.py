from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def hackerearth(headers, browser, he_user):
    if(len(he_user) == 0):
        problems = "No Account Provided/ Present"
    else:
        url = "https://www.hackerearth.com/login/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        user = driver.find_element_by_id("id_login")
        passw = driver.find_element_by_id("id_password")
        user.send_keys("your_hackerearth_username")
        passw.send_keys("your_hackerearth_password")
        driver.find_element_by_name("signin").click()

        # after logging in redirecting to the page needed
        url1 = "https://www.hackerearth.com/@"+he_user
        driver.get(url1)
        cont1 = driver.execute_script(
            "return document.documentElement.outerHTML")
        driver.quit()
        r1 = BeautifulSoup(cont1, 'lxml')
        # print(r1.prettify())
        problem = r1.find('span', class_="dark weight-700")
        problems = problem.get_text()
    return problems
