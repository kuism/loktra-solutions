from bs4 import BeautifulSoup
import urllib2
from product import Product
import re
from tabulate import tabulate


class Search():
    def __init__(self, keyword):
        self.keyword = keyword
        self.pagination = 0
        self.products = {}
        self.search_url = "http://www.shopping.com/products?KW={}".format(
            keyword)
        self.pagination_url = "http://www.shopping.com/products~PG-{}?KW={}"

    @staticmethod
    def try_url(url):
        try:
            return urllib2.urlopen(url)
        except Exception, e:
            raise (e)

    def execute(self, page_no=0):
    	if page_no in self.products:
            return self.products[page_no], self.pagination
        else:
            self.products[page_no] = []

        print "Please wait while we bring you the results. :)"
        if page_no == 0:
            url = self.search_url
        else:
            url = self.pagination_url.format(page_no, self.keyword)

        page = Search.try_url(url)
        soup = BeautifulSoup(page, "html.parser")

        if page_no == 0:
            pagination = soup.find_all(class_="paginationNew")
            if pagination:
                self.pagination = int("".join(
                    re.findall(r'\d+',
                               pagination[0].find_all("a")[-2].get_text())))


        items = soup.find_all(class_="gridBox")
        for item in items:
            name = str(
                item.find_all(
                    class_="quickLookGridItemFullName")[0].get_text())
            price = "".join(
                re.findall(
                    r'[\.,\d]+',
                    str(item.find_all(class_="productPrice")[0].get_text())))
            image = str(item.find_all(class_="imgZoomUrl149")[0].get("src"))
            product = Product(name, image, price)
            self.products[page_no].append(product)

        return self.products[page_no], self.pagination


if __name__ == "__main__":
    Search.try_url("asd")
