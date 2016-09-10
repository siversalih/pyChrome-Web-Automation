import time
import json

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
    print "Selenium module is not installed...Exiting program."
    exit(1)

##### Window #######

class Window:
    config_filename = None
    driver = None
    drivername = ""
    positionWin = ()
    sizeWin = ()
    zoomWin = 0
    scrollWin = ()

    def __init__(self,driver, config = 0):
        self.driver = driver
        self.config_filename = "config.json"
        self.drivername = "chromedriver"
        self.positionWin = (100,50)
        self.sizeWin = (720,480)
        self.zoomWin = 70
        self.scrollWin = (0,0)

        if config:
            self.config_filename = config
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
        if self.validateScroll(scrollWin):
            self.scrollWin = scrollWin

        self.size(self.sizeWin)
        self.position(self.positionWin)
        self.zoom(self.zoomWin)
        self.scrol(self.scrollWin)

    def dealloc(self):
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

    def position(self, windowPosition):
        if not isinstance(windowPosition,tuple):
            print "Invalid Window Position Format {}".format(windowPosition)
            return 1
        windowPosition = self.validatePosition(windowPosition)
        if windowPosition == 0:
            print "Invalid Window Position Format {}".format(windowPosition)
            return 1
        self.positionWin = windowPosition
        self.driver.set_window_position(self.positionWin[0],self.positionWin[1])
        actualPosition = self.driver.get_window_position()
        self.positionWin = [actualPosition.get('x'),actualPosition.get('y')]
        print("Window Position \t X: {} \t Y: {}".format(self.positionWin[0],self.positionWin[1]))
        return 0

    def size(self, windowSize):
        if not isinstance(windowSize,tuple):
            print "Invalid Window Size Format {}".format(windowSize)
            return 1
        windowSize = self.validateSize(windowSize)
        if windowSize == 0:
            print "Invalid Window Size Format {}".format(windowSize)
            return 1
        self.sizeWin = windowSize
        self.driver.set_window_size(self.sizeWin[0], self.sizeWin[1])
        actualSize = self.driver.get_window_size()
        self.sizeWin = [actualSize.get('width'),actualSize.get('height')]
        print("Window Size \t\t W: {} \t H: {}".format(self.sizeWin[0],self.sizeWin[1]))
        return 0

    def zoom(self, percent):
        if not isinstance(percent,int):
            print "Invalid Value format for Percent {}".format(percent)
            return 1
        if self.validateZoom(percent) == 0:
            print "Zoom {} not in range (10-100)".format(percent)
            return 1
        self.zoomWin = percent
        self.driver.execute_script("document.body.style.zoom='{}%'".format(self.zoom))
        print "Window Zoom: \t\t {}".format(self.zoom)
        return 0

    def zoomIn(self):
        if self.zoomWin + 10 > 100:
            print "Can't Zoom In to {}%".format(self.zoomWin+10)
            return 1
        print "Zooming In: {} -> {}".format(self.zoomWin,self.zoomWin+10)
        self.zoomWin = self.zoomWin + 10
        self.zoom(self.zoomWin)
        return 0

    def zoomOut(self):
        if self.zoomWin - 10 < 1:
            print "Can't Zoom Out to {}%".format(self.zoomWin-10)
            return 1
        print "Zooming Out: {} -> {}".format(self.zoomWin,self.zoomWin-10)
        self.zoomWin = self.zoomWin - 10
        self.zoom(self.zoomWin)
        return 0

    def scrollToElement(self, element):
        try:
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find"
            return 1
        location_dic = element.location
        if isinstance(location_dic,dict):
            x = location_dic.get('x')
            y = location_dic.get('y')
            self.scrollWin = (int(x),int(y))
            print "Scrolling to point {}".format(element.location)
            time.sleep(1)
            return 0
        else:
            return 1

    def scrol(self,scrollWin):
        if not isinstance(scrollWin,tuple):
            print "Invalid Scroll Format {}".format(scrollWin)
            return 1
        if self.validateScroll(scrollWin) == 0:
            print "Can't scroll to ({},{})".format(scrollWin[0],scrollWin[1])
            return 1
        else:
            self.scrollWin = scrollWin
            x = scrollWin[0]
            y = scrollWin[1]
            self.driver.execute_script("window.scrollTo({}, {})".format(x,y))
            print "Window Scroll: \t\t {}".format(self.scrollWin)
        return 0

    def scrollDown(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (y + step) > scrollHeight:
            print "Can't Scroll Down to {}".format(y + step)
            return 1
        print "Scrolling Down: {} -> {}".format(y,y+step)
        self.scrollWin = (x,y+step)
        self.scrol(self.scrollWin)

        return 0

    def scrollUp(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (y - step) < 0:
            print "Can't Scroll Up to {}".format(y - step)
            return 1
        print "Scrolling Up: {} -> {}".format(y,y-step)
        self.scrollWin = (x,y-step)
        self.scrol(self.scrollWin)
        return 0

    def scrollRight(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (x + step) > scrollWidth:
            print "Can't Scroll Right to {}".format(x + step)
            return 1
        print "Scrolling Right: {} -> {}".format(x,x+step)
        self.scrollWin = (x+step,y)
        self.scrol(self.scrollWin)
        return 0

    def scrollLeft(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scrollWin[0]
        y = self.scrollWin[1]
        if (x - step) < 0:
            print "Can't Scroll Left to {}".format(x - step)
            return 1
        print "Scrolling Left: {} -> {}".format(x,x-step)
        self.scrollWin = (x-step,y)
        self.scrol(self.scrollWin)
        return 0

    def validateSize(self, sizeWin):
        if not sizeWin and not len(sizeWin) == 2:
            print ("Invalid Size Format {}".format(sizeWin))
            return 0
        w = sizeWin[0]
        h = sizeWin[1]
        if (w < 400):
            print "Min: {} Passed: {}".format(400,w)
            w = 400
        elif (w > 2000):
            print "Max: {} Passed: {}".format(2000,w)
            w = 2000
        if (h < 272):
            print "Min: {} Passed: {}".format(272,h)
            h = 272
        elif (h > 1000):
            print "Max: {} Passed: {}".format(1000,h)
            h = 1000
        sizeWin = (w,h)
        return sizeWin

    def validateZoom(self, percent):
        if not isinstance(percent,int):
            print "Invalid Zoom Format {}".format(percent)
            return 0
        if (percent < 10):
            print "Min: {} Passed: {}".format(10,percent)
            return 0
        elif (percent > 100):
            print "Max: {} Passed: {}".format(100,percent)
            return 0
        return 1

    def validateScroll(self, scrollWin):
        if not isinstance(scrollWin,tuple):
            print "Invalid Scroll Format {}".format(scrollWin)
            return 0
        x = int(scrollWin[0])
        y = int(scrollWin[1])
        scrollHeight = 100
        scrollWidth = 100
        if self.driver:
            scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
            scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        if (x < 0):
            print "X Min: {} Passed: {}".format(0,x)
            return 0
        if (x > scrollWidth):
            print "X Max: {} Passed: {}".format(scrollWidth,x)
            return 0
        if (y < 0):
            print "Y Min: {} Passed: {}".format(0,y)
            return 0
        if (y > scrollHeight):
            print "Y Max: {} Passed: {}".format(scrollHeight,y)
            return 0
        scrollWin = (x,y)
        return scrollWin

    def validatePosition(self, positionWin):
        if not positionWin and not len(positionWin) == 2:
            print ("Invalid Position Format {}".format(positionWin))
            return 0
        x = positionWin[0]
        y = positionWin[1]
        if (x < 0):
            print "Min: {} Passed: {}".format(0,x)
            x = 0
        elif (x > 2000):
            print "Max: {} Passed: {}".format(2000,x)
            x = 2000
        if (y < 23):
            print "Min: {} Passed: {}".format(23,y)
            y = 23
        elif (y > 1000):
            print "Max: {} Passed: {}".format(1000,y)
            y = 1000
        positionWin = (x,y)
        return positionWin

