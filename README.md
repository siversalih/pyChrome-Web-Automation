# pyChrome


## Selenium
Selenium is a browser automation library. Most often used for testing web-applications, Selenium may be used for any task that requires automating interaction with the browser. The primary new feature in Selenium 2.0 is the integration of the WebDriver API.

## WebDriver
WebDriver is designed to provide a simpler, more concise programming interface in addition to addressing some limitations in the Selenium-RC API. Selenium-WebDriver was developed to better support dynamic web pages where elements of a page may change without the page itself being reloaded. WebDriver’s goal is to supply a well-designed object-oriented API that provides improved support for modern advanced web-app testing problems. 

For full documentation of using Selenium Webdriver APIs, see [Selenium with Python][df0]. 

**ChromeDriver** - A Webdriver for Chromium. pyChrome uses ChromeDriver 	as a standalone server that implements WebDriver's wire protocol for Chrome browser. ChromeDriver is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS). 

More documentation on Chrome Webdriver can be found at [ChromeDriver][df2]

**PhantomJS** - A Headless Webdriver, pyChrome uses PhantomJS  for automating web page interaction in background (Ghost mode). Similar to ChromeDriver, PhantomJS provides a JavaScript API enabling automated navigation, screenshots, user behavior and assertions making it a common tool. But because PhantomJS is a headless browser, it does not require any browser client (i.e Chrome). And that what makes it unique. PhantomJS is available for Mac, Linux, and Windows.

More documentation on PhantomJS Webdriver can be found at [PhantomJS][df6]



## pyChrome
![alt tag][DSNIMG]

pyChrome is a scripted Web Automation Platform engine. It uses Selenium Webdriver APIs from ChromeDriver, and PhantomJS. pyChrome also includes other Python modules, such as json, urllib2, numpy, scipy to control, analyze and interact with the browser where Selenium Webdriver APIs may not meet the demand or optimal solution. Also pyChrome is a console type application. Which it can be imported to any type of Python project as a module for creating bigger application and use case scenarios, such as for botting, web automation, data mining, and it has headless browsing capabilities.

## Milestones
However, there are still much more APIs need to be implemented for pyChrome to be a full Web Automation Platform.

API functions and structure that so far has been integrated;

- Opening and Closing a page (basics)
- Controlling the window (size, position)
- Browser Navigation Control (back, forward)
- Login to Facebook
- Search using Google Search Engine
- Scroll functionality
- Zoom functionality
- Take Screenshot
- Locate Web Element(s) (id,tag,name,class,text)
- Click on element
- Send keys to element
- Dump Web Page or Web Element HTML code
- Ghost Mode - Headless Browser capabilities
- Tab Control (open, close, switch)

API functions and structure need to be implemented but not limited to;

- Actions (macros, control keys)
- More Element search type (xpath)
- Image Processing functionality
- Logging Level

So pyChrome is still in development phase and is open for anyone to fork and pitch in with this project.

## Objectives
1. Create a fully functional WebDriver browser using Selenium Webdriver APIs.
2. Leverage Selenium Webdriver APIs (ChromeDriver and PhantomJS), and other Python libraries (i.e urllib2, scipy) to create an Automation Platform engine.
3. Ease of use APIs - Using Algorithms and Object-oriented programming techniques in Python to design smarter higher layer APIs.
4. Headless Engine - Use PhantomJS to browse, automate, and mine unnoticeably.

## Requirements

-	Python
	-	[Python 2.7 or Python 3.5][tm1]
-	Selenium
	-	[Selenium 3.0.0.b2][tm3]
	-	[Installation Guide][df1]
- Client
	-	[Chrome][r3]
- Server
	-	[Google Chrome Driver 2.23][r4]
	-	[PhantomJS 2.1.1][r5]

## Checkout pyChrome
```sh
$ git clone https://github.com/siversalih/pyChrome.git
```
###The Files
-	**pyChrome.py**
	-	It is the main class object. pyChrome.py extends and simplify the APIs beyond just Selenium Webdriver APIs. It inherits some functionality from Selenium Webdriver APIs, but it also uses other modules such as urllib2, scipy, numpy, json, and javascript for creating a true Automation Platform engine. 

-	**src/browser.py** 
	-	It is a subclass of pyChrome.py. It manages the client (Chrome or Ghostdriver) such as for opening and closing web page, navigating through pages, controlling tabs, finding Web element within the page, and interacting with the page.

-	**src/window.py**
	-	It is a subclass of pyChrome.py. It handles position, size, zooming and scrolling functionality of the window. It is required component when browsing using Chrome Driver. However, it does not have any effect when using PhantomJS driver (Ghostdriver).

-	**src/capture.py**
	-	It is a subclass of pyChrome.py. It handles capturing screen in PNG format, dumping Web page or Web element source code in HTML format.

