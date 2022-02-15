# Lekcja22
# Selenium Webdriver

# [20:45] Буйлук Андрей
import os
import time
from selenium import webdriver

#for mac
# import os
# driver = webdriver.Firefox()
# driver.get('https://chromedriver.chromium.org/downloads')
# driver = webdriver.Chrome()
# driver.get('https://chromedriver.chromium.org/downloads')



# [20:53] Буйлук Андрей
# from selenium import webdriver
# for mac
# EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# driver = webdriver.Chrome(executable_path=EXE_PATH)
# driver.get('https://google.com')import os

# driver_path_chrome = os.getcwd() + '\chromedriver.exe'
driver_path_firefox = os.getcwd() + '\geckodriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path_chrome)
# driver.get('https://chromedriver.chromium.org/downloads')
driver = webdriver.Firefox(executable_path=driver_path_firefox)
driver.get('https://chromedriver.chromium.org/downloads')
driver.get_screenshot_as_file('screen01.png')
# driver.quit()
time.sleep(5)
driver = webdriver.Firefox(executable_path=driver_path_firefox)
driver.get('https://www.wp.pl')
driver.get_screenshot_as_file('screen02.png')
driver.quit()


# [21:34] Швец Людмила Андреевна
# Это я скинула для mac, заработало без ошибок
#
# [21:36] Швец Людмила Андреевна
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# # for mac
# # EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# # driver = webdriver.Chrome(executable_path=EXE_PATH)
# # driver.get('https://google.com')import os
#
# # driver_path_chrome = os.getcwd() + 'chromedriver.exe'
# driver_path_firefox = os.getcwd() + '/geckodriver'
# s = Service(driver_path_firefox)
#
#
# # driver = webdriver.Chrome(executable_path=driver_path_chrome)
# # driver.get('https://chromedriver.chromium.org/downloads')driver = webdriver.Firefox(service=s)
# driver.get('https://chromedriver.chromium.org/downloads')