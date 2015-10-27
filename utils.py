#!/usr/bin/python


import simplejson as json
import webbrowser as web
import os

'''simple utils used by the other modules'''

def loadjson(filename):
    '''load a json file and return a python dict'''
    with open(filename, 'r') as f:
        return json.load(f)

def writejson(jstring, filename):
    '''write json to a file'''
    with open(filename, 'w') as f:
        json.dump(jstring, f, indent=4)

def TerminalSize():
    '''get the terminal size in rows and columns'''
    try:
        hight, width = os.popen('stty size', 'r').read().split()
        return int(hight), int(width)
    except Exception:
        print "can't get terminal size, default used"
        return 80, 80

def color_print(text, color):
    '''print colored text in the terminal'''
    print color, text, '\033[0m'

def open_link(link):
    '''open a link in the browser'''
    web.open(link)

