from selenium import webdriver
# import is not working yet, need to find python.exe folder and move webdriver to same folder

browser = webdriver.Firefox()

browser.get("https://www.google.com/")

browser.quit()


# descobrir onde está o python
#import os
#import sys

#print(os.path.dirname(sys.executable))