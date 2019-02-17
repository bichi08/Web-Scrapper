import re
from pageDownloader.web_search import WebSearch
from Logger.logger import set_logger

original_list = None
logger = set_logger()


class Parser():
    def __init__(self, html, myhtml_parser, version):
        self.py_version = version
        self.html = str(html)
        self.parser = myhtml_parser
        self.head = None
        self.body = None
        # self.start_tags = self.extract_start_tags(self.html)
        # self.end_tags = self.extract_end_tags(self.html)
        self.all_urls = None
        self.target_urls = None
        self.initiate_each_process_with_mp()

    # Step 1
    def remove_comments(self):
        html = self.html
        try:
            html = re.sub(r"<!.*?>", "", html)
            self.html = html
            logger.info("Comments removed !")
        except Exception as e:
            import traceback
            logger.error("traceback.format_exc()")

    # step 2
    # Populate Head And Body
    def extract_head_and_body(self):
        html = self.html
        head = re.search(r"<head.*?</head>", html)
        if head:
            self.head = head.group()
            logger.info("Head populated !")
        body = re.search(r"<body.*?</body>", html)
        if body:
            self.body = body.group()
            logger.info("Body populated !")

    def feed_parser(self, html):
        # self.parser.feed(html)
        pass

    # Step 3
    # Extract all urls
    def urls_present(self, tag=None):
        html = self.html
        if tag:
            tags = re.findall(r"<{}.*?</{}>".format(tag, tag), html)
            if tags:
                urls = []
                url_data_dct = {}
                for x in tags:
                    mtch = re.search(r'"(http.*?)"', x)
                    if mtch:
                        urls.append(mtch.group(1))
                        url_data_dct[mtch.group(1)] = x
            if urls and url_data_dct:
                return urls, url_data_dct
        else:
            urls = re.findall(r'="(http.*?)"', html, re.M)
            urls = [z for z in urls if bool(re.search(r"[{};#]+", z)) == False and len(z) > 10]
            if urls:
                global original_list
                original_list = urls
                self.all_urls = urls
                logger.info("{} URLs Found !".format(len(urls)))
            else:
                logger.info("URLs not Found !")

    def all_urls_found(self):
        html = self.html
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
            self.all_urls = urls
            logger.info("")
        return urls

    def target_urls(self, html):
        urls = re.findall(r'"(http.*?)"', html)
        return urls

    def extract_tags(self, html, tags):
        tag_dict = dict()
        if tags:
            if isinstance(tags, list):
                tag_dict = {x: re.findall(r"<{}.*?</{}>".format(x, x), html) for x in tags}
            else:
                tag_dict = {x: re.findall(r"<{}.*?</{}>".format(x, x), html) for x in [tags]}
        return tag_dict

    def extract_target_urls_page(self):
        # urls = self.target_urls
        urls = self.all_urls

        # open the urls in their own threads
        # and return the results
        # wb = WebSearch()
        pool = None
        if self.py_version >= (3, 0):
            from multiprocessing import Pool, TimeoutError
            import urllib
            pool = Pool(4)
            results = pool.map(urllib.request.urlopen, urls)
            # results = pool.map(WebSearch(),urls)
        else:
            from multiprocessing.dummy import Pool
            # make the Pool of workers
            pool = Pool(4)
            # results = pool.map(urllib2.urlopen, urls)
            results = pool.map(self.request_url, urls)

        # close the pool and wait for the work to finish
        pool.close()
        pool.join()
        print(results)
        for i in results:
            print(i.code)

    def request_url(self, url):
        wb = WebSearch(url, url_flg=True)
        return wb

    # initiate_each_process_with_multiprocessing
    def initiate_each_process_with_mp(self):
        self.remove_comments()
        self.extract_head_and_body()
        self.all_urls_found()
        self.extract_target_urls_page()
