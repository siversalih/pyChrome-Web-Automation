import os
import sys
import random
from ast import literal_eval
import time
cur_dir = os.getcwd()
par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)
sys.path.insert(0, par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing from {}\nTry copy {} to pyChrome.py directory and run it from there.".format(os.getcwd(),os.path.basename(__file__))
    exit(1)

def NestedElement(node,root):
    print "Searching inside {}".format(node.get_attribute('id'))
    locator = "li"
    elements = browser.findElementsByTag(locator,element=node)

print "\n"
print "***** Welcome to pyChrome Demo *****"
print "\nThis demo shows how you can use pyChrome for Automating & Testing Drag & Drop functionality in Web Application\n" \

browser = PyChrome()
os.chdir(cur_dir)
sys.path.insert(0, cur_dir)

link = "https://marcojakob.github.io/dart-dnd/custom-avatar/web/"
select_link = 0

select_link = "1"
while select_link != '8':
    browser.size((820,800))
    print "\nSelect a Link\n" \
        "1. Basics \n" \
        "2. Intermediate\n" \
        "3. Folder Tree UI\n" \
        "4. Advanced Modern UI\n" \
        "5. Free Drag & Drop\n" \
        "6. Column Drag & Drop\n" \
        "7. Draggable Box\n" \
        "8. Exit the Demo\n"
    select_link = raw_input("Select a form to demo Autofill (1-8)\n > ")

    try:
        select_link = int(select_link)
    except ValueError:
        print "Value Error"
        continue
    if select_link < 1 or select_link > 8:
        continue
    else:
        if select_link == 1:
            link = "https://marcojakob.github.io/dart-dnd/custom-avatar/web/"
        elif select_link == 2:
            link = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
        elif select_link == 3:
            link = "http://www.dhtmlgoodies.com/scripts/drag-drop-folder-tree/drag-drop-folder-tree.html"
        elif select_link == 4:
            link = "http://tympanus.net/Development/DragDropInteractions/index.html"
        elif select_link == 5:
            link = "https://marcojakob.github.io/dart-dnd/free-dragging/web/"
        elif select_link == 6:
            link = "http://www.dhtmlgoodies.com/scripts/drag-drop-nodes/drag-drop-nodes-demo3.html"
        elif select_link == 7:
            link = "https://greensock.com/draggable"
        elif select_link == 8:
            browser.quit()
            exit(0)
        else:
            continue
    print "\nSelected Link: {}\n".format(link)
    if browser.getTabLink() != link:
        browser.open(link)
    else:
        browser.refresh()
    if select_link == 1:
        locator = "/html/body/div/div"
        dest_element = browser.findElement(xpath=locator)
        locator = "document"
        elements = browser.findElementsByClass(locator)
        for src_element in elements:
            browser.moveToElement(src_element)
            browser.holdElement(src_element)
            browser.moveToElement(dest_element)
            browser.releaseElement(dest_element)
    elif select_link == 2:
        for index in range(1,8):
            locator = "box{}".format(index)
            src_element = browser.findElement(id=locator)
            locator = "box10{}".format(index)
            dest_element = browser.findElement(id=locator)
            browser.dragAndDrop(src_element,dest_element)
    elif select_link == 3:
        locator = "tree_ul_0"
        root_element = browser.findElement(id=locator)
        locator = "li"
        elements = browser.findElementsByTag(locator,element=root_element)
        for element in elements:
            link_element = browser.findElement(tag='a',element=element)
            browser.holdElement(link_element)
            locator = "nodeATag0"
            dest_element = browser.findElement(id=locator)
            browser.moveToElement(dest_element)
            browser.releaseElement(dest_element)
    elif select_link == 4:
        locator = "grid__item"
        pick_elements = browser.findElementsByClass(locator)
        locator = "drop-area__item"
        drop_elements = browser.findElementsByClass(locator)
        for pick_element in pick_elements:
            random_drop = random.randint(0,3)
            drop_element = drop_elements[random_drop]
            browser.dragAndDrop(pick_element,drop_element)
    elif select_link == 5:
        locator = "draggable"
        element = browser.findElement(classname=locator)
        position = raw_input("Enter a offset to move the box by\n > ")
        position= literal_eval(position)
        x=position[0]
        y=position[1]
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Value Error"
            continue
        browser.holdElement(element)
        browser.moveByOffset(position)
        browser.releaseElement(element)
    elif select_link == 6:
        locator = "allItems"
        element = browser.findElement(id=locator)
        locator = "li"
        all_items = browser.findElementsByTag(locator)
        for element in all_items:
            random_drop = random.randint(1,5)
            locator = "box{}".format(random_drop)
            drop_element = browser.findElement(id=locator)
            browser.holdElement(element)
            browser.moveToElement(drop_element)
            browser.releaseElement(drop_element)
    elif select_link == 7:
        browser.size((1080,800))
        locator = "//*[@id='tossContainer']/div[31]"
        green_box = browser.findElementByXPath(locator)
        browser.scrollToElement(green_box)
        locator = "//*[@id='tossContainer']/div[32]"
        red_box = browser.findElementByXPath(locator)
        offset = (400,0)
        browser.switchElement(red_box)
        browser.holdElement(red_box)
        browser.moveByOffset(offset)
        time.sleep(0.2)
        browser.releaseElement(red_box)
        for i in range(0,2):
            if i % 2 == 0:
                down = 100
            else: down = -100
            for j in range(0,5):
                browser.switchElement(green_box)
                offset = (0,down)
                browser.holdElement(green_box)
                time.sleep(0.2)
                browser.moveByOffset(offset)
                time.sleep(0.2)
                browser.releaseElement(green_box)
                time.sleep(0.2)
                browser.switchElement(red_box)
                offset = (0,down)
                browser.holdElement(red_box)
                time.sleep(0.2)
                browser.moveByOffset(offset)
                time.sleep(0.2)
                browser.releaseElement(red_box)
                time.sleep(0.2)
            browser.switchElement(red_box)
            offset = (-196,0)
            browser.holdElement(red_box)
            time.sleep(0.2)
            browser.moveByOffset(offset)
            time.sleep(0.2)
            browser.releaseElement(red_box)
            time.sleep(0.2)
            browser.switchElement(green_box)
            offset = (196,0)
            browser.holdElement(green_box)
            time.sleep(0.2)
            browser.moveByOffset(offset)
            time.sleep(0.2)
            browser.releaseElement(green_box)
            time.sleep(0.2)











