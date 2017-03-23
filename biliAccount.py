# coding:utf-8

from bs4 import BeautifulSoup
import urllib2
import json
import datetime


class biliAccount():
    def __init__(self):
        pass

    def is_json(self, json_content):
        try:
            json.loads(json_content)
        except ValueError:
            return False
        return True

    def get_js_content(self, bili_nickname):
        bilibili_name = bili_nickname
        URL = "http://interface.bilibili.com/card/" + bilibili_name + ".js"
        request = urllib2.Request(
            URL, headers={'User-Agent': 'Mozilla/5.0\
             (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        request.add_header('Referer', "http://www.bilibili.com/")
        urlhandle = urllib2.urlopen(request, None, timeout=20)
        page_context = urlhandle.read()
        soup = BeautifulSoup(page_context, "html.parser")
        return soup

    def deal_json_content(self, bili_nickname):
        soup = self.get_js_content(bili_nickname)
        if str(soup) == "ShowCard(false);":
            user_info = u"B站不存在改昵称"
        else:
            user_str = str(soup).replace("ShowCard(", "").replace("});", "}")
            user_json = json.loads(user_str)
            user_name = user_json.get('name')
            user_sex = user_json.get('sex')
            # user_face = user_json.get('face')   #照片
            user_birthday = user_json.get('birthday')

            reg_unixtime = user_json.get('regtime')
            regtime_value = datetime.datetime.fromtimestamp(reg_unixtime)
            user_regtime = regtime_value.strftime('%Y年%m月%d日 %H:%M:%S')
            user_regtime = unicode(user_regtime, 'utf-8')
            user_sign = user_json.get('sign')
            user_attentions_number = str(len(user_json.get('attentions')))
            user_fans_number = str(user_json.get('fans'))
            user_level = str(user_json.get('level_info')['current_level'])
            user_online_min = str(user_json.get('level_info')['current_min'])
            user_current_exp = str(user_json.get('level_info')['current_exp'])

            user_info = "" + user_name + "\n" + user_sex + "\t" + user_birthday
            user_info += "\n" + u"B站注册时间:" + user_regtime + "\n" + u"当前等级:"
            user_info += user_level + u" 当前经验:" + user_current_exp
            user_info += u" 当前在线时间:" + user_online_min + "\n" + u"签名:"
            user_info += user_sign + "\n" + u"粉丝数:" + user_fans_number
            user_info += u"\t关注数:" + user_attentions_number
        return user_info

# if __name__ == '__main__':
#     biliacc = biliAccount()
#     info = biliacc.deal_json_content("名字不能随便娶的2")
#     print info
