import logging

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
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)
try:
    from element import Element
except ImportError:
    logging.critical("element.py is missing...Exiting program.")
    exit(1)


#### Record ####

class Capture:
    driver = None
    element = None
    directory = None
    ghostmode = None

    def __init__(self,driver,element,directory,ghostmode):
        self.driver = driver
        self.element = element
        self.directory = directory
        self.ghostmode = ghostmode

    def dealloc(self):
        if self.driver:
            del self.driver
        if self.element:
            self.element.dealloc()
            del self.element
        del self.directory
        del self.ghostmode

    def screenshot(self, save_name = 0, save_directory = 0):
        filename = "save_image"
        if self.ghostmode:
            filename = "save_image_ghost"
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
            logging.error("Failed to Screen Capture {}".format(self.driver.current_url))
            return 1
        return 0

    def sourceDump(self, filename = 0):
        extension = ".html"
        name = "source"
        if filename:
            name = filename

        if not self.driver or not self.driver.current_url:
            logging.error("There is no driver or URL to get the source")
            return 1
        try:
            urlopen = urllib.urlopen(self.driver.current_url) # Open the URL.
        except Exception:
            logging.error("Failed to get the source code for {}".format(self.driver.current_url))
            return 1
        source = urlopen.readlines() # Read the source and save it to a variable.
        if not extension in name:
            name = "{}{}".format(name,extension)
        file = open(name,"wb") #open file in binary mode
        file.writelines(source)
        file.close()
        logging.info("Source Code Dump: {}".format("{}/{}".format(self.directory,name)))
        return 0

    def elementDump(self, element = 0, filename = 0):
        extension = ".html"
        name = "source"
        if filename:
            name = filename
        if element:
            self.element.selectedElement = element

        if not isinstance(self.element.selectedElement,WebElement) or self.element.selectedElement == None:
            logging.error("There is no element to get the source code")
            return 1
        try:
            source=self.element.selectedElement.get_attribute('innerHTML')
        except Exception:
            logging.error("Failed to get the source code for {}".format(self.element.selectedElement))
            return 1
        if not extension in name:
            name = "{}{}".format(name,extension)
        file = open(name,"wb") #open file in binary mode
        file.writelines(source)
        file.close()
        logging.info("Element Source Dump: {}".format("{}/{}".format(self.directory,name)))
        return 0
