# PyChrome


PyChrome is a Web Automation module to create Web Automation application using Selenium with Python. It is integrated with WebDriver using ChromeDriver to access and control Chromium browser. It can also emulate headless browser using PhantomJS (Ghost Driver) to browse unnoticeable. PyChrome is open-source and it is written in Python 2. It’s run via command-line rather than as GUI editor application. Thus, it is more flexible to be modified at user's discretion, and it can be easily imported as a module to any project for creating Web Automation application in Python programming language. The application of using PyChrome (Selenium Python) is tremendous for Web applications. It can be used for Web automation, creating Web bots, data mining, scraping the web, browse unnoticeably using Headless browser, and testing web application.



Currently, the project is in development phase. Be sure to check the website  at [pychrome.wordpress.com][website] for the latest update.


To setup Selenium Python environment, check installation tutorial for [macOS][macos] or [Windows][windows].

For tutorial on how to use PyChrome module in your project, see these [videos][videos].



## Checkout PyChrome
```sh
$ git clone https://github.com/siversalih/pyChrome.git
```
### The Files
![alt tag][DSNIMG]

-	**pyChrome.py**
	-	It is the main class object. pyChrome.py extends and simplify the APIs beyond just Selenium Webdriver APIs. It inherits most functionality from Selenium Webdriver APIs, but it also uses other modules such as urllib2, scipy, numpy, json, and javascript for creating a Web Automation Platform. 

-	**src/browser.py** 
	-	It is a subclass of pyChrome.py. It manages the client (Chrome or Ghostdriver) such as for opening and closing web page, navigating through pages, controlling tabs, finding Web element within the page, and interacting with the page.

-	**src/window.py**
	-	It is a subclass of pyChrome.py. It handles position, size, zooming and scrolling functionality of the window. It is required component when browsing using Chrome Driver. However, it does not have any effect when using PhantomJS driver.

-	**src/capture.py**
	-	It is a subclass of Browser. It handles screen capturing in PNG format, dumping Web page or Web element source code in HTML format. It also handle record functionality. It can manually or programmatically record selected element to playback in sequence. It has other functions including for storing and loading captured elements to and from JSON file.

-	**src/combo.py**
	-	It is a subclass of pyChrome.py. It contains set of functons for performing quick task (quick acess) that is used oftenly, such as Login to Facebook, Opening Google Search Engine, Checking Email etc...

-	**src/navigation.py**
	-	It is a subclass of browser.py. It manages navigating through pages using back() and forward() command.

-	**src/tab.py**
	-	It is a subclass of browser.py. It manages controlling multiple tabs such as creating a new tab, closing existing tab, or switching to adjacent tab. It can also index to tab.

-	**src/interaction.py**
	-	It is a sublcass of browser.py. It manages interacting with the page Web Element. These are such as clicking on element, sending text to element, or sending action keys to element.

-	**src/element.py**
	-	Currently, it is a subclass of pyChrome.py. It contains and manages searching and locating Web Element by id, name, classname, tag, partial text, link text, css selector, and xpath. It has also other functions that uses special algorithms to better traverse through elements and manipulate  element. 

-	**bin/chromedriver**
	-	It's a Webdriver that Selenium Webdriver requires specifically for accessing Chrome client. pyChrome.py uses ChromeDriver APIs to access Chrome browser functionality such as opening a page, and finding a Web element on the page. This checkout includes ChromeDriver 2.29 for macOS.

-	**bin/phantomjs**
	-	It's a Webdriver that Selenium Webdriver requires specifically for headless browsing. pyChrome.py uses PhantomJS as a Ghostdriver to browse, automate, and mine unnoticeably. This checkout includes PhantomJS 2.1.1 for macOS. 

-	**bin/chromedriver.exe**
	-	It's a Webdriver that Selenium Webdriver requires specifically for accessing Chrome client. pyChrome.py uses ChromeDriver APIs to access Chrome browser functionality such as opening a page, and finding a Web element on the page. This checkout includes ChromeDriver 2.29 for Windows.

-	**bin/phantomjs.exe**
	-	It's a Webdriver that Selenium Webdriver requires specifically for headless browsing. pyChrome.py uses PhantomJS as a Ghostdriver to browse, automate, and mine unnoticeably. This checkout includes PhantomJS 2.1.1 for Windows. 

-	**config.json** (Recommended)
	- Contains all the configuration settings for how the server and the client should start. When pyChrome.py object gets created, it reads the configuration settings from config.json. If the file is not present, it creates a default settings. Users can also modify these settings via calling pyChrome.py APIs.

- 	demo/* (Optional)
	- Demo to run most of the implemented functions

-	test/test.py (Optional)
	- Test Suite to run all the implemented functions


## Documentation

For documentation on Selenium, see [Selenium Documentation][res1] webpage. 

For documentation on using Selenium with Python, check [Selenium Python][res2] website. 

For getting started with using WebDriver for Chrome, see [Chrome WebDriver][res3] document.

For getting started with using GhostDriver, see [PhantomJS][res4] document.

For documentation on how PyChrome works, see [PyChrome][PyChrome] webpage.

[web1]: <https://selenium-python.readthedocs.io/>
[web2]: <https://sites.google.com/a/chromium.org/chromedriver/home/>
[web3]: <http://phantomjs.org/quick-start.html/>

[req1]: <https://www.python.org/downloads/>
[req2]: <https://pypi.python.org/pypi/selenium/>
[req3]: <https://selenium-python.readthedocs.io/installation.html>
[req4]: <https://www.google.com/chrome/browser/desktop/>
[req5]: <https://chromedriver.storage.googleapis.com/index.html?path=2.9/>
[req6]: <http://phantomjs.org/download.html/>

[test1]: <https://github.com/siversalih/pyChrome/blob/master/test/Test_Results_win32.pdf/>
[test2]: <https://github.com/siversalih/pyChrome/blob/master/test/Test_Results_macOS.pdf/>


[totest1]: <https://www.python.org/downloads/>
[totest2]: <https://chromedriver.storage.googleapis.com/index.html?path=2.9/>
[totest3]: <http://phantomjs.org/download.html/>
[totest4]: <https://pypi.python.org/pypi/selenium#downloads/>
[totest5]: <https://www.python.org/downloads/>
[totest6]: <https://chromedriver.storage.googleapis.com/index.html?path=2.9/>
[totest7]: <http://phantomjs.org/download.html/>
[totest8]: <https://pypi.python.org/pypi/selenium#downloads/>

[res1]: <http://www.seleniumhq.org/docs/>
[res2]: <https://selenium-python.readthedocs.io/>
[res3]: <https://sites.google.com/a/chromium.org/chromedriver/getting-started/>
[res4]: <http://phantomjs.org/quick-start.html>

[DSNIMG]: <https://github.com/siversalih/pyChrome/blob/master/design/Design_Chart.png/>

[website]: <https://pychrome.wordpress.com/>
[videos]: <https://www.youtube.com/playlist?list=PL8R5Fi8yjw7mNAgRZpQWxJ_ndcL4Tcn0C>
[macos]: <https://youtu.be/kizSRWlnPvE/>
[windows]: <https://youtu.be/3rguo2u3NqM/>
[pychrome]: <https://pychrome.wordpress.com/about/>

