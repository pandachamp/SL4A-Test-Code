import android
import time
import math

droid = android.Android()
droid.startLocating(100,1)
time.sleep(10)

def getDistance(Lat0,Lat1,Long0,Long1):
 lat1 = radians(Lat0)
 lon1 = radians(Long0)
 lat2 = radians(Lat1)
 lon2 = radians(Long1)
 dlon = lon2 - lon1
 dlat = lat2 - lat1
 a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
 c = 2 * atan2(sqrt(a), sqrt(1-a))
 distance = (R * c)*1000
 if distance<5:
  return 0
 elif:
  return distance

def getLocation():
 lastlat= droid.readLocation().result["gps"]["longitude"]
 lastlong= droid.readLocation().result["gps"]["latitude"]

de=0
Long=[]
Lat=[]
while True:
 #lat and long return float
 getLocation()
 
 if de==0:
  Long[0]=lastlong
  Lat[0]=lastlat
  de=1
 elif de==1:
  Long[1]=lastlong
  Lat[1]=lastlat
  de=2
 elif de==2:
  Long[0]=Long[1]
  Lat[0]=Lat[1]
  Long[1]=lastlong
  Lat[1]=lastlat
 dis = getDistance(Lat[0],Lat[1],Long[0],Long[1])
 print dis
 time.sleep(10)