from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.window import WindowTypes

from config import parser_url

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="chromedriver_win32/chromedriver", options=options)
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

links = [
    # "https://vnexpress.net/goc-nhin/binh-luan-nhieu",
    # "https://vnexpress.net/goc-nhin/giao-duc-tri-thuc",
    # "https://vnexpress.net/goc-nhin/van-hoa-loi-song",
    # "https://vnexpress.net/goc-nhin/moi-truong",
    "https://vnexpress.net/the-gioi",
    "https://vnexpress.net/kinh-doanh",
    "https://vnexpress.net/khoa-hoc",
    "https://vnexpress.net/phap-luat",
    "https://vnexpress.net/giao-duc",
    "https://vnexpress.net/so-hoa",
    "https://vnexpress.net/thoi-su"]

all_urls = []


def get_all_urls_from_link(link_input):
    browser.get(link_input)
    sleep(1)
    titles = browser.find_elements(by=By.CSS_SELECTOR, value=".title-news > a")

    sentences = []

    # remove link quảng cáo, abcxyz, ...
    for title in titles:
        title_link = title.get_attribute('href')
        if not title_link.startswith("https://vnexpress.net"):
            titles.remove(title)
        else:
            body = {}
            try:
                body['url'] = title_link
                print(body)
                print(parser_url())
                rq = requests.post(
                    url=parser_url(), json=body)
            except:
                continue
            all_urls.append(title_link)
            print(len(all_urls))

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

# for url in all_urls:
#     print("link: ", url)
