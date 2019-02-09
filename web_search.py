import logging
logger=logging.getLogger()
class WebSearch():
    def __init__(self, srch_query,url_flg=False):
        self.url_flg = url_flg
        if url_flg == False:
            self.search_eng_str = "https://www.bing.com/search?q={}&qs=n&from=QBLH"
            self.search_eng_query = self.search_eng_str.format(srch_query)
        elif url_flg == True:
            self.search_eng_query = self.url_flg
        self.search_query = srch_query
        self.html = None
        self.code = None

    def download_page(self):
        import sys
        version = (3, 0)
        cur_version = sys.version_info
        url = self.search_eng_query
        while True:
            if cur_version >= version:  # If the Current Version of Python is 3.0 or above
                import urllib.request
                from urllib.request import Request, urlopen
                from urllib.request import URLError, HTTPError
                print("Py-Ver 3.0")
                logger.info("Python Version : {}".format(3.0))

                try:
                    headers = {}
                    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                    #req = urllib.request.Request(url, headers=headers)
                    resp = urllib.request.urlopen(url)
                    respData = str(resp.read())
                    self.html = respData
                    if self.html:
                        break
                    #return respData
                except Exception as e:
                    print("Could not open URL. Please check your internet connection and/or ssl settings")
            else:  # If the Current Version of Python is 2.x
                import urllib2
                from urllib2 import Request, urlopen
                from urllib2 import URLError, HTTPError
                print("Py-Ver 2.7")
                logger.info("Python Version : {}".format(2.7))
                try:
                    headers = {}
                    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                    # req = urllib2.Request(url, headers=headers)
                    print "0"
                    #request = urllib2.Request(url, headers=headers)
                    request = urllib2.Request(url)
                    print "1"
                    result = urllib2.urlopen(request)
                    print "2"
                    contents = result.read()
                    self.code = result.getcode()
                    logger.info("Request return code : {}".format(self.code))
                    self.html = contents
                    if self.html:
                        break
                    #return page
                except:
                    print("Could not open URL. Please check your internet connection and/or ssl settings")
                    import traceback
                    print(traceback.format_exc())
                    logger.error(traceback.format_exc())

                    #return "Page Not found"

    def return_html(self):
        from multiprocessing import Process
        try:
            prc = Process(target=self.download_page(),args=())
            prc.start()
            prc.join()
            return self.html
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            logger.error(traceback.format_exc())
