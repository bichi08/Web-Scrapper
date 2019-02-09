from time import time
import re
import logging

from datetime import datetime
curr_time  = datetime.now()
timestamp = "-".join([str(x) for x in [curr_time.year,curr_time.month,curr_time.day,curr_time.hour,curr_time.minute,curr_time.second]])

#logging.basicConfig(filename='{}.log'.format(timestamp), filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='{}.log'.format(timestamp),
                    format='%(asctime)s %(message)s',
                    filemode='w')
#logging.warning('This will get logged to a file')
#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


from htmlparser import return_htmlparser_class
from parser import Parser
from web_search import WebSearch
from utils import *

original_list = None
target_tag = "h2"

import sys
version = (3, 0)
cur_version = sys.version_info







kwd = "India"
# HTML parser class is ready !
parser = return_htmlparser_class(cur_version)

#now searching through web
ws = WebSearch(kwd)
logger.info("search Engine query : {}".format(ws.search_eng_query))
html = ws.return_html()
print(html)

sc = Parser(html,parser,cur_version)
