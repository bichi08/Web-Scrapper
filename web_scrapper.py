from time import time
import re
from html.parser import HTMLParser
from html.entities import name2codepoint

original_list = None

def fprint(itr):
    if type(itr) == type([]):
        for i in itr:
            print(i)
    elif type(itr) == type({}):
        for k,v in itr.items():
            print("{} : {}".format(k,v))
            
 class WebSearch():
    def __init__(self,srch_query):
        self.search_eng_str = "https://www.bing.com/search?q={}&qs=n&from=QBLH"
        self.search_eng_query = self.search_eng_str.format(srch_query)
        self.search_query = srch_query
        self.html = None
        
    def search_web(self):
        from urllib import request
        
        bng_srch_frmt = self.search_eng_query
        resp = request.urlopen(bng_srch_frmt)
        html = str(resp.read())
        self.html = html
        
    def return_html(self):
        prc = Process(target=self.search_web(). args=(self.search_eng_query,))
        prc.start()
        prc.join()
        return self.html
