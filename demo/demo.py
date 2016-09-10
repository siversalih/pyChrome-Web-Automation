from ast import literal_eval
import os
import sys

par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing...Exiting program."
    exit(1)

def main(argv):

    filename = ""
    if(argv):
        filename = argv[0]
    else:
        filename = 'config.json'
    directory = os.getcwd()
    file_directory = "{}/{}".format(directory,filename)
    if(not os.path.exists(file_directory)):
        print("{} is not in {}".format(filename,directory))
        exit(1)

    browser = PyChrome(filename)
    char = ''
    while not char is 'q':
        print   "\nPress \n" \
                "O to Open a Page\n" \
                "G to Search\n" \
                "B to Back to Previous Page\n" \
                "E to Open Element Menu\n" \
                "F to Forward to Next Page\n" \
                "C to Open Capture Menu\n" \
                "FB to Login into Facebook\n" \
                "S to Change Size\n" \
                "P to Change Position\n" \
                "I to Open Interaction Menu\n" \
                "T to Open Tab Menu\n" \
                "Z to Change Zoom\n" \
                "- to Zoom Out\n" \
                "+ to Zoom In\n" \
                "R to Open Scroll Menu\n" \
                'M to Switch between Chrome and Ghost Driver\n' \
                "Q to Quit"
        char = raw_input('>> ')
        char.lower()
        if char == 'o':
            url = raw_input('Enter URL\n>> ')
            url.lower()
            browser.open(url)
        if char == 'g':
            browser.open("http://www.google.com")
            search = raw_input('Search on Google (what is selenium webdriver)\n>> ')
            if search == 0 or len(search) == 0:
                print "Search is Empty {}".format(search)
            else:
                browser.search(search)
        elif char == 'b':
            browser.back()
        elif char == 'e':
            while not char is 'q':
                print "\nPress \n" \
                    "I to Find element by ID\n" \
                    "N to Find element by Name\n" \
                    "T to Find element by Tag\n" \
                    "X to Find element by Partial Text\n" \
                    "Q to Return to Previous Menu"
                char = raw_input('>> ')
                char.lower()
                if char == 'i':
                    char = raw_input('Enter the element''s ID\n>> ')
                    if char == "" or len(char) == 0:
                        continue
                    element = browser.findElementByID(char)
                    if element == 0:
                        print "Couldn't find any element with ID '{}'".format(char)
                        continue
                    else: char = 'r'
                elif char == 'n':
                    char = raw_input('Enter the element''s Name\n>> ')
                    if char == "" or len(char) == 0:
                        continue
                    element = browser.findElementByName(char)
                    if element == 0:
                        print "Couldn't find any element with Name '{}'".format(char)
                        continue
                    else: char = 'r'
                elif char == 't':
                    char = raw_input('Enter the element''s Tag\n>> ')
                    if char == "" or len(char) == 0:
                        continue
                    element = browser.findElementByTag(char)
                    if element == 0:
                        print "Couldn't find any element with Tag '{}'".format(char)
                        continue
                    else: char = 'r'
                elif char == 'x':
                    char = raw_input('Enter the element''s Partial Text\n>> ')
                    if char == "" or len(char) == 0:
                        continue
                    element = browser.findElementByPartialText(char)
                    if element == 0:
                        print "Couldn't find any element with Partial Text '{}'".format(char)
                        continue
                    else: char = 'q'
                elif char == 'q':
                    break
        elif char == 'f':
            browser.forward()
        elif char == 'c':
            while not char is 'q':
                print "\nPress \n" \
                    "S to Take Screenshot\n" \
                    "P to Dump Web Page HTML source\n" \
                    "E to Dump Selected Element HTML source\n" \
                    "Q to Return to Previous Menu"
                char = raw_input('>> ')
                char.lower()
                if char == 's':
                    save_name = ""
                    save_name = raw_input('Enter the filename (default leave blank)\n>> ')
                    if save_name == 0 or len(save_name) == 0:
                        save_name = 0
                    browser.screenshot(save_name=save_name)
                elif char == 'p':
                    save_name = raw_input('Enter the filename or leave blank for default\n>> ')
                    if save_name is "" or len(save_name) == 0:
                        save_name = 0
                    browser.sourceDump(filename=save_name)
                elif char == 'e':
                    save_name = raw_input('Enter the filename or leave blank for default\n>> ')
                    if save_name is "" or len(save_name) == 0:
                        save_name = 0
                    browser.elementDump(0,save_name)
                elif char == 'q':
                    break
        elif char == 'fb':
            username = raw_input('Enter Username\n>> ')
            username.lower()
            if not username and len(username) == 0:
                print "Username is empty ({})".format(username)
                continue
            password = raw_input('Enter Password\n>> ')
            password.lower()
            if not password and len(password) == 0:
                print "Password is empty ({})".format(password)
                continue
            browser.loginFacebook(username,password)
        elif char == 's':
            size = ()
            size = raw_input('Enter Window Size (w, h)\n>> ')
            if not '(' in size or not ')' in size or not ',' in size:
                print "Invalid Size Format {}".format(size)
                continue
            try:
                size = literal_eval(size)
                if browser.sizeWindow(size):
                    print "Failed to Resize Window with {}".format(size)
            except ValueError:
                print "Value Error: malformed string {}".format(size)
        elif char == 'p':
            position = ()
            position = raw_input('Enter Window Position (x, y)\n>> ')
            if not '(' in position or not ')' in position or not ',' in position:
                print "Invalid Position Format {}".format(position)
                continue
            try:
                position = literal_eval(position)
                if browser.positionWindow(position):
                    print "Failed to Position Window with {}".format(position)
            except ValueError:
                print "Value Error: malformed string {}".format(position)
        elif char == 'i':
            while not char is 'q':
                print "\nPress \n" \
                    "C to Click on Selected Element\n" \
                    "T to Send Text to Selected Element\n" \
                    "Q to Return to Previous Menu"
                char = raw_input('>> ')
                char.lower()
                if char == 'c':
                    if browser.selectedElement == None or not isinstance(browser.selectedElement, WebElement):
                        print "No Web element been selected"
                        continue
                    if browser.clickonElement():
                        print "Failed to click or Couldn't find ID {}"
                elif char == 't':
                    if browser.selectedElement == None or not isinstance(browser.selectedElement, WebElement):
                        print "No Web element been selected"
                        continue
                    text = raw_input('Enter your text to send\n>> ')
                    if text == 0 or len(text) == 0:
                        print "Text is empty {}".format(text)
                        continue
                    if browser.sendTextToElement(text):
                        print "Failed to send '{}'".format(text)
                elif char == 'q':
                    break
        elif char == 'z':
            zoom = ""
            zoom = raw_input('Enter Zoom (1-100)\n>> ')
            try:
                zoom = int(zoom)
                browser.zoomWindow(zoom)
            except ValueError:
                print "Value Error: {} Invalid entry for integer. \nInput numerical value from 1 to 100".format(zoom)

        elif char == '+':
            browser.zoomIn()

        elif char == '-':
            browser.zoomOut()

        elif char == 'r':
            while not char is 'q':
                print   "\nPress \n" \
                    "S to Scroll to a Point\n" \
                    "E to Scroll to Selected Element\n" \
                    "U to Scroll Up\n" \
                    "D to Scroll Down\n" \
                    "L to Scroll Left \n" \
                    "R to Scroll Right \n" \
                    "Q to Return to Previous Menu"
                char = raw_input('>> ')
                char.lower()
                if char == 's':
                    x = raw_input('Enter scroll point in X direction (int)\n>> ')
                    try:
                        scroll = int(x)
                    except ValueError:
                        print "Value Error: {} Invalid entry for integer. \nInput numerical value".format(x)
                        continue
                    y = raw_input('Enter scroll point in Y direction (int)\n>> ')
                    try:
                        y = int(y)
                    except ValueError:
                        print "Value Error: {} Invalid entry for integer. \nInput numerical value".format(y)
                        continue
                    browser.scrollWindow((x,y))
                if char == 'e':
                    if browser.selectedElement == 0 or not isinstance(browser.selectedElement,WebElement):
                        print "No Element selected to scroll"
                    else:
                        browser.scrollToElement()
                if char == 'u':
                    if browser.driver and len(browser.driver.current_url):
                        browser.scrollUp()
                    else:
                        print "No Page is shown to scroll up"
                if char == 'd':
                    if browser.driver and len(browser.driver.current_url):
                        browser.scrollDown()
                    else:
                        print "No Page is shown to scroll down"
                if char == 'l':
                    if browser.driver and len(browser.driver.current_url):
                        browser.scrollLeft()
                    else:
                        print "No Page is shown to scroll left"
                if char == 'r':
                    if browser.driver and len(browser.driver.current_url):
                        browser.scrollRight()
                    else:
                        print "No Page is shown to scroll right"
                if char == 'q':
                    break

        elif char == 't':
            while not char is 'q':
                print   "\nPress \n" \
                    "N to Open New Tab\n" \
                    "C to Close Current Tab\n" \
                    "R to Switch to Right Tab\n" \
                    "L to Switch to Left Tab\n" \
                    "I to Switch to Tab at Index\n" \
                    "X to Close Tab at Index\n" \
                    "Q to Return to Previous Menu"
                char = raw_input('>> ')
                char.lower()
                if char == 'n':
                    browser.newTab(url="http://www.google.com")
                if char == 'c':
                    browser.closeTab()
                if char == 'r':
                    browser.rightTab()
                if char == 'l':
                    browser.leftTab()
                if char == 'i':
                    index = raw_input('Enter Tab Index\n>> ')
                    try:
                        index = int(index)
                    except ValueError:
                        print "Invalid Format for integer"
                    if (index > 9) or (index < 1):
                        print "Tab index range is 1 to 9 - Passed: {}".format(index)
                        continue
                    browser.switchTab(index)
                if char == 'x':
                    index = raw_input('Enter Tab Index\n>> ')
                    try:
                        index = int(index)
                    except ValueError:
                        print "Invalid Format for integer"
                    if (index > 9) or (index < 1):
                        print "Tab index range is 1 to 9 - Passed: {}".format(index)
                        continue
                    browser.closeTab(index)
                if char == 'q':
                    break

        elif char == 'm':
            browser.switchDriverMode()

        elif char in 'q':
            browser.quit()
            break

if __name__ == "__main__":
   main(sys.argv[1:])

