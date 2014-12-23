# -*- coding: utf-8 -*-

import logging
import re
import requests
from BeautifulSoup import BeautifulSoup

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

class Scraper(object):
    """ # """

    headers = {
        "User-agent": "KPCC - Southern California Public Radio (ckeller@scpr.org)"
    }

    live_html = "http://www.niemanlab.org/collection/predictions-2015/"

    def handle(self, *args, **kwargs):
        """ # """
        print "Running Nieman Prediction Scraper"
        self.get_list_of_content_urls()
        self.get_each_article()

    def get_list_of_content_urls(self):
        """ # """

        r = requests.get(self.live_html, headers=self.headers)
        soup = BeautifulSoup(r.text)
        item_list = soup.findAll("div", {"class": "predix-loop-article"})
        self.article_list = []
        for item in item_list:
            article_author = item.find("span", {"class": "newfront-other-recent-author"}).text.encode("utf-8")
            article_url = item.findAll("a")[1]["href"]
            article_headline = item.findAll("a")[1].text.encode('utf-8')
            file_name = re.sub(r'\W+', ' ', article_headline)
            file_name = file_name.lower().replace(" ", "-")
            self.article_list.append({
                "article_author": article_author,
                "article_url": article_url,
                "article_headline": article_headline,
                "file_name": file_name
            })

    def get_each_article(self):
        """ # """
        html_file= open("index.html", "w")
        html_file.write("<h1>Nieman Lab Predictions for Journalism 2015</h1>")
        for obj in self.article_list:
            print "Scraping %s" % (obj["article_headline"])
            r = requests.get(obj["article_url"], headers=self.headers)
            soup = BeautifulSoup(r.text)
            article_text = soup.findAll("div", {"class": "simple-body"})[0]
            article_text = str(article_text)
            article_text = article_text.replace("&#8217;", "'").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("—", "-")
            obj["article_text"] = self.remove_img_tags(article_text)
            html_file.write("<h4>%s</h4>" % (obj["article_headline"]))
            html_file.write("<h5>By %s</h5>" % (obj["article_author"]))
            html_file.write("<h6><a href='%s'>Originally published on Nieman Lab</a></h6>" % (obj["article_url"]))
            html_file.write(obj["article_text"])
            html_file.write("<hr />")
            html_file.write("<br />")
        print "Processing finished"
        html_file.close()

    def remove_img_tags(self, data):
        p = re.compile(r"<img.*?/>")
        return p.sub("", data)

if __name__ == '__main__':
    scrape = Scraper()
    scrape.handle()
