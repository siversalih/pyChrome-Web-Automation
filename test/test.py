import os
import time
import unittest

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
        print "Test Begin: Openning Page {}".format(self.url)
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

        totalTabs = len(self.browser.tabs)
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
        if self.browser.tab.index == 4:
            err = err or 0
        else: err = 1
        if len(self.browser.tabs) == 4:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.tab.windowHandle:
            err = err or 0
        else: err = 1

        err = err or self.browser.leftTab()
        err = err or self.browser.leftTab()
        err = err or self.browser.closeTab()
        if self.browser.tab.index == 2:
            err = err or 0
        else: err = 1
        if len(self.browser.tabs) == 3:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.tab.windowHandle:
            err = err or 0
        else: err = 1

        err = err or self.browser.leftTab()
        err = err or self.browser.closeTab()
        if self.browser.tab.index == 1:
            err = err or 0
        else: err = 1
        if len(self.browser.tabs) == 2:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.tab.windowHandle:
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

        if self.browser.tab.index == 1:
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

        if self.browser.tab.index == 5:
            err = err or 0
        else: err = 1

        self.assertFalse(err,0)
        print "Test Ended"


    def closeTab(self):
        if not self.driver or not self.tab:
            print "There is no session or client or tab to close"
            return 0
        if self.tab:
            print "Closing Tab: Tab {}".format(self.tab.index)
            location = 0
            if len(self.tabs) == 1:
                location = 1
                self.tabs.remove(self.tab)
                self.tabs = []
                self.tab.dealloc()
                del self.tab
                self.tab = None
                self.driver.close()
            else:
                location = self.tab.index
                self.tabs.remove(self.tab)
                self.tab.dealloc()
                del self.tab
                self.tab = None
                self.driver.close()
                for i in range(len(self.tabs)):
                    tab = self.tabs[i]
                    tab.index = i+1
                if location > len(self.tabs):
                    self.tab = self.tabs[len(self.tabs)-1]
                else:
                    self.tab = self.tabs[location-1]
                try:
                    self.driver.switch_to_window(self.tab.windowHandle)
                except WebDriverException:
                    print "WebDriverException: Can't Switch to Tab {}".format(self.tab.index)
                    return 1
                time.sleep(1)
                try:
                    print "Tab {} Focus: {}  URL {}".format(self.tab.index,self.driver.title,self.driver.current_url)
                except TimeoutException:
                    print "Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url)
        return 0


    def closeTab(self):
        if not self.driver or not self.tab:
            print "There is no session or client or tab to close"
            return 0
        if self.tab:
            print "Closing Tab: Tab {}".format(self.tab.index)
            location = 0
            if len(self.tabs) == 1:
                location = 1
                self.tabs.remove(self.tab)
                self.tabs = []
                self.tab.dealloc()
                del self.tab
                self.tab = None
                self.driver.close()
            else:
                location = self.tab.index
                self.tabs.remove(self.tab)
                self.tab.dealloc()
                del self.tab
                self.tab = None
                self.driver.close()
                for i in range(len(self.tabs)):
                    tab = self.tabs[i]
                    tab.index = i+1
                if location > len(self.tabs):
                    self.tab = self.tabs[len(self.tabs)-1]
                else:
                    self.tab = self.tabs[location-1]
                try:
                    self.driver.switch_to_window(self.tab.windowHandle)
                except WebDriverException:
                    print "WebDriverException: Can't Switch to Tab {}".format(self.tab.index)
                    return 1
                time.sleep(1)
                try:
                    print "Tab {} Focus: {}  URL {}".format(self.tab.index,self.driver.title,self.driver.current_url)
                except TimeoutException:
                    print "Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url)
        return 0

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
        if self.browser.tab.index == 3:
            err = err or 0
        else: err = 1
        if len(self.browser.tabs) == 5:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.tab.windowHandle:
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
        if self.browser.tab.index == self.index:
            err = err or 0
        else: err = 1
        if len(self.browser.tabs) == 2:
            err = err or 0
        else: err = 1
        if self.browser.driver.current_window_handle == self.browser.tab.windowHandle:
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
        if not len(elements) == 2:
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
            print "Found {} elements by Classname {}".format(len(elements),self.locator)
        if not len(elements) == 2:
            err = 1
        else: err = err or 0
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

class sendTextToElementNameTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    name_str = ""
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

    def runTest(self):
        print "\nTest Begin: Send Text to Name of Element"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.sendTextToName(self.name_str,self.text)
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
        err = err or self.browser.clickonElement(self.element)
        time.sleep(1)
        self.assertFalse(err,0)
        print "Test Ended"

class clickonIDTest(unittest.TestCase):
    browser = None
    filename = ""
    directory = ""
    url = ""
    id_str = ""

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
        print "\nTest Begin: Click on ID"
        time.sleep(1)
        err = self.browser.open(self.url)
        time.sleep(1)
        err = err or self.browser.clickonID(self.id_str)
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
        print "\nTest Begin: Scroll Right"
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
        err = self.browser.loginFacebook(self.username,self.password)
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