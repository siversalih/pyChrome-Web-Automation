from time import sleep
import os

par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing...Exiting program."
    exit(1)

print "\n"
print "***** Welcome to pyChrome Demo *****"
print "\nThis demo shows how one could leverage pyChrome engine to autonomously perform the following tasks"

print "1. Open the URL www.yahoo.com \n" \
      "2. Find the most trending topic on Yahoo.com \n" \
      "3. Click on Top Trending Topic \n" \
      "4. In the resulting page, click the second link. \n"

raw_input('\nPress Enter to Start\n>')
browser = PyChrome()
point = (0,0)
browser.position(point)
sleep(1)
size = (820,800)
browser.size(size)
sleep(1)
link = "www.yahoo.com"
browser.open(link)
sleep(1)
locator = "trending-list"
element = browser.findElementByClass(locator)
sleep(1)
locator = "li"
elements = browser.findElementsByTag(locator,element)
sleep(1)
element = elements[0]
browser.clickElement(element)
sleep(1)
locator = "ov-a"
elements = browser.findElementsByClass(locator)
sleep(1)
browser.selectElement(elements[1])
browser.clickLink()

print "\n*****Demo Complete*****"
raw_input('\nPress Enter to Quit\n>')

browser.quit()
