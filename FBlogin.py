#!/usr/bin/python

# it all needs reimplimenting
# it's a solution for just now

import utils

import BaseHTTPServer as httpserver
from urllib import urlencode
from urlparse import urlparse
import requests
import webbrowser as web
import simplejson as json

class httpServHandler(httpserver.BaseHTTPRequestHandler):
    #FIXME needs rethinking
    def do_GET(self):
        if not self.path.find('?') == -1:
            parsed_path = urlparse(self.path)
            try:
                params = dict([p.split('=') for p in parsed_path[4].split('&')])
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Success! You may close this tab.')
                global code
                code =  params['code']
                return 

            except:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('failed')
                return

class login(object):
    '''login with facebook graph API and retrive an access_token'''

    def __init__(self):
        
        self.appData = utils.loadjson('./app.json')
        self.appID = self.appData['appid']
        self.appSecret = self.appData['appsecret']

        self.redirURL = 'http://localhost:7777/'
        self.server = httpserver.HTTPServer(('localhost', 7777), httpServHandler)

    def getCode(self, permissions):
        '''retrive a graph CODE with the wanted permissions
           later used to get an acutall access_token for this permissions
        '''
        fields = urlencode({'client_id': self.appID, 
                'redirect_uri': self.redirURL, 'scope': permissions, 
                                             'response_type': 'code'})
        
        dialogURL = 'https://www.facebook.com/dialog/oauth?'
        web.open(dialogURL + fields) #TODO: open a headless browser
        self.server.handle_request()

    def getAccessToken(self):
        '''get the access_token using the early retrived CODE'''
        fields = urlencode({'client_id': self.appID,
                 'redirect_uri': self.redirURL,'client_secret': self.appSecret, 'code': str(code)})
        #(code) is a global variable defined in the httpServHandler class [in it's do_GET method]
        #TODO FIX this global variable thing

        codeURL = 'https://graph.facebook.com/v2.3/oauth/access_token?'
        req = requests.get(codeURL, params = fields)
        return req.json()

    def extendToken(self, token):
        '''extend token's life time'''
        pass

def get_token():
    #for using this module in directly from the terminal
    #I have my resonses for this
    l = login()
    l.getCode('read_stream')
    res = l.getAccessToken()
    token = res['access_token']
    l.appData['access_token'] = token
    utils.writejson(l.appData, './app.json')
    sys.exit()

if __name__ == '__main__':
    get_token()
