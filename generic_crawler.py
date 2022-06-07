
import requests
from pyquery import PyQuery
from flask_restful import Api, Resource
from flask import Flask
import config
app = Flask(__name__)
api = Api(app)
print('Hello')


@app.route('/crawl', methods=['GET'])
def crawl():
    rq = requests.get(config.get_news_specs_url())
    sites = rq.json()
    for site in sites:
        print(site['domain'])
        rq = requests.get(site['domain'])
        r = rq.text.encode("utf-8")
        pq = PyQuery(r)

        for element in site['elements']:
            if (element['type'] == 'HREF'):
                print(element['path'])
                title_elements = [title for title in pq(
                    element['path']).items()]
                print(len(title_elements))
                for title_element in title_elements:
                    url = title_element.attr('href')
                    if site['name'] not in url:
                        url = site['domain'] + url
                    print(url)
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)
