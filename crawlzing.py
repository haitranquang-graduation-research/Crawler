from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.window import WindowTypes

from config import parser_url
options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="chromedriver_win32/chromedriver", options=options)

links = ["https://zingnews.vn/cong-nghe.html",
         "https://zingnews.vn/thoi-su.html",
         "https://zingnews.vn/suc-khoe.html",
         "https://zingnews.vn/oto-xe-may.html",
         "https://zingnews.vn/am-nhac.html",
         "https://zingnews.vn/phim-anh.html",
         "https://zingnews.vn/tam-nhin.html",
         "https://zingnews.vn/phan-tich-the-gioi.html",
         "https://zingnews.vn/phim-anh.html",
         "https://zingnews.vn/dinh-duong.html",
         "https://zingnews.vn/xu-huong.html",
         "https://zingnews.vn/am-thuc.html",
         "https://zingnews.vn/vu-an.html",
         "https://zingnews.vn/xe-may.html",
         "https://zingnews.vn/thoi-trang.html",
         "https://zingnews.vn/esports-the-thao.html",
         ]

all_urls = []


def get_all_urls_from_link(link_input):
    browser.get(link_input)
    titles = browser.find_elements(
        by=By.CSS_SELECTOR, value=".article-title > a")

    sentences = []

    # remove link quảng cáo, abcxyz, ...
    for title in titles:
        title_link = title.get_attribute('href')
        if not title_link.startswith("https://zingnews.vn"):
            titles.remove(title)
        else:
            print(title_link)
            try:
                body = {}
                body['url'] = title_link
                print(body)
                rq = requests.post(
                    url=parser_url(), json=body)
            except Exception as e:
                print(e)
                continue
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
