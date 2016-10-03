import logging
import json
import time
import os
import sys


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
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support.ui import Select
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
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

#### Record ####

class Capture(Element,Interaction):
    driver = None
    directory = None
    captured_elements = []

    def screenshot(self, save_name=None, save_directory=None):
        filename = "save_image"
        extension = "png"
        directory = self.directory
        if save_name:
            filename = save_name
        if save_directory:
            directory = save_directory
        try:
            self.driver.save_screenshot('{}/{}.{}'.format(directory,filename,extension))
            logging.info("Screen Captured: {}".format("{}/{}.{}".format(directory,filename,extension)))
        except Exception:
            logging.error("Failed to Screen Capture {}".format(self.getcurrentTabLink()))
            return 1
        return 0

    def sourceDump(self, filename=None):
        extension = ".html"
        name = "source"
        if filename:
            name = filename
        if not self.driver:
            logging.error("There is no driver or URL to get the source")
            return 1
        try:
            urlopen = urllib.urlopen(self.getcurrentTabLink()) # Open the URL.
        except Exception:
            logging.error("Failed to get the source code for {}".format(self.getcurrentTabLink()))
            return 1
        source = urlopen.readlines() # Read source and save it to a variable.
        if not extension in name:
            name = "{}{}".format(name,extension)
        file = open(name,"wb") # Open file in binary mode
        file.writelines(source)
        file.close()
        logging.info("Source Code Dump: {}".format("{}/{}".format(self.directory,name)))
        return 0

    def elementDump(self,element,filename=None):
        extension = ".html"
        name = "source"
        if filename:
            name = filename
        if not isinstance(element,WebElement):
            logging.error("There is no element to get the source code")
            return 1
        try:
            source=element.get_attribute('innerHTML')
        except Exception:
            logging.error("Failed to get the source code for {}".format(element))
            return 1
        if not extension in name:
            name = "{}{}".format(name,extension)
        file = open(name,"wb")
        file.writelines(source)
        file.close()
        logging.info("Web Element Source Dump: {}".format("{}/{}".format(self.directory,name)))
        return 0

    def record(self,element=None):
        if not isinstance(self.captured_elements,list):
            self.captured_elements = []
        if element:
            err = self.switchElement(element)
            if err:
                logging.error("Failed to Select Element to Record")
                return 1
        else:
            self.switchElement()
            element = self.selectedElement
            if element == 0:
                logging.error("Failed to Find Active Element to Record")
                return 1

        logging.info("Recording Element {}".format(element))

        # Record Value & Highlight
        tag = element.tag_name
        type = self.getAttributeValue('type')
        if tag == 'body':
            logging.warning("Currently at the 'body' element of the page. No specific element is selected to record")
            return 1
        elif tag == 'input' or tag == 'i':
            if type and "radio" in type.lower():
                parent_element = self.findParentElement(element)
                self.highlightElement(parent_element)
                self.switchElement(element)
            elif type and "checkbox" in type.lower():
                parent_element = self.findParentElement(element)
                self.highlightElement(parent_element)
                self.switchElement(element)
                tag = element.tag_name
                type = self.getAttributeValue('type')
            else:
                self.highlightElement(element)
            value = self.getElementValue()
        elif tag == 'div':
            self.highlightElement(element)
            interactive_element = self.findInteractiveElement(element)
            interactive_element_tag = element.tag_name
            interactive_element_type = self.getAttributeValue('type')
            if interactive_element:
                if interactive_element_type == 'hidden':
                    value = element.text
                else:
                    err = self.record(interactive_element)
                    return err
            else:
                logging.error("Element with tag {} is not supported for recording".format(tag))
                return 1
        elif tag == 'select':
            self.highlightElement(element)
            self.switchElement(element)
            value = self.getElementValue()
            elements = self.findElementsByTag('option',element)
            if elements and len(elements):
                for element in elements:
                    element_val = self.getElementValue(element)
                    if element_val == value:
                        self.switchElement(element)
                        break
            else:
                logging.error("Attempting to locate sub-element of 'select' but it's failing. Currently only 'option' tag supported")
                return 1
        elif tag == 'option':
            value = self.getElementValue()
            select_element = self.findParentElement(element)
            select_tag = select_element.tag_name
            while select_tag != 'select':
                select_element = self.findParentElement(select_element)
                select_tag = select_element.tag_name
                if select_tag == "body":
                    logging.error("base element is not select type.")
                    return 1
            if value:
                try:
                    select = Select(select_element)
                    select.select_by_value(value)
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to record")
                    return 1
            else:
                logging.warning("option tag doesn't contain value")
            self.highlightElement(select_element)
            self.switchElement(element)
        elif tag == 'button':
            self.switchElement(element)
            value = element.text
            self.highlightElement()
        elif tag == 'a':
            value = element.text
            self.highlightElement()
        elif tag == "textarea":
            value = self.getElementValue(element)
            self.highlightElement()
        elif tag == 'label':
            value = element.text
            self.highlightElement()
            #interactive_element = self.findInteractiveElement(element)
            #if interactive_element:
            #    err = self.record(interactive_element)
            #    return err
            #else:
            #    logging.error("Element with tag {} is not supported for recording".format(tag))
            #    return 1
        elif tag == 'span':
            self.highlightElement()
            parent_element = self.findParentElement(element)
            interactive_element = self.findInteractiveElement(parent_element)
            #element = interactive_element
            self.switchElement(interactive_element)
            value = self.getElementValue()
        else:
            logging.error("Element with tag {} is not supported for recording".format(tag))
            return 1

        contain_captured_element = self.__isElementInCapturedElements(element)
        if contain_captured_element != 0:
            if contain_captured_element.value != value:
                contain_captured_element.value = value
                logging.info("Updated Record Element")
        else:
            link = self.getcurrentTabLink()
            id = self.getAttributeValue('id')
            name = self.getAttributeValue('name')
            xpath = self.getXpath(element)
            element_captured = CaptureElement(link,xpath,element,type=type,id=id,tag=tag,value=value,name=name)
            self.captured_elements.append(element_captured)
            logging.info("Recorded New Element")
            logging.info("{}".format(element_captured.output()))
        return 0

    def recordButton(self,element=None):
        if element:
            if isinstance(element,WebElement) and element.tag_name == 'button':
                button_element = element
            else:
                logging.error("element is not instance of Web Element or Button type element")
                return 1
        else:
            logging.info("Recording Button element")
            body_element = self.findBodyElement()
            if body_element == None or body_element == 0 or not isinstance(body_element,WebElement):
                logging.error("Couldn't find Body element to procede with recording button")
                return 1
            button_element = self.findSubElement(body_element,tag='button')
        if button_element == None or button_element == 0 or not isinstance(button_element,WebElement):
            logging.error("Couldn't find Button element to record")
            return 1
        err = self.record(button_element)
        if err:
            logging.error("Failed to record Button")
        else:
            logging.info("Button Element Recorded")
        return err

    def storeRecorder(self,filename=None,directory=None):
        if len(self.captured_elements) == 0:
            logging.error("There is no element captured to store.")
            return 1
        if filename == None:
            filename = "recorded_elements"
        if directory:
            self.directory = directory
        extension = "json"
        captured_elements_dic = []
        for captured_element in self.captured_elements:
            captured_element_dic = {
                'link':captured_element.link,
                'type':captured_element.type,
                'id':captured_element.id,
                'tag':captured_element.tag,
                'value':captured_element.value,
                'name':captured_element.name,
                'xpath':captured_element.xpath
            }
            captured_elements_dic.append(captured_element_dic)
        with open('{}.{}'.format(filename,extension), 'w') as outfile:
            json.dump(captured_elements_dic, outfile, indent=4, sort_keys=True, separators=(',', ':'))
        return 0

    def loadRecorder(self,filename=None,directory=None):
        extension = ".json"
        if not filename:
            filename = "recorded_elements"
        if directory:
            self.directory = directory
        if extension not in filename:
            filename = "{}{}".format(filename,extension)
        file_directory = "{}/{}".format(self.directory,filename)
        if not os.path.exists(file_directory):
            logging.error("{} is not in {}".format(filename,self.directory))
            return 1
        with open(filename) as jsonFile:
            captured_elements_dic = json.load(jsonFile)
        if captured_elements_dic and len(captured_elements_dic):
            if self.captured_elements:
                logging.warning("Writing over exsiting recorded elements")
                for captured_element in self.captured_elements:
                    captured_element.dealloc()
                    del captured_element
                del self.captured_elements[:]
                self.captured_elements = []
        for captured_element_dic in captured_elements_dic:
            link = str(captured_element_dic.get('link'))
            type = str(captured_element_dic.get('type'))
            id = str(captured_element_dic.get('id'))
            tag = str(captured_element_dic.get('tag'))
            value = str(captured_element_dic.get('value').encode('ascii', 'ignore').decode('ascii'))
            name = str(captured_element_dic.get('name'))
            xpath = str(captured_element_dic.get('xpath'))
            element_captured = CaptureElement(link,xpath,type=type,id=id,tag=tag,value=value,name=name)
            self.captured_elements.append(element_captured)
        return 0

    def playback(self):
        if len(self.captured_elements) == 0:
            logging.error("There is not element recorded to playback")
            return 1
        self.refresh()
        for captured_element in self.captured_elements:
            tag = captured_element.tag
            type = captured_element.type
            link = captured_element.link
            xpath = captured_element.xpath
            id = captured_element.id
            name = captured_element.name
            cur_link = self.getcurrentTabLink()
            if link != cur_link:
                self.open(link)
            if xpath:
                element = self.findElement(xpath=xpath)
            if id and not element:
                element = self.findElement(id=id)
            if name and not element:
                element = self.findElement(name=name)
            if element == None or element == 0 or not isinstance(element,WebElement):
                logging.error("Element couldn't be found from its Xpath {}".format(xpath))
                return 1
            if captured_element.element == None:
                logging.info("Updating captured element")
                captured_element.updateElement(element)
            if tag == "input" or tag == 'i':
                if type and type.lower() == "checkbox":
                    parent_element = self.findParentElement(element)
                    self.highlightElement(parent_element)
                    self.switchElement(element)
                    try:
                        element.click()
                    except ElementNotVisibleException:
                        logging.error("ElementNotVisibleException: Element is not visible to click")
                        return 1
                elif type and "radio" in type.lower():
                    parent_element = self.findParentElement(element)
                    self.highlightElement(parent_element)
                    self.switchElement(element)
                    try:
                        element.click()
                    except ElementNotVisibleException:
                        logging.error("ElementNotVisibleException: Element is not visible to click")
                        return 1
                elif type and "password" in type.lower():
                    self.highlightElement(element)
                    cap_value = captured_element.value
                    self.sendTextToElement(cap_value,element)
                elif type and "email" in type.lower():
                    self.highlightElement(element)
                    cap_value = captured_element.value
                    self.sendTextToElement(cap_value,element)
                elif type and "text" in type.lower():
                    self.highlightElement(element)
                    cap_value = captured_element.value
                    self.sendTextToElement(cap_value,element)
                elif type and "number" in type.lower():
                    self.highlightElement(element)
                    cap_value = captured_element.value
                    self.sendTextToElement(cap_value,element)
                elif type and "button" in type.lower():
                    self.highlightElement(element)
                    try:
                        element.click()
                    except ElementNotVisibleException:
                        logging.error("ElementNotVisibleException: Element is not visible to click")
                        return 1
                elif type and "submit" in type.lower():
                    self.highlightElement(element)
                    try:
                        element.click()
                    except ElementNotVisibleException:
                        logging.error("ElementNotVisibleException: Element is not visible to click")
                        return 1
                    except WebDriverException:
                        logging.info("WebDriverException")
                else:
                    self.highlightElement(element)
                    ele_value = self.getElementValue()
                    cap_value = captured_element.value
                    self.sendTextToElement(cap_value,element)
                    try:
                        try:
                            element.click()
                        except ElementNotVisibleException:
                            logging.error("ElementNotVisibleException: Element is not visible to click")
                            return 1
                    except WebDriverException:
                        logging.warning("Element is not clickable")
            elif tag == 'div':
                self.highlightElement(element)
                ele_value = element.text
                cap_value = captured_element.value
                if ele_value != cap_value:
                    try:
                        element.send_keys(cap_value)
                    except ElementNotVisibleException:
                        logging.warning("ElementNotVisibleException: Element not visible to send {}. ".format(cap_value))
            elif tag == 'select':
                parent_element = self.findParentElement(element)
                if parent_element.tag_name != "select":
                    parent_element = self.findParentElement(parent_element)
                self.highlightElement(parent_element)
                try:
                    element.click()
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to click")
                    return 1
            elif tag == 'option':
                value = self.getElementValue()
                select_element = self.findParentElement(element)
                select_tag = select_element.tag_name
                while select_tag != 'select':
                    select_element = self.findParentElement(select_element)
                    select_tag = select_element.tag_name
                    if select_tag == "body":
                        logging.error("base element is not select type.")
                        return 1
                if value:
                    try:
                        select = Select(select_element)
                        select.select_by_value(value)
                    except ElementNotVisibleException:
                        logging.error("ElementNotVisibleException: Element is not visible to record")
                        return 1
                else:
                    logging.warning("option tag doesn't contain value")
                self.highlightElement(select_element)
                self.switchElement(element)
            elif tag == 'button':
                self.highlightElement(element)
                try:
                    element.click()
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to click")
                    return 1
            elif tag == 'a':
                self.highlightElement(element)
                try:
                    element.click()
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to click")
                    return 1
            elif tag == 'span':
                self.highlightElement()
                parent_element = self.findParentElement(element)
                interactive_element = self.findInteractiveElement(parent_element)
                self.switchElement(interactive_element)
                value = self.getElementValue()
                try:
                    element.click()
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to click")
                    return 1
            elif tag == "textarea":
                self.highlightElement()
                cap_value = captured_element.value
                self.sendTextToElement(cap_value,element)
            elif tag == 'label':
                self.highlightElement()
                try:
                    element.click()
                except ElementNotVisibleException:
                    logging.error("ElementNotVisibleException: Element is not visible to click")
                    return 1
            else:
                logging.error("Element with tag {} is not supported for Playback".format(tag))
                return 1
            time.sleep(1)
        return 0

    def getRecordedElements(self):
        return self.captured_elements

    def deleteRecord(self):
        if len(self.captured_elements) == 0:
            logging.error("There is not recorded element to delete")
            return 1
        else:
            last_element = self.captured_elements[len(self.captured_elements)-1]
            logging.info("Deleted last captured element: {}".format(last_element))
            self.captured_elements.remove(last_element)
            last_element.dealloc()
            del last_element
        return 0

    def clearRecorder(self):
        if self.captured_elements:
            for captured_element in self.captured_elements:
                captured_element.dealloc()
                del captured_element
            del self.captured_elements[:]
        return 0

    def __compareElement(self,element_one,element_two):
        if not isinstance(element_one,WebElement):
            return 0
        if not isinstance(element_two,WebElement):
            return 0
        if element_one == element_two:
            return 1
        else:
            return 0

    def __isElementInCapturedElements(self,element):
        if len(self.captured_elements) == 0:
            return 0
        for captured_element in self.captured_elements:
            if captured_element.element:
                if self.__compareElement(element,captured_element.element):
                    return captured_element
        return 0

