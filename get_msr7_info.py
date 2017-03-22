# coding:utf-8
# get_msr7_info.py

from bs4 import BeautifulSoup
import urllib2
from time import sleep
import socket

class get_msr7_info():
    def __init__(self):
        pass

    def get_black(self):
        URL = "http://www.xiji.com/product-14172.html"
        request = urllib2.Request(
            URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        request.add_header('Referer', "http://www.xiji.com/")
        try:
            try:
                urlhandle = urllib2.urlopen(request, None, timeout=20)
            except urllib2.URLError, e:
                if isinstance(e.reason, socket.timeout):
                    print "Urllib Socket error!!!!"
                else:
                    raise
            except socket.timeout, e:
                print "Socket error!!!"
                sleep(3)
                return
            else:
                sleep(3)
                return
        except Exception:
            sleep(3)
            return
        page_context = urlhandle.read()
        soup = BeautifulSoup(page_context, "html.parser")
        # page_title = soup.select('title')[0].get_text()
        shop_type = soup.select('.item-content')[0].select('.selected')[0].get_text()
        shop_status_1 = soup.select('.xj-product-undercarriage')[0].find_all('a')[0].get_text()
        return shop_status_1

    def get_red(self):
        URL = "http://www.xiji.com/product-14173.html"
        request = urllib2.Request(
            URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        request.add_header('Referer', "http://www.xiji.com/")
        try:
            try:
                urlhandle = urllib2.urlopen(request, None, timeout=20)
            except urllib2.URLError, e:
                if isinstance(e.reason, socket.timeout):
                    print "Urllib Socket error!!!!"
                else:
                    raise
            except socket.timeout, e:
                print "Socket error!!!"
                sleep(3)
                return
            else:
                sleep(3)
                return
        except Exception:
            sleep(3)
            return
        page_context = urlhandle.read()
        soup = BeautifulSoup(page_context, "html.parser")
        # page_title = soup.select('title')[0].get_text()
        shop_type = soup.select('.item-content')[0].select('.selected')[0].get_text()
        shop_status_2 = soup.select('.xj-product-undercarriage')[0].get_text()
        return shop_status_2

    def get_result(self):
        shop_status_1 = self.get_black() if self.get_black() is None else ''
        shop_status_2 = self.get_red() if self.get_red() is None else ''
        if shop_status_2 == u"即將開售" and shop_status_1 == u"到貨通知":
            message_result = 'NO'
        else:
            message_result = u"黑色" + shop_status_1 + u"\n棕色" + shop_status_2
        return message_result

# if __name__ == '__main__':
#     msr7 = get_msr7_info()
#     msr7.get_result()

