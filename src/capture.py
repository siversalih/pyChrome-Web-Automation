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
    directory = None

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
            logging.error("Failed to Screen Capture {}".format(self.cur_tab.link))
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
            urlopen = urllib.urlopen(self.cur_tab.link) # Open the URL.
        except Exception:
            logging.error("Failed to get the source code for {}".format(self.cur_tab.link))
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