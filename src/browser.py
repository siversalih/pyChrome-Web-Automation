import time
import logging
import os
import sys
try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)
try:
    from tab import Tab
except ImportError:
    logging.critical("tab.py is missing...Exiting program.")
    exit(1)
try:
    from navigation import Navigation
except ImportError:
    logging.critical("navigation.py is missing...Exiting program.")
    exit(1)
try:
    from tab import TabObject
except ImportError:
    logging.critical("tab.py is missing...Exiting program.")
    exit(1)
try:
    from capture import Capture
except ImportError:
    logging.critical("capture.py is missing...Exiting program.")
    exit(1)

##### Browser #####
class Browser(Navigation,Tab,Capture):
    driver = None
    cur_tab = None
    tabs = None
    directory = None
    ghostmode = None

    def __init__(self,driver,ghostmode):
        self.driver = driver
        self.ghostmode = ghostmode
        self.cur_tab = TabObject(self.driver,1,self.driver.window_handles[0],self.driver.current_url,self.driver.title)
        self.tabs = None
        self.tabs = []
        self.tabs.append(self.cur_tab)
        self.directory = os.getcwd()

    def dealloc(self):
        if self.cur_tab:
            self.tabs.remove(self.cur_tab)
            self.cur_tab.dealloc()
            del self.cur_tab
        if self.tabs:
            for tab in self.tabs:
                tab.dealloc()
            del self.tabs[:]
            del self.tabs
        if self.directory:
            del self.directory
        if self.captured_elements:
            for captured_element in self.captured_elements:
                captured_element.dealloc()
                del captured_element
            del self.captured_elements[:]
        if self.driver:
            del self.driver