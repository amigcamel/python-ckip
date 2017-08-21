# -*-coding:utf-8-*-
"""__init__ module."""
import re

import six
from six.moves import urllib
from six.moves.http_cookiejar import CookieJar


def parse_tree(string):
    """Send HTTP request and parse result."""
    if not isinstance(string, six.text_type):
        try:
            string = string.decode('utf-8')
        except Exception:
            raise UnicodeError('Input encoding should be UTF8 of UNICODE')
    string = string.encode('cp950')

    url = 'http://parser.iis.sinica.edu.tw/'

    cj = CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj)
    )

    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 Gecko/20100101 Firefox/29.0'),
        ('referer', 'http://parser.iis.sinica.edu.tw/'),
        ('Host', 'parser.iis.sinica.edu.tw')
    ]

    raw = urllib.request.urlopen(url).read()
    raw = raw.decode('cp950') if isinstance(raw, six.binary_type) else raw
    fid = re.search('name="id" value="(\d+)"', raw).group(1)

    postdata = dict()
    postdata['myTag'] = string
    postdata['id'] = fid

    postdata = urllib.parse.urlencode(postdata)
    postdata = postdata.encode('utf-8') if six.PY3 else postdata
    res_url = 'http://parser.iis.sinica.edu.tw/svr/webparser.asp'

    res = opener.open(res_url, postdata).read()
    res = res.decode('cp950')
    res = re.findall('<nobr>#\d+:(.*?)</nobr>', res)

    return res
