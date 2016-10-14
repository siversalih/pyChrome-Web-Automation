import logging

try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import NoSuchAttributeException
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support.ui import Select
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

##### Element ######

class Element:
    driver = None
    selectedElement = None
    elements = None

    ##### Locating Element #####

    def findElementByID(self,id_str, element=None):
        if not self.validateLocator(id_str):
            logging.error("Invalid ID: {}".format(id_str))
            return 0
        logging.info("Searching for element by ID: '{}'".format(id_str))
        try:
            if element:
                element = element.find_element_by_id(id_str)
            else:
                element = self.driver.find_element_by_id(id_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by ID '{}'".format(id_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. "
                          "Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with ID: '{}'".format(id_str))
        else:
            logging.info("Couldn't find element by id '{}'".format(id_str))
            return 0
        return element

    def findElementByName(self,name_str,element=None):
        if not self.validateLocator(name_str):
            logging.error("Invalid Name: {}".format(name_str))
            return 0
        logging.info("Searching for element by Name: '{}'".format(name_str))
        try:
            if element:
                element = element.find_element_by_name(name_str)
            else:
                element = self.driver.find_element_by_name(name_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Name '{}'".format(name_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Name: '{}'".format(name_str))
        else:
            logging.error("Couldn't find element by Name '{}'".format(name_str))
            return 0
        return element

    def findElementByTag(self,tag_str,element=None):
        if not self.validateLocator(tag_str):
            logging.error("Invalid Tag: {}".format(tag_str))
            return 0
        logging.info("Searching for element by Tag: '{}'".format(tag_str))
        try:
            if element:
                element = element.find_element_by_tag_name(tag_str)
            else:
                element = self.driver.find_element_by_tag_name(tag_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Tag '{}'".format(tag_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Tag: '{}'".format(tag_str))
        else:
            logging.error("Couldn't find element by Tag '{}'".format(tag_str))
            return 0
        return element

    def findElementByPartialText(self,text_str,element=None):
        if not self.validateLocator(text_str):
            logging.error("Invalid Partial Text: {}".format(text_str))
            return 0
        logging.info("Searching for element by Partial Text: '{}'".format(text_str))
        try:
            if element:
                element = element.find_element_by_partial_link_text(text_str)
            else:
                element = self.driver.find_element_by_partial_link_text(text_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Partial Text '{}'".format(text_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Partial Text: '{}'".format(text_str))
        else:
            logging.error("Couldn't find element by Partial Text '{}'".format(text_str))
            return 0
        return element

    def findElementByLinkText(self,link_str,element=None):
        if not self.validateLocator(link_str):
            logging.error("Invalid Link Text: {}".format(link_str))
            return 0
        logging.info("Searching for element by Link Text: '{}'".format(link_str))
        try:
            if element:
                element = element.find_element_by_link_text(link_str)
            else:
                element = self.driver.find_element_by_link_text(link_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Link Text '{}'".format(link_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Link Text: '{}'".format(link_str))
        else:
            logging.error("Couldn't find element by Link Text '{}'".format(link_str))
            return 0
        return element

    def findElementByClass(self,class_str,element=None):
        if not self.validateLocator(class_str):
            logging.error("Invalid Classname: {}".format(class_str))
            return 0
        logging.info("Searching for element by Classname: '{}'".format(class_str))
        try:
            if element:
                element = element.find_element_by_class_name(class_str)
            else:
                element = self.driver.find_element_by_class_name(class_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Classname '{}'".format(class_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Classname: '{}'".format(class_str))
        else:
            logging.error("Couldn't find element by Classname '{}'".format(class_str))
            return 0
        return element

    def findElementByXPath(self,xpath_str,element=None):
        if not self.validateLocator(xpath_str):
            logging.error("Invalid Xpath: {}".format(xpath_str))
            return 0
        logging.info("Searching for element by Xpath: '{}'".format(xpath_str))
        try:
            if element:
                element = element.find_element_by_xpath(xpath_str)
            else:
                element = self.driver.find_element_by_xpath(xpath_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by Xpath '{}'".format(xpath_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with Xpath: '{}'".format(xpath_str))
        else:
            logging.error("Couldn't find element by Xpath '{}'".format(xpath_str))
            return 0
        return element

    def findElementByCSS(self,css_str,element=None):
        if not self.validateLocator(css_str):
            logging.error("Invalid CSS Selector: {}".format(css_str))
            return 0
        logging.info("Searching for element by CSS Selector: '{}'".format(css_str))
        try:
            if element:
                element = element.find_element_by_css_selector(css_str)
            else:
                element = self.driver.find_element_by_css_selector(css_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element by CSS Selector '{}'".format(css_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            logging.info("Found element with CSS Selector: '{}'".format(css_str))
        else:
            logging.error("Couldn't find element by CSS Selector '{}'".format(css_str))
            return 0
        return element

    ##### Locating Multiple Elements #####

    def findElementsByName(self,name_str,element=None):
        if not self.validateLocator(name_str):
            logging.error("Invalid Name: {}".format(name_str))
            return 0
        logging.info("Searching for elements by Name: '{}'".format(name_str))
        try:
            if element:
                elements = element.find_elements_by_name(name_str)
            else:
                elements = self.driver.find_elements_by_name(name_str)
        except NoSuchElementException:
            logging.error("Couldn't find any element by Name '{}'".format(name_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by Name '{}'".format(name_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by Name: '{}'".format(len(elements),name_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by Name '{}'".format(name_str))
            return 0
        return elements

    def findElementsByID(self,id_str,element=None):
        if not self.validateLocator(id_str):
            logging.error("Invalid ID: {}".format(id_str))
            return 0
        logging.info("Searching for elements by ID: '{}'".format(id_str))
        try:
            if element:
                elements = element.find_elements_by_id(id_str)
            else:
                elements = self.driver.find_elements_by_id(id_str)
        except NoSuchElementException:
            logging.error("Couldn't find any element by ID '{}'".format(id_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by ID '{}'".format(id_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by ID: '{}'".format(len(elements),id_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by ID '{}'".format(id_str))
            return 0
        return elements

    def findElementsByTag(self,tag_str,element=None):
        if not self.validateLocator(tag_str):
            logging.error("Invalid Tag: {}".format(tag_str))
            return 0
        logging.info("Searching for elements by Tag: '{}'".format(tag_str))
        try:
            if element:
                elements = element.find_elements_by_tag_name(tag_str)
            else:
                elements = self.driver.find_elements_by_tag_name(tag_str)
        except NoSuchElementException:
            logging.error("Couldn't find any element by Tag '{}'".format(tag_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by Tag '{}'".format(tag_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by Tag: '{}'".format(len(elements),tag_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by Tag '{}'".format(tag_str))
            return 0
        return elements

    def findElementsByPartialText(self,text_str,element=None):
        if not self.validateLocator(text_str):
            logging.error("Invalid Partial Text: {}".format(text_str))
            return 0
        logging.info("Searching for elements by Partial Text: '{}'".format(text_str))
        try:
            if element:
                elements = element.find_elements_by_partial_link_text(text_str)
            else:
                elements = self.driver.find_elements_by_partial_link_text(text_str)
        except NoSuchElementException:
            logging.error("Couldn't find any element by Partial Text '{}'".format(text_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by Partial Text '{}'".format(text_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by Partial Text: '{}'".format(len(elements),text_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by Partial Text '{}'".format(text_str))
            return 0
        return elements

    def findElementsByLinkText(self,link_str,element=None):
        if not self.validateLocator(link_str):
            logging.error("Invalid Link Text: {}".format(link_str))
            return 0
        logging.info("Searching for elements by Link Text: '{}'".format(link_str))
        try:
            if element:
                elements = element.find_elements_by_link_text(link_str)
            else:
                elements = self.driver.find_elements_by_link_text(link_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find any element by Link Text '{}'".format(link_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by Link Text '{}'".format(link_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by Link Text: '{}'".format(len(elements),link_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by Link Text '{}'".format(link_str))
            return 0
        return elements

    def findElementsByClass(self,class_str,element=None):
        if not self.validateLocator(class_str):
            logging.error("Invalid Classname: {}".format(class_str))
            return 0
        logging.info("Searching for elements by Classname: '{}'".format(class_str))
        try:
            if element:
                elements = element.find_elements_by_class_name(class_str)
            else:
                elements = self.driver.find_elements_by_class_name(class_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find any element by Classname '{}'".format(class_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by Classname '{}'".format(class_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by Classname: '{}'".format(len(elements),class_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by Classname '{}'".format(class_str))
            return 0
        return elements

    def findElementsByXPath(self,xpath_str,element=None):
        if not self.validateLocator(xpath_str):
            logging.error("Invalid XPath: {}".format(xpath_str))
            return 0
        logging.info("Searching for elements by XPath: '{}'".format(xpath_str))
        try:
            if element:
                elements = element.find_elements_by_xpath(xpath_str)
            else:
                elements = self.driver.find_elements_by_xpath(xpath_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find any element by XPath '{}'".format(xpath_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by XPath '{}'".format(xpath_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by XPath: '{}'".format(len(elements),xpath_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by XPath '{}'".format(xpath_str))
            return 0
        return elements

    def findElementsByCSS(self,css_str,element=None):
        if not self.validateLocator(css_str):
            logging.error("Invalid CSS Selector: {}".format(css_str))
            return 0
        logging.info("Searching for elements by CSS Selector: '{}'".format(css_str))
        try:
            if element:
                elements = element.find_elements_by_css_selector(css_str)
            else:
                elements = self.driver.find_elements_by_css_selector(css_str)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find any element by CSS Selector '{}'".format(css_str))
            return 0
        except TimeoutException:
            logging.error("TimeoutException: Can't determine loading status. Taking too long. Check your internet connection and try again")
            return 0
        if elements and len(elements) == 0:
            logging.error("Couldn't find any element by CSS Selector '{}'".format(css_str))
            return 0
        elif len(elements) > 0:
            self.elements = elements
            logging.info("Found {} elements by CSS Selector: '{}'".format(len(elements),css_str))
            self.selectedElement = self.elements[0]
        else:
            logging.error("Couldn't find any element by CSS Selector '{}'".format(css_str))
            return 0
        return elements

    ##### Wrapper Functions #####
    def validateLocator(self, locator):
        if not locator:
            logging.error("Locator is NULL")
            return 0
        if not isinstance(locator,str):
            logging.error("Locator is not type str")
            return 0
        if locator == "" or locator == "\n" or locator == " " or locator.__contains__("\n") or len(locator) < 1:
            logging.error("Locator is Invalid")
            return 0
        return 1

    # This function is required to register a particular Web Element (which is defines by the user), so that the browser
    # internel variable (selectedElement) can be assigned to that user defined element.
    def switchElement(self,element=None):
        if element:
            logging.info("Switching to Element")
            # If the user pass in valid Web Element, it will discard the current focused element, and it assigns the
            # new Web Element that passed-in by the user
            if isinstance(element,WebElement):
                logging.info("Switching Current Web Element focus from {} to {}".format(self.selectedElement,element))
                self.selectedElement = element
            # If the user pass in element as an integer. It will then treat this as an index to grab particular element
            # in elements variable. If the variable elements is empty, it will return 1 as in the variable is empty.
            elif isinstance(element,int):
                if self.elements == None or len(self.elements) == 0:
                    logging.warning("Elements is empty")
                    return 1
                else:
                    index = element
                    if index > len(self.elements)-1 or index < 0:
                        logging.warning("Invalid index to select element")
                        return 1
                    logging.info("Switching Current Web Element focus from {} to {}".format(self.selectedElement,self.elements[index]))
                    self.selectedElement = self.elements[index]
            # It didn't select any element
            else:
                logging.error("Error: No element selected")
                return 1
        else:
            logging.info("Switching to Active Element")
            element = None
            try:
                element = self.driver.switch_to_active_element()
            except NoSuchElementException:
                logging.error("NoSuchElementException: Couldn't find active element")
                return 0
            if element and isinstance(element,WebElement):
                logging.info("Got Active Element")
                self.switchElement(element)
            else:
                logging.warning("Couldn't find Active element")
                return 0
        return 0

    def selectElements(self,elements):
        if not isinstance(elements,list):
            logging.error("Elements is not a list")
            return 1
        if self.elements and len(self.elements):
            del self.elements[:]
        self.elements = []
        self.elements = elements
        return 0

    def findElementLink(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.switchElement(element)
                if err:
                    return 0
            else:
                logging.error("Element is not Web Element type")
                return 0
        if self.selectedElement and isinstance(self.selectedElement, WebElement):
            element = self.selectedElement
            tag_attr = element.tag_name
            if tag_attr != "a":
                logging.warning("Attempting to search for Link Element by the Tag attribute 'a' inside {}".format(element))
                element_link = self.findElementByTag("a",element)
                if element_link == 0 or not isinstance(element_link,WebElement):
                    logging.error("The current element does not contain link address")
                    return 0
                elif isinstance(element_link, WebElement):
                    self.switchElement(element_link)
                    return element_link
                else:
                    return 0
            elif tag_attr == "a":
                logging.info("Current selected Element is Link type Web Element")
                return element
            else:
                return 0
        else:
            logging.error("Current selected element is not Web Element type")
            return 0

    def findSubElement(self,element=None,id=None,name=None,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None):
        if element:
            if isinstance(element,WebElement):
                err = self.switchElement(element)
                if err:
                    return 0
            else:
                logging.error("Passed in element is not Web Element type")
                return 0

        element = self.selectedElement
        if element == 0 or not isinstance(element,WebElement):
            logging.error("Current selected element is not Web Element type")
            return 0
        subelement = None
        if tag:
            valid = self.validateLocator(tag)
            if not valid:
                return 0
            subelement = self.findElementByTag(tag,element)
        if id:
            valid = self.validateLocator(id)
            if not valid:
                return 0
            subelement = self.findElementByID(id,element)
        if name:
            valid = self.validateLocator(name)
            if not valid:
                return 0
            subelement = self.findElementByName(name,element)
        if classname:
            valid = self.validateLocator(classname)
            if not valid:
                return 0
            subelement = self.findElementByClass(classname,element)
        if xpath:
            valid = self.validateLocator(xpath)
            if not valid:
                return 0
            subelement = self.findElementByXPath(xpath,element)
        if css:
            valid = self.validateLocator(css)
            if not valid:
                return 0
            subelement = self.findElementByCSS(css,element)
        if linktext:
            valid = self.validateLocator(linktext)
            if not valid:
                return 0
            subelement = self.findElementByLinkText(linktext,element)
        if partialtext:
            valid = self.validateLocator(partialtext)
            if not valid:
                return 0
            subelement = self.findElementByPartialText(partialtext,element)

        if subelement == None:
            logging.error("Web Element locator not specified to find sub-element of {}".format(element))
            return  0
        err = self.switchElement(subelement)
        if err:
            logging.error("Couldn't locate sub-element of {}".format(element))
            return 0
        else: return subelement

    def findElement(self,element=None,id=None,name=None,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None):
        # Find Element
        if not element:
            if id:
                valid = self.validateLocator(id)
                if not valid:
                    return 0
                element = self.findElementByID(id)
            if name:
                valid = self.validateLocator(name)
                if not valid:
                    return 0
                element = self.findElementByName(name)
            if classname:
                valid = self.validateLocator(classname)
                if not valid:
                    return 0
                element = self.findElementByClass(classname)
            if xpath:
                valid = self.validateLocator(xpath)
                if not valid:
                    return 0
                element = self.findElementByXPath(xpath)
            if tag:
                valid = self.validateLocator(tag)
                if not valid:
                    return 0
                element = self.findElementByTag(tag)
            if css:
                valid = self.validateLocator(css)
                if not valid:
                    return 0
                element = self.findElementByCSS(css)
            if linktext:
                valid = self.validateLocator(linktext)
                if not valid:
                    return 0
                element = self.findElementByLinkText(linktext)
            if partialtext:
                valid = self.validateLocator(partialtext)
                if not valid:
                    return 0
                element = self.findElementByPartialText(partialtext)
            err = self.switchElement(element)
            if err:
                logging.error("No input argument to find element")
                return 0
            else: return element
        else:
            # Find Sub-Element
            if isinstance(element,WebElement):
                subelement = self.findSubElement(element=element,id=id,name=name,classname=classname,xpath=xpath,tag=tag,css=css,linktext=linktext,partialtext=partialtext)
                if subelement == None or subelement == 0 or not isinstance(subelement, WebElement):
                    logging.error("Couldn't find Subelement of element {}".format(element))
                else: return subelement
            # Find Sub-Element from List of Element by its locator
            elif isinstance(element,list):
                del self.elements[:]
                del self.elements
                self.elements = element
                for temp_element in self.elements:
                    if classname:
                        class_attr = temp_element.get_attribute("class")
                        if class_attr == classname:
                            self.switchElement(temp_element)
                            return temp_element
                    if name:
                        name_attr = temp_element.get_attribute("name")
                        if name_attr == name:
                            self.switchElement(temp_element)
                            return temp_element
                    if id:
                        id_attr = temp_element.get_attribute("id")
                        if id_attr == id:
                            self.switchElement(temp_element)
                            return temp_element
                    if tag:
                        tag_attr = temp_element.tag_name
                        if tag_attr == tag:
                            self.switchElement(temp_element)
                            return temp_element
                    if linktext:
                        linktext_attr = temp_element.text
                        if linktext_attr == linktext:
                            self.switchElement(temp_element)
                            return temp_element
                    if partialtext:
                        linktext_attr = temp_element.text
                        if partialtext in linktext_attr:
                            self.switchElement(temp_element)
                            return temp_element
                logging.error("Couldn't find particular element from the list by given its locator")
                return 0
            else: return 0

    def findParentElement(self,element=None):
        if element:
            if isinstance(element,WebElement):
                err = self.switchElement(element)
                if err:
                    return 0
            else:
                logging.error("Passed in element is not Web Element type {}".format(element))
                return 0
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Current selected element is not Web Element type {}".format(self.selectedElement))
            return 0
        try:
            element = self.selectedElement.find_element_by_xpath('..')
        except NoSuchElementException:
            logging.error("NoSuchElementException: Element {} does not have parent element".format(self.selectedElement,element))
            return 0
        if element == 0 or element == None or not isinstance(element,WebElement):
            logging.error("Element {} does not have parent element {}".format(self.selectedElement,element))
            return 0
        else:
            logging.info("Found Parent Element: {}".format(element))
            self.switchElement(element)
            return self.selectedElement

    def findBodyElement(self):
        element = self.findElementByTag("body")
        if element == 0 or element == None:
            logging.error("Page does not contain 'body' tag. Can't find body element.")
            return 0
        else:
            logging.info("Found Body Web Element: {}".format(element))
            self.switchElement(element)
            return self.selectedElement

    def highlightElement(self,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return 1
        try:
            self.driver.execute_script("arguments[0].style.border='3px solid red'", self.selectedElement)
        except NoSuchElementException:
            logging.error("NoSuchElementException: No element to highlight")
            return 1
        return 0

    def getElementValue(self,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        try:
            val = self.selectedElement.get_attribute('value')
        except NoSuchElementException:
            logging.error("NoSuchElementException: No element to get the value")
            return None
        except NoSuchAttributeException:
            logging.error("NoSuchAttributeException: Element does not have attribute value")
            return None
        if val == 'None' or val == None:
            return None
        return str(val)

    def getAttributeValue(self,attribute,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        try:
            val = self.selectedElement.get_attribute('{}'.format(attribute))
        except NoSuchElementException:
            logging.error("NoSuchElementException: No element to get specified attribute value")
            return None
        except NoSuchAttributeException:
            logging.error("NoSuchAttributeException: Element does not have attribute {}".format(attribute))
            return None
        if val == 'None' or val == None:
            return None
        return str(val)

    def getXpath(self,element=None):
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
        temp = self.selectedElement
        try:
            xpath = self.driver.execute_script("function absoluteXPath(element) {"+
                        "var comp, comps = [];"+
                        "var parent = null;"+
                        "var xpath = '';"+
                        "var getPos = function(element) {"+
                        "var position = 1, curNode;"+
                        "if (element.nodeType == Node.ATTRIBUTE_NODE) {"+
                        "return null;"+
                        "}"+
                        "for (curNode = element.previousSibling; curNode; curNode = curNode.previousSibling){"+
                        "if (curNode.nodeName == element.nodeName) {"+
                        "++position;"+
                        "}"+
                        "}"+
                        "return position;"+
                        "};"+
                        "if (element instanceof Document) {"+
                        "return '/';"+
                        "}"+
                        "for (; element && !(element instanceof Document); element = element.nodeType ==Node.ATTRIBUTE_NODE ? element.ownerElement : element.parentNode) {"+
                        "comp = comps[comps.length] = {};"+
                        "switch (element.nodeType) {"+
                        "case Node.TEXT_NODE:"+
                        "comp.name = 'text()';"+
                        "break;"+
                        "case Node.ATTRIBUTE_NODE:"+
                        "comp.name = '@' + element.nodeName;"+
                        "break;"+
                        "case Node.PROCESSING_INSTRUCTION_NODE:"+
                        "comp.name = 'processing-instruction()';"+
                        "break;"+
                        "case Node.COMMENT_NODE:"+
                        "comp.name = 'comment()';"+
                        "break;"+
                        "case Node.ELEMENT_NODE:"+
                        "comp.name = element.nodeName;"+
                        "break;"+
                        "}"+
                        "comp.position = getPos(element);"+
                        "}"+
                        "for (var i = comps.length - 1; i >= 0; i--) {"+
                        "comp = comps[i];"+
                        "xpath += '/' + comp.name.toLowerCase();"+
                        "if (comp.position !== null) {"+
                        "xpath += '[' + comp.position + ']';"+
                        "}"+
                        "}"+
                        "return xpath;"+
                        "} return absoluteXPath(arguments[0]);", element)
        except NoSuchElementException:
            logging.error("NoSuchElementException: No element to get the value")
            self.switchElement(temp)
            return None
        return str(xpath)

    def findSiblingsElements(self,element=None):
        if element:
            if isinstance(element,WebElement):
                self.switchElement(element)
            else:
                logging.error("Element is not Web Element instance")
                return None
        if not isinstance(self.selectedElement,WebElement):
            logging.error("Element is not Web Element instance")
            return None
        temp = self.selectedElement
        element = self.findParentElement(temp)
        xpath = self.getXpath(element)
        xpath = "{}/*".format(xpath)
        try:
            elements = self.findElementsByXPath(xpath)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find Elements")
            return 0
        except StaleElementReferenceException:
            logging.error("StaleElementReferenceException: Element is destroyed")
            return 0
        if elements and len(elements):
            return elements
        else:
            self.switchElement(temp)
            return 0

    def findPreviousElement(self,element=None):
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
        elements = self.findSiblingsElements(element)
        if elements and len(elements):
            index = 0
            for index,temp_element in enumerate(elements):
                if temp_element == element:
                    break
            if index == 0:
                return 0
            else:
                self.switchElement(elements[index-1])
                return elements[index-1]
        else:
            return 0

    def findNextElement(self,element=None):
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
        elements = self.findSiblingsElements(element)
        if elements and len(elements):
            index = 0
            for index,temp_element in enumerate(elements):
                if temp_element == element:
                    break
            if index == len(elements)-1:
                return 0
            else:
                self.switchElement(elements[index+1])
                return elements[index+1]
        else:
            return 0

    def findInteractiveElement(self,element=None):
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
        if element.tag_name == "input" or element.tag_name == "button" or element.tag_name == "select" or \
                        element.tag_name == "option" or element.tag_name == "a":
            self.switchElement(element)
            return element
        elif element.tag_name == "body":
            return 0
        temp = element
        element = self.findParentElement(temp)
        input_element = self.findElementByTag('input',element=element)
        if input_element:
            self.switchElement(element=input_element)
            return input_element
        i_element = self.findElementByTag('i',element=element)
        if i_element:
            self.switchElement(element=i_element)
            return i_element
        button_element = self.findElementByTag('button',element=element)
        if button_element:
            self.switchElement(element=button_element)
            return button_element
        select_element = self.findElementByTag('select',element=element)
        if select_element:
            self.switchElement(element=select_element)
            return select_element
        option_element = self.findElementByTag('option',element=element)
        if option_element:
            self.switchElement(element=option_element)
            return option_element
        link_element = self.findElementByTag('a',element=element)
        if link_element:
            self.switchElement(element=link_element)
            return link_element
        return self.findInteractiveElement(element=element)

    def findOptionElement(self,value,select):
        if not value:
            logging.error("Value is empty")
            return 0
        if isinstance(select,Select):
            options = select.options
            for element in options:
                cur_element_val = str(element.get_attribute("value").encode('ascii', 'ignore').decode('ascii'))
                if cur_element_val == value:
                    self.selectElements(options)
                    self.switchElement(element)
                    return element
        elif isinstance(select,WebElement):
            select = Select(select)
            return self.findOptionElement(value,select=select)
        elif isinstance(select,list):
            for element in select:
                if element.get_attribute("value") == value:
                    self.selectElements(elements=select)
                    self.switchElement(element)
                    return element
        else:
            logging.error("input select {}, is not instance of Select, Web Element, or List.".format(select))
            return 0
        logging.warning("Couldn't find any element with the value {} from select".format(value))
        return 0

    def getElementCoordinates(self,element=None):
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
        location_dic = element.location
        if location_dic and isinstance(location_dic,dict):
            x = location_dic.get('x')
            y = location_dic.get('y')
        else:
            logging.error("Element location is not determined")
            return 0
        return (x,y)