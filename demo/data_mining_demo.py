import os
import sys
import time

par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)
sys.path.insert(0, par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing from {}\nTry copy {} to pyChrome.py directory and run it from there.".format(os.getcwd(),os.path.basename(__file__))
    exit(1)

browser = PyChrome()
link = "www.google.com"
browser.open(link)
locator = "q"
browser.findElement(name=locator)

print "\n"
print "***** Welcome to pyChrome Demo *****"
print "\nThis demo shows how one could leverage Selenium WebDriver (or pyChrome) for Data Mining.\n" \
        "In this example, I'll use Google Search Engine to display some data " \
      "and this program collects those data and scan through its page. \n" \
      "\nThe objective:\n"

print "- Search for keywords (i.e 'Video Games News' or 'Current Events')\n" \
      "- Traverse through the links\n" \
      "- Store the link text\n" \
      "- Store the description text\n" \
      "- Click on the link\n" \
      "- Scroll through the page (as if some other program were analyzing the page)\n" \
      "- Back out of the page\n" \
      "- Click on the next link\n" \
      "- Continue the same process for other links in the current Search page\n" \
      "- Once it reaches the end of the page, jump to the next page\n" \
      "- And continue the same process"


text = raw_input('\nEnter some keywords to collect its data from Google Database\n>')
browser.sendText(text)
locator = "btnG"
browser.findElement(name=locator)
browser.clickElement()

pages = 3

while pages:
    search_number = 0
    locator = "srg"
    element = browser.findElement(classname=locator)
    locator = "g"
    elements = browser.findElementsByClass(locator,element)
    search_numbers = len(elements)
    page_link = browser.browser.cur_tab.link

    for index in range(0,search_numbers):
        del elements[:]
        del elements
        del element

        locator = "srg"

        element = browser.findElement(classname=locator)
        locator = "g"
        elements = browser.findElementsByClass(locator,element)

        g_element = elements[index]
        browser.selectElement(g_element)
        browser.scrollToElement(g_element)

        locator = "st"
        desc_element = browser.findSubElement(g_element,classname=locator)
        description = desc_element.text.encode('ascii', 'ignore').decode('ascii')

        browser.selectElement(g_element)
        locator = "a"
        link_element = browser.findSubElement(g_element,tag=locator)
        title = link_element.text.encode('ascii', 'ignore').decode('ascii')
        print ("\n>>>> Collecting Data: {}\n".format(title))
        browser.clickElement(link_element)
        time.sleep(1)
        browser.scrollBottom(animate=True)
        print ("\n>>>> Collected Data: {}\n".format(description))
        time.sleep(1)

        while page_link != browser.browser.cur_tab.link:
            browser.back()

        time.sleep(2)

    locator = "Next"
    next_element = browser.findElement(linktext=locator)
    browser.scrollToElement(next_element)
    browser.clickElement(next_element)

    pages = pages - 1


print "\n*****Demo Complete*****"
raw_input('\nPress Enter to Quit\n> ')

browser.quit()
