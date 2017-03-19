# coding=utf8

import itchat
from time import sleep
import datetime

# linux platform
itchat.auto_login(enableCmdQR=1)
# UNIX platform
# itchat.auto_login(enableCmdQR=2)

# script running time interval
sleep_time = 3600
time_now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")


itchat.send(time_now + '\nStart monitor the msr7 shopping info now ....', 'exuxus')

while True:
    import get_msr7_info
    re = get_msr7_info.get_msr7_info()
    msr7_info = re.get_result()
    if msr7_info == "NO":
        pass
        # message_content = u"233"
    else:
    	message_front = '\n' + time_now
   	message_end = '\n'
        message_content = msr7_info
    	message_value = message_front + message_content + message_end
    	itchat.send(message_value, 'exuxus')
    sleep(sleep_time)


itchat.send('Monitor the msr7 has stopped !!!', 'exuxus')
print 'Exit not....'
