import time
import logging

try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)
try:
    import urllib2
except ImportError:
    logging.critical("urllib2 module is not installed...Exiting program.")
    exit(1)
try:
    import urllib
except ImportError:
    logging.critical("urllib module is not installed...Exiting program.")
    exit(1)
try:
    from element import Element
except ImportError:
    logging.critical("element.py is missing...Exiting program.")
    exit(1)
try:
    from interaction import Interaction
except ImportError:
    logging.critical("interaction.py is missing...Exiting program.")
    exit(1)
try:
    from navigation import Navigation
except ImportError:
    logging.critical("navigation.py is missing...Exiting program.")
    exit(1)
try:
    from tab import Tab
except ImportError:
    logging.critical("tab.py is missing...Exiting program.")
    exit(1)

##### Browser #####

class Browser:
    driver = None
    ghostmode = None
    navigation = None
    element = None
    interaction = None
    tab = None
    tabs = None

    def __init__(self,driver,ghostmode):
        self.driver = driver
        self.ghostmode = ghostmode
        self.tab = Tab(1,self.driver.window_handles[0],self.driver.current_url,self.driver.title)
        self.tabs = None
        self.tabs = []
        self.tabs.append(self.tab)

        self.navigation = Navigation(self.driver)
        self.element = Element(self.driver)
        self.interaction = Interaction(self.driver)
        self.interaction.elements = self.element.elements
        self.interaction.selectedElement = self.element.selectedElement

    def open(self, url):
        # Invalid URL
        if url == 0 or len(url) == 0:
            logging.error("Couldn't Open the page {}\nPlease check the URL".format(url))
            return 1

        # Search Instead
        if not "www." in url and not ".com" in url and not "." in url:
            err = self.search(url)
            if err:
                logging.error("Failed to Search")
                return 1
            return 0

        # Try Open the URL
        if not url is "http://www.google.com":
            url = self.validateURL(url)
        if url == 0:
            return 1
        if (url):
            if(self.driver):
                window_handles = self.driver.window_handles
                current_window = self.driver.current_window_handle
                position = 0
                for position, item in enumerate(window_handles):
                        if item == current_window:
                            break
                if self.ghostmode:
                    logging.info("Opening in GhostMode: {} on Tab {}".format(url,position+1))
                else:
                    logging.info("Opening: {} on Tab {}".format(url,position+1))
                try:
                    self.driver.get(url)
                    self.tab.link = self.driver.current_url
                    self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
                    element=self.element.findElementByTag("body")
                    if element and isinstance(element,WebElement):
                        self.element.selectedElement = element
                        self.interaction.selectedElement = element
                        self.selectedElement = element
                        self.element.selectElement(element)
                except TimeoutException:
                    logging.warning("TimeoutException: Didn't load the page fully")
                    return 0
                except WebDriverException:
                    logging.error("WebDriverException: Couldn't Open {}\nPlease check the URL or Internet Connection".format(url))
                    return 1
            logging.info("Page Title: {}".format(self.tab.title))
            return 0
        time.sleep(2)
        return 0

    def close(self):
        if self.tabs:
            logging.info("Closing {} Tabs".format(len(self.tabs)))
        if self.driver == None:
            return 1
        if self.tabs and len(self.tabs):
            for tab in self.tabs:
                if tab:
                    try:
                        self.driver.switch_to_window(tab.windowHandle)
                        self.driver.close()
                    except WebDriverException:
                        logging.error("WebDriverException: WebDriver Not Found")
                        return 1
                    tab.dealloc()
                    tab = None
                    del  tab
        self.tabs = None
        self.tabs = []
        if self.tab:
            self.tab.dealloc()
            self.tab = None
            del self.tab

        if self.interaction:
            self.interaction.dealloc()
        del self.interaction
        if self.element:
            self.element.dealloc()
        del self.element
        if self.navigation:
            self.navigation.dealloc()
        del self.navigation

        return 0

    def closeTab(self, tabnum = 0):
        if not self.driver or not self.tab:
            logging.error("There is no session or client or tab to close")
            return 0
        if self.tab:
            if tabnum:
                if tabnum < 1 or tabnum > 9:
                    logging.error("Tab Range Invalid: Can't Close Tab {}".format(tabnum))
                    return 1
                if tabnum > len(self.tabs):
                    logging.error("There is no Tab {}".format(tabnum))
                    return 1
                self.tab = self.tabs[tabnum-1]
                try:
                    self.driver.switch_to_window(self.tab.windowHandle)
                except WebDriverException:
                    logging.error("WebDriverException: Can't Switch to Tab {}".format(self.tab.index))
                    return 1
                time.sleep(1)
            logging.error("Closing Tab: Tab {}".format(self.tab.index))
            if len(self.tabs) == 1:
                self.tabs.remove(self.tab)
                self.tabs = None
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
                    logging.error("WebDriverException: Can't Switch to Tab {}".format(self.tab.index))
                    return 1
                time.sleep(1)
                title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
                try:
                    logging.info("Tab {} Focus: {}  URL {}".format(self.tab.index,title,self.driver.current_url))
                except TimeoutException:
                    logging.info("Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url))
        return 0

    def newTab(self,url=None):
        if len(self.tabs) == 9:
            logging.warning("Max Number of Tabs Reached {}".format(len(self.tabs)))
            return 1
        link = "https://www.google.com"
        time.sleep(1)
        try:
            self.driver.execute_script("window.open('{}');".format(link))
        except WebDriverException:
            logging.error("WebDriverException: Couldn't open a new tab")
            return 1
        location = len(self.driver.window_handles)
        logging.info("New Tab: Tab {}".format(location))
        time.sleep(1)
        try:
            self.driver.switch_to_window(self.driver.window_handles[len(self.tabs)])
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to New Tab")
            return 1
        time.sleep(1)
        if url:
            url = self.validateURL(link=url)
            if url:
                err = self.open(url)
                if err:
                    logging.error("Couldn't open URL in the new Tab")
                    return 1
        title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        newTab = Tab(location,self.driver.window_handles[len(self.tabs)],self.driver.current_url,title)
        self.tab = newTab
        self.tabs.append(self.tab)
        #self.tab.printTab()
        try:
            logging.info("Tab {} Focus: {}  URL {}".format(self.tab.index,title,self.driver.current_url))
        except TimeoutException:
            logging.error("TimeoutException: Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url))
        element=self.element.findElementByTag("body")
        if element:
            self.element.selectedElement = element
        return 0

    def rightTab(self):
        if self.tab.index == 9:
            logging.warning("Window at Tab {}. Can't Switch to Right Tab".format(self.tab.index))
            return 0
        if self.tab.index == len(self.tabs):
            logging.warning("Window at Tab {}. There is No Right Tab".format(self.tab.index))
            return 0
        logging.info("Switching to Right Tab ({} -> {})".format(self.tab.index,self.tab.index+1))
        self.tab = self.tabs[self.tab.index]
        try:
            self.driver.switch_to_window(self.tab.windowHandle)
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to Right Tab")
            return 1
        except UnicodeEncodeError:
            logging.error("UnicodeEncodeError: Tab {} Focus: URL {}".format(self.tab.index,self.tab.link))
        time.sleep(1)
        title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        try:
            logging.info("Tab {} Focus: {}  URL {}".format(self.tab.index,title,self.driver.current_url))
        except TimeoutException:
            logging.error("Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url))
        element=self.element.findElementByTag("body")
        if element:
            self.element.selectedElement = element
        return 0

    def leftTab(self):
        if self.tab.index == 1:
            logging.warning("Window at Tab {}. Can't Switch to Left Tab".format(self.tab.index))
            return 0
        if len(self.tabs) < 2:
            logging.warning("This is the only Tab Opened. There is not left Tab")
            return 0
        leftTab = self.tabs[self.tab.index-2]
        logging.info("Switching to Left Tab ({} <- {})".format(leftTab.index,self.tab.index))
        self.tab = leftTab
        try:
            self.driver.switch_to_window(self.tab.windowHandle)
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to Left Tab")
            return 1
        time.sleep(1)
        title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        try:
            logging.info("Tab {} Focus: {}  URL {}".format(self.tab.index,title,self.driver.current_url))
        except TimeoutException:
            logging.warning("TimeoutException: Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url))
        except UnicodeEncodeError:
            logging.warning("UnicodeEncodeError: Tab {} Focus: URL {}".format(self.tab.index,self.tab.link))
        element=self.element.findElementByTag("body")
        if element:
            self.element.selectedElement = element
        return 0

    def switchTab(self, index):
        if index == 0:
            logging.error("Tab Index starts from index 1")
            return 1
        if index > len(self.tabs):
            logging.error("Tab Index '{}' is greater than number of tabs opened '{}'".format(index,len(self.tabs)))
            return 1
        self.tab = self.tabs[index-1]
        try:
            self.driver.switch_to_window(self.tab.windowHandle)
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to Tab {}".format(index))
            return 1
        time.sleep(1)
        title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        try:
            logging.info("Tab {} Focus: {}  URL {}".format(self.tab.index,title,self.driver.current_url))
        except TimeoutException:
            logging.warning("TimeoutException: Tab {} Focus: URL {}".format(self.tab.index,self.driver.current_url))
        element=self.element.findElementByTag("body")
        if element:
            self.element.selectedElement = element
        return 0

    def validateURL(self, link):
        if not "www." in link and not "http" in link:
            link = "www.{}".format(link)
        if not "http" in link:
            link = "http://{}".format(link)
        if link is "http://www.google.com" or "www.google.com":
            return link
        try:
            urllib2.urlopen(link)
        except urllib2.HTTPError, e:
            logging.error("{}: {} not reachable".format(e.code,link))
            return 0
        except urllib2.URLError, e:
            logging.error("{}: {} not reachable".format(e.args,link))
            return 0
        return link

    def search(self, text):
        if text == 0 or len(text) == 0:
            logging.error("Nothing to search {}".format(text))
            return 1
        logging.info("Preparing to Search...")
        if not self.driver.current_url is "http://www.google.com":
            self.open("http://www.google.com")
        name_str = "q"
        element = self.element.findElementByName(name_str)
        if element == 0:
            logging.error("Couldn't find any element by its name attribute {}".format(name_str))
            return 1
        self.interaction.sendTextToElement(text,element)
        name_str = "btnG"
        element = self.element.findElementByName(name_str)
        if element == 0:
            logging.error("Couldn't find any element by its name attribute {}".format(name_str))
            return 1
        logging.info("Searching for {}".format(text))
        if self.interaction.clickElement(element):
            return 1
        self.tab.link = self.driver.current_url
        self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        return 0

    def clickLink(self,element=None):
        self.element.selectedElement=self.selectedElement
        self.interaction.selectedElement=self.selectedElement
        err = self.interaction.clickLink(element)
        if not err:
            self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
            self.tab.link = self.driver.current_url
        return err


    def clickElement(self, element=None):
        self.element.selectedElement=self.selectedElement
        self.interaction.selectedElement=self.selectedElement
        err = self.interaction.clickElement(element)
        if not err:
            self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        return err

    def clickButton(self,element=None):
        self.element.selectedElement=self.selectedElement
        self.interaction.selectedElement=self.selectedElement
        err = self.interaction.clickButton(element)
        if not err:
            self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
            self.tab.link = self.driver.current_url
        return err

    def back(self):
        self.element.selectedElement=self.selectedElement
        self.interaction.selectedElement=self.selectedElement
        err = self.navigation.back()
        if not err:
            self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
            self.tab.link = self.driver.current_url
        return err

    def forward(self):
        self.element.selectedElement=self.selectedElement
        self.interaction.selectedElement=self.selectedElement
        err = self.navigation.forward()
        if not err:
            self.tab.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
            self.tab.link = self.driver.current_url
        return err