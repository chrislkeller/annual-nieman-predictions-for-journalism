# -*- coding: utf-8 -*-

import re
import requests
import logging
from BeautifulSoup import BeautifulSoup

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

class Scraper(object):
    """ # """

    headers = {
        "User-agent": ""
    }

    # year = 2015
    year = 2016

    # live_html = "http://www.niemanlab.org/collection/predictions-2015/"
    live_html = "http://www.niemanlab.org/collection/predictions-2016/"

    def handle(self, *args, **kwargs):
        """ # """
        print "Running Nieman Prediction Scraper"
        this_article_list = self.get_list_of_content_urls()
        self.get_each_article(this_article_list)

    def get_list_of_content_urls(self):
        """ # """
        r = requests.get(self.live_html, headers=self.headers)
        soup = BeautifulSoup(r.text)
        soup = soup.find("div", {"class": "predix2016-mostrecentorder"})
        item_list = soup.findAll("a")
        this_article_list = []
        for item in item_list:
            article_author = item.find("div", {"class": "newfront-other-recent-author"}).text.encode("utf-8")
            article_url = item["href"]
            article_headline = item.find("div", {"class": "predix-loop-headline"}).text.encode("utf-8")
            file_name = re.sub(r'\W+', ' ', article_headline)
            file_name = file_name.lower().replace(" ", "-")
            this_article_list.append({
                "article_author": article_author,
                "article_url": article_url,
                "article_headline": article_headline,
                "file_name": file_name
            })
        logger.debug(this_article_list)
        return this_article_list

    def get_each_article(self, article_list):
        """ # """
        filename = "_%d_predictions_index.html" % (self.year)
        html_file= open(filename, "w")
        html_file.write("<h1>Nieman Lab Predictions for Journalism %d</h1>" % (self.year))
        for obj in article_list:
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
