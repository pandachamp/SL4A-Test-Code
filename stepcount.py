import android
import time
import math

droid = android.Android()
droid.startSensingTimed(1,50)
time.sleep(1)

x=0
y=0
z=0
axis = 'o'
cx = 0
px = 0
cy = 0
py = 0
cz = 0
pz = 0
threshold = 0.5
step = 0
def chkAxis():
	global x , y , z
	if x > 8 and x < 11
		return 'x'
	elif y > 8 and y <11
		return 'y'
	elif z > 8 and z < 11
		return 'z'
	else:
		return 'o'

while True:
	
	x = droid.readSensors().result['xforce']
	y = droid.readSensors().result['yforce']
	z = droid.readSensors().result['zforce']
	axis = chkAxis()

	if axis == 'x':
		cz = z
		if math.fabs(cz-pz) > threshold:
			step = step+1
		pz = z
	if axis == 'y':
		cz = z
		if math.fabs(cz-pz)>threshold:
			step=step+1
		pz = z
	if axis = 'z':
		cy = y
		if math.fabs(cy-py)>threshold:
			step=step+1
		py = y

	print step
	time.sleep(1)