-	**src/combo.py**
	-	It is a subclass of pyChrome.py. It contains set of functons for performing task that is used often, such as Login to Facebook, Opening Google Search Engine, Checking Email etc...

-	**src/navigation.py**
	-	It is a subclass of browser.py. It manages navigating through pages using back() and forward() command.

-	**src/tab.py**
	-	It is a subclass of browser.py. It manages controlling multiple tabs such as creating a new tab, closing existing tab, or switching to adjacent tab. It can also index to any open tab.

-	**src/interaction.py**
	-	It is a sublcass of browser.py. It manages interacting with the page Web Element. These are such as clicking on element, sending text to element, or sending action keys to element.

-	**src/element.py**
	-	It is a subclass of browser.py. It contains and manages searching and locating Web Element via its id, name, classname, tag, partial text, link text and xpath. It also has other functions that uses special algorithms to better locate element or list of elements. 

-	**bin/chromedriver**
	-	It's a Webdriver that Selenium Webdriver requires specifically for accessing Chrome client. pyChrome.py uses ChromeDriver APIs to access Chrome browser functionality such as opening a page, and finding a Web element on the page. This checkout is already bundled with ChromeDriver 2.23 for Mac OSX. Although, if you are on different OS, you will need to download the correct version for your OS from [Google Chrome Driver][df3] and overwrite it with the one included in this checkecout.

-	**bin/phantomjs**
	-	It's a Webdriver that Selenium Webdriver requires specifically for headless browsing. pyChrome.py uses PhantomJS as a Ghostdriver to browse, automate, and mine unnoticeably. This checkout is already bundled with PhantomJS 2.1.1 for Mac OSX. Although, if you are on different OS, you will need to download the correct version for your OS from [PhantomJS][r5] and overwrite it with the one included in this checkecout.

-	**config.json** (Recommended)
	- Contains all the configuration settings for how the server and the client should start. When pyChrome.py object gets created, it reads the configuration settings from config.json. If the file is not present, it creates a default settings. Users can also modify these settings via calling pyChrome.py APIs.

- 	demo/demo.py (Optional)
	- Demo to run all the implemented functions in pyChrome.py

-	test/test.py (Optional)
	- Test Suite to run all the implemented functions in pyChrome.py


## Usage
#####Initials
1.	Import pyChrome

    ```sh
    from pyChrome import PyChrome
    ```
2.	Create pyChrome
	- **Chrome Browser Driver**

		```sh
		browser = PyChrome()
		```
	- **Headless Browser Driver** (Ghost Mode)

		```sh
		browser = PyChrome(ghostmode=True)
		```
	- Read from configuration file

		```sh
		browser = PyChrome("config.json")
		```
	- Toggle Between Driver in Runtime
		
		```sh
		browser.switchDriverMode(ghostmode=True)
		```

#####Basics
-   Open a page

    ```sh
	    browser.open("http://www.google.com")
	```
-   Close the page

    ```sh
	    browser.close()
	```
-   Quit the session

    ```sh
	    browser.quit()
	```

#####Window Control
*Note: Headless browsing (ghost mode) will not have any affect on controlling the Window.*

-   Position

    ```sh
	    position = (300,200)
	    browser.positionWindow(position)
	```
-   Size

    ```sh
	    size = (1080,720)
	    browser.sizeWindow(size)
	```
-   Zoom

    ```sh
	    val = 60
	    browser.zoomWindow(val)
	```
-   Zoom Out

    ```sh
	    browser.zoomOut()
	```
-   Zoom In

    ```sh
	    browser.zoomIn()
	```
-   Scroll to Point

    ```sh
    	point = (50,400)
    	browser.scrollWindow(point)
	```
-   Scroll to Element

    ```sh
    	url = "http://www.ign.com"
    	locator = "Send Us News"
    	element = browser.findElementByPartialText(locator)
    	browser.scrollToElement(element)
	```
-   Scroll Down

    ```sh
	    browser.scrollDown()
	```
-   Scroll Up

    ```sh
	    browser.scrollUp()
	```
-   Scroll Left

    ```sh
	    browser.scrollLeft()
	```
-   Scroll Right

    ```sh
	    browser.scrollRight()
	```

#####Navigation Control
-   Back

    ```sh
	    browser.back()
	```
-   Forward

    ```sh
	    browser.forward()
	```

#####Capture
-   Screenshot

    ```sh
        name = "screenshot_capture"
        browser.screenshot(save_name=name)
	```
-   Dump Web Page HTML

    ```sh
        browser.open("http://www.google.com")
        filename = "pagesource"
        browser.sourceDump(filename=filename)
	```
-   Dump Web Element HTML

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
    	browser.open(url)
    	locator = "Documentation"
    	element = browser.findElementByPartialText(locator)
    	filename = "elementsource"
    	browser.elementDump(element,filename)
	```

#####Locate Web Element
-   Find Element by Partial Text

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
	    browser.open(url)
	    locator = "Documentation"
	    element = browser.findElementByPartialText(locator)
	```
