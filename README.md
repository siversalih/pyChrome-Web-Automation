# pyChrome


## Selenium
Selenium is a browser automation library. Most often used for testing web-applications, Selenium may be used for any task that requires automating interaction with the browser. The primary new feature in Selenium 2.0 is the integration of the WebDriver API.

## WebDriver
WebDriver is designed to provide a simpler, more concise programming interface in addition to addressing some limitations in the Selenium-RC API. Selenium-WebDriver was developed to better support dynamic web pages where elements of a page may change without the page itself being reloaded. WebDriver’s goal is to supply a well-designed object-oriented API that provides improved support for modern advanced web-app testing problems. 

For full documentation of using Selenium Webdriver APIs, see [Selenium with Python][df0]. 

**ChromeDriver** - Webdriver for Chromium. pyChrome uses ChromeDriver 	as a standalone server that implements WebDriver's wire protocol for Chrome browser. ChromeDriver is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS). 

More documentation on Chrome Webdriver can be found at [ChromeDriver][df2]

**PhantomJS** - Headless WebKit, pyChrome uses PhantomJS to process any web application in background (GhostDriver). Which means it does not require any browser or client (i.e Chrome) to display the Web Content. Therefore, it's a bit faster to process the information. PhantomJS is available for Mac, Linux, and Windows.

More documentation on PhantomJS Webdriver can be found at [PhantomJS][df6]


## pyChrome
![alt tag][DSNIMG]

pyChrome is a scripted Web Automation Platform using Selenium with Python. Currently, the supported WebDriver are ChromeDriver and PhantomJS. As the project progress, it may includes other Python libraries to control, scrap, analyze, and interact with the browser and its content. pyChrome can be imported to any Python project as a module for creating an application and use case scenarios such as bot, web automation, data mining, headless browsing, and testing web application. 

Currently, it's in development phase and is ongoing project. Be sure to check back for more updates.

## Milestones

API functions and structure that have been integrated:

- Basics
	- Open a page
	- Close a page
	- Quit the Session
- Window Control
	- Size
	- Position
- Zoom Functionality
	- Zoom (In,Out,Value)
- Scroll Functionality
	- Scroll (Down,Right,Up,Left,Value,Element inView)
- Headless Browser capabilities
	- Init/Start with GhostDriver Mode
	- Switch to GhostDriver Mode at Runtime
- Tab Control
	- Open New Tab
	- Close Tab	(current,index)
	- Switch Tab (left,right,index)
- Quick Access
	- Search using Google Search Engine
	- Facebook Login
- Logging Level
	- Level (info,warning,error,critical)
- Capture
	- Take Screenshot
	- Dump Web Page HTML code
	- Dump Web Element HTML code
	- Recorder (record,playback,store,load,delete,clear)
- Browser Navigation
	- Back
	- Forward
	- Refresh
- Web Element
	-	Locate Single Element (id,tag,name,class,text,link,css,xpath)
	-	Locate Multiple Elements (id,tag,name,class,text,link,css,xpath)
	- 	Locate Sub-Element (id,tag,name,class,text,link)
	- 	Locate Parent Element
	-	Locate SiblingsElements
	-	Locate Next Element
	-	Locate Previous Element
	-	Locate Body Element
	-	Locate Active Element
	-	Find Interactive Element (a,button,input,i,select,option)
	-	Find Option Element in Select
	-	Find Xpath of Element
	-	Get Element Value
	-	Get Element Value for Attribute
	-	Switch/Focus to Element
	-	Highlight Element
	-	Get Element Coordinates
- Interaction
	- Click Element
	- Send Text to Element
	- Select Option Element (in dropdown menu)
	- Double Click Element
	- Click & Hold Element
	- Release Element
	- Move Element by Offset
	- Move Cursor to Element
	- Drag & Drop Element
	- Send Keys to Element

## Objectives
1. Create a Web Automation Toolkit using Selenium WebDriver with Python
2. Leverage Selenium APIs, with Javascript, and other Python libraries to create an Automation Platform engine.
3. Ease of use APIs - Using Algorithms and Object-oriented programming techniques to design smarter and easier higher layer functions.
4. Headless Engine - Use PhantomJS to browse, automate, and test web unnoticeably.
5. Console Application - Run only via command-line so it can be imported to other Python projects with ease

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
	-	It's a Webdriver that Selenium Webdriver requires specifically for accessing Chrome client. pyChrome.py uses ChromeDriver APIs to access Chrome browser functionality such as opening a page, and finding a Web element on the page. This checkout is already bundled with ChromeDriver 2.23 for Mac OSX. Although, if you are on different OS, you will need to download the correct version for your OS from [Google Chrome Driver][df3] and overwrite it with the one included in this checkecout.

