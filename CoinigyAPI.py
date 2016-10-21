# -*- coding: utf-8 -*-

import requests

class Coinigy(object):
      
    def __init__(self,key = '',secret = ''):
        self.key = key
        self.secret = secret
        self.url = 'https://www.coinigy.com/api'
        self.apiv = 'v1'
        self.method = {'feed':'newsFeed'}
    
    def get_keys(self,path):
        f = open(path,"r")
        self.key = f.readline().strip()
        self.secret = f.readline().strip()
        
    def request(self, method, data=None):
        headers = {'Content-Type': 'application/json',
                   'X-API-KEY': self.key,
                   'X-API-SECRET': self.secret}
        uri='{method}'.format(method=method)
        url=self.url+'/'+self.apiv+'/'+uri
        
        return requests.post(url, headers=headers)   
                         
    def userInfo(self):
        return self.request('userInfo')  
               
    def activity(self):
        return self.request('activity') 
        
    def notifications(self):
        return self.request('pushNotifications')
        
    def accounts(self):
        return self.request('accounts')
    
    #WIP
    def balances(self):
        params=None
        return self.request('balances', data=params)
    
    #WIP
    def balanceHistory(self):
        params=None
        return self.request('balanceHistory', data=params)
        
    def orders(self):
        return self.request('orders')  
    
    def alerts(self):
        return self.request('alerts')  
        
    def userWatchList(self):
        return self.request('userWatchList')
        
    def newsFeeds(self):
        return self.request('newsFeed')  
