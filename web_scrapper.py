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
    
    
class HTMLParser_1():
    def __init__(self, html):
        self.html = html
        self.parser = MyHTMLParser()
        self.start_tags = self.extract_start_tags(self.html)
        self.end_tags = self.extract_end_tags(self.html)
        
    def feed_parser(self, html):
        self.parser.feed(html)
        
    @property
    def urls_found(self):
        urls = re.findall(r'="(http.*?)"', html, re.M)
        urls = [z for z in urls if bool(re.search(r"[{};#]+", z)) == False and len(z) > 10]
        if urls:
            global original_list
            original_list = urls
        urls = [re.sub("\\\\","",z) if "\\" in z else z for z in urls]
        if len(urls) == 1 and len(urls[0]) > 30:
            print("URLs not Found !")
        else:
            print("{} URLs Found !".format(len(urls)))
        return urls
        
        
        
