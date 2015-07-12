#######################################################
#              
#                     SL4A Project
#        Smart Health care By Puri - ENE22 39A
#      Group members : Soccer 02A , Pun 25A : ENE22
#        Project for ENE 206 - Acedemic Year 2557
#    King Mongkut's University of Technology Thonburi
#
#######################################################
import android
droid=android.Android()

welcomelayout = """<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/background"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent" android:background="#ffffffff">

		<RelativeLayout
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:text="Hello"
            android:textSize="30px"
            android:id="@+id/textView"
            android:layout_above="@+id/textView2"
            android:layout_centerHorizontal="true"
            android:layout_marginBottom="81dp" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:text="My name is Byakko"
            android:id="@+id/textView2"
            android:textSize="65px"

            android:layout_centerVertical="true"
            android:layout_centerHorizontal="true" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Your health care application "
            android:id="@+id/textView3"
            android:textSize="25px"
            android:layout_below="@+id/textView2"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="58dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Agree"
            android:id="@+id/agree"
            android:layout_alignParentBottom="true"
            android:layout_centerHorizontal="true" />
        android:layout_centerVertical="true"
            android:layout_centerHorizontal="true" />
    </RelativeLayout>
    </LinearLayout>
"""

mainlayout = """<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/background"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent" android:background="#ffffffff">

    <RelativeLayout
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true">


        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:text="What do you want to do?"
            android:id="@+id/main_text1"
            android:layout_alignParentTop="true"
            android:layout_centerHorizontal="true"
            android:textSize="50px"
            android:layout_marginTop="86dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Exercise"
            android:id="@+id/main_ex"
            android:layout_below="@+id/main_text1"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="46dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Settings"
            android:id="@+id/main_set"
            android:layout_below="@+id/main_ex"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="26dp" />
    </RelativeLayout>
    </LinearLayout>
"""
settinglayout ="""<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/background"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent" android:background="#ffffffff">

<RelativeLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_gravity="center_horizontal">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:text="Your Name :"
            android:id="@+id/set_name_text"
            android:textSize="50px"
            android:layout_alignParentTop="true"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="64dp" />

        <EditText
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:id="@+id/set_name_input"
            android:layout_marginTop="51dp"
            android:layout_below="@+id/set_name_text"
            />

         <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:text="Relative Person Phone Number:"
            android:id="@+id/set_phone_text"
            android:layout_marginTop="41dp"
            android:layout_below="@+id/set_name_input"
            android:textSize="40px"
            android:layout_centerHorizontal="true" />

        <EditText
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:id="@+id/set_phone_input"
            android:layout_below="@+id/set_phone_text"
            android:layout_centerHorizontal="true"
            android:inputType="textCapWords|textPhonetic|number"
            android:layout_marginTop="51dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Okay"
            android:id="@+id/set_okay_but"
            android:layout_alignParentBottom="true"
            android:layout_centerHorizontal="true"
            android:layout_marginBottom="29dp" />
    </RelativeLayout>

    </LinearLayout>
"""
exlayout = """<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/background"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent" android:background="#ffffffff">

    <RelativeLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_gravity="center_horizontal">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Walking"
            android:textSize="50px"
            android:id="@+id/ex_walk_text"
            android:layout_marginTop="41dp"
            android:layout_alignParentTop="true"
            android:layout_centerHorizontal="true" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="- -"
            android:id="@+id/ex_stepc_text"
            android:textSize="200px"
            android:layout_below="@+id/ex_walk_text"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="63dp" />
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Start"
            android:id="@+id/ex_start_but"
            android:layout_below="@+id/ex_stepc_text"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="48dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Clear"
            android:id="@+id/ex_clear_but"
            android:layout_below="@+id/ex_start_but"
            android:layout_centerHorizontal="true"
            android:layout_marginTop="34dp" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Back"
            android:id="@+id/ex_back_but"
            android:layout_alignParentBottom="true"
            android:layout_centerHorizontal="true"
            android:layout_marginBottom="35dp" />

    </RelativeLayout>
    </LinearLayout>
"""

Name = ''
Phone = ''

def WelcomeAcloop():
    while True:
        event = droid.eventWait().result
        if event['name']=='click':
            id = event['data']['id']
            if id =='agree':
                MainAc()
                return

def MainAcloop():
	while True:
		event = droid.eventWait().result
		if event['name']=='click':
			id = event['data']['id']
			if id =='main_ex':
				print 'mainex'
				ExAc()
				return
			elif id == 'main_set':
				print 'mainset'
				SettingAc()
				return

def SettingAcloop():
	while True:
		event = droid.eventWait().result
		if event['name']=='click':
			id = event['data']['id']
			if id == 'set_okay_but':
				ph =  droid.fullQueryDetail('set_phone_input').result['text']
				na = droid.fullQueryDetail('set_name_input').result['text']
				Phone = ph.encode('ascii','ignore')
				Name = na.encode('ascii','ignore')
				droid.makeToast('Save Successful XD')
				MainAc()
				return
g=0
def test1():
	droid.fullSetProperty('ex_walk_text','text','start')

def test2():
	droid.fullSetProperty('ex_walk_text','text','stop')

def ExAcloop():
	while True:
		event = droid.eventWait().result
		if event['name'] == 'click':
			id = event['data']['id']
			if id == 'ex_start_but':
				if g==0:
					print 'test1'
					test1()
					g=1
				elif g==1:
					print 'test2'
					test2()
					g=0
			elif id == 'ex_clear_but':
				return
			elif id == 'ex_back_but':
				return

def WelcomeAc():
    print 'welcome'
    print droid.fullShow(welcomelayout)
    WelcomeAcloop()

def MainAc():
	print 'mainac'
	print droid.fullShow(mainlayout)
	MainAcloop()

def SettingAc():
	print 'settingac'
	print droid.fullShow(settinglayout)
	SettingAcloop()

def ExAc():
	print 'exac'
	print droid.fullShow(exlayout)
	ExAcloop()

#MainActivity
try:
	WelcomeAc()
except:
	pass