-	**bin/phantomjs**
	-	It's a Webdriver that Selenium Webdriver requires specifically for headless browsing. pyChrome.py uses PhantomJS as a Ghostdriver to browse, automate, and mine unnoticeably. This checkout is already bundled with PhantomJS 2.1.1 for Mac OSX. Although, if you are on different OS, you will need to download the correct version for your OS from [PhantomJS][r5] and overwrite it with the one included in this checkecout.

-	**config.json** (Recommended)
	- Contains all the configuration settings for how the server and the client should start. When pyChrome.py object gets created, it reads the configuration settings from config.json. If the file is not present, it creates a default settings. Users can also modify these settings via calling pyChrome.py APIs.

- 	demo/* (Optional)
	- Demo to run most of the implemented functions

-	test/test.py (Optional)
	- Test Suite to run all the implemented functions


## Usage
#####Initials
1.	Import pyChrome

    ```sh
    from pyChrome import PyChrome
    ```
2.	Start pyChrome
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
	point = (300,200)
	browser.position(point)
	```
-   Size

    ```sh
	siz = (1080,720)
	browser.size(siz)
	```
-   Zoom

    ```sh
	val = 60
	browser.zoom(val)
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
	browser.scrol(point)
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

-   Scroll To Top (with animation)

    ```sh
	browser.scrollTop(animated=True)
	```
	
-   Scroll To Bottom (with animation)

    ```sh
	browser.scrollBottom(animated=True)
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
-   Refresh

    ```sh
	browser.refresh()
	```

#####Capture
-	**Screenshot**

    ```sh
	name = "screenshot_capture"
	browser.screenshot(save_name=name)
	```
-	**Dump Source Code**

	- Web Page

    ```sh
	browser.open("http://www.google.com")
	filename = "pagesource"
	browser.sourceDump(filename=filename)
	```
	- Web Element

    ```sh
    url = "http://www.seleniumhq.org/projects/webdriver/"
    browser.open(url)
    locator = "Documentation"
    element = browser.findElementByPartialText(locator)
    filename = "elementsource"
    browser.elementDump(element,filename)
	```

-	**Recorder**

	- Record

	There are two ways of recording Web element, manually or programmatically. However, it's recorded with a single command and using same function. To record an element, the user must manually select an element on the client (Browser); to select an element with button or link tag, it can be selected with a right click; to select an element with input or div (textfield or radio button) tag, it can be selected with left click or entering text; to select an element with select (dropdown menu) tag, it can be selected when picking one of the options. The second method is programmatically locating Web Element and then sending the element to record. 

    ```sh
    url = "https://signup.live.com"
    browser.open(url)
    # Manually from the client (Browser), Click a Textfield and Enter a text, then run the command:
    browser.record()
    # Or Programmatically Locate a Web Element, then send the element to record it with the command:
    element = browser.findBodyElement()
    browser.record(element=element)
   
	```

	- Playback

	In order to playback the recorded element, atleast one element must be recorded.

    ```sh
   url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
    browser.open(url)
   # Manually from the Browser, click a Textfield and Enter a text, then run the command: 
	browser.record()
   # To playback, run the command:
   browser.playback()
	```

	- Store Recorder

	The Recorder stores the captured elements in JSON format with given filename at the root directory of the project. 

    ```sh
    url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
    browser.open(url)
    locator = "FirstName"
    element = browser.findElementByName(name_str=locator)
    browser.record(element=element)
    filename_recorder = "recorded_elements"
    browser.storeRecorder(filename_recorder)
	```

	- Load Recorder

	Before loading the Recorder, the client (Browser) must be opened on any page, and the specified file must be in the project root directory. Then the recorder can be loaded with a command as shown in below.
		
    ```sh
    url = "http://www.google.com"
    browser.open(url)
    filename_recorder = "recorded_elements"
    browser.loadRecorder(filename_recorder)
	```

	- Delete Last Recorded Element
	
	```sh
    browser.deleteRecord()
	```
	
	- Clear all the Recorded Elements
	
	```sh
    browser.clearRecorder()
	```

	- Get all the Recorded Elements
	
	```sh
    recorded_items = browser.getRecordedElements()
	```
	
#####Locate Web Element
The most challenging part of Web Automation is finding the Web Element locator (or xpath). And it's done manually by the Automator prior of locating it's Web Element. Once the Web Element location determined, the Web Element itself can be obtained by id, name, tag, class, partial text, link text, css selector and xpath. Depending of which attribute is available and the Automator approach, finding the Web element is easy as follows:

-	**Locating Web Element**
	
	-	Find Element by ID

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
	-   Find Element by Partial Text

    ```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "Documentation"
	element = browser.findElementByPartialText(locator)
	```
	-   Find Element by Link Text

    ```sh
	url = "http://www.yahoo.com"
	browser.open(url)
	locator = "Flickr"
	element = browser.findElementByLinkText(locator)
	```
	-   Find Element by Classname

    ```sh
    url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
    browser.open(url)
    locator = "input"
    element = browser.findElementByClass(locator)
	```
	-   Find Element by XPath

    ```sh
	url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "//*[@id='wp-submit']"
	element = browser.findElementByXPath(locator)
	```

	-   Find Element - Generic Function

    ```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "submit"
	element = browser.findElement(name=locator)
	```

	```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "submit"
	element = browser.findElement(element=None,id=None,name=locator,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None)
	```

-	**Locating Sub-Element**

	To locate sub-element, the parent element (Web Element object) must be obtained first. Then using the same function and its parent element, the sub-element can be located from its locator as shown in below.

	- Find Sub-Element

	```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "header"
	element = browser.findElementByID(locator)
	locator = "ul"
	sub_element = browser.findElementByTag(locator,element)
	```	

	-	Find Sub-Element using Generic Function

	```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "header"
	element = browser.findElement(id=locator)
	locator = "ul"
	sub_element = browser.findElement(element=element,tag=locator)
	```
	```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "header"
	element = browser.findElement(element=None,id=locator,name=None,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None)
	locator = "ul"
	sub_element = browser.findElement(element=element,id=None,name=None,classname=None,xpath=None,tag=locator,css=None,linktext=None,partialtext=None)
	```

-	**Locating Parent Web Element**

	```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "header"
	element = browser.findElementByID(locator)
	locator = "ul"
	sub_element = browser.findElementByTag(locator,element)
	parent_element = browser.findParentElement()
	```

-	**Locating Multiple Web Elements**

	-   Find Elements by ID

    ```sh
    url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
    browser.open(url)
	locator = "wp-submit"
    elements = browser.findElementsByID(locator)
	```
	
	-   Find Elements by Name

    ```sh
    url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
    browser.open(url)
	locator = "loginform"
    elements = browser.findElementsByName(locator)
	```
	
	-   Find Elements by Tag

    ```sh
	url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "p"
	elements = browser.findElementsByTag(locator)
	```
	-   Find Elements by Partial Text

    ```sh
	url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "WordPress"
	elements = browser.findElementsByPartialText(locator)
	```
	-   Find Elements by Link Text

    ```sh
	url = "http://www.yahoo.com"
	browser.open(url)
	locator = "Mail"
	elements = browser.findElementsByLinkText(locator)
	```
	-   Find Elements by Class

    ```sh
    url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "input"
	elements = browser.findElementsByClass(locator)
	```
	-   Find Elements by Xpath

    ```sh
    url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "//input[@class='input']"
	elements = browser.findElementsByXPath(locator)
	```

-	**Locating Body Web Element**

	```sh
    url = "https://www.yahoo.com/"
	browser.open(url)
	body_element = browser.findBodyElement()
	```

-	**Switch to Active Web Element**

	```sh
    url = "https://www.yahoo.com/"
	browser.open(url)
	browser.switchElement()
	active_element = browser.selectedElement
	```

-	**Switch to Web Element**

	```sh
    url = "https://www.yahoo.com/"
	browser.open(url)
	body_element = browser.findBodyElement()
	browser.switchElement(body_element)
	```

-	**Highlight Web Element**

	```sh
    url = "https://www.yahoo.com/"
	browser.open(url)
	body_element = browser.findBodyElement()
	browser.highlightElement()
	```

-	**Get Web Element Value**
	
	```sh
	url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
	browser.open(url)
	locator = "FirstName"
	browser.findElementByName(name_str=locator)
	value = browser.getElementValue()
	```

-	**Get Value for Attribute of a Web Element**
	
	```sh
	url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
	browser.open(url)
	locator = "FirstName"
	browser.findElementByName(name_str=locator)
	attribute = 'id'
	value = browser.getAttributeValue(attribute=attribute)
	```

-	**Find Xpath of a Web Element (Absolute Path)**

	```sh
	url = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
	browser.open(url)
	locator = "FirstName"
	browser.findElementByName(name_str=locator)
	xpath = browser.getXpath()
	```

-	**Find Sibling of a Web Elements**

	```sh
	url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
	browser.open(url)
	locator = "menu_support"
	browser.findElement(id=locator)
	sibling_elements = browser.findSiblingsElements()
	```

-	**Find Previous Element of Current Node**

	```sh
	url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
	browser.open(url)
	locator = "menu_download"
	element = browser.findElement(id=locator)
	element = browser.findPreviousElement(element)
	```

-	**Find Next Element of Current Node**

	```sh
	url = "http://www.seleniumhq.org/docs/03_webdriver.jsp"
	browser.open(url)
	locator = "menu_about"
	element = browser.findElement(id=locator)
	element = browser.findNextElement(element)
	```
-	**Find Interactive Element around Selected Element**

	```sh
	interactive_element = browser.findInteractiveElement(element=element)
	```
-	**Find Option Element in Select Element (Dropdown)**

	```sh
	link = "http://www.destinylfg.net/"
	browser.open(link)
	locator = "collapsed"
	element = browser.findElement(classname=locator)
	browser.clickElement(element)
	locator = "filters-platform-select"
	value = "ps4"
	select_element = browser.findElement(id=locator)
	option_element = browser.findOptionElement(value=value,select= select_element)	
	```
-	**Get Element Coordinates**

	```sh
	url = "https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	browser.open(url)
	locator = "user_login"
	element = browser.findElementByID(locator)
	element_coor = browser.getElementCoordinates(element)
	x = element_coor[0]
	y = element_coor[1]
	```

#####Interaction
-   Send Text to Element

    ```sh
	url = "https://www.google.com"
	browser.open(url)
	locator = "q"
	text = "Selenium Webdriver"
	element = browser.findElementByName(locator)
	browser.sendTextToElement(text,element)
	```

-   Send Text (Generic Function)

    ```sh
	url = "https://www.google.com"
	browser.open(url)
	text = "Selenium Webdriver"
	browser.sendText(text)
	```

-   Click on Element

    ```sh
	url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "menu_download"
	element = browser.findElementByID(locator)
	browser.clickElement(element)
	```

-   Click on Button (Generic Function)

    ```sh
   url = "https://www.google.com"
	browser.open(url)
	text = "Selenium Webdriver"
	browser.sendText(text)
	browser.findBodyElement()
	browser.clickButton()
	```

-   Click on Link (Generic Function)

    ```sh
   url = "http://www.seleniumhq.org/projects/webdriver/"
	browser.open(url)
	locator = "menu_documentation"
	browser.findElement(id=locator)
	browser.clickLink()
	```

-	Select Option Element in Dropdown Menu

	```sh
	link = "http://www.destinylfg.net/"
	browser.open(link)
	locator = "collapsed"
	element = browser.findElement(classname=locator)
	browser.clickElement(element)
	locator = "filters-platform-select"
	value = "ps4"
	select_element = browser.findElement(id=locator)
	option_element = browser.findOptionElement(value=value,select= select_element)	
	browser.selectElement(option_element)
	```

- Double Click Element

	```sh
	browser.doubleClickElement(element)
	```

- Release Element

	```sh
	browser.releaseElement(element)
	```

- Click and Hold Element

	```sh
	browser.holdElement(element)
	```

- Move Element by Offset

	```sh
	link = "https://marcojakob.github.io/dart-dnd/free-dragging/web/"
	locator = "draggable"
	browser.open(link)
	element = browser.findElement(classname=locator)
	browser.holdElement(element)
	offset = (100,200)
	browser.moveByOffset(offset)
	```

- Move to Element

	Move the mouse cursor to center of an element

	```sh
	link = "https://marcojakob.github.io/dart-dnd/custom-avatar/web/"
	browser.open(link)
	locator = "document"
	elements = browser.findElementsByClass(locator)
	element = elements[0]
	browser.moveToElement(element)
	```

- Drag & Drop Element

	```sh
	link = "http://demos.telerik.com/kendo-ui/dragdrop/index"
	locator = "draggable"
	browser.open(link)
	src_element = browser.findElement(id=locator)
	locator = "droptarget"
	dest_element = browser.findElement(id=locator)
	browser.dragAndDrop(src_element,dest_element)
	```

- Send Keys to Element

	This function sends a key or list of keys to an element. However, it requires using Keys class, and then specify which key to send.

	```sh
	import Keys
	key = Keys.TAB
	browser.sendKeysToElement(key,element)
	# or send list of keys
	keys = [Keys.TAB, Keys.CONTROL]
	browser.sendKeysToElement(keys,element)
	```

#####Tab Control
-	Open New Tab

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

-	Get Current Tab Link

    ```sh
	link = browser.getTabLink()
	```

-	Get Current Tab Title

    ```sh
	title = browser.getTabTitle()
	```

#####Headless Browsing
-   Init with GhostDriver

    ```sh
	browser = PyChrome(ghostmode=True)
	```
-   Switch to GhostDriver at Runtime

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

####[Test Results][TSTPDF]

**Mac**

-	[Python 2.7 or Python 3.5][tm1]
-	[chromedriver_mac64.zip][tm2]
- 	[phantomjs-2.1.1-macosx.zip][r5]
-	[Selenium 3.0.0.b2][tm3]

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
[TSTPDF]: <https://github.com/siversalih/pyChrome/blob/master/test/Test_Results.pdf