import time
import os
import sys
import logging
from sys import platform

curr_dir = os.getcwd()
logging.info("Current Work directory: {}".format(curr_dir))
src_dir = "{}/src".format(curr_dir)
logging.info("Source directory: {}".format(src_dir))

if not(os.path.exists(src_dir)):
    logging.critical("Path {} does not exist".format(src_dir))
    exit(1)
sys.path.insert(0, src_dir)

try:
    from window import Window
except ImportError:
    logging.critical("window.py is missing...Exiting program.")
    exit(1)

try:
    from browser import Browser
except ImportError:
    logging.critical("browser.py is missing...Exiting program.")
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

try:
    from combo import Combo
except ImportError:
    logging.critical("combo.py is missing...Exiting program.")
    exit(1)

binary_dir = "{}/bin".format(curr_dir)
logging.info("Binary directory: {}".format(binary_dir))
if(not os.path.exists(binary_dir)):
    logging.critical("Path {} does not exist".format(binary_dir))
    exit(1)
try:
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)
try:
    import json
except ImportError:
    logging.critical("json module is not installed...Exiting program.")
    exit(1)

class PyChrome(Element,Interaction,Combo):
    config_filename = ""
    drivername = ""
    directory = ""
    bin_dir = ""
    pageload_timeout = 0
    driver = None
    ghost = 0
    window = None
    browser = None
    selectedElement = None
    elements = None

    def __init__(self, config_filename=None, ghostmode=0):
        self.config_filename = "config.json"
        self.bin_dir = binary_dir
        self.directory = os.getcwd()
        self.pageload_timeout = -1
        self.ghost = False
        if ghostmode and self.validateGhostmode(ghostmode):
            self.ghost = ghostmode
            logging.info("Ghost Mode: {}".format(self.ghost))
        if config_filename:
            self.config_filename = config_filename
            file_directory = "{}/{}".format(self.directory,self.config_filename)
            if(os.path.exists(file_directory)):
                self.__readJSONFile(self.config_filename,ghostmode=ghostmode)
            else:
                logging.critical("{} is not in {}".format(self.config_filename,self.directory))
                exit(1)
        self.__start(ghostmode=self.ghost)
        return

    def __selectPlatform(self,ghostmode=0):
        if ghostmode:
            self.drivername = "phantomjs"
        else:
            self.drivername = "chromedriver"
        if platform == "linux" or platform == "linux2":
            logging.critical("pyChrome does not support to run on linux at this point".format())
            exit(1)
        elif platform == "darwin":
            logging.info("pyChrome is running on Mac OS")
        elif platform == "win32":
            logging.info("pyChrome is running on Windows")
            self.drivername = self.drivername + ".exe"
        else:
            logging.critical("pyChrome can not detect the platform you running.".format())
            exit(1)

    def __readJSONFile(self, config_filename=None, ghostmode=0):
        if config_filename:
            self.config_filename = config_filename
            logging.info("Reading configuration file {}".format(self.config_filename))
        with open(self.config_filename) as jsonFile:
            config = json.load(jsonFile)
        self.drivername = config.get('driver')
        if self.drivername == "chromedriver" and ghostmode:
            self.drivername = "phantomjs"
        elif self.drivername == "phantomjs" and ghostmode == False:
            self.drivername = "chromedriver"
        if platform == "linux" or platform == "linux2":
            logging.critical("pyChrome does not support to run on linux at this point".format())
            exit(1)
        elif platform == "darwin":
            logging.info("pyChrome is running on Mac OS")
        elif platform == "win32":
            self.drivername = self.drivername + ".exe"
        else:
            logging.critical("pyChrome can not detect the platform you running.".format())
            exit(1)
        directory = config.get('directory')
        file_directory = "{}/{}".format(directory,self.drivername)
        if directory and len(directory):
            if os.path.exists(file_directory):
                self.directory = directory
            else:
                logging.critical("{} is not in {}".format(self.drivername,directory))
                exit(1)
        else:
            directory = self.bin_dir
            file_directory = "{}/{}".format(directory,self.drivername)
            if os.path.exists(file_directory):
                self.bin_dir = directory
            else:
                logging.critical("{} is not in {}".format(self.drivername,self.directory))
                exit(1)
        pageload_timeout = config.get('pageload_timeout')
        if self.validatePageLoadTimeout(pageload_timeout):
            self.pageload_timeout = pageload_timeout
            logging.info("Page Load Timeout Set to {}".format(self.pageload_timeout))
        if ghostmode and self.validateGhostmode(ghostmode):
            self.ghost = ghostmode
        else:
            ghostmode = config.get('ghost')
            if self.validateGhostmode(ghostmode):
                self.ghost = ghostmode
        return 0

    def __start(self, ghostmode = 0):
        if ghostmode and self.validateGhostmode(ghostmode):
            self.ghost = ghostmode
        if not self.drivername:
            self.__selectPlatform(ghostmode)
        if self.ghost:
            logging.info("Using WebDrver {}".format(self.drivername))
            logging.info("Starting Ghost Browser")
            file_directory = "{}/{}".format(self.bin_dir,self.drivername)
            if (os.path.exists(file_directory)):
                self.driver = webdriver.PhantomJS(executable_path=file_directory)
                self.driver.set_page_load_timeout(self.pageload_timeout)
                self.browser = Browser(self.driver,True)
            else:
                logging.critical("GhostDriver (PhantomJS) is not present!")
                exit(1)
        else:
            logging.info("Using WebDrver {}".format(self.drivername))
            logging.info("Starting Chrome Browser")
            file_directory = "{}/{}".format(self.bin_dir,self.drivername)
            if (os.path.exists(file_directory)):
                chrome_options = Options()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                chrome_options.add_argument("--disable-extensions")
                self.driver = webdriver.Chrome(file_directory,0,chrome_options,None,None,None)
                self.driver.set_page_load_timeout(self.pageload_timeout)
                self.window = Window(self.driver, config_filename=self.config_filename)
                self.browser = self.window.browser
            else:
                logging.critical("WebDriver is not present!")
                exit(1)
        logging.info("Driver Location: {}".format(self.bin_dir))
        logging.info("Driver Name: {}\n".format(self.drivername))
        self.findBodyElement()
        self.elements = []
        time.sleep(1)
        return 0

    def quit(self):
        logging.info("Quiting {} Session".format(self.drivername))
        if self.browser:
            self.browser.dealloc()
            del self.browser
        if self.window:
            self.window.dealloc()
            del self.window
        if self.driver:
            self.driver.stop_client()
            self.driver.quit()
            del self.driver
        else:
            logging.warning("Driver is not present! There is not Driver to deallocate")
            return 1
        logging.info("Quited the Session and Closed the Client")
        if self.elements:
            del self.elements[:]
            del self.elements
        if self.selectedElement:
            del self.selectedElement
        return 0

    def switchDriverMode(self, ghostmode = 0):
        if ghostmode and self.validateGhostmode(ghostmode):
            logging.info("Setting Ghost Mode to {}".format(ghostmode))
            self.ghost = ghostmode
            self.ghostmode = self.ghost
        else:
            logging.info("Switching Ghost Mode: {} -> {}".format(self.ghost,self.ghost ^ True))
            self.ghost = self.ghost ^ True
        self.quit()
        self.__init__(self.config_filename,self.ghost)
        return 0

    def validatePageLoadTimeout(self,pageload_timeout):
        try:
            pageload_timeout = int(pageload_timeout)
        except ValueError:
            logging.error("ValueError Exep: Page Load Timeout Invalid Format: {}".format(pageload_timeout))
            return 0
        if not isinstance(pageload_timeout,int):
            logging.error("Page Load Timeout is not Int instance".format(pageload_timeout))
            return 0
        if pageload_timeout < -1:
            logging.error("Page Load Timeout is < -1".format(pageload_timeout))
            return 0
        if pageload_timeout > 120:
            logging.error("Page Load Timeout is > 120".format(pageload_timeout))
            return 0
        return 1

    def validateGhostmode(self,ghostmode):
        if not isinstance(ghostmode, bool):
            logging.error("Ghost Mode is not Boolean expression".format(ghostmode))
            return 0
        return 1

    def open(self,url):
        # Invalid URL
        if url == 0 or len(url) == 0:
            logging.error("Couldn't Open the page {}. \nPlease check the URL".format(url))
            return 1
        # Search Instead
        if not "www." in url and not ".com" in url and not "." in url:
            err = self.search(url)
            if err:
                logging.error("Failed to Search")
                return 1
            return 0
        err=self.browser.open(url)
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def getTabTitle(self):
        return self.browser.getcurrentTabTitle()

    def getTabLink(self):
        return self.browser.getcurrentTabLink()

    def close(self):
        return self.browser.close()

    def closeTab(self, tabnum=0):
        err = self.browser.closeTab(tabnum=tabnum)
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def newTab(self,url=None):
        err = self.browser.newTab(url=url)
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def rightTab(self):
        err = self.browser.rightTab()
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def leftTab(self):
        err = self.browser.leftTab()
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def switchTab(self, index):
        err = self.browser.switchTab(index)
        element = self.findBodyElement()
        if not element:
            err = 1
        return err

    def position(self, windowPosition):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.position(windowPosition)

    def size(self, windowSize):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.size(windowSize)

    def zoom(self, percent):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.zoom(percent)

    def zoomIn(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.zoomIn()

    def zoomOut(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.zoomOut()

    def scrollToElement(self, element):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        err = self.switchElement(element)
        return  err or self.window.scrollToElement(element)

    def scrol(self,scrollWin):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrol(scrollWin=scrollWin)

    def scrollDown(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollDown()

    def scrollBottom(self,animate=0):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollBottom(animate)

    def scrollUp(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollUp()

    def scrollTop(self,animate=0):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollTop(animate)

    def scrollRight(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollRight()

    def scrollLeft(self):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.scrollLeft()

    def validateSize(self, sizeWin):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.validateSize(sizeWin)

    def validateZoom(self, percent):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.validateZoom(percent)

    def validateScroll(self, scrollWin):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.validateScroll(scrollWin)

    def validatePosition(self, positionWin):
        if self.ghost:
            logging.warning("When in Ghost Mode using {}, there is no Window.".format(self.drivername))
            return 0
        return self.window.validatePosition(positionWin)

    def back(self):
        return self.browser.back()

    def forward(self):
        return self.browser.forward()

    def refresh(self):
        return self.browser.refresh()

    def elementDump(self,element,filename=None):
        return self.browser.elementDump(element,filename=filename)

    def screenshot(self, save_name=None, save_directory=None):
        return self.browser.screenshot(save_name=save_name,save_directory=save_directory)

    def sourceDump(self, filename=None):
        return self.browser.sourceDump(filename=filename)

    def record(self,element=None):
        if element:
            err = self.switchElement(element)
            if err:
                logging.error("Failed to Select Element to Record")
                return 1
        else:
            self.switchElement()
        err = self.browser.record(self.selectedElement)
        return err

    def storeRecorder(self,filename=None,directory=None):
        err = self.browser.storeRecorder(filename=filename,directory=directory)
        return err

    def loadRecorder(self,filename=None,directory=None):
        err = self.browser.loadRecorder(filename,directory=directory)
        return err

    def playback(self):
        err = self.browser.playback()
        return err

    def recordButton(self,element=None):
        err = self.browser.recordButton(element=element)
        return err

    def getRecordedElements(self):
        return self.browser.getRecordedElements()

    def deleteRecord(self):
        return self.browser.deleteRecord()

    def clearRecorder(self):
        return self.browser.clearRecorder()

if __name__ == "__main__":
    argv = sys.argv[1:]
    if(argv):
        filename = argv[0]
    else:
        filename = 'config.json'
    directory = os.getcwd()
    file_directory = "{}/{}".format(directory,filename)
    if(not os.path.exists(file_directory)):
        logging.critical("{} is not in {}".format(filename,directory))
        exit(1)