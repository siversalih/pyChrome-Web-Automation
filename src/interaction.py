import time
import logging

try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

##### Interactions ######

class Interaction:
    driver = None

    def sendTextToElement(self, text, element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.switchElement(element)
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
        if text == 0 or text == None or len(text) == 0:
            logging.error("Text is empty or not defined")
            return 1
        type = self.getAttributeValue('type')
        if type == "number":
            self.driver.execute_script("arguments[0].setAttribute('value', arguments[1])",element,text)
        else:
            try:
                element.clear()
                logging.info("Sending '{}' to Element '{}'".format(text,element))
                element.send_keys(text)
            except ElementNotVisibleException:
                logging.error("ElementNotVisibleException: Element is Not Visible")
                return 1
            except StaleElementReferenceException:
                logging.error("StaleElementReferenceException: Trying to send Text to Stale Element {}".format(element))
                return 1
            except WebDriverException:
                logging.error("WebDriverException: WebDriver does not exist or failing to interact with the element")
                return 1
        time.sleep(0.5)
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
                self.switchElement(input_element)
        err = self.sendTextToElement(text)
        return err

    def clickLink(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.switchElement(element)
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
                err = self.switchElement(element)
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
                self.switchElement(button_element)
        err = self.clickElement(self.selectedElement)
        if err:
            logging.error("Couldn't Click on Button of Current Selected Element")
            return 1
        else:
            return 0

    def selectElement(self,option=None,value=None):
        if option:
            if isinstance(option,WebElement):
                self.switchElement(option)
            else:
                logging.error("Option is not instance of Web Element")
                return 1
        option = self.selectedElement
        tag = option.tag_name
        if tag == "select":
            if value:
                try:
                    select = Select(option)
                    select.select_by_value(value)
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to record")
                    return 1
            else:
                logging.error("To select an element, value is required")
                return 1
        elif tag == "option":
            value = self.getElementValue()
            select_element = self.findParentElement(option)
            select_tag = select_element.tag_name
            while select_tag != 'select':
                select_element = self.findParentElement(select_element)
                select_tag = select_element.tag_name
                if select_tag == "body":
                    logging.error("base element is not select type.")
                    return 1
            return self.selectElement(select_element,value=value)
        else:
            logging.error("Element with tag {} can't be selected".format(tag))
            return 1
        return 0

    def clickElement(self, element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        try:
            self.selectedElement.click()
            err = self.browser.cur_tab.update()
            if err:
                logging.error("Failed to update the tab")
                return err
            logging.info("Page Title: {}".format(self.browser.getcurrentTabTitle()))
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Couldn't Click on this element.")
            return 1
        except WebDriverException:
            logging.error("WebDriverException: Element is not Clickable at point {}".format(self.selectedElement.location))
            return 1
        time.sleep(1)
        if self.ghost == False:
            self.scrol((0,0))
        return 0

    def doubleClickElement(self, element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        if self.selectedElement.tag_name == 'a':
            logging.error("Element is link type and can not be double clicked")
            return 1

        try:
            self.selectedElement.click()
            self.selectedElement.click()
            err = self.browser.cur_tab.update()
            if err:
                logging.error("Failed to update the tab")
                return err
            logging.info("Page Title: {}".format(self.browser.getcurrentTabTitle()))
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Couldn't Click on this element.")
            return 1
        except AttributeError:
            logging.error("AttributeError: Element does not have double click attribute")
            return 1
        except WebDriverException:
            logging.error("WebDriverException: Element is not Clickable at point {}".format(self.selectedElement.location))
            return 1
        time.sleep(1)
        if self.ghost == False:
            self.scrol((0,0))
        return 0

    def holdElement(self,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        element = self.selectedElement
        try:
            action_chains = ActionChains(self.driver)
            action_chains.click_and_hold(element).perform()
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is not visible")
            return 1
        except Exception:
            logging.error("Element in Source is not draggable")
            return 1
        logging.info("Clicked and Holding element: {}".format(element))
        time.sleep(0.1)
        return 0

    def releaseElement(self,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        element = self.selectedElement
        try:
            action_chains = ActionChains(self.driver)
            action_chains.release(element).perform()
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is not visible")
            return 1
        except Exception:
            logging.error("Element in Source is not draggable")
            return 1
        logging.info("Released Element: {}".format(element))
        time.sleep(0.1)
        return 0

    def moveByOffset(self,position):
        if not isinstance(position,tuple):
            logging.error("position is not instance of tuple")
            return 1
        try:
            dest_x = int(position[0])
            dest_y = int(position[1])
        except ValueError:
            logging.error("ValueError: Value are not integer type")
            return 1
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_by_offset(xoffset=dest_x,yoffset=dest_y).perform()
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is not visible")
            return 1
        except Exception:
            logging.error("Element in Source is not draggable")
            return 1
        time.sleep(0.1)
        return 0

    def moveToElement(self,element):
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is not visible")
            return 1
        except Exception:
            logging.error("Element in Source is not draggable")
            return 1
        time.sleep(0.2)
        self.switchElement(element)
        return 0

    def dragAndDrop(self,source,destination):
        if not isinstance(source,WebElement):
            logging.error("Source is not instance of Web Element")
            return 1
        if not isinstance(destination,WebElement):
            logging.error("Destination is not instance of Web Element")
            return 1
        try:
            action_chains = ActionChains(self.driver)
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        try:
            self.holdElement(source)
            time.sleep(0.2)
            self.moveToElement(destination)
            time.sleep(0.2)
            self.releaseElement(destination)
        except WebDriverException:
            logging.error("WebDriverException: Driver is not available to perform action")
            return 1
        except ElementNotVisibleException:
            logging.error("ElementNotVisibleException: Element is not visible")
            return 1
        except Exception:
            logging.error("Element in Source is not draggable")
            return 1
        time.sleep(0.5)
        self.switchElement(destination)
        return 0

    def sendKeysToElement(self,keys,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        actions = ActionChains(self.driver)
        if isinstance(keys,unicode):
            logging.info("Sending single key to active element")
            actions = actions.send_keys(keys)
        elif isinstance(keys,list):
            logging.info("Sending list of keys to active element")
            for key in keys:
                if isinstance(keys,unicode):
                    actions = actions.send_keys(key)
                else:
                    logging.warning("One of the key from the list is not type of unicode")
        else:
            logging.error("keys is not instance of Keys or List")
            return 1
        time.sleep(0.1)
        actions.perform()
        time.sleep(0.2)
        return 0