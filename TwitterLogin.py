import stdiomask
from selenium import webdriver
import time

usn = input("Please Type Username: ")
ps = stdiomask.getpass()


class ChromeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https:/twitter.com')
        time.sleep(2)
    #finds button and clicks
        but = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
        but.click()
        time.sleep(1)
    
    #finds username bar
        un = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        
        #sends the username letters
        un.send_keys(usn)
        time.sleep(1)
        #finds password bar
        un = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        #sends the password letters
        un.send_keys(ps)
        
        #log button press
        logbut = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        logbut.click()


bot = ChromeBot()
bot.login()

