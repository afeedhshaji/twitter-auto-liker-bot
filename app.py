from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)  # wait for the page to load it's contents
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def likeTweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')  # js to scroll by a bit
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            # print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(3)
                except Exception as e:
                    print("Error..")


'''
Instantiate the class with your username and password as the parameters.
Call the login method and likeTweet method.

'''
