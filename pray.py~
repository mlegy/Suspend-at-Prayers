#!/usr/bin/env python

import urllib, json
import schedule
import time

url = "http://muslimsalat.com/daily.json?key=103c54f0cfb2e2adeb337716a12c1317"
response = urllib.urlopen(url);
data = json.loads(response.read())

def suspend():
	import os
	os.system("dbus-send --system --print-reply \
			   --dest=\"org.freedesktop.UPower\" \
			   /org/freedesktop/UPower \
			   org.freedesktop.UPower.Suspend ")

def getTime(pray):	
	time = data["items"][0][pray]
	minutes = hours = 0
	
	if "am" in time:
		time = time.replace("am","")
		head, sep, tail = time.partition(':')
		hours = int(head)
		minutes = int(tail)

	elif "pm" in time:
		time = time.replace("pm","")
		head, sep, tail = time.partition(':')
		hours = int(head) + 12
		minutes = int(tail)
	
	pray_time = str(str(hours) + ":" + str(minutes))
	return pray_time

prayers = ["fajr","dhuhr","asr","maghrib","isha"]
for pray in prayers:
	pray_time = getTime(pray)	
	schedule.every().day.at(pray_time).do(suspend)
	print pray_time

while True:
    schedule.run_pending()
    time.sleep(1)