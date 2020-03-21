from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver\chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") \
            .send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input") \
            .send_keys(pw)
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


    def make_like(self, hashtag):
        self.driver.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
        #     .send_keys(hashtag)
        # sleep(3)
        # self.driver.find_element_by_xpath("//a[contains(@href, '/#{}')]".format(hashtag)) \
        #     .click()
        # hash_menu = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div")
        # print(hash_menu)

my_bot = InstaBot("login", "password")
my_bot.make_like('canolli')