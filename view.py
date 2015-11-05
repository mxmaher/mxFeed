#!/usr/bin/python

import utils

class Colors(object): 
    '''Colors definition for terminal printing'''
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    AQUA = '\033[96m'
    RED = '\033[91m'
    YELLOW = '\033[93m'

class FeedView(object):

    def __init__(self, feed):
        '''printing a minimal facebook feed in the terminal'''
        
        self.data = feed
        self.numOfPosts = len(self.data)
        self.tSize = utils.TerminalSize()
        self.colors = Colors()
    
    def to_lines(self, text, width=80, sur=2):
        '''breaks text into lines that fits the givin width'''
        #TODO needs more work
        text = text.split()
        string = ''
        lines = []

        for word in text:
            length = len(string) + len(word) + (sur * 2)
            if length < width:
                string += ' ' + word
            else:
                lines.append(string.strip())
                string = word
        lines.append(string.strip())

        return lines

    def print_link(self, link, indent=4):
        '''links can get very long so make them short 
        just for printing'''
        
        max_len = self.tSize[1] - 25
        nlink = ''
        for char in link:
            length = len(nlink) + 1
            if length < max_len:
                nlink += char
            else:
                break
        nlink += '...'
        ind = ' ' * indent
        utils.color_print(ind + nlink, self.colors.AQUA)

    def sanitize_post(self, index):
        '''sanitize the content of the post
        and return just the needed fields'''
        
        PostDict = self.data[index]
        name = PostDict['from']['name']
        post = {'name': name}

        if PostDict.has_key('type'):
            post['type'] = PostDict['type']
        else:
            post['type'] = ''

        if PostDict.has_key('message'):
            post['message'] = PostDict['message']
        else:
            post['message'] = ''

        if PostDict.has_key('link'):
            post['link'] = PostDict['link']
        else:
            post['link'] = ''

        if PostDict.has_key('description'):
            post['des'] = PostDict['description']
        else:
            post['des'] = ''

        return post

    def print_post(self, index):
        '''print a post by it's index in the feed'''

        #FIXME needs more work 
        post = self.sanitize_post(index)
        width = self.tSize[1] - 3

        utils.color_print('\n{0} '.format(index + 1) + post['name'] + '  [' + post['type'] + ']\n', self.colors.PURPLE) 

        if not post['message'] == '':
            message = self.to_lines(post['message'], width)
            for line in message:
                utils.color_print('    ' + line, self.colors.BLUE)
            print 

        if not post['link'] == '':
            self.print_link(post['link'], indent=4)
            print 

        if not post['des'] == '':
            desc = self.to_lines(post['des'], width)
            for line in desc:
                utils.color_print('  | ' + line, self.colors.GREEN)
            print
        #print '-' * (width + 3)

    def print_feed(self):
        '''print the full feed'''
        #TODO print the feed in reverse order insted
        for i in xrange(self.numOfPosts):
            self.print_post(i)

    def filter(self, name):
        '''return the indexs of posts that's from this name'''
        indexs = []
        for i in range(self.numOfPosts):
            post = self.sanitize_post(i)
            if post['name'].lower() == name.lower():
                indexs.append(i)

        return indexs

