# '''
# Author: Alok Patel
#
# better net bandwidth needed for better experience
#
# Point to be noted before you use this program:-
# This program will take access of your cursor and
# keyboard until loop inside program ends
#
# Don't click in public group untill program is finished
# or close terminal to close program while executing
# It will write your msg and press enter automaticaly
# Use it on your own risk
#'''

import pywhatkit as kt
import pyautogui as pg
import time

# time is 24 hour based
# hour range -> (0 to 24) min range(0-60)
# kt.sendwhatmsg("+91XXXXXXXXXX", 'your first msg!!!', hour, min)
kt.sendwhatmsg("+91789786xxxx", 'Sending msg using whatsapp automation!!!', 17, 55)

time.sleep(20)
## set frequency
for i in range(100):
    pg.press('enter')
    # pg.write('your msg which you have to repeat')
    pg.write('Sending msg using whatsapp automation!!!')

    pg.press('enter')