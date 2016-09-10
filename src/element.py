try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)

##### Element ######

class Element:
    driver = None
    selectedElement = None
    elements = None

    def __init__(self,driver):
        self.driver = driver
        self.elements = None
        self.elements = []
        self.selectedElement = self.findElementByTag('body')

    def dealloc(self):
        if self.driver:
            del self.driver
        if self.elements:
            del self.elements[:]
            del self.elements
        if self.selectedElement:
            del self.selectedElement

    def findElementByID(self,id_str):
        element = 0
        if id_str == 0 and len(id_str) == 0:
            print "ID String is Empty '{}'".format(id_str)
            return 0
        print "Searching for element with ID: '{}'".format(id_str)
        try:
            element = self.driver.find_element_by_id(id_str)
        except NoSuchElementException:
            print "Couldn't find Element by id '{}'".format(id_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with id: '{}'".format(id_str)
            return element
        else:
            print "Couldn't find Element by id '{}'".format(id_str)
            return 0

    def findElementByName(self,name_str):
        element = 0
        if name_str == 0 and len(name_str) == 0:
            print "Name String is Empty '{}'".format(name_str)
            return 0
        print "Searching for element with name: '{}'".format(name_str)
        try:
            element = self.driver.find_element_by_name(name_str)
        except NoSuchElementException:
            print "Couldn't find Element by name '{}'".format(name_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element,WebElement):
            self.selectedElement = element
            print "Found element with name: '{}'".format(name_str)
            return element
        else:
            print "Couldn't find Element by name '{}'".format(name_str)
            return 0

    def findElementByTag(self,tag_str):
        element = 0
        if tag_str == 0 and len(tag_str) == 0:
            print "Tag String is Empty '{}'".format(tag_str)
            return 0
        print "Searching for element with tag: '{}'".format(tag_str)
        try:
            element = self.driver.find_element_by_tag_name(tag_str)
        except NoSuchElementException:
            print "Couldn't find Element by tag '{}'".format(tag_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element,WebElement):
            self.selectedElement = element
            print "Found element with tag: '{}'".format(self.selectedElement.tag_name)
            return element
        else:
            print "Couldn't find Element by tag '{}'".format(tag_str)
            return 0

    def findElementByPartialText(self,text_str):
        element = 0
        if text_str == 0 and len(text_str) == 0:
            print "Text String is Empty '{}'".format(text_str)
            return 0
        print "Searching for element with partial Text: '{}'".format(text_str)
        try:
            element = self.driver.find_element_by_partial_link_text(text_str)
        except NoSuchElementException:
            print "Couldn't find Element by text '{}'".format(text_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element,WebElement):
            self.selectedElement = element
            print "Found element with text: '{}'".format(text_str)
            return element
        else:
            print "Couldn't find Element by text '{}'".format(text_str)
            return 0

    def findElementsByID(self,id_str):
        elements = []
        if id_str == 0 and len(id_str) == 0:
            print "ID string is empty '{}'".format(id_str)
            return 0
        print "Searching for elements with id: '{}'".format(id_str)
        try:
            elements = self.driver.find_elements_by_id(id_str)
        except NoSuchElementException:
            print "Couldn't find any element by id '{}'".format(id_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by id '{}'".format(id_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements with id: '{}'".format(len(elements),id_str)
            self.selectedElement = self.elements[0]
            return self.elements
        else:
            return 0

    def findElementsByName(self,name_str):
        elements = []
        if name_str == 0 and len(name_str) == 0:
            print "Name String is Empty '{}'".format(name_str)
            return 0
        print "Searching for elements with name: '{}'".format(name_str)
        try:
            elements = self.driver.find_elements_by_name(name_str)
        except NoSuchElementException:
            print "Couldn't find any element by name '{}'".format(name_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by name '{}'".format(name_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements with name: '{}'".format(len(elements),name_str)
            self.selectedElement = self.elements[0]
            return self.elements
        else:
            return 0

    def findElementsByTag(self,tag_str):
        elements = []
        if tag_str == 0 and len(tag_str) == 0:
            print "Tag string is empty '{}'".format(tag_str)
            return 0
        print "Searching for elements with tag: '{}'".format(tag_str)
        try:
            elements = self.driver.find_elements_by_tag_name(tag_str)
        except NoSuchElementException:
            print "Couldn't find any element by tag '{}'".format(tag_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by tag '{}'".format(tag_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements with tag: '{}'".format(len(elements),tag_str)
            self.selectedElement = self.elements[0]
            return self.elements
        else:
            return 0

    def findElementsByClass(self,class_str):
        elements = []
        if class_str == 0 and len(class_str) == 0:
            print "Classname string is empty '{}'".format(class_str)
            return 0
        print "Searching for elements with classname: '{}'".format(class_str)
        try:
            elements = self.driver.find_elements_by_class_name(class_str)
        except NoSuchElementException:
            print "Couldn't find any element by classname '{}'".format(class_str)
            return 0
        except TimeoutException:
            print "TimeoutException: timeout: cannot determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by classname '{}'".format(class_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements with classname: '{}'".format(len(elements),class_str)
            self.selectedElement = self.elements[0]
            return self.elements
        else:
            return 0
