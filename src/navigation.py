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
        page_title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        logging.info("Returning to Page: {}".format(page_title))
        time.sleep(1)
        return 0

    def forward(self):
        try:
            self.driver.forward()
        except WebDriverException:
            logging.error("WebDriverException: Couldn't forward to next page")
            return 1
        page_title = self.driver.title.encode('ascii', 'ignore').decode('ascii')
        logging.info("Forwarding to Page: {}".format(page_title))
        time.sleep(1)
        return 0
