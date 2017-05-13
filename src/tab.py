import logging
import time

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
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

class Tab:
    driver = None
    cur_tab = None
    tabs = None

    def open(self, url):
        # Try Open the URL
        if not url is "http://www.google.com":
            url = self.cur_tab.validateURL(url)
        if url == 0:
            return 1
        if (url):
            if(self.driver):
                logging.info("Opening: {} on Tab {}".format(url,self.cur_tab.index))
                try:
                    self.cur_tab.openPage(url=url)
                    logging.info("Page Title: {}".format(self.cur_tab.title))
                except TimeoutException:
                    logging.warning("TimeoutException: Didn't load the page fully")
                    return 1
                except WebDriverException:
                    logging.error("WebDriverException: Couldn't Open {}. \nPlease check the URL or Internet Connection".format(url))
                    return 1
        time.sleep(2)
        return 0

    def close(self):
        if self.cur_tab:
            self.tabs.remove(self.cur_tab)
            self.cur_tab.dealloc()
            del self.cur_tab
        if self.tabs:
            for tab in self.tabs:
                tab.dealloc()
            del self.tabs[:]
            del self.tabs
        return 0

    def closeTab(self, tabnum=0):
        if not self.driver or not self.cur_tab:
            logging.error("There is no session or client or tab to close")
            return 1
        if self.cur_tab:
            if tabnum:
                if tabnum < 1 or tabnum > 9:
                    logging.error("Tab Range Invalid: Can't Close Tab {}".format(tabnum))
                    return 1
                if tabnum > len(self.tabs):
                    logging.error("There is no Tab {}".format(tabnum))
                    return 1
                self.switchTab(tabnum)
            logging.info("Closing Tab: Tab {}".format(self.cur_tab.index))
            if len(self.tabs) == 1:
                self.close()
            else:
                location = self.cur_tab.index
                self.tabs.remove(self.cur_tab)
                self.cur_tab.dealloc()
                del self.cur_tab
                for i in range(len(self.tabs)):
                    tab = self.tabs[i]
                    tab.index = i+1
                if location > len(self.tabs):
                    self.cur_tab = self.tabs[len(self.tabs)-1]
                else:
                    self.cur_tab = self.tabs[location-1]
                try:
                    self.driver.switch_to_window(self.cur_tab.windowHandle)
                except WebDriverException:
                    logging.error("WebDriverException: Window Handle Can't Switch to Tab {}".format(self.cur_tab.index))
                    return 1
                logging.info("Focus Tab: {}  Title {}  URL {}".format(self.cur_tab.index,self.cur_tab.title,self.cur_tab.link))
                time.sleep(1)
        return 0

    def newTab(self,url=None):
        if len(self.tabs) == 9:
            logging.warning("Max Number of Tabs Reached {}".format(len(self.tabs)))
            return 1
        link = "https://www.google.com"
        try:
            self.driver.execute_script("window.open('{}');".format(link))
        except WebDriverException:
            logging.error("WebDriverException: Couldn't open a new tab")
            return 1
        location = len(self.driver.window_handles)
        logging.info("New Tab: Tab {}".format(location))
        time.sleep(1)
        title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        if url:
            link = url
        newTab = TabObject(self.driver,location,self.driver.window_handles[location-1],link,title)
        self.cur_tab = newTab
        self.tabs.append(self.cur_tab)
        logging.info("Focus Tab: {}  Title {}  URL {}".format(self.cur_tab.index,self.cur_tab.title,self.cur_tab.link))
        return 0

    def rightTab(self):
        if self.cur_tab.index == 9:
            logging.warning("Window at Tab {}. Can't Switch to Right Tab".format(self.cur_tab.index))
            return 0
        if self.cur_tab.index == len(self.tabs):
            logging.warning("Window at Tab {}. There is No Right Tab".format(self.cur_tab.index))
            return 0
        logging.info("Switching to Right Tab ({} -> {})".format(self.cur_tab.index,self.cur_tab.index+1))
        err = self.switchTab(self.cur_tab.index+1)
        return err

    def leftTab(self):
        if self.cur_tab.index == 1:
            logging.warning("Window at Tab {}. Can't Switch to Left Tab".format(self.cur_tab.index))
            return 0
        if len(self.tabs) < 2:
            logging.warning("This is the only Tab Opened. There is not left Tab")
            return 0
        logging.info("Switching to Left Tab ({} <- {})".format(self.cur_tab.index-1,self.cur_tab.index))
        err = self.switchTab(self.cur_tab.index-1)
        return err

    def switchTab(self, index):
        if index == 0:
            logging.error("Tab Index starts from index 1")
            return 1
        if index > len(self.tabs):
            logging.error("Tab Index '{}' is greater than number of tabs opened '{}'".format(index,len(self.tabs)))
            return 1
        self.cur_tab = self.tabs[index-1]
        try:
            self.driver.switch_to_window(self.cur_tab.windowHandle)
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to Tab {}".format(self.cur_tab.index))
            return 1
        logging.info("Focus Tab: {}  Title {}  URL {}".format(self.cur_tab.index,self.cur_tab.title,self.cur_tab.link))
        time.sleep(1)
        return 0

    def getcurrentTabLink(self):
        self.cur_tab.update()
        return str(self.cur_tab.link)

    def getcurrentTabTitle(self):
        self.cur_tab.update()
        return str(self.cur_tab.title)


