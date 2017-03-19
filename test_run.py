# coding=utf8

import itchat
from time import sleep


itchat.auto_login(enableCmdQR=1)

while True:
    message_content = u"233 ,test by xyzsss 哈哈哈哈哈哈"
    itchat.send(message_content, 'exuxus')
    sleep(3)

print 'Exit not....'

