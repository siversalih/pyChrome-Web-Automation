import time
import copy
try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.keys import Keys
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)
try:
    from element import Element
except ImportError:
    print "element.py is missing...Exiting program."
    exit(1)

try:
    from window import Window
except ImportError:
    print "window.py is missing...Exiting program."
    exit(1)


##### Interactions ######

class Interaction(Element,Window):
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

    def sendTextToElement(self, text, element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.selectElement(element)
                if err:
                    return 1
            else:
                print "Passed in element is not Web Element type {}".format(element)
                return 1
        if not isinstance(self.selectedElement,WebElement):
            print "Current selected element is not Web Element type {}".format(self.selectedElement)
            return 1
        element = self.selectedElement
        tag_name = element.tag_name
        if tag_name != "input":
            print "The selected element is not input type element. \n" \
                    "Attempting to search for input tag inside element {}".format(element)
            element = self.findElementByTag("input",element)
            if element == 0 or not isinstance(element,WebElement):
                print "Couldn't find input tag inside selected element {}".format(element)
                return 1
            else:
                self.selectElement(element)
        element = self.selectedElement
        if text == 0 or text == None or len(text) == 0:
            print "Text is empty or not defined"
            return 1
        try:
            print "Sending '{}' to Element '{}'".format(text,element)
            element.send_keys(text)
        except ElementNotVisibleException:
            print "Element is Not Visible"
            return 1
        except StaleElementReferenceException:
            print "Trying to send Text to Stale Element {}".format(element)
            return 1
        time.sleep(1)
        return 0


    def sendText(self, text):
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            print "Selected Element is NULL or not defined as Web Element: {}".format(self.selectedElement)
            return 1
        name_attr = self.selectedElement.get_attribute("name")
        if name_attr != "q":
            print "Current selected element is not query type element. \n" \
                  "Attempting to search for name='q' inside current element"
            input_element = self.findElementByName("q",self.selectedElement)
            if input_element == 0 or not isinstance(input_element,WebElement):
                print "Couldn't find name='q' inside current element"
            else:
                self.selectElement(input_element)
        err = self.sendTextToElement(text)
        return err

    def clickElement(self, element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.selectElement(element)
                if err:
                    return 1
            else:
                print "Passed in element is not Web Element type {}".format(element)
                return 1
        if not isinstance(self.selectedElement,WebElement):
            print "Current selected element is not Web Element type {}".format(self.selectedElement)
            return 1
        try:
            try:
                print "Click the page: {}".format(self.selectedElement.text)
            except UnicodeEncodeError:
                print "Click the page: {}".format(self.selectedElement.id)
            self.selectedElement.click()
            try:
                print "Page Title: {}".format(self.driver.title)
            except UnicodeEncodeError:
                print "Page Title: {}".format(self.driver.title.encode('ascii', 'ignore').decode('ascii'))
            except StaleElementReferenceException:
                print "Page Title"
        except ElementNotVisibleException:
            print "Element is Not Visible to Click"
            return 1
        except WebDriverException:
            print "Element is not Clickable at point {}".format(self.selectedElement.location)
            return 1
        time.sleep(2)
        self.scrol((0,0))
        return 0

    def clickLink(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.selectElement(element)
                if err:
                    return 1
            else:
                print "Passed in element is not Web Element type {}".format(element)
                return 1
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            print "No Element has been selected"
            return 1
        tag_name = self.selectedElement.tag_name
        if tag_name != "a":
            print "Current selected element is not link type element. \n" \
                  "Attempting to search for 'a' tag inside current element"
            link_element = self.findElementByTag("a",self.selectedElement)
            if link_element == 0 or not isinstance(link_element,WebElement):
                print "Couldn't find 'a' tag inside current element"
                return 1
            else:
                self.selectedElement = link_element
        err = self.clickElement(self.selectedElement)
        if err:
            print "Couldn't Click on Button of Current Selected Element"
            return 1
        else:
            return 0

    def clickButton(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.selectElement(element)
                if err:
                    return 1
            else:
                print "Passed in element is not Web Element type {}".format(element)
                return 1
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            print "No Element has been selected"
            return 1
        tag_name = self.selectedElement.tag_name
        if tag_name != "button":
            print "Current selected element is not button type element. \n" \
                  "Attempting to search for button tag inside current element"
            button_element = self.findElementByTag("button",self.selectedElement)
            if button_element == 0 or not isinstance(button_element,WebElement):
                print "Couldn't find button tag inside current element"
                return 1
            else:
                self.selectElement(button_element)
        err = self.clickElement(self.selectedElement)
        if err:
            print "Couldn't Click on Button of Current Selected Element"
            return 1
        else:
            return 0
