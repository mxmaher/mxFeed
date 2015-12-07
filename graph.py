#!/usr/bin/python

import copy 
import json
import requests
from urllib import urlencode

BASE_URL = 'https://graph.facebook.com'

class Graph(object):

    def __init__(self, access_token):
        '''a way to talk to the graph API, must provide
           an access_token first'''

        self.token = access_token

    def _get(self, id=None, url=None):
        '''make a GET request to the graph API, returns a json object'''
        
        params = {'access_token': self.token} #must be provided every time
        
        if url:
            res = requests.get(url, params=params).json()
        else:
            #do the request with a graph Node ID insted of a full URL
            res = requests.get('{0}/{1}'.format(BASE_URL, id),
                    params=params).json()

        self._check(res) #check the response for returned Errors
        return res

    def _check(self, data):
        '''Check for errors returned by the graph API'''
        if 'error' in data:
            raise Exception(data['error'].get('message'))

    def newsfeed(self):
        '''get the newsfeed for the current authenticated session'''

        Url = BASE_URL + '/me/home'
        feed = self._get(url=Url)
        return feed

    def get_group_feed(self, group):
        '''get the newsfeed of a group'''

        Url = BASE_URL + 'me/groups//{0}/'.format(group)
        res = self._get(url=Url)
        id = res['data'][0]['id']

        Url2 = BASE_URL + '{0}/feed'.format(id)
        return self._get(url=Url2)



