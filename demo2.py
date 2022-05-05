from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(executable_path="chromedriver.exe")
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

links = ["https://vnexpress.net/the-gioi",
         "https://vnexpress.net/kinh-doanh",
         "https://vnexpress.net/khoa-hoc",
         "https://vnexpress.net/du-lich",
         "https://vnexpress.net/giao-duc"]

all_urls = []


def get_all_urls_from_link(link_input):
    browser.get(link_input)
    sleep(5)
    titles = browser.find_elements(by=By.CSS_SELECTOR, value=".title-news > a")

    sentences = []

    # remove link quảng cáo, abcxyz, ...
    for title in titles:
        title_link = title.get_attribute('href')
        if not title_link.startswith("https://vnexpress.net"):
            titles.remove(title)
        else:
            all_urls.append(title_link)

    # phần này để tách từng câu trong content bài viết
    # for title in titles:
    #     title_link = title.get_attribute('href')
    #     print("title: ", title_link)
    #
    #     # browser.switch_to.new_window(WindowTypes.TAB)
    #     # sleep(2)
    #     # browser.get(title_link)
    #
    #     # crawl content in this tab
    #     sleep(5)
    #     paragraphs = browser.find_elements(by=By.CSS_SELECTOR, value="article > p")  # get all <p> tags in <article>
    #     paragraphs.pop()  # remove the last <p> tag (usually redundant)
    #
    #     # convert array of paragraphs to array of sentences
    #     for paragraph in paragraphs:
    #         pre_sentences = paragraph.text.split(".")
    #         for pre_sentence in pre_sentences:
    #             if pre_sentence:  # check sentence not blank
    #                 sentences.append(pre_sentence)
    #
    #     sleep(1)
    #
    #     # print split sentences
    #     for sentence in sentences:
    #         print("sentence: ", sentence)


for link in links:
    get_all_urls_from_link(link)

for url in all_urls:
    print("link: ", url)

