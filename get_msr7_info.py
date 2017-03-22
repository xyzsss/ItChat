# coding:utf-8
# get_msr7_info.py

from bs4 import BeautifulSoup
import urllib2
from time import sleep
import socket

class get_msr7_info():
    def __init__(self):
        pass


    def url_open(self, request):
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
        except Exception:
            sleep(3)
            return
        return urlhandle


    def get_shop_status(self, url, shop_color):
        request = urllib2.Request(
            url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        request.add_header('Referer', "http://www.xiji.com/")
        urlhandle = self.url_open(request)
        if urlhandle is not None:
            page_context = urlhandle.read()
            soup = BeautifulSoup(page_context, "html.parser")
            shop_type = soup.select('.item-content')[0].select('.selected')[0].get_text()
            if shop_color == "black":
                shop_status = soup.select('.xj-product-undercarriage')[0].find_all('a')[0].get_text()
            elif shop_color == "red":
                shop_status = soup.select('.xj-product-undercarriage')[0].get_text()
            else:
                shop_status = ''
        else:
            shop_status = ''
        return shop_status


    def get_result(self):
        shop_status_black = self.get_shop_status("http://www.xiji.com/product-14172.html", "black")
        shop_status_red = self.get_shop_status("http://www.xiji.com/product-14173.html", "red")
        if shop_status_red == u"即將開售" and shop_status_black == u"到貨通知":
            message_result = 'NO'
        else:
            message_result = u"黑色" + shop_status_black + u"\n棕色" + shop_status_red
        return message_result

# if __name__ == '__main__':
#     msr7 = get_msr7_info()
#     msr7.get_result()
