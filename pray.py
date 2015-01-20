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
			   org.freedesktop.UPower.Suspend")

def separate(ampm,time):
	time = time.replace(ampm,"")
	head, sep, tail = time.partition(':')
	if ampm =="am":
		hours = int(head)
	elif ampm == "pm":
		hours = int(head) + 12
	minutes = int(tail)
	pray_time = str(str(hours) + ":" + str(minutes))
	return pray_time

def getTime(pray):	
	time = data["items"][0][pray]
	minutes = hours = 0
	ampm = "am" if "am" in time else "pm"
	return separate(ampm,time)
	
prayers = ["fajr","dhuhr","asr","maghrib","isha"]
for pray in prayers:
	pray_time = getTime(pray)	
	schedule.every().day.at(pray_time).do(suspend)

while True:
    schedule.run_pending()
    time.sleep(1)
