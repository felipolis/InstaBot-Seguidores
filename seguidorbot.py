from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe')

    # //input[name="username"]
    # //input[name="password"]

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        sleep(3)

        user_element = driver.find_element_by_xpath('//input[@name="username"]')
        user_element.clear()
        user_element.send_keys(self.username)

        sleep(2)

        password_element = driver.find_element_by_xpath('//input[@name="password"]')
        password_element.clear()
        password_element.send_keys(self.password)
        sleep(1)
        password_element.send_keys(Keys.RETURN)

        sleep(8)

        self.curtir_fotos('memesbr')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        # [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_css_selector('button [aria-label="Curtir"]').click()
                sleep(19)
            except Exception as e:
                print(e)
                sleep(5)


user = str(input("Digite o nome de usuario: "))
passw = str(input("Digite a sua senha: "))
archanjoBot = instagramBot(user, passw)
archanjoBot.login()
