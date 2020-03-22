from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver\chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") \
            .send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input") \
            .send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button") \
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]") \
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, ' /{}')]".format(self.username))
        self.driver.find_element_by_xpath("//a[contains(@href, '/obserwujących')]")\
            .click()


    def like_photo(self, hashtag):
        self.driver.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
        sleep(2)
        for i in range(1, 2):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

        # searching for photo link
        hrefs = self.driver.find_elements_by_css_selector("article a")
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        for index, href in enumerate(pic_hrefs):
            self.driver.get(href)
            like_button = self.driver.find_element_by_css_selector("section > span:first-child > button")
            sleep(1)
            like_button.click()
            sleep(1)


my_bot = InstaBot("login ", "password")
my_bot.like_photo('hashtag')