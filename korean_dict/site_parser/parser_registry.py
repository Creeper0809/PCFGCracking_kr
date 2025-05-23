from typing import Optional
from urllib.parse import urlparse

from korean_dict.site_parser.dcinside_parser import DcinsideParser
from korean_dict.site_parser.naver_news_parser import NaverNewsParser
from korean_dict.site_parser.site_parser import SiteParser

PARSERS = {
    "news.naver.com": NaverNewsParser(),
    "gall.dcinside.com": DcinsideParser(),
}

def get_parser_for(url):
    host = urlparse(url).netloc
    for domain, parser in PARSERS.items():
        if host == domain or host.endswith("." + domain):
            return parser
    return None

