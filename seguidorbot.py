from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


class instagramBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.driver = Chrome()
        self.wdw = WebDriverWait(self.driver, 10)

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

        self.curtir_fotos(self.hashtag)

    def curtir_fotos(self, hashtag):
        wdw = self.wdw
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)

            sleep(5)

            try:
                driver.find_element_by_css_selector('button [aria-label="Curtir"]').click()
                sleep(15)
            except Exception as e:
                print(e)
                sleep(5)


user = str(input("Digite o nome de usuario: "))
passw = str(input("Digite a sua senha: "))
hash = str(input("Digite uma hashtag [sem a #]: "))
archanjoBot = instagramBot(user, passw, hash)
archanjoBot.login()