class CaptureElement:
    link = ""
    type = ""
    id = ""
    tag = ""
    value = ""
    name = ""
    xpath = ""
    element = None

    def __init__(self,link,xpath,element=None,type=None,id=None,tag=None,value=None,name=None):
        self.link = link
        self.xpath = xpath
        if element:
            self.element = element
        if type:
            self.type = type
        if id:
            self.id = id
        if tag:
            self.tag = tag
        if value:
            self.value = value
        if name:
            self.name = name

    def updateElement(self,element):
        self.element = element
        return 0

    def __str__(self):
        str = "Link: {}\nTag: {}\nID: {}\nName: {}\nType: {}\nValue: {}".format(self.link,self.tag,self.id,self.name,
                                                                                self.type,self.value.encode('ascii', 'ignore').decode('ascii'))
        return str

    def output(self):
        str = "Tag: {} ID: {} Name: {} Type: {} Value: {}".format(self.tag,self.id,self.name,self.type,self.value.encode('ascii', 'ignore').decode('ascii'))
        return str

    def dealloc(self):
        if self.link:
            del self.link
        if self.type:
            del self.type
        if self.id:
            del self.id
        if self.tag:
            del self.tag
        if self.value:
            del self.value
        if self.name:
            del self.name
        if self.xpath:
            del self.xpath
        if self.element:
            del self.element