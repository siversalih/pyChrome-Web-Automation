import time

try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.keys import Keys
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)
try:
    from element import Element
except ImportError:
    print "window.py is missing...Exiting program."
    exit(1)

##### Interactions ######

class Interaction(Element):
    driver = None

    def __init__(self,driver):
        self.driver = driver

    def dealloc(self):
        if self.driver:
            del self.driver
        if self.elements:
            del self.elements
        if self.selectedElement:
            del self.selectedElement

    def sendTextToName(self,name_str,text):
        element = self.findElementByName(name_str)
        if element == 0:
            return 1
        self.selectedElement = element
        self.sendTextToElement(text,element)
        return 0

    def sendTextToElement(self, text, element = 0):
        if element and isinstance(element, WebElement):
            self.selectedElement = element
        if not self.selectedElement or not isinstance(self.selectedElement, WebElement):
            return 1
        if text == 0 or len(text) == 0:
            return 1
        try:
            print "Sending '{}' to Element ID '{}'".format(text,self.selectedElement.id)
            self.selectedElement.send_keys(text)
            time.sleep(0.2)
        except ElementNotVisibleException:
            print "Element Not Visible"
            return 1
        return 0

    def clickonElement(self, element = 0):
        if element:
            self.selectedElement = element
        if self.selectedElement == None:
            return 1
        if not isinstance(self.selectedElement, WebElement):
            return 1
        try:
            print "Click on {}".format(self.selectedElement.text)
            self.selectedElement.click()
        except ElementNotVisibleException:
            print "Element Not Visible"
            return 1
        except WebDriverException:
            print "Element is not clickable at point {}".format(self.selectedElement.location)
            return 1

        return 0

    def clickonID(self,id_str):
        element = self.findElementByID(id_str)
        if element:
            self.selectedElement = element
            self.clickonElement(element)
            return 0
        else:
            print "Couldn't find any element with ID {}".format(id_str)
            return 1

