import os
import sys
import time
import unittest

par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)
sys.path.insert(0, par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing...Exiting program."
    exit(1)

##### Browser #####

class closeBrowserTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Closing the Client"
        time.sleep(1)
        err = self.browser.close()
        self.assertFalse(err,0)
        print "Test Ended"

class quitBrowserTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Quit the Client"
        time.sleep(1)
        err = self.browser.quit()
        self.assertFalse(err,0)
        print "Test Ended"

class openTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.google.com"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "Test Begin: Openning Page"
        time.sleep(1)
        err = self.browser.open(self.url)
        self.assertFalse(err,0)
        print "Test Ended"

class openTabTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Open Tab"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="www.apple.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="www.facebook.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        totalTabs = len(self.browser.browser.tabs)
        if totalTabs == 5:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)

        print "Test Ended"

class closeTabTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Close Tab"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="www.apple.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="www.facebook.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        err = err or self.browser.closeTab()
        if self.browser.browser.cur_tab.index == 4:
            err = err or 0
        else: err = 1
        if len(self.browser.browser.tabs) == 4:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.browser.cur_tab.windowHandle:
            err = err or 0
        else: err = 1

        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.closeTab()
        if self.browser.browser.cur_tab.index == 2:
            err = err or 0
        else: err = 1
        if len(self.browser.browser.tabs) == 3:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.browser.cur_tab.windowHandle:
            err = err or 0
        else: err = 1

        err = err or self.browser.leftTab()
        err = err or self.browser.closeTab()
        if self.browser.browser.cur_tab.index == 1:
            err = err or 0
        else: err = 1
        if len(self.browser.browser.tabs) == 2:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.browser.cur_tab.windowHandle:
            err = err or 0
        else: err = 1

        err = err or self.browser.closeTab()

        self.assertFalse(err,0)
        print "Test Ended"

class switchToLeftTabTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Switch to Left Tab"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="www.apple.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="www.facebook.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()

        if self.browser.browser.cur_tab.index == 1:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)
        print "Test Ended"

class switchToRightTabTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Switch to Right Tab"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="www.apple.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="www.facebook.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.rightTab()
        err = err or self.browser.rightTab()
        err = err or self.browser.rightTab()
        err = err or self.browser.rightTab()
        err = err or self.browser.rightTab()

        if self.browser.browser.cur_tab.index == 5:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)
        print "Test Ended"

class switchToTabTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None

    def runTest(self):
        print "Test Begin: Switch to Tab by Index"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="www.apple.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="www.facebook.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        err = err or self.browser.switchTab(3)
        if self.browser.browser.cur_tab.index == 3:
            err = err or 0
        else: err = 1
        if len(self.browser.browser.tabs) == 5:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.browser.cur_tab.windowHandle:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)
        print "Test Ended"

class closeTabAtIndexTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    index = 0
    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.index = 2

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.index = None

    def runTest(self):
        print "Test Begin: Close Tab at Index"
        err = self.browser.open("http://www.gmail.com")

        time.sleep(1)
        err = err or self.browser.newTab(url="stackoverflow.com")
        time.sleep(1)
        err = err or self.browser.newTab(url="https://www.python.org")
        time.sleep(1)

        err = err or self.browser.closeTab(tabnum=self.index)
        if self.browser.browser.cur_tab.index == self.index:
            err = err or 0
        else: err = 1
        if len(self.browser.browser.tabs) == 2:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.browser.cur_tab.windowHandle:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)
        print "Test Ended"

##### Locating Element(s) ######

class findElementByIDTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "user_login"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By ID"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByID(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByNameTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "log"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By Name"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByName(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByTagTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "form"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By Tag"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByTag(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByPartialTextTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "WordPress"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By Partial Text"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByPartialText(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByLinkTextTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.yahoo.com"
        self.locator = "Flickr"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By Link Text"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByLinkText(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByClassTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "input"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By Classname"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByClass(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementByXPathTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "//*[@id=\"wp-submit\"]"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Element By XPath"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByXPath(self.locator)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"


class findElementsByIDTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "wp-submit"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By ID"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByID(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by ID {}".format(len(elements),self.locator)

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByNameTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "loginform"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Name"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByName(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Name {}".format(len(elements),self.locator)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByTagTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "p"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Tag"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByTag(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Tag {}".format(len(elements),self.locator)
        if not len(elements) == 6:
            err = 1
        else: err = err or 0

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByPartialTextTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "WordPress"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Partial Text"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByPartialText(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Partial Text {}".format(len(elements),self.locator)
        if not len(elements) == 2:
            err = 1
        else: err = err or 0
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByLinkTextTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.yahoo.com"
        self.locator = "Mail"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Link Text"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByLinkText(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Link Text {}".format(len(elements),self.locator)
        if not len(elements) == 3:
            err = 1
        else: err = err or 0
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByClassTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "input"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Classname"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByClass(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Classname {}".format(len(elements),self.locator)
        if not len(elements) == 2:
            err = 1
        else: err = err or 0
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementsByXPathTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "//input[@class=\"input\"]"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Elements By XPath"
        err = self.browser.open(self.url)
        time.sleep(1)
        elements = self.browser.findElementsByXPath(self.locator)
        if elements == 0 or len(elements) == 0:
            err = 1
        else:
            err = 0 or err
            print "Found {} elements by Xpath {}".format(len(elements),self.locator)
        if not len(elements) == 2:
            err = 1
        else: err = err or 0
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"


class subElementSearchTest_1(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    locator = ""
    element = None
    elements = []

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "www.yahoo.com"
        self.locator = "trending-list"
        self.element = None
        self.elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.locator = None
        self.element = None
        del self.elements[:]
        del self.elements

    def runTest(self):
        print "\nTest Begin: Locate Sub-element Test 1"
        err = self.browser.open(self.link)
        time.sleep(1)
        self.element = self.browser.findElementByClass(self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "li"
        self.elements = self.browser.findElementsByTag(self.locator,self.element)
        if self.elements == None or not len(self.elements) == 10:
            err = 1
        else: err = 0 or err
        self.element = self.elements[0]
        err = err or self.browser.clickElement(self.element)
        time.sleep(1)
        self.locator = "ov-a"
        self.elements = self.browser.findElementsByClass(self.locator)
        if self.elements == None or not len(self.elements) == 6:
            err = 1
        else: err = 0 or err
        self.element = self.elements[1]
        err = err or self.browser.clickElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class subElementSearchTest_2(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    locator = ""
    element = None
    elements = []
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "www.google.com"
        self.locator = "q"
        self.text = "What is Selenium Webdriver"
        self.element = None
        self.elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.locator = None
        self.text = None
        self.element = None
        del self.elements[:]
        del self.elements

    def runTest(self):
        print "\nTest Begin: Locate Sub-element Test 2"
        err = self.browser.open(self.link)
        if err:
            err = 1
        else: err = 0 or err
        self.element = self.browser.findElement(name=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        err = self.browser.sendText(self.text)
        if err:
            err = 1
        else: err = 0 or err
        self.locator = "btnG"
        self.element = self.browser.findElement(name=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        err = self.browser.clickButton()
        if err:
            err = 1
        else: err = 0 or err
        self.locator = "srg"
        self.element = self.browser.findElementByClass(self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "g"
        self.elements = self.browser.findElementsByClass(self.locator,self.element)
        if self.elements == 0 or self.elements == None or len(self.elements) == 0:
            err = 1
        else: err = 0 or err
        err = self.browser.switchElement(2)
        if err:
            err = 1
        else: err = 0 or err
        err = self.browser.clickLink()
        if err:
            err = 1
        else: err = 0 or err

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class subElementSearchTest_3(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    locator = ""
    element = None
    elements = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.seleniumhq.org/projects/webdriver/"
        self.locator = "header"
        self.element = None
        self.elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.locator = None
        self.element = None
        del self.elements[:]
        del self.elements

    def runTest(self):
        print "\nTest Begin: Locate Sub-element Test 3"
        err = self.browser.open(self.link)
        self.element = self.browser.findElement(id=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "ul"
        self.element = self.browser.findElement(element=self.element,tag=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "li"
        self.elements = self.browser.findElementsByTag(self.locator,self.element)
        if self.elements == None or self.elements == 0 or len(self.elements) < 3:
            err = 1
        else: err = 0 or err
        err = err or self.browser.switchElement(2)
        err = err or self.browser.clickElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class parentElementSearchTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    locator = ""
    element = None
    elements = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.seleniumhq.org/projects/webdriver/"
        self.locator = "header"
        self.element = None
        self.elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.locator = None
        self.element = None
        del self.elements[:]
        del self.elements

    def runTest(self):
        print "\nTest Begin: Locate Parent Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElement(id=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "ul"
        self.element = self.browser.findElement(element=self.element,tag=self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.locator = "li"
        self.elements = self.browser.findElementsByTag(self.locator,self.element)
        if self.elements == None or self.elements == 0 or len(self.elements) < 3:
            err = 1
        else: err = 0 or err
        err = err or self.browser.switchElement(2)
        self.element = self.browser.findParentElement()
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.element = self.browser.findParentElement(self.element)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        id_name = self.element.get_attribute("id")
        if id_name != "header":
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementBodyTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.seleniumhq.org/projects/webdriver/"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Locate Body Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findBodyElement()
        if self.element.tag_name == 'body':
            err = err or 0
        else: err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findActiveElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.text = "First"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.text = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Active Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == 0:
            err = 1
        err = err or self.browser.sendTextToElement(self.text,self.element)
        self.browser.switchElement(self.element)
        if self.element.tag_name != "input":
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class highlightElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.text = "First"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.text = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Find Active Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == 0:
            err = 1
        err = err or self.browser.sendTextToElement(self.text,self.element)
        err = err or self.browser.highlightElement()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementValueTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    text = ""
    value = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.text = "First"
        self.element = None
        self.value = ""

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.text = None
        self.locator = None
        self.value = None

    def runTest(self):
        print "\nTest Begin: Find Element Value Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == 0:
            err = 1
        err = err or self.browser.sendTextToElement(self.text,self.element)
        self.browser.switchElement(self.element)
        if self.element.tag_name != "input":
            err = 1
        self.value = self.browser.getElementValue()
        if self.value != self.text:
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findAttributeValueTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    text = ""
    value = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.text = "First"
        self.element = None
        self.value = ""

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.text = None
        self.locator = None
        self.value = None

    def runTest(self):
        print "\nTest Begin: Find Attribute Value of an Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == 0:
            err = 1
        err = err or self.browser.sendTextToElement(self.text,self.element)
        self.browser.switchElement(self.element)
        if self.element.tag_name != "input":
            err = 1
        self.value = self.browser.getAttributeValue(attribute="id")
        if self.value != "FirstName":
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findXpathTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    xpath = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.xpath = ""

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.locator = None
        self.xpath = None

    def runTest(self):
        print "\nTest Begin: Find Xpath of an Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == 0:
            err = 1
        self.xpath = self.browser.getXpath()
        if self.xpath != "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/fieldset[1]/label[1]/input[1]":
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class findSiblingElementsTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None
    elements = []

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
        self.locator = "menu_support"
        self.element = None
        self.elements = []
    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None
        if self.elements:
            del self.elements[:]

    def runTest(self):
        print "\nTest Begin: Find Sibling Elements"
        err = self.browser.open(self.url)
        self.element = self.browser.findElement(id=self.locator)
        if self.element == None:
            err = 1
        self.elements = self.browser.findSiblingsElements()
        if self.elements == None or len(self.elements) != 5:
            err = 1

        self.assertFalse(err,0)
        print "Test Ended"

class findPreviousElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
        self.locator = "menu_download"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Find Previous Element"
        err = self.browser.open(self.url)
        self.element = self.browser.findElement(id=self.locator)
        if self.element == None:
            err = 1
        self.element = self.browser.findPreviousElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_documentation":
            err = 1
        self.element = self.browser.findPreviousElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_support":
            err = 1
        self.element = self.browser.findPreviousElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_about":
            err = 1
        self.element = self.browser.findPreviousElement(self.element)
        if self.element:
            err = 1
        self.assertFalse(err,0)
        print "Test Ended"

class findNextElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
        self.locator = "menu_about"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Find Next Element"
        err = self.browser.open(self.url)
        self.element = self.browser.findElement(id=self.locator)
        if self.element == None:
            err = 1
        self.element = self.browser.findNextElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_support":
            err = 1
        self.element = self.browser.findNextElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_documentation":
            err = 1
        self.element = self.browser.findNextElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_download":
            err = 1
        self.element = self.browser.findNextElement(self.element)
        if self.element == 0:
            err = 1
        self.locator = self.browser.getAttributeValue('id')
        if self.locator == None:
            err = None
        if self.locator != "menu_projects":
            err = 1
        self.element = self.browser.findNextElement(self.element)
        if self.element:
            err = 1
        self.assertFalse(err,0)
        print "Test Ended"

class findOptionElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    value = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.destinylfg.net/"
        self.locator = "collapsed"
        self.value = "ps4"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.locator = None
        self.value = None

    def runTest(self):
        print "\nTest Begin: Find Option Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElement(classname=self.locator)
        if self.element == 0:
            err = 1
        self.browser.clickElement(self.element)
        self.locator = "filters-platform-select"
        self.element = self.browser.findElement(id=self.locator)
        self.element = self.browser.findOptionElement(value=self.value,select=self.element)

        if self.element == 0 or self.element.tag_name != "option":
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class getElementCoordinatesTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    coor = None
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
        self.locator = "user_login"
        self.coor = None
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.coor = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Get Element Coordinates"
        err = self.browser.open(self.url)
        time.sleep(1)
        self.element = self.browser.findElementByID(self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        self.coor = self.browser.getElementCoordinates(self.element)
        x = self.coor[0]
        y = self.coor[1]
        if int(x) < 100 and int(y) < 100:
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

##### Interaction ######

class sendTextToElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    name_str = ""
    element = None
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com"
        self.name_str = "q"
        self.text = "Selenium Webdriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.name_str = None
        self.text = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Send Text to Element"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        self.element = self.browser.findElementByName(self.name_str)
        if self.element == 0:
            err = 1
        err = err or self.browser.sendTextToElement(self.text,self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class sendTextTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    element = None
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com"
        self.text = "Selenium Webdriver"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.text = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Send Text"
        err = self.browser.open(self.url)
        err = err or self.browser.sendText(self.text)

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class clickonElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    id_str = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.id_str = "menu_download"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.id_str = None

    def runTest(self):
        print "\nTest Begin: Click on Element"
        err = self.browser.open(self.url)
        time.sleep(1)
        self.element = self.browser.findElementByID(self.id_str)
        if self.element == 0:
            err = 1
        err = err or self.browser.clickElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class clickButtonTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    text = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com"
        self.text = "Selenium Documentation"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Click on Button"
        err = self.browser.open(self.url)
        err = err or self.browser.sendText(self.text)
        self.browser.findBodyElement()
        err = err or self.browser.clickButton()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class clickLinkTest(unittest.TestCase):
    browser = None
    filename = None
    directory = None
    url = None
    locator = None
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.locator = "menu_documentation"
        self.element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Click on Link"
        err = self.browser.open(self.url)
        self.element =  self.browser.findElementByID(self.locator)
        if self.element == 0:
            err = 1
        else: err = 0 or err
        err = err or self.browser.clickLink()

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class selectOptionElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    element = None
    locator = ""
    value = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.destinylfg.net/"
        self.locator = "collapsed"
        self.value = "ps4"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.element = None
        self.locator = None
        self.value = None

    def runTest(self):
        print "\nTest Begin: Select Option Element Test"
        err = self.browser.open(self.link)
        self.element = self.browser.findElement(classname=self.locator)
        if self.element == 0:
            err = 1
        self.browser.clickElement(self.element)
        self.locator = "filters-platform-select"
        self.element = self.browser.findElement(id=self.locator)
        self.element = self.browser.findOptionElement(value=self.value,select=self.element)
        if self.element == 0 or self.element.tag_name != "option":
            err = 1
        err = err or self.browser.selectElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class dragAndDropTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    src_element = None
    dest_element = None
    locator = ""


    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://demos.telerik.com/kendo-ui/dragdrop/index"
        self.locator = "draggable"
        self.src_element = None
        self.dest_element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.src_element = None
        self.dest_element = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Drag and Drop Test"
        err = self.browser.open(self.link)
        self.src_element = self.browser.findElement(id=self.locator)
        if not self.src_element:
            err = 1
        self.locator = "droptarget"
        self.dest_element = self.browser.findElement(id=self.locator)
        if not self.dest_element:
            err = 1
        err = err or self.browser.dragAndDrop(self.src_element,self.dest_element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class dragAndDropTest_2(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    src_element = None
    dest_element = None
    locator = ""


    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
        self.locator = "box1"
        self.src_element = None
        self.dest_element = None

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.src_element = None
        self.dest_element = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Drag and Drop Test 2"
        err = self.browser.open(self.link)
        for index in range(1,8):
            self.locator = "box{}".format(index)
            self.src_element = self.browser.findElement(id=self.locator)
            self.locator = "box10{}".format(index)
            self.dest_element = self.browser.findElement(id=self.locator)
            self.browser.dragAndDrop(self.src_element,self.dest_element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class moveToElement(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    src_element = None
    dest_element = None
    elements = []
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://marcojakob.github.io/dart-dnd/custom-avatar/web/"
        self.locator = "/html/body/div/div"
        self.src_element = None
        self.dest_element = None
        self.elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.src_element = None
        self.dest_element = None
        self.locator = None
        del self.elements[:]
        del self.elements

    def runTest(self):
        print "\nTest Begin: Move to Element"
        err = self.browser.open(self.link)
        self.dest_element = self.browser.findElement(xpath=self.locator)
        if not self.dest_element:
            err = 1
        self.locator = "document"
        self.elements = self.browser.findElementsByClass(self.locator)
        if not self.elements and len(self.elements) != 4:
            err = 1
        self.elements = self.browser.findElementsByClass(self.locator)
        for self.src_element in self.elements:
            err = err or self.browser.moveToElement(self.src_element)
            err = err or self.browser.holdElement(self.src_element)
            err = err or self.browser.moveToElement(self.dest_element)
            err = err or self.browser.releaseElement(self.dest_element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class moveToPosition(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    link = ""
    locator = ""
    element = None
    position = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.link = "https://marcojakob.github.io/dart-dnd/free-dragging/web/"
        self.locator = "draggable"
        self.element = None
        self.position = ()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.link = None
        self.locator = None
        self.element = None
        self.position = ()

    def runTest(self):
        print "\nTest Begin: Move to Position"
        err = self.browser.open(self.link)
        self.element = self.browser.findElement(classname=self.locator)
        err = err or self.browser.holdElement(self.element)
        position = (100,200)
        err = err or self.browser.moveByOffset(position)
        err = err or self.browser.releaseElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class doubleClickElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.the-art-of-web.com/javascript/doublesubmit/"
        self.locator = "//*[@id='content']/form[1]/fieldset/input[1]"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None

    def runTest(self):
        print "\nTest Begin: Click on Element"
        err = self.browser.open(self.url)
        time.sleep(1)
        self.element = self.browser.findElement(xpath=self.locator)
        if self.element == 0:
            err = 1
        err = err or self.browser.doubleClickElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

##### Window Control #####

class positionTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    position = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.position = (300,200)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.position = None

    def runTest(self):
        print "\nTest Begin: Position Window"
        time.sleep(1)
        err = self.browser.position(self.position)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class sizeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    size = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.size = (1080,720)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.size = None

    def runTest(self):
        print "\nTest Begin: Size Window"
        time.sleep(1)
        err = self.browser.size(self.size)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class zoomTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    val = 0

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"
        self.val = 60

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.val = None

    def runTest(self):
        print "\nTest Begin: Zoom"
        time.sleep(1)
        err = self.browser.open(self.url)
        err = err or self.browser.zoom(self.val)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class zoomInTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "\nTest Begin: Zoom In"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.zoomIn()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class zoomOutTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "\nTest Begin: Zoom Out"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.zoomOut()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class scrollTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    position = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"
        self.position = (0,400)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.val = None

    def runTest(self):
        print "\nTest Begin: Scroll"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.scrol(self.position)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class scrollElementTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.ign.com"
        self.locator = "Send Us News"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None

    def runTest(self):
        print "\nTest Begin: Scroll to Element"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByPartialText(self.locator)
        if element == 0:
            err = 1
        else:
            err = 0 or err
            err = err or self.browser.scrollToElement(element)
            time.sleep(1)

        self.assertFalse(err,0)
        print "Test Ended"

class scrollDownTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "\nTest Begin: Scroll Down"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.scrollDown()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class scrollUpTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "\nTest Begin: Scroll Up"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.scrollDown()
        time.sleep(1)
        err = err or self.browser.scrollDown()
        time.sleep(1)
        err = err or self.browser.scrollUp()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class scrollRightTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    size = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"
        self.size = (320,720)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.size = None

    def runTest(self):
        print "\nTest Begin: Scroll Right"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = self.browser.size(self.size)
        time.sleep(1)
        err = err or self.browser.scrollRight()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class scrollLeftTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    size = ()

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=Selenium+Webdriver"
        self.size = (320,720)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.size = None

    def runTest(self):
        print "\nTest Begin: Scroll Left"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = self.browser.size(self.size)
        time.sleep(1)
        err = err or self.browser.scrollRight()
        time.sleep(1)
        err = err or self.browser.scrollRight()
        time.sleep(1)
        err = err or self.browser.scrollLeft()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

##### Navigation Control #####

class backTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url1 = ""
    url2 = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url1 = "https://www.google.com"
        self.url2 = "https://www.gmail.com"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url1 = None
        self.url2 = None

    def runTest(self):
        print "\nTest Begin: Back to Previous Page"
        time.sleep(1)
        err = self.browser.open(self.url1)
        time.sleep(1)
        err = err or self.browser.open(self.url2)
        time.sleep(1)
        err = err or self.browser.back()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class forwardTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url1 = ""
    url2 = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url1 = "https://www.google.com"
        self.url2 = "https://www.gmail.com"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url1 = None
        self.url2 = None

    def runTest(self):
        print "\nTest Begin: Forward to Next Page"
        time.sleep(1)
        err = self.browser.open(self.url1)
        time.sleep(1)
        err = err or self.browser.open(self.url2)
        time.sleep(1)
        err = err or self.browser.back()
        time.sleep(1)
        err = err or self.browser.forward()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class refreshTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""


    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://www.gmail.com"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "\nTest Begin: Refresh Page"
        time.sleep(0.5)
        err = self.browser.open(self.url)
        time.sleep(0.5)
        err = err or self.browser.refresh()
        time.sleep(0.5)
        self.assertFalse(err,0)
        print "Test Ended"

##### Record #####

class screenshotTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    save_name = ""


    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.save_name = "screenshot_capture"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.save_name = None

    def runTest(self):
        print "\nTest Begin: Screenshot"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.screenshot(save_name=self.save_name)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class pageSourceDumpTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    source_name = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.google.com"
        self.source_name = "sourcePage"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.source_name = None

    def runTest(self):
        print "\nTest Begin: Dump Page Source Code"
        err = self.browser.open("http://www.google.com")
        time.sleep(1)
        err = err or self.browser.sourceDump(filename=self.source_name)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class elementSourceDumpTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    source_filename = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.locator = "Documentation"
        self.source_filename = "elementsource"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.source_filename = None

    def runTest(self):
        print "\nTest Begin: Find Elements By Classname"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByPartialText(self.locator)
        if element == 0:
            err = 1
        else:
            err = 0 or err
            time.sleep(1)
            err = self.browser.elementDump(element,self.source_filename)
            time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class recordTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None
    recorded_elements = []

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.recorded_elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None
        for recorded_element in self.recorded_elements:
            recorded_element.dealloc()
            del recorded_element
        del self.recorded_elements[:]
        del self.recorded_elements

    def runTest(self):
        print "\nTest Begin: Record Test"
        err = self.browser.open(self.url)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        err = err or self.browser.record(element=self.element)
        self.locator = "LastName"
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        err = err or self.browser.record(element=self.element)
        self.recorded_elements = self.browser.getRecordedElements()
        if len(self.recorded_elements) != 2:
            err = 1
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class playbackTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None
    recorded_elements = []

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.recorded_elements = []

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None
        for recorded_element in self.recorded_elements:
            recorded_element.dealloc()
            del recorded_element
        del self.recorded_elements[:]
        del self.recorded_elements

    def runTest(self):
        print "\nTest Begin: Playback Test"
        err = self.browser.open(self.url)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        self.browser.sendTextToElement("FirstName",self.element)
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        self.locator = "LastName"
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        self.browser.sendTextToElement("LastName",self.element)
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        self.recorded_elements = self.browser.getRecordedElements()
        if len(self.recorded_elements) != 2:
            err = 1
        self.url = "http://www.google.com"
        err = err or self.browser.open(self.url)
        err = err or self.browser.playback()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class storeRecordsTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None
    filename_recorder = ""
    file_directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.filename_recorder = "recorded_elements"
        self.file_directory = "{}/{}.json".format(self.directory,self.filename_recorder)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None
        os.remove(self.file_directory)
        self.filename_recorder = None
        self.file_directory = None

    def runTest(self):
        print "\nTest Begin: Store Recorded Elements Test"
        err = self.browser.open(self.url)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        self.locator = "LastName"
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        err = err or self.browser.storeRecorder(self.filename_recorder)
        if not os.path.exists(self.file_directory):
            err = 1

        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class loadRecordsTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    locator = ""
    element = None
    filename_recorder = ""
    file_directory = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
        self.locator = "FirstName"
        self.filename_recorder = "recorded_elements"
        self.file_directory = "{}/{}.json".format(self.directory,self.filename_recorder)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.locator = None
        self.element = None
        os.remove(self.file_directory)
        self.filename_recorder = None
        self.file_directory = None

    def runTest(self):
        print "\nTest Begin: Load Recorded Elements Test"
        err = self.browser.open(self.url)
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        self.browser.sendTextToElement("First",self.element)
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        self.locator = "LastName"
        self.element = self.browser.findElementByName(name_str=self.locator)
        if self.element == None or self.element == 0:
            err = 1
        time.sleep(1)
        self.browser.sendTextToElement("Last",self.element)
        time.sleep(1)
        err = err or self.browser.record(element=self.element)
        err = err or self.browser.storeRecorder(self.filename_recorder)
        if not os.path.exists(self.file_directory):
            err = 1
        time.sleep(1)
        err = err or self.browser.loadRecorder(self.filename_recorder)
        time.sleep(1)
        err = err or self.browser.open("www.google.com")
        time.sleep(1)
        err = err or self.browser.playback()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

##### Ghost Mode (Headless) #####

class openInGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.url = "http://www.google.com"


    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None

    def runTest(self):
        print "Test Begin: Openning Ghost Page {}".format(self.url)
        time.sleep(1)
        err = self.browser.open(self.url)
        self.assertFalse(err,0)
        print "Test Ended"

class findElementInGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.text = "Documentation"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.text = None

    def runTest(self):
        print "\nTest Begin: Find Element By Partial Text in Ghostmode"
        err = self.browser.open(self.url)
        time.sleep(1)
        element = self.browser.findElementByPartialText(self.text)
        if element == 0:
            err = 1
        else: err = 0 or err
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class screenshotGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    save_name = ""


    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.url = "http://www.seleniumhq.org/projects/webdriver/"
        self.save_name = "screenshot_capture_ghostmode"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url = None
        self.save_name = None

    def runTest(self):
        print "\nTest Begin: Screenshot in Ghostmode"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.screenshot(save_name=self.save_name)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class backGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url1 = ""
    url2 = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.url1 = "https://www.google.com"
        self.url2 = "https://www.gmail.com"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.url1 = None
        self.url2 = None

    def runTest(self):
        print "\nTest Begin: Back to Previous Page in Ghostmode"
        time.sleep(1)
        err = self.browser.open(self.url1)
        time.sleep(1)
        err = err or self.browser.open(self.url2)
        time.sleep(1)
        err = err or self.browser.back()
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class fbloginGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    username = ""
    password = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.url = "http://www.facebook.com"
        self.username = "deviousgroup@gmail.com"
        self.password = "123456qW"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.username = None
        self.password = None
        self.url = None

    def runTest(self):
        print "Test Begin: Facebook Login in Ghostmode"
        time.sleep(1)
        err = self.browser.loginFacebook(self.username,self.password,ghostmode=True)
        self.assertFalse(err,0)
        print "Test Ended"

class searchGhostModeTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename,ghostmode=True)
        self.text = "What is Selenium Chrome WebDriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.text = None

    def runTest(self):
        print "Test Begin: Search Using Google Search Engine in Ghostmode"
        time.sleep(1)
        err = self.browser.search(self.text)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

##### Combo #####

class searchTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    text = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.text = "What is Selenium Chrome WebDriver"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.text = None

    def runTest(self):
        print "Test Begin: Search Using Google Search Engine"
        time.sleep(1)
        err = self.browser.search(self.text)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

    ##### Window Control #####

class fbloginTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    username = ""
    password = ""

    @classmethod
    def setUpClass(self):
        self.filename = 'config.json'
        self.directory = os.getcwd()
        file_directory = "{}/{}".format(self.directory,self.filename)
        if(not os.path.exists(file_directory)):
            print("{} is not in {}".format(self.filename,self.directory))
            exit(1)
        self.browser = PyChrome(self.filename)
        self.url = "http://www.facebook.com"
        self.username = "deviousgroup@gmail.com"
        self.password = "123456qW"

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        self.browser = None
        self.filename = None
        self.directory = None
        self.username = None
        self.password = None
        self.url = None

    def runTest(self):
        print "Test Begin: Login to Facebook"
        time.sleep(1)
        err = self.browser.loginFacebook(self.username,self.password)
        self.assertFalse(err,0)
        print "Test Ended"



if __name__ == '__main__':
	unittest.main()
