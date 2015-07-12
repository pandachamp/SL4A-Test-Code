#StopWatch.py

#------------Ресурсы------------
    
layout="""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    android:id="@+id/MainWidget"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    xmlns:android="http://schemas.android.com/apk/res/android">
        android:background="#ff000000"
    <TextView
            android:id="@+id/display"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:layout_alignParentTop="true"
            android:textColor="#0bda51"
            android:text="00:00:00.000"
            android:textStyle="bold"
            android:gravity="center"
            android:textSize="60dp" />
    <Button
            android:id="@+id/startbutton"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_below="@id/display"
            android:layout_alignParentLeft="true"
            android:textSize="40dp"
            android:layout_toLeftOf = "@id/center"/>
    <Button
            android:id="@+id/center"
            android:layout_below="@id/display"
            android:layout_height="wrap_content"
            android:layout_width="0dp"
            android:layout_centerHorizontal="true" />
    <Button
            android:id="@+id/stopbutton"
            android:layout_width="0pdp"
            android:layout_height="wrap_content"
            android:enabled="false"
            android:textSize="40dp"
            android:layout_below="@id/display"
            android:layout_alignParentRight="true"
            android:layout_toRightOf = "@id/center"/>
            
    <TextView
        android:id="@+id/info"
        android:layout_width="fill_parent"
        android:layout_height="0dp"
        android:layout_below="@id/stopbutton"
        android:textColor="#FFFFFF"
        android:text=""
        android:textStyle="bold"
        android:layout_alignParentBottom="true"
        android:textSize="30dp"
        android:layout_alignParentBottom="true"/>

        
</RelativeLayout>
"""
rCircle_label = "Круг"
rStart_label = "Старт"
rClear_label = "Очистить"
rStop_label = "Стоп"
#---------------------


import android, os, datetime
    
#Глобальные переменные
starttime=datetime.datetime.now()
runed = False #если True то таймер запущен
lastcircle = 0
cleared = True #если True, то показания секундомера очищены

def format_time(tm):
 hours = int(tm.seconds / 3600)
 minuts = int((tm.seconds - hours*3600)/60)
 seconds=tm.seconds - hours*3600 - minuts*60
 microseconds = round(tm.microseconds/1000)
 return "{0:0>02}:{1:0>02}:{2:0>02}.{3:0>03}".format(hours,minuts,seconds,microseconds)

#Возвращает разницу времени в виде строки. Если now =0, то разница с текущим временем
def timediff(prev, now=0):
 if not now: now=datetime.datetime.now()
 diff=now-prev	
 return format_time(diff)
		
def stopwatch_start():
 global runed,lastcircle,starttime
 runed=True
 starttime=datetime.datetime.now()
 lastcircle = starttime
 droid.fullSetProperty("startbutton","text",rCircle_label)
 droid.fullSetProperty("stopbutton","enabled","true")

def stopwatch_circle():
    #код опущен
    # t - сформированная строка с временем круга
 lastdata =  droid.fullQueryDetail("info").result['text']
 newdata = lastdata+"\n"+t;
 droid.fullSetProperty("info","text",newdata)    
 lastcircle = datetime.datetime.now()

def stopwatch_stop():
    #код опущен
	

def stopwatch_clear():
    #код опущен
	
def eventloop():
 while True:
  event=droid.eventWait(50).result
  if runed:      
   droid.fullSetProperty("display","text",timediff(starttime))
   if event != None:
  if event["name"]=="key":
   droid.vibrate(30)
   if event["data"]["key"] == '4':
    return
   elif event["data"]["key"]=='24' and cleared:
    if runed:
     stopwatch_circle()
    else:
     topwatch_start()
   elif event["data"]["key"]=='25' and runed:
      stopwatch_stop()
                
  elif event["name"]=="click":
   droid.vibrate(30)
   id=event["data"]["id"]
   if id=="startbutton" and not runed:
    stopwatch_start()
   elif id=="stopbutton" and runed:
    stopwatch_stop()
   elif id=="stopbutton" and not runed:
    stopwatch_clear()
   elif id=="startbutton" and runed:
    stopwatch_circle()
  elif event["name"]=="screen":
   if event["data"]=="destroy":
    return
            
droid = android.Android()
try:
 print(droid.fullShow(layout))
 droid.fullKeyOverride([24,25],True)
 droid.fullSetProperty("MainWidget","background","#ff000000")
 droid.fullSetProperty("startbutton","text",rStart_label)
 droid.fullSetProperty("stopbutton","text",rStop_label)
 eventloop()
finally:
 
 droid.fullDismiss()