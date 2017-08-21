# -*-coding:utf-8-*-
"""__init__ module."""
import urllib
import urllib2
import cookielib
import re


def parse_tree(string):
    """Send HTTP request and parse result."""
    if not isinstance(string, unicode):
        try:
            string = string.decode('utf-8')
        except Exception:
            raise UnicodeError('Input encoding should be UTF8 of UNICODE')
    string = string.encode('cp950')

    url = 'http://parser.iis.sinica.edu.tw/'

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 Gecko/20100101 Firefox/29.0'),
        ('referer', 'http://parser.iis.sinica.edu.tw/'),
        ('Host', 'parser.iis.sinica.edu.tw')
    ]

    raw = urllib.urlopen(url).read()
    fid = re.search('name="id" value="(\d+)"', raw).group(1)

    postdata = dict()
    postdata['myTag'] = string
    postdata['id'] = fid

    postdata = urllib.urlencode(postdata)

    res_url = 'http://parser.iis.sinica.edu.tw/svr/webparser.asp'

    res = opener.open(res_url, postdata).read()
    res = res.decode('cp950')
    res = re.findall('<nobr>#\d+:(.*?)</nobr>', res)

    return res
