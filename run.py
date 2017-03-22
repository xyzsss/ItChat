# coding=utf8

import itchat
from time import sleep, time
import datetime
from sys import platform

if platform == "linux" or platform == "linux2":
    itchat.auto_login(enableCmdQR=1)
elif platform == "darwin":
    itchat.auto_login(enableCmdQR=2)
elif platform == "win32":
    itchat.auto_login(enableCmdQR=True)

# script running time interval
# slee_time         : running interval time
# heart_report_time : report time interval for check service status
sleep_time = 3600
heart_report_time = 43200
running_days = 0
time_now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

itchat.send(time_now + '\nStart monitor the msr7 shopping info now ....', 'exuxus')

start_while_time = int(time())
while True:
    import get_msr7_info
    re = get_msr7_info.get_msr7_info()
    msr7_info = re.get_result()
    if msr7_info == "NO":
        itchat.send('.Unchaged.', 'exuxus')
        # message_content = u"233"
    else:
        message_front = '\n' + time_now
        message_end = '\n'
        message_content = msr7_info
        message_value = message_front + message_content + message_end
        itchat.send(message_value, 'exuxus')
    current_timestamp = int(time())
    if (current_timestamp - start_while_time) / heart_report_time >= 1:
        running_days += 1
        itchat.send(u"WXRobot running for " + str(running_days/2.0) + u" days .", 'exuxus')
        start_while_time = current_timestamp
    sleep(sleep_time)

itchat.send('Monitor the msr7 has stopped !!!', 'exuxus')
print 'Exit not....'
