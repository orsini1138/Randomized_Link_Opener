import time, random
import pyautogui as pgui
import webbrowser as web

# insert links to photos here as strings, ie 'https:\\image-location.com'
links = []

# make sure path is set to chrome, or change to preferred browser
browserPath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

while True:
    # shuffles list of links each time through to give a new order. remove this for static list
    random.shuffle(links)
    for i in range(len(links)):
        time.sleep(20) #change to 15
        web.get(browserPath).open(links[i])
        pgui.hotkey('ctrlleft', 'tab')
        pgui.hotkey('ctrlleft', 'w')