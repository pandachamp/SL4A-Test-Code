import android
import time
import math

droid = android.Android()

lastlong =0.0
lastlat =0.0
R=6373.0

droid.startLocating(100,1)
#time.sleep(5)

def getDistance(Lat0,Lat1,Long0,Long1):
 lat1 = math.radians(Lat0)
 lon1 = math.radians(Long0)
 lat2 = math.radians(Lat1)
 lon2 = math.radians(Long1)

 dlon = lon2 - lon1
 dlat = lat2 - lat1
 a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
 c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
 distance = (R * c)*1000
 if distance<5:
  return 0
 elif:
  return distance

def getLocation():
 time.sleep(10)
 lastlong= droid.readLocation().result["gps"]["longitude"]
 lastlat= droid.readLocation().result["gps"]["latitude"]

de=0
Long=[]
Lat=[]
sumdis=0.0

while True:
 #lat and long are float
 try:
  getLocation()
 except KeyError:
  print 'GPS wont work'

 if de==0:
  Long.append(lastlong)
  Lat.append(lastlat)
  de=1
 elif de==1:
  Long.append(lastlong)
  Lat.append(lastlat)
  de=2
 elif de==2:
  Long[0]=Long[1]
  Lat[0]=Lat[1]
  Long[1]=lastlong
  Lat[1]=lastlat
  dis = getDistance(Lat[0],Lat[1],Long[0],Long[1])
  sumdis=sumdis+dis
  print sumdis
  print Lat
  print Long
  print'\n'
 time.sleep(10)