-   Find Element by ID

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
	    browser.open(url)
	    locator = "menu_support"
	    element = browser.findElementByID(locator)
	```
-   Find Element by Name

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
	    browser.open(url)
	    locator = "submit"
	    element = browser.findElementByName(locator)
	```
-   Find Element by Tag

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
	    browser.open(url)
	    locator = "a"
	    element = browser.findElementByTag(locator)
	```
-   Find Elements by ID

    ```sh
	    url = "http://www.gamespot.com"
	    browser.open(url)
	    locator = "view-guid-meta"
	    elements = browser.findElementsByID(locator)
	```
-   Find Elements by Name

    ```sh
	    url = "http://www.gamespot.com"
	    browser.open(url)
	    locator = "application-name"
	    element = browser.findElementsByName(locator)
	```
-   Find Elements by Tag

    ```sh
	    url = "http://www.gamespot.com"
	    browser.open(url)
	    locator = "link"
	    element = browser.findElementsByTag(locator)
	```
-   Find Elements by Class

    ```sh
	    url = "http://www.gamespot.com"
	    browser.open(url)
	    locator = "img"
	    element = browser.findElementsByClass(locator)
	```

#####Interaction
-   Send Text to Element

    ```sh
	    url = "https://www.google.com"
	    locator = "q"
	    text = "Selenium Webdriver"
	    element = browser.findElementByName(locator)
	    browser.sendTextToElement(text,element)
	```
-   Click on Element

    ```sh
	    url = "http://www.seleniumhq.org/projects/webdriver/"
	    locator = "menu_download"
	    element = browser.findElementByID(locator)
	    browser.clickonElement(element)
	```

#####Tab Control
-	Open a New Tab

    ```sh
	    browser.newTab()
	```
-	Close Current Tab

    ```sh
	    browser.closeTab()
	```
-	Switch to Left Tab

    ```sh
	    browser.leftTab()
	```
-	Switch to Right Tab

    ```sh
	    browser.rightTab()
	```
-	Switch to Index Tab

    ```sh
    	index = 3
	    browser.switchTab(index)
	```
-	Close Tab at Index

    ```sh
    	index = 3
	    browser.closeTab(index)
	```

#####Headless Browsing
-   Init with Ghostdriver

    ```sh
	    browser = PyChrome(ghostmode=True)
	```
-   Switch to Ghostdriver at Runtime

    ```sh
	    browser.switchDriverMode(ghostmode=True)
	```

#####Combo
-   Search

    ```sh
	    text = "What is Selenium Chrome WebDriver"
	    browser.search(text)
	```
-   Facebook Login

    ```sh
	    username = "valid_username"
	    password = "valid_password"
	    browser.loginFacebook(username,password)
	```

## Test

```sh
python test.py
```
**Mac**

-	[Python 2.7 or Python 3.5][tm1]
-	[chromedriver_mac64.zip][tm2]
- 	[phantomjs-2.1.1-macosx.zip][r5]
-	[Selenium 3.0.0.b2][tm3]

[Results][TSTPDF]

**Windows**

-	Not Tested
-  Should run with the Windows version of ChromeDriver and PhantomJS

**Linux**

-	Not Tested
-  Should run with the Linux version of ChromeDriver and PhantomJS

##Resources

For full documentation of using Selenium Webdriver, see [Selenium Documentation][df4]. 

For full documentation of using Selenium with Python, see [Selenium with Python][df0]. 

For getting started with Chrome WebDriver, see [Chrome Web Driver][df5]

For getting started with PhantomJS, see [PhantomJS][df7]



[tm1]: <https://www.python.org/downloads/>
[tm2]: <http://chromedriver.storage.googleapis.com/index.html?path=2.23/>
[tm3]: <https://pypi.python.org/pypi/selenium>

[r1]: <https://www.python.org/downloads/>
[r2]: <http://www.seleniumhq.org/download/>
[r3]: <https://www.google.com/chrome/browser/desktop/>
[r4]: <http://chromedriver.storage.googleapis.com/index.html?path=2.23/>
[r5]: <http://phantomjs.org/download.html>

[df0]: <http://selenium-python.readthedocs.io/>
[df1]: <http://selenium-python.readthedocs.io/installation.html>
[df2]: <https://sites.google.com/a/chromium.org/chromedriver/home>
[df3]: <https://sites.google.com/a/chromium.org/chromedriver/downloads>
[df4]: <http://www.seleniumhq.org/docs/>
[df5]: <https://sites.google.com/a/chromium.org/chromedriver/getting-started>
[df6]: <http://phantomjs.org/documentation/>
[df7]: <http://phantomjs.org/quick-start.html>

[DSNIMG]: <https://github.com/siversalih/pyChrome/blob/master/design/Design_Chart.png>
[TSTPDF]: <https://github.com/siversalih/pyChrome/blob/master/test/Test_Results.pdf>