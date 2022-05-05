from random import randint
from requests import head
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')

while True:
    browser.get(
        "https://vnexpress.net/tin-tuc-24h")
    browser.switch_to.window(browser.window_handles[0])

    header = 1
    for element in range(30):
        browser.get(
            "https://vnexpress.net/tin-tuc-24h")
        browser.switch_to.window(browser.window_handles[0])
        count = 0
        print(element)
        while True:
            try:
                if count > 10:
                    break
                start = browser.find_element_by_tag_name('html')
                if count > 0:
                    start.send_keys(Keys.PAGE_DOWN)
                count = count + 1
                try:
                    next_news = browser.find_element_by_xpath(
                        '//*[@id="automation_TV0"]/div/article[' + str(element) + ']/div/a/picture/img')
                except:
                    continue

                next_news.click()
                print(browser.current_url)
                # browser.switch_to.window(browser.window_handles[1])
                try:
                    header = browser.find_element(
                        by=By.CLASS_NAME, value="title-detail")
                    print(header.text)
                except:
                    print(header)
                sleep(1)

                break
            except:
                continue


browser.close()
