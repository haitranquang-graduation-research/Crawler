import random
import requests
from pyquery import PyQuery
from flask_restful import Api, Resource
from flask import Flask
import config
app = Flask(__name__)
api = Api(app)

url_list = []

def general_crawl(url, site):
    rq = requests.get(url)
    r = rq.text.encode("utf8")
    pq = PyQuery(r)
    for element in site['elements']:
        if (element['type'] == 'HREF'):
            # print(element['path'])
            title_elements = [title for title in pq(
                element['path']).items()]
            # print(len(title_elements))
            for title_element in title_elements:
                try:
                    url = title_element.attr('href')
                    if url.startswith('/'):
                        url = url[1:]
                    if (site['name'] not in url) and (not url.startswith('https')):
                        url = site['domain'] + url
                    # print(url)
                    # url_dto = {}
                    # url_dto['url'] = url
                    # requests.post(config.get_parser_url(), json=url_dto, timeout=1)
                    url_list.append(url)
                except:
                    continue


@app.route('/crawl', methods=['GET'])
def crawl():
    rq = requests.get(config.get_news_specs_url())
    sites = rq.json()
    for site in sites:
        # print(site['domain'])
        try:
            general_crawl(site['domain'], site)
            for path in site['crawlPaths']:
                general_crawl(path['path'], site)
        except:
            continue
    random.shuffle(url_list)
    for url in url_list:
        # print(url)
        url_dto = {}
        url_dto['url'] = url
        requests.post(config.get_parser_url(), json=url_dto)
    return 'Success'


@app.route('/recrawl', methods=['GET'])
def recrawl():
    rq = requests.get(config.get_missing_data_url())
    urls = rq.json()
    for url in urls:
        try:
            # print(url)
            requests.post(config.get_parser_url(), json=url)
        except:
            continue
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)
