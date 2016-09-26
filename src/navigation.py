import time
import logging

try:
    from selenium.common.exceptions import WebDriverException
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

##### Navigation #####

class Navigation:
    driver = None

    def __init__(self,driver):
        self.driver = driver

    def dealloc(self):
        if self.driver:
            del self.driver

    def back(self):
        try:
            self.driver.back()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't return to previous page")
            return 1
        self.cur_tab.update()
        logging.info("Returning to Page: {}".format(self.cur_tab.title))
        time.sleep(1)
        return 0

    def forward(self):
        try:
            self.driver.forward()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't forward to next page")
            return 1
        self.cur_tab.update()
        logging.info("Forwarding to Page: {}".format(self.cur_tab.title))
        time.sleep(1)
        return 0

    def refresh(self):
        try:
            self.driver.refresh()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't refresh the page")
            return 1
        self.cur_tab.update()
        logging.info("Page Refreshed: {}".format(self.cur_tab.title))
        time.sleep(1)
        return 0