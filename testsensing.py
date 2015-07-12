import android
droid = android.Android()
droid.startSensingTimed(1,50)
while true:
	print droid.readSensors().result