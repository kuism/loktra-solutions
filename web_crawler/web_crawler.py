from product import Product
from search import Search
from tabulate import tabulate


class WebCrawler():
    def getOptions(self):
    	print "\n"
        print tabulate([["Search", 1], ["Exit", 0]], headers=['Option', 'Key'])
        key = raw_input("\nInput keys to continue:  ")
        page_no = 0
        try_again = False
        if key == "1":
            keyword = raw_input("Input the keyword:  ")
            current_search = Search(str(keyword))
            while True:
            	try:
                	products, pagination = current_search.execute(page_no)
                except:
                	print "Something went wrong. Please start again"
                	return

                if len(products) > 0:
	                print tabulate(
	                    [[product.name, product.price] for product in products],
	                    headers=['Name', 'Price'])
	                print "\n\n"
	                print "{} more pages to display.".format(pagination)
	                page_no = int(
	                    raw_input(
	                        "Input page number to continue or Type 0 To Main Menu:  "))

	                if page_no == 0:
	                	self.getOptions()
	                	break
	                elif page_no > pagination or page_no < 0:
	                 	print "Incorrect Page Number"
	                 	self.getOptions()
	                 	break
                else:
					print "\n 0 Results to display"
					self.getOptions()
					break
        else:
            return


def main():
    WebCrawler().getOptions()


if __name__ == '__main__':
    main()