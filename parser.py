import re
from web_search import WebSearch

class Parser():
    def __init__(self, html,myhtml_parser,version):
        self.py_version = version
        self.html = html
        self.parser = myhtml_parser
        #self.start_tags = self.extract_start_tags(self.html)
        #self.end_tags = self.extract_end_tags(self.html)
        self.target_urls = None

    def feed_parser(self, html):
        #self.parser.feed(html)
        pass

    def all_urls_found(self,html):
        urls = re.findall(r'="(http.*?)"', html, re.M)
        urls = [z for z in urls if bool(re.search(r"[{};#]+", z)) == False and len(z) > 10]
        if urls:
            global original_list
            original_list = urls
        urls = [re.sub("\\\\", "", z) if "\\" in z else z for z in urls]
        if len(urls) == 1 and len(urls[0]) > 30:
            print("URLs not Found !")
        else:
            print("{} URLs Found !".format(len(urls)))
        return urls

    def target_urls(self,html):
        urls = re.findall(r'"(http.*?)"',html)
        return urls

    def extract_tags(self,html,tags):
        tag_dict = dict()
        if tags:
            if isinstance(tags,list):
                tag_dict = {x:re.findall(r"<{}.*?</{}>".format(x,x),html) for x in tags}
            else:
                tag_dict = {x: re.findall(r"<{}.*?</{}>".format(x, x),html) for x in [tags]}
        return tag_dict

    def extract_target_urls_page():
        target_urls = self.target_urls

        # open the urls in their own threads
        # and return the results
        #wb = WebSearch()
        if self.py_version >= (3, 0):
            from multiprocessing import Pool, TimeoutError
            pool = Pool(4)
            results = pool.map(urllib.request.urlopen,urls)
            #results = pool.map(WebSearch(),urls)
        else:
            from multiprocessing.dummy import Pool as ThreadPool
            # make the Pool of workers
            pool = Pool(4)
            results = pool.map(urllib2.urlopen, urls)

        # close the pool and wait for the work to finish
        pool.close()
        pool.join()

    # initiate_each_process_with_multiprocessing
    def initiate_each_process_with_mp():
        pass
