from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        ''' email = bot.find_element_by_class_name('session[username_or_email]') '''
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            # tweets = bot.find_element_by_name('article')
            # tweets = bot.find_elements_by_class_name('css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll')
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            tweets = bot.find_elements_by_class_name(
                'css-4rbku5 css-18t94o4 css-1dbjc4n')
            print(tweets)
            # links = [elem.get_attribute('href') for elem in tweets]
            # print(links)


ed = TwitterBot(os.environ.get('email'), os.environ.get('password'))
ed.login()
ed.like_tweet('Girls')
