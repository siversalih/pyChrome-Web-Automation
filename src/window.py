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
    position = ()
    size = ()
    zoom = 0
    scroll = ()

    def __init__(self,driver, config = 0):
        self.driver = driver
        self.config_filename = "config.json"
        self.drivername = "chromedriver"
        self.position = (100,50)
        self.size = (720,480)
        self.zoom = 70
        self.scroll = (0,0)

        if config:
            self.config_filename = config
        with open(self.config_filename) as jsonFile:
            config = json.load(jsonFile)

        position = config.get('position')
        x = position[0]
        y = position[1]
        position = self.validatePosition(position)
        if position:
            self.position = position

        size = config.get('size')
        w = size[0]
        h = size[1]
        size = self.validateSize((w,h))
        if size:
            self.size = size

        zoom = config.get('zoom')
        if self.validateZoom(zoom):
            self.zoom = zoom

        scroll = config.get('scroll')
        if self.validateScroll(scroll):
            self.scroll = scroll

        self.sizeWindow(self.size)
        self.positionWindow(self.position)
        self.zoomWindow(self.zoom)
        self.scrollWindow(self.scroll)

    def dealloc(self):
        if self.config_filename:
            del self.config_filename
        if self.driver:
            del self.driver
        if self.drivername:
            del self.drivername
        if self.position:
            del self.position
        if self.size:
            del self.size
        if self.zoom:
            del self.zoom
        if self.scroll:
            del self.scroll

    def positionWindow(self, windowPosition):
        if not isinstance(windowPosition,tuple):
            print "Invalid Window Position Format {}".format(windowPosition)
            return 1
        windowPosition = self.validatePosition(windowPosition)
        if windowPosition == 0:
            print "Invalid Window Position Format {}".format(windowPosition)
            return 1
        self.position = windowPosition
        self.driver.set_window_position(self.position[0],self.position[1])
        actualPosition = self.driver.get_window_position()
        self.position = [actualPosition.get('x'),actualPosition.get('y')]
        print("Window Position \t X: {} \t Y: {}".format(self.position[0],self.position[1]))
        return 0

    def sizeWindow(self, windowSize):
        if not isinstance(windowSize,tuple):
            print "Invalid Window Size Format {}".format(windowSize)
            return 1
        windowSize = self.validateSize(windowSize)
        if windowSize == 0:
            print "Invalid Window Size Format {}".format(windowSize)
            return 1
        self.size = windowSize
        self.driver.set_window_size(self.size[0], self.size[1])
        actualSize = self.driver.get_window_size()
        self.size = [actualSize.get('width'),actualSize.get('height')]
        print("Window Size \t\t W: {} \t H: {}".format(self.size[0],self.size[1]))
        return 0

    def zoomWindow(self, percent):
        if not isinstance(percent,int):
            print "Invalid Value format for Percent {}".format(percent)
            return 1
        if self.validateZoom(percent) == 0:
            print "Zoom {} not in range (10-100)".format(percent)
            return 1
        self.zoom = percent
        self.driver.execute_script("document.body.style.zoom='{}%'".format(self.zoom))
        print "Window Zoom: \t\t {}".format(self.zoom)
        return 0

    def zoomIn(self):
        if self.zoom + 10 > 100:
            print "Can't Zoom In to {}%".format(self.zoom+10)
            return 1
        print "Zooming In: {} -> {}".format(self.zoom,self.zoom+10)
        self.zoom = self.zoom + 10
        self.zoomWindow(self.zoom)
        return 0

    def zoomOut(self):
        if self.zoom - 10 < 1:
            print "Can't Zoom Out to {}%".format(self.zoom-10)
            return 1
        print "Zooming Out: {} -> {}".format(self.zoom,self.zoom-10)
        self.zoom = self.zoom - 10
        self.zoomWindow(self.zoom)
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
            self.scroll = (int(x),int(y))
            print "Scrolling to point {}".format(element.location)
            time.sleep(1)
            return 0
        else:
            return 1

    def scrollWindow(self,scroll):
        if not isinstance(scroll,tuple):
            print "Invalid Scroll Format {}".format(scroll)
            return 1
        if self.validateScroll(scroll) == 0:
            print "Can't scroll to ({},{})".format(scroll[0],scroll[1])
            return 1
        else:
            self.scroll = scroll
            x = scroll[0]
            y = scroll[1]
            self.driver.execute_script("window.scrollTo({}, {})".format(x,y))
            print "Window Scroll: \t\t {}".format(self.scroll)
        return 0

    def scrollDown(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scroll[0]
        y = self.scroll[1]
        if (y + step) > scrollHeight:
            print "Can't Scroll Down to {}".format(y + step)
            return 1
        print "Scrolling Down: {} -> {}".format(y,y+step)
        self.scroll = (x,y+step)
        self.scrollWindow(self.scroll)
        return 0

    def scrollUp(self):
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        step = (scrollHeight / 10)
        x = self.scroll[0]
        y = self.scroll[1]
        if (y - step) < 0:
            print "Can't Scroll Up to {}".format(y - step)
            return 1
        print "Scrolling Up: {} -> {}".format(y,y-step)
        self.scroll = (x,y-step)
        self.scrollWindow(self.scroll)
        return 0

    def scrollRight(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scroll[0]
        y = self.scroll[1]
        if (x + step) > scrollWidth:
            print "Can't Scroll Right to {}".format(x + step)
            return 1
        print "Scrolling Right: {} -> {}".format(x,x+step)
        self.scroll = (x+step,y)
        self.scrollWindow(self.scroll)
        return 0

    def scrollLeft(self):
        scrollWidth = self.driver.execute_script("return document.body.scrollWidth")
        step = (scrollWidth / 10)
        x = self.scroll[0]
        y = self.scroll[1]
        if (x - step) < 0:
            print "Can't Scroll Left to {}".format(x - step)
            return 1
        print "Scrolling Left: {} -> {}".format(x,x-step)
        self.scroll = (x-step,y)
        self.scrollWindow(self.scroll)
        return 0

    def validateSize(self, size):
        if not size and not len(size) == 2:
            print ("Invalid Size Format {}".format(size))
            return 0
        w = size[0]
        h = size[1]
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
        size = (w,h)
        return size

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

    def validateScroll(self, scroll):
        if not isinstance(scroll,tuple):
            print "Invalid Scroll Format {}".format(scroll)
            return 0
        x = int(scroll[0])
        y = int(scroll[1])
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
        return 1

    def validatePosition(self, position):
        if not position and not len(position) == 2:
            print ("Invalid Position Format {}".format(position))
            return 0
        x = position[0]
        y = position[1]
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
        position = (x,y)
        return position

