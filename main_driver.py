from sys import version_info

from HtmlParser.myhtmlparser import return_htmlparser_class
from HtmlParser.parser import Parser
from pageDownloader.web_search import WebSearch
# from Exceptions_classes.WebSearchException import keyworkSearchException
from Logger.logger import set_logger

logger = set_logger()

version = (3, 0)
cur_version = version_info


def prepare_search_kwd_for_search_engine(kwd):
    if " " not in kwd:
        return kwd
    else:
        import re
        kwd = re.sub(r"[\s]+", "+", kwd.strip())
        print(kwd)
        if kwd:
            return kwd
        else:
            pass
            #raise keyworkSearchException


kwd = "Gifted Movie review"

kwd = prepare_search_kwd_for_search_engine(kwd)
# HTML parser class is ready !
parser = return_htmlparser_class(cur_version)

# now searching through web
ws = WebSearch(kwd)
logger.info("search Engine query : {}".format(ws.search_eng_query))
html = ws.return_html()
print(html)

sc = Parser(html, parser, cur_version)
