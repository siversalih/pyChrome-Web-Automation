try:
    from selenium.common.exceptions import WebDriverException
except ImportError:
    print "Selenium module is not installed...Exiting program."
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
            print "WebDriverException: Couldn't return to previous page"
            return 1
        print "Page Title: {}".format(self.driver.title)
        return 0

    def forward(self):
        try:
            self.driver.forward()
        except WebDriverException:
            print "WebDriverException: Couldn't forward to next page"
            return 1
        print "Page Title: {}".format(self.driver.title)
        return 0
