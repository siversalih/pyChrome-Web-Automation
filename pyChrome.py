import time
import os
import sys

curr_dir = os.getcwd()
src_dir = "{}/src".format(curr_dir)
if not(os.path.exists(src_dir)):
    print("Path {} does not exist".format(src_dir))
    exit(1)
sys.path.insert(0, src_dir)

binary_dir = "{}/bin".format(curr_dir)
if(not os.path.exists(binary_dir)):
    print("Path {} does not exist".format(binary_dir))
    exit(1)

try:
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)
try:
    import json
except ImportError:
    print "json module is not installed...Exiting program."
    exit(1)
try:
    from navigation import Navigation
except ImportError:
    print "navigation.py is missing...Exiting program."
    exit(1)
try:
    from window import Window
except ImportError:
    print "window.py is missing...Exiting program."
    exit(1)
try:
    from element import Element
except ImportError:
    print "element.py is missing...Exiting program."
    exit(1)
try:
    from interaction import Interaction
except ImportError:
    print "interaction.py is missing...Exiting program."
    exit(1)
try:
    from browser import Browser
except ImportError:
    print "browser.py is missing...Exiting program."
    exit(1)
try:
    from capture import Capture
except ImportError:
    print "capture.py is missing...Exiting program."
    exit(1)
try:
    from combo import Combo
except ImportError:
    print "combo.py is missing...Exiting program."
    exit(1)

class PyChrome(Window,Browser,Navigation,Element,Interaction,Capture,Combo):
    config_filename = ""
    drivername = ""
    directory = ""
    bin_dir = ""
    pageload_timeout = 0
    driver = None
    ghost = 0
    window = None
    browser = None
    capture = None
    combo = None

    def __init__(self, config_filename = 0, ghostmode = 0):
        self.config_filename = "config.json"
        self.drivername = "chromedriver"
        self.bin_dir = binary_dir
        self.directory = os.getcwd()
        self.pageload_timeout = -1
        self.ghost = False
        if ghostmode and self.validateGhostmode(ghostmode):
            self.ghost = ghostmode

        if config_filename:
            self.config_filename = config_filename
            file_directory = "{}/{}".format(self.directory,self.config_filename)
            if(os.path.exists(file_directory)):
                print "Reading {} file".format(self.config_filename)
                self.readJSONFile(self.config_filename,ghostmode=ghostmode)
            else:
                print("{} is not in {}".format(self.config_filename,self.directory))
                exit(1)
        self.__start(ghostmode=self.ghost)
        return

    def readJSONFile(self, config_filename = 0, ghostmode = 0):
        if config_filename:
            self.config_filename = config_filename
        with open(self.config_filename) as jsonFile:
            config = json.load(jsonFile)
        self.drivername = config.get('driver')
        directory = ""
        directory = config.get('directory')
        file_directory = "{}/{}".format(directory,self.drivername)
        if directory and len(directory):
            if os.path.exists(file_directory):
                self.directory = directory
            else:
                print("{} is not in {}".format(self.drivername,directory))
                exit(1)
        else:
            directory = self.bin_dir
            file_directory = "{}/{}".format(directory,self.drivername)
            if os.path.exists(file_directory):
                self.bin_dir = directory
                #self.directory = directory
            else:
                print("{} is not in {}".format(self.drivername,self.directory))
                exit(1)

        pageload_timeout = config.get('pageload_timeout')
        if self.validatePageLoadTimeout(pageload_timeout):
            self.pageload_timeout = pageload_timeout

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
        if self.ghost:
            self.drivername = "phantomjs"
        file_directory = "{}/{}".format(self.bin_dir,self.drivername)
        if (os.path.exists(file_directory)):
            if self.ghost == False:
                print "Starting Chrome Browser"
                chrome_options = Options()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                chrome_options.add_argument("--disable-extensions")
                self.driver = webdriver.Chrome(file_directory,0,chrome_options,None,None,None)
                self.window = Window(self.driver, config=self.config_filename)
                self.zoomWin = self.window.zoomWin
                self.sizeWin = self.window.sizeWin
                self.scrollWin = self.window.scrollWin
                self.positionWin = self.window.positionWin
                self.driver.set_page_load_timeout(self.pageload_timeout)
            else:
                print "Starting Ghost Browser"
                self.driver = webdriver.PhantomJS(executable_path=file_directory)
            print("Driver Location: {}".format(self.bin_dir))
            print("Driver Name: {}\n".format(self.drivername))
            time.sleep(1)

            if self.browser == None:
                self.browser = Browser(self.driver,self.ghost)
                self.tabs = self.browser.tabs
                self.tab = self.browser.tab
            self.ghostmode = self.ghost
            self.element = self.browser.element
            self.elements = self.browser.element.elements
            self.selectedElement = self.browser.element.selectedElement
            self.interaction = self.browser.interaction
            self.navigation = self.browser.navigation

            if self.combo == None:
                self.combo = Combo(self.driver,self.browser)

            if self.capture == None:
                self.capture = Capture(self.driver,self.browser.element,self.directory,self.ghostmode)
            self.capture.ghostmode = self.ghost

        else:
            print("Driver is not present!")
            exit(1)

    def quit(self):
        print "Quiting {}".format(self.drivername)
        if self.driver == None:
            print "There is no Driver present"
            return 1
        if self.browser:
            self.browser.close()
            del self.browser
        if self.driver:
            self.driver.stop_client()
            self.driver.quit()
            self.driver = None
        if self.capture:
            self.capture.dealloc()
            del self.capture
        if self.interaction:
            self.interaction.dealloc()
            del self.interaction
        if self.navigation:
            self.navigation.dealloc()
            del self.navigation
        if self.element:
            self.element.dealloc()
            del self.element
        if self.window:
            self.window.dealloc()
            del self.window
            del self.sizeWin
            del self.zoomWin
            del self.scrollWin
            del self.positionWin
        if self.combo:
            self.combo.dealloc()
            del self.combo
        if self.elements:
            del self.elements
        if self.selectedElement:
            del self.selectedElement
        if self.tabs:
            del self.tabs[:]
            del self.tabs
        if self.tab:
            del self.tab
        if self.drivername:
            del self.drivername
        return 0

    def switchDriverMode(self, ghostmode = 0):
        if ghostmode and self.validateGhostmode(ghostmode):
            self.ghost = ghostmode
            self.ghostmode = self.ghost
        else:
            self.ghost = self.ghost ^ True
        self.quit()
        self.__init__(self.config_filename,self.ghost)
        return 0

    def validatePageLoadTimeout(self,pageload_timeout):
        try:
            pageload_timeout = int(pageload_timeout)
        except ValueError:
            print "Page Load Timeout Invalid Format"
            return 0
        if not isinstance(pageload_timeout,int):
            return 0
        if pageload_timeout < -1:
            return 0
        if pageload_timeout > 120:
            return 0
        return 1

    def validateGhostmode(self,ghostmode):
        if not isinstance(ghostmode, bool):
            return 0
        return 1


if __name__ == "__main__":
    argv = sys.argv[1:]
    if(argv):
        filename = argv[0]
    else:
        filename = 'config.json'
    directory = os.getcwd()
    file_directory = "{}/{}".format(directory,filename)
    if(not os.path.exists(file_directory)):
        print("{} is not in {}".format(filename,directory))
        exit(1)
