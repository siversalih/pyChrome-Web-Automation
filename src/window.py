import time
import json
import logging
import os
import sys

try:
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.keys import Keys
except ImportError:
    logging.critical("Selenium module is not installed...Exiting program.")
    exit(1)

try:
    from browser import Browser
except ImportError:
    logging.critical("browser.py is missing...Exiting program.")
    exit(1)

##### Window #######
class Window:
    directory = ""
    config_filename = ""
    driver = None
    drivername = ""
    positionWin = ()
    sizeWin = ()
    zoomWin = 0
    scrollWin = ()
    browser = None

    def __readJSONFile(self):
        file_directory = "{}/{}".format(self.directory,self.config_filename)
        if not (os.path.exists(file_directory)):
            logging.critical("{} is not in {}".format(self.config_filename,self.directory))
            exit(1)
        with open(self.config_filename) as jsonFile:
            config = json.load(jsonFile)
        positionWin = config.get('position')
        x = positionWin[0]
        y = positionWin[1]
        positionWin = self.validatePosition(positionWin)
        if positionWin:
            self.positionWin = positionWin
        sizeWin = config.get('size')
        w = sizeWin[0]
        h = sizeWin[1]
        sizeWin = self.validateSize((w,h))
        if sizeWin:
            self.sizeWin = sizeWin
        zoomWin = config.get('zoom')
        if self.validateZoom(zoomWin):
            self.zoomWin = zoomWin
        scrollWin = config.get('scroll')
        scrollWin = (scrollWin[0],scrollWin[1])
        if self.validateScroll(scrollWin):
            self.scrollWin = scrollWin
        return 0

    def __init__(self,driver, config_filename=0):
        self.driver = driver
        self.directory = os.getcwd()
        self.config_filename = "config.json"
        self.drivername = "chromedriver"
        self.positionWin = (100,50)
        self.sizeWin = (720,480)
        self.zoomWin = 70
        self.scrollWin = (0,0)
        if config_filename:
            self.config_filename = config_filename
            self.__readJSONFile()
        self.size(self.sizeWin)
        self.position(self.positionWin)
        self.zoom(self.zoomWin)
        self.scrol(self.scrollWin)
        self.browser = Browser(self.driver,False)

    def dealloc(self):
        if self.directory:
            del self.directory
        if self.config_filename:
            del self.config_filename
        if self.driver:
            del self.driver
        if self.drivername:
            del self.drivername
        if self.positionWin:
            del self.positionWin
        if self.sizeWin:
            del self.sizeWin
        if self.zoomWin:
            del self.zoomWin
        if self.scrollWin:
            del self.scrollWin
        if self.browser:
            self.browser.dealloc()
            del self.browser

    def position(self, windowPosition):
        if not isinstance(windowPosition,tuple):
            logging.error("Invalid Window Position Format {}".format(windowPosition))
            return 1
        windowPosition = self.validatePosition(windowPosition)
        if windowPosition == 0:
            logging.error("Invalid Window Position Format {}".format(windowPosition))
            return 1
        self.positionWin = windowPosition
        self.driver.set_window_position(self.positionWin[0],self.positionWin[1])
        actualPosition = self.driver.get_window_position()
        self.positionWin = [actualPosition.get('x'),actualPosition.get('y')]
        logging.info("Window Position \t X: {} \t Y: {}".format(self.positionWin[0],self.positionWin[1]))
        return 0

    def size(self, windowSize):
        if not isinstance(windowSize,tuple):
            logging.error("Invalid Window Size Format {}".format(windowSize))
            return 1
        windowSize = self.validateSize(windowSize)
        if windowSize == 0:
            logging.error("Invalid Window Size Format {}".format(windowSize))
            return 1
        self.sizeWin = windowSize
        self.driver.set_window_size(self.sizeWin[0], self.sizeWin[1])
        actualSize = self.driver.get_window_size()
        self.sizeWin = [actualSize.get('width'),actualSize.get('height')]
        logging.info("Window Size \t\t W: {} \t H: {}".format(self.sizeWin[0],self.sizeWin[1]))
        return 0

    def zoom(self, percent):
        if not isinstance(percent,int):
            logging.error("Invalid Value format for Percent {}".format(percent))
            return 1
        if self.validateZoom(percent) == 0:
            logging.error("Zoom {} not in range (10-100)".format(percent))
            return 1
        self.zoomWin = percent
        self.driver.execute_script("document.body.style.zoom='{}%'".format(self.zoomWin))
        logging.info("Window Zoom: \t\t {}".format(self.zoomWin))
        return 0

    def zoomIn(self):
        if self.zoomWin + 10 > 100:
            logging.error("Can't Zoom In to {}%".format(self.zoomWin+10))
            return 1
        logging.info("Zooming In: {} -> {}".format(self.zoomWin,self.zoomWin+10))
        self.zoomWin = self.zoomWin + 10
        self.zoom(self.zoomWin)
        return 0

    def zoomOut(self):
        if self.zoomWin - 10 < 1:
            logging.error("Can't Zoom Out to {}%".format(self.zoomWin-10))
            return 1
        logging.info("Zooming Out: {} -> {}".format(self.zoomWin,self.zoomWin-10))
        self.zoomWin = self.zoomWin - 10
        self.zoom(self.zoomWin)
        return 0

    def scrollToElement(self, element):
        try:
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except NoSuchElementException:
            logging.error("NoSuchElementException: Couldn't find element")
            return 1
        location_dic = element.location
        if isinstance(location_dic,dict):
            x = location_dic.get('x')
            y = location_dic.get('y')
            self.scrollWin = (int(x),int(y))
            logging.info("Scrolling to point {}".format(element.location))
            time.sleep(1)
            return 0
        else:
            logging.error("Didn't scroll to Element")
            return 1

    def scrol(self,scrollWin):
        if not isinstance(scrollWin,tuple):
            logging.error("Invalid Scroll Format ({},{})".format(scrollWin[0],scrollWin[1]))
            return 1
        if self.validateScroll(scrollWin) == 0:
            logging.error("Can't scroll to ({},{})".format(scrollWin[0],scrollWin[1]))
            return 1
        else:
            self.scrollWin = scrollWin
            x = scrollWin[0]
            y = scrollWin[1]
            self.driver.execute_script("window.scrollTo({}, {})".format(x,y))
            logging.info("Window Scroll: \t\t {}".format(self.scrollWin))
        time.sleep(1)
        return 0

    def scrollDown(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (y + step) > scrollHeight:
            logging.warning("Scrolling Down: Can't Scroll to {}".format(y + step))
            return 1
        logging.info("Scrolling Down: {} -> {}".format(y,y+step))
        self.scrollWin = (x,y+step)
        self.scrol(self.scrollWin)
        time.sleep(0.5)
        return 0

    def scrollBottom(self,animate = 0):
        if animate:
            timeout = 5.0
            initial = 0
            pause = 0.2
            while not self.scrollDown():
                if animate:
                    time.sleep(pause)
                initial = initial + pause
                if initial > timeout:
                    break
        else:
            scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
            x = self.scrollWin[0]
            logging.info("Scrolling to bottom of the page at ({},{})".format(x,scrollHeight))
            self.scrollWin = (x,scrollHeight)
            self.scrol(self.scrollWin)
        return 0

    def scrollUp(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (y - step) < 0:
            logging.warning("Scrolling Up: Can't Scroll to {}".format(y - step))
            return 1
        logging.info("Scrolling Up: {} -> {}".format(y,y-step))
        self.scrollWin = (x,y-step)
        self.scrol(self.scrollWin)
        time.sleep(0.5)
        return 0

    def scrollTop(self,animate = 0):
        if animate:
            timeout = 5.0
            initial = 0
            pause = 0.2
            while not self.scrollUp():
                if animate:
                    time.sleep(pause)
                initial = initial + pause
                if initial > timeout:
                    break
        else:
            self.scrollWin = (0,0)
            self.scrol(self.scrollWin)
            logging.info("Scrolling to top of the page at {}".format(self.scrollWin))
        return 0

    def scrollRight(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (x + step) > scrollWidth:
            logging.warning("Scrolling Right: Can't Scroll to {}".format(x + step))
            return 1
        logging.info("Scrolling Right: {} -> {}".format(x,x+step))
        self.scrollWin = (x+step,y)
        self.scrol(self.scrollWin)
        time.sleep(0.3)
        return 0

    def scrollLeft(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (x - step) < 0:
            logging.warning("Scrolling Left: Can't Scroll to {}".format(x - step))
            return 1
        logging.info("Scrolling Left: {} -> {}".format(x,x-step))
        self.scrollWin = (x-step,y)
        self.scrol(self.scrollWin)
        time.sleep(0.3)
        return 0

    def validateSize(self, sizeWin):
        if not sizeWin and not len(sizeWin) == 2:
            logging.error("Invalid Size Format {}".format(sizeWin))
            return 0
        w = sizeWin[0]
        h = sizeWin[1]
        if (w < 400):
            logging.warning("Out of Range for Width: Passed {} Selected {}".format(w,400))
            w = 400
        elif (w > 2000):
            logging.warning("Out of Range for Width: Passed {} Selected {}".format(w,2000))
            w = 2000
        if (h < 272):
            logging.warning("Out of Range for Height: Passed {} Selected {}".format(h,272))
            h = 272
        elif (h > 1000):
            logging.warning("Out of Range for Height: Passed {} Selected {}".format(h,1000))
            h = 1000
        sizeWin = (w,h)
        logging.info("Window Sized to {}".format(sizeWin))
        return sizeWin

    def validateZoom(self, percent):
        if not isinstance(percent,int):
            logging.error("Invalid Zoom Format {}".format(percent))
            return 0
        if (percent < 10):
            logging.warning("Out of Range for Zoom: Passed {} Selected {}".format(percent,10))
            return 0
        elif (percent > 100):
            logging.warning("Out of Range for Zoom: Passed {} Selected {}".format(percent,100))
            return 0
        return 1

    def validateScroll(self, scrollWin):
        if not isinstance(scrollWin,tuple):
            logging.error("Invalid Scroll Format ({},{})".format(scrollWin[0],scrollWin[1]))
            return 0
        x = int(scrollWin[0])
        y = int(scrollWin[1])
        scrollHeight = 100
        scrollWidth = 100
        if self.driver:
            scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
            scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        if (x < 0):
            logging.warning("Out of Range for Scroll Width: Passed {} Selected {}".format(x,0))
            return 0
        if (x > scrollWidth):
            logging.warning("Out of Range for Scroll Width: Passed {} Selected {}".format(x,scrollWidth))
            return 0
        if (y < 0):
            logging.warning("Out of Range for Scroll Height: Passed {} Selected {}".format(y,0))
            return 0
        if (y > scrollHeight):
            logging.warning("Out of Range for Scroll Height: Passed {} Selected {}".format(y,scrollHeight))
            return 0
        scrollWin = (x,y)
        logging.info("Scrolling to {}".format(scrollWin))
        return scrollWin

    def validatePosition(self, positionWin):
        if not positionWin and not len(positionWin) == 2:
            logging.error("Invalid Position Format {}".format(positionWin))
            return 0
        x = positionWin[0]
        y = positionWin[1]
        if (x < 0):
            logging.warning("Out of Range for X Position: Passed {} Selected {}".format(x,0))
            x = 0
        elif (x > 2000):
            logging.warning("Out of Range for X Position: Passed {} Selected {}".format(x,2000))
            x = 2000
        if (y < 23):
            logging.warning("Out of Range for Y Position: Passed {} Selected {}".format(y,23))
            y = 23
        elif (y > 1000):
            logging.warning("Out of Range for Y Position: Passed {} Selected {}".format(y,1000))
            y = 1000
        positionWin = (x,y)
        logging.info("Window Position to {}".format(positionWin))
        return positionWin

