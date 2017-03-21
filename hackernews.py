# coding:utf-8

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2
import json
from time import sleep


def is_json(json_content):
    try:
        json.loads(json_content)
    except ValueError:
        return False
    return True


def is_ascii(text):
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True


# TOP
URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
request = urllib2.Request(
    URL, headers={'User-Agent': 'Mozilla/5.0\
     (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
urlhandle = urllib2.urlopen(request, None, timeout=20)
page_context = urlhandle.read()
soup = BeautifulSoup(page_context, "html.parser")
item_list = str(soup).replace("]", "").replace("[", "").\
    replace(" \n", "").split(",")

for item in item_list:
    item = item.strip()
    request_url = "https://hacker-news.firebaseio.com/v0/item/" + item\
        + ".json?print=pretty"
    print "###########\t\t" + request_url
    # request_url = "https://hacker-news.firebaseio.com/v0/item/13907904.json?print=pretty"
    try:
        urlhandle = urllib2.urlopen(request_url, None, timeout=20)
    except Exception:
        continue
    url_content = urlhandle.read()
    content = BeautifulSoup(url_content, "html.parser")
    if is_json(str(content)):
        content_json = json.loads(str(content))
        if content_json:
            content_url = content_json.get('url') if content_json.get('url') is not None else ''
            content_url = str(content_url)
            content_title = content_json.get('title') if content_json.get('title') is not None else ''
            if isinstance(content_title, unicode):
                content_title = content_title
            else:
                content_title = str(content_title)
            content_score = content_json.get('score') if content_json.get('score') is not None else 0
            content_id = content_json.get('id') if content_json.get('id') is not None else 0
        print "\n".join([content_title, content_url, str(content_id) + "(Score:" + str(content_score) + ")"])
    else:
        print "\nSKIPPED !!!\n"
    # sleep(5)

print 'Over!!!'
