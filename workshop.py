import android

droid = android.Android()
droid.dialogCreateInput("Grade Cal","input subject")
droid.dialogSetPositiveButtonText("OK")
droid.dialogSetNegativeButtonText("Cancel")
droid.dialogShow()
if droid.dialogGetResponse().result["which"]=="positive":
 n = int(droid.dialogGetResponse().result["value"])

Grade = []
c = []
sumg=0
sumc=0

def calGrade(a):
 droid.dialogCreateInput("Grade Cal","Credit subject "+str(a))
 droid.dialogSetPositiveButtonText("OK")
 droid.dialogSetNegativeButtonText("Cancel")
 droid.dialogShow()
 if droid.dialogGetResponse().result["which"]=="positive":
  credit = int(droid.dialogGetResponse().result["value"])
  c.append(credit)
 droid.dialogCreateInput("Grade Cal","Grade subject "+str(a))
 droid.dialogSetPositiveButtonText("OK")
 droid.dialogSetNegativeButtonText("Cancel")
 droid.dialogShow()
 if droid.dialogGetResponse().result["which"]=="positive":
  g = float(droid.dialogGetResponse().result["value"])
 
 x  = g*credit
 Grade.append(x)

g=[]
for i in range(1,n+1):
 calGrade(i)

for i in range(0,n):
 sumg = sumg+Grade[i]
 sumc = sumc+c[i]

allg = (sumg/sumc)

droid.dialogCreateAlert("Grade Cal","Your grade is "+str(allg))
droid.dialogSetPositiveButtonText("Yes")
droid.dialogShow()

##


import android

droid = android.Android()
droid.dialogCreateInput("Grade Cal","input subject")
droid.dialogSetPositiveButtonText("OK")
droid.dialogSetNegativeButtonText("Cancel")
droid.dialogShow()
if droid.dialogGetResponse().result["which"]=="positive":
 n = int(droid.dialogGetResponse().result["value"])

Grade = []
c = []
sumg=0
sumc=0

def calGrade(a):
 droid.dialogCreateInput("Grade Cal","Credit subject "+str(a))
 droid.dialogSetPositiveButtonText("OK")
 droid.dialogSetNegativeButtonText("Cancel")
 droid.dialogShow()
 if droid.dialogGetResponse().result["which"]=="positive":
  credit = int(droid.dialogGetResponse().result["value"])
  c.append(credit)
 droid.dialogCreateInput("Grade Cal","Grade subject "+str(a))
 droid.dialogSetPositiveButtonText("OK")
 droid.dialogSetNegativeButtonText("Cancel")
 droid.dialogShow()
 if droid.dialogGetResponse().result["which"]=="positive":
  GG = droid.dialogGetResponse().result["value"]

 if GG=="A":
  g=4
 elif GG=="B+":
  g=3.5
 elif GG=="B":
  g=3
 elif GG=="C+":
  g=2.5
 elif GG=="C":
  g=2
 elif GG=="D+":
  g=1.5
 elif GG=="D":
  g=1
 elif GG=="F":
  g=0
 
 x  = g*credit
 Grade.append(x)

g=[]
for i in range(1,n+1):
 calGrade(i)

for i in range(0,n):
 sumg = sumg+Grade[i]
 sumc = sumc+c[i]

allg = (sumg/sumc)

droid.dialogCreateAlert("Grade Cal","Your grade is "+str(allg))
droid.dialogSetPositiveButtonText("Yes")
droid.dialogShow()
 