class TabObject:
    driver = None
    link = ""
    index = 1
    title = ""
    windowHandle = None

    def __init__(self, driver, index, windowHandle, link=None, title=None):
        self.driver = driver
        self.title = None
        if title:
            self.title = title
        self.index = index
        self.windowHandle = windowHandle
        try:
            self.driver.switch_to_window(self.windowHandle)
        except WebDriverException:
            logging.error("WebDriverException: Can't Switch to New Tab")
        self.link = "http://www.google.com"
        if link:
            self.link = self.validateURL(link)
        self.openPage(self.link)

    def update(self):
        try:
            self.link = self.driver.current_url
            self.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        except TimeoutException:
            logging.warning("TimeoutException: Didn't load the page fully")
            return 1
        except WebDriverException:
            logging.error("WebDriverException: Couldn't Open {}. \nPlease check the URL or Internet Connection".format(url))
            return 1
        return 0

    def openPage(self,url):
        try:
            self.driver.get(url)
            time.sleep(1)
            self.link = self.driver.current_url
            self.title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        except TimeoutException:
            logging.warning("TimeoutException: Didn't load the page fully")
            return 1
        except WebDriverException:
            logging.error("WebDriverException: Couldn't Open {}. \nPlease check the URL or Internet Connection".format(url))
            return 1
        logging.info("Page Title: {}".format(self.title))
        return 0

    def dealloc(self):
        try:
            self.driver.switch_to_window(self.windowHandle)
            self.driver.close()
        except WebDriverException:
            logging.error("WebDriverException: WebDriver Not Found. Couldn't dealloc Tab {}".format(self.index))
            return 1
        del self.link
        del self.index
        del self.title
        del self.windowHandle

    def printTab(self):
        logging.info("-----Tab Info-------")
        logging.info("Tab: {}".format(self.index))
        logging.info("Title: {}".format(self.title))
        logging.info("Link: {}".format(self.link))
        logging.info("Window Handle: {}".format(self.windowHandle))
        logging.info("--------------------")

    def validateURL(self, link):
        if link == "data:," or link == "about:blank":
            self.link = "https://www.google.com"
            return link
        if not "www." in link and not "http" in link:
            link = "www.{}".format(link)
        if not "http" in link:
            link = "http://{}".format(link)
        if link == "http://www.google.com" or link == "www.google.com":
            return link
        return link
