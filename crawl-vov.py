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
# options.headless = True
browser = webdriver.Chrome(
    executable_path="chromedriver_win32/chromedriver")
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

links = ["https://vov.vn/chinh-tri/dang",
         "https://vov.vn/chinh-tri/quoc-hoi",
         "https://vov.vn/xa-hoi/tin-24h",
         "https://vov.vn/viec-lam",
         "https://vov.vn/xa-hoi/giao-duc",
         "https://vov.vn/tin-nong",
         "https://vov.vn/van-hoa/van-hoc",
         "https://vov.vn/kinh-te/thi-truong",
         "https://vov.vn/quan-su-quoc-phong/vu-khi",
         "https://vov.vn/quan-su-quoc-phong/phan-tich",
         "https://vov.vn/quan-su-quoc-phong/viet-nam",
         "https://vov.vn/van-hoa/nghe-si",
         "https://vov.vn/giai-tri/hau-truong-showbiz",
         "https://vov.vn/thoi-trang-lam-dep",
         ]

all_urls = []


def get_all_urls_from_link(link_input):
    browser.get(link_input)
    sleep(5)
    titles = browser.find_elements(by=By.CSS_SELECTOR, value=".vovvn-title")

    sentences = []

    # remove link quảng cáo, abcxyz, ...
    for title in titles:
        title_link = title.get_attribute('href')
        if not title_link.startswith("https://vov.vn"):
            titles.remove(title)
        else:
            print(title_link)
            try:
                body = {}
                body['url'] = title_link
                print(body)
                rq = requests.post(
                    url=parser_url(), json=body)
            except:
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

