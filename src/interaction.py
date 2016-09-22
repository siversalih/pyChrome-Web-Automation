import time
import logging

try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.keys import Keys
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

##### Interactions ######

class Interaction:
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
                    logging.error("Select Element returned Error")
                    return 1
            else:
                logging.error("Passed in element is not Web Element type {}".format(element))
                return 1
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Current selected element is not Web Element type {}".format(self.selectedElement))
            return 1
        element = self.selectedElement
        tag_name = element.tag_name
        if tag_name != "input":
            logging.warning("The selected element is not input type element. "
                            "Attempting to search for input tag inside element {}".format(element))
            element = self.findElementByTag("input",element)
            if element == 0 or not isinstance(element,WebElement):
                logging.error("Couldn't find input tag inside selected element {}".format(element))
                return 1
            else:
                self.selectElement(element)
        element = self.selectedElement
        if text == 0 or text == None or len(text) == 0:
            logging.error("Text is empty or not defined")
            return 1
        try:
            logging.info("Sending '{}' to Element '{}'".format(text,element))
            element.send_keys(text)
        except ElementNotVisibleException:
            logging.error("Element is Not Visible")
            return 1
        except StaleElementReferenceException:
            logging.error("Trying to send Text to Stale Element {}".format(element))
            return 1
        time.sleep(1)
        return 0

    def sendText(self, text):
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            logging.error("Selected Element is NULL or not defined as Web Element: {}".format(self.selectedElement))
            return 1
        name_attr = self.selectedElement.get_attribute("name")
        if name_attr != "q":
            logging.warning("Current selected element is not query type element. "
                            "Attempting to search for name='q' inside current element")
            input_element = self.findElementByName("q",self.selectedElement)
            if input_element == 0 or not isinstance(input_element,WebElement):
                logging.error("Couldn't find name='q' inside current element")
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
                logging.error("Passed in element is not Web Element type {}".format(element))
                return 1
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Current selected element is not Web Element type {}".format(self.selectedElement))
            return 1
        try:
            try:
                element_text = self.selectedElement.text.encode('ascii', 'ignore').decode('ascii')
                logging.info("Click the page: {}".format(element_text))
            except UnicodeEncodeError:
                logging.error("Click the page: {}".format(self.selectedElement.id))
            self.selectedElement.click()
            err = self.browser.cur_tab.update()
            if err:
                return err
            logging.info("Page Title: {}".format(self.browser.cur_tab.title))
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is Not Visible to Click")
            return 1
        except WebDriverException:
            logging.error("WebDriverException: Element is not Clickable at point {}".format(self.selectedElement.location))
            return 1
        time.sleep(2)
        if self.ghost == False:
            self.scrol((0,0))
        return 0

    def clickLink(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.selectElement(element)
                if err:
                    return 1
            else:
                logging.error("Passed in element is not Web Element type {}".format(element))
                return 1
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            logging.error("No Element has been selected")
            return 1
        tag_name = self.selectedElement.tag_name
        if tag_name != "a":
            logging.warning("Current selected element is not link type element. "
                            "Attempting to search for 'a' tag inside current element")
            link_element = self.findElementByTag("a",self.selectedElement)
            if link_element == 0 or not isinstance(link_element,WebElement):
                logging.error("Couldn't find 'a' tag inside current element")
                return 1
            else:
                self.selectedElement = link_element
        err = self.clickElement(self.selectedElement)
        if err:
            logging.error("Couldn't Click on Button of Current Selected Element")
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
                logging.error("Passed in element is not Web Element type {}".format(element))
                return 1
        if self.selectedElement == 0 or self.selectedElement == None or not isinstance(self.selectedElement,WebElement):
            logging.error("No Element has been selected")
            return 1
        tag_name = self.selectedElement.tag_name
        if tag_name != "button":
            logging.warning("Current selected element is not button type element. "
                            "Attempting to search for button tag inside current element")
            button_element = self.findElementByTag("button",self.selectedElement)
            if button_element == 0 or not isinstance(button_element,WebElement):
                logging.error("Couldn't find button tag inside current element")
                return 1
            else:
                self.selectElement(button_element)
        err = self.clickElement(self.selectedElement)
        if err:
            logging.error("Couldn't Click on Button of Current Selected Element")
            return 1
        else:
            return 0
