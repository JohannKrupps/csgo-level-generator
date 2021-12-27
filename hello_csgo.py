import random
import subprocess
import os


levelBoundPos=2048
levelBoundNeg=-2048
#Alternate Generation
#fixed number, no min/max and high/low
def chunk():
	min=levelBoundNeg/2
	max=levelBoundPos/2
	low=random.randint(min,1)
	high=random.randint(0,max)
	while True:
		#print("In Chunk")
		ints=random.randint(low,high)
		#print ints
		if(ints%2==0 and ints!=0): #mod 8 is good
			final=ints
			break
	return final
	
#for some reason, small numbers won't make a level
#...sometimes
#ACKCHUALLY its the modulus division
#def sheet():
	#min=-256
	#max=257
	#low=random.randint(min,1)
	#high=random.randint(0,max)
#	while True:
#		ints=random.randint(-32,33) #-128,129 is bretty cool
		#print("In Sheet")
		#print ints
#		if(ints%4==0 and ints!=0): #mod 2 is good
#			final=ints
#			break
#	return final

fileStart=open("header.txt","r")
fileMap=open("one_solid.txt","r")
fileBounds=open("outerlimits12.txt","r")
filePlayers=open("one_spawnpoint.txt","r")
fileDMSpawn=open("one_DM_spawn.txt","r")
fileBombsites=open("bombsites.txt","r")
fileEnd=open("footernewer.txt","r")
finalFile=open("de_random_map.vmf","w")
compilepath0="\"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\\""
compilepath1="\"E:\\Gayms\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\\""
whichpath=1
if(whichpath==0):
	vbsp=compilepath0+"bin\\vbsp.exe -game "+compilepath0+"csgo\\ de_random_map.vmf"
	vvis=compilepath0+"bin\\vvis.exe -game "+compilepath0+"csgo\\ -fast de_random_map.bsp"
	vrad=compilepath0+"bin\\vrad.exe -game "+compilepath0+"csgo\\ de_random_map.bsp"
else:
	vbsp=compilepath1+"bin\\vbsp.exe -game "+compilepath1+"csgo\\ de_random_map.vmf"
	vvis=compilepath1+"bin\\vvis.exe -game "+compilepath1+"csgo\\ -fast de_random_map.bsp"
	vrad=compilepath1+"bin\\vrad.exe -game "+compilepath1+"csgo\\ de_random_map.bsp"

id=10000

start=fileStart.read()
finalFile.write(start+"\n")

map=fileMap.read()
for x in range(0,250):
	#print("In Generation")
	solid=map
	
	blocktype=random.randint(0,100)
	xOffset=random.randint(levelBoundNeg/2,levelBoundPos/2)*1.5 #was 32,1024
	yOffset=random.randint(levelBoundNeg/2,levelBoundPos/2)*1.5 #was -64,65
	zOffset=0#random.randint(0,levelBoundPos/32) #was 32,1024
	#-512,1024 made some baller levels
	
	solid0=solid.replace("aSolidID",str(id))
	id+=1
	solid1=solid0.replace("aSideID0",str(id))
	id+=1
	solid2=solid1.replace("aSideID1",str(id))
	id+=1
	solid3=solid2.replace("aSideID2",str(id))
	id+=1
	solid4=solid3.replace("aSideID3",str(id))
	id+=1
	solid5=solid4.replace("aSideID4",str(id))
	id+=1
	solid6=solid5.replace("aSideID5",str(id))
	id+=1
	if(0<=blocktype and blocktype<=24):
		while True:
		#floor/ceiling
			startX=chunk()+xOffset
			startY=chunk()+yOffset
			startZ=chunk()/8+zOffset
			endX=chunk()+xOffset
			endY=chunk()+yOffset
			endZ=chunk()/8+zOffset
			if(endX-startX>0 and endY-startY>0 and endZ-startZ>0):
				break
	elif(25<=blocktype and blocktype<=49):
		while True:
		#X-facing wall
			startX=chunk()/2+xOffset
			startY=chunk()+yOffset
			startZ=chunk()/2+zOffset
			endX=chunk()/2+xOffset
			endY=chunk()+yOffset
			endZ=chunk()/2+zOffset
			if(endX-startX>0 and endY-startY>0 and endZ-startZ>0):
				break
	elif(50<=blocktype and blocktype<=74):
		while True:
		#Y-facing wall
			startX=chunk()+xOffset
			startY=chunk()/2+yOffset
			startZ=chunk()/2+zOffset
			endX=chunk()+xOffset
			endY=chunk()/2+yOffset
			endZ=chunk()/2+zOffset
			if(endX-startX>0 and endY-startY>0 and endZ-startZ>0):
				break
	else:
		while True:
		#Floor/ceiling
			startX=chunk()+xOffset
			startY=chunk()+yOffset
			startZ=chunk()/8+zOffset
			endX=chunk()+xOffset
			endY=chunk()+yOffset
			endZ=chunk()/8+zOffset
			if(endX-startX>0 and endY-startY>0 and endZ-startZ>0):
				break
	v1=solid6.replace("startX",str(startX))
	v2=v1.replace("startY",str(startY))
	v3=v2.replace("startZ",str(startZ))
	v4=v3.replace("endX",str(endX))
	v5=v4.replace("endY",str(endY))
	v6=v5.replace("endZ",str(endZ))
	finalFile.write(v6+"\n")
	
#spawnblock=fileMap.read()
#finalFile.write("Spawnblocks start")
locationX=random.randint(-1224,800)
locationY=random.randint(-1224,-1000)
for sp in range(0,2):
	spwn=map
	flipX=0
	flipY=0
	if(sp==1):
		flipX=locationX*2
		flipY=locationY*2
	asolid0=spwn.replace("aSolidID",str(id))
	id+=1
	asolid1=asolid0.replace("aSideID0",str(id))
	id+=1
	asolid2=asolid1.replace("aSideID1",str(id))
	id+=1
	asolid3=asolid2.replace("aSideID2",str(id))
	id+=1
	asolid4=asolid3.replace("aSideID3",str(id))
	id+=1
	asolid5=asolid4.replace("aSideID4",str(id))
	id+=1
	asolid6=asolid5.replace("aSideID5",str(id))
	id+=1

	av1=asolid6.replace("startX",str((locationX-80)-flipX))
	av2=av1.replace("startY",str((locationY-80)-flipY))
	av3=av2.replace("startZ",str(-8))
	av4=av3.replace("endX",str((locationX+360)-flipX))
	av5=av4.replace("endY",str((locationY+360)-flipY))
	av6=av5.replace("endZ",str(0))
	finalFile.write(av6+"\n")
#finalFile.write("Spawnblocks end\n")
	
bounds=fileBounds.read()
insideMin=bounds.replace("inMin",str(levelBoundNeg))
outsideMin=insideMin.replace("outMin",str(levelBoundNeg-32))
insideMax=outsideMin.replace("inMax",str(levelBoundPos))
outsideMax=insideMax.replace("outMax",str(levelBoundPos+32))
finalFile.write(outsideMax+"\n")

spawner=filePlayers.read()

for j in range(0,4):
	idChange=spawner.replace("spawnID",str(id))
	id+=1
	xLoc=idChange.replace("randX",str(locationX+80*j))
	for i in range(0,4):
		yLoc=xLoc.replace("randY",str(locationY+80*i))
		finalFile.write(yLoc+"\n")

for j in range(0,4):
	teamChange=spawner.replace("info_player_terrorist","info_player_counterterrorist")
	idChange=teamChange.replace("spawnID",str(id))
	id+=1
	xLoc=idChange.replace("randX",str(-locationX+80*j))
	for i in range(0,4):
		yLoc=xLoc.replace("randY",str(-locationY+80*i))
		finalFile.write(yLoc+"\n")

dmSpawns=fileDMSpawn.read()
for dm in range(0,31):
	xLoc=random.randint(-1024,1025)
	yLoc=random.randint(-1024,1025)
	newX=dmSpawns.replace("xRan",str(xLoc))
	newY=newX.replace("yRan",str(yLoc))
	finalFile.write(newY+"\n")
	

sites=fileBombsites.read()
#x difference: 448
#y difference: 544
last=""
for bmb in range(0,2):
	sitePointX=random.randint(-1000,-700)
	sitePointY=random.randint(700,1000)
	replacer1="siteXLow"
	replacer2="siteYLow"
	replacer3="siteXHi"
	replacer4="siteYHi"
	flipX=0
	flipY=0
	if(bmb==1):
		flipX=sitePointX*2
		flipY=sitePointY*2
		replacer1="site2XLow"
		replacer2="site2YLow"
		replacer3="site2XHi"
		replacer4="site2YHi"


		cv1=last.replace(replacer1,str(sitePointX-flipX))
		cv2=cv1.replace(replacer2,str(sitePointY))
		cv4=cv2.replace(replacer3,str(sitePointX+448-flipX))
		last=cv4.replace(replacer4,str(sitePointY+544))
	else:
		bv1=sites.replace(replacer1,str(sitePointX-flipX))
		bv2=bv1.replace(replacer2,str(sitePointY))
		bv4=bv2.replace(replacer3,str(sitePointX+448-flipX))
		last=bv4.replace(replacer4,str(sitePointY+544))

finalFile.write(last+"\n")

end=fileEnd.read()
finalFile.write(end+"\n")



fileStart.close()
fileMap.close()
fileBounds.close()
filePlayers.close()
fileBombsites.close()
fileEnd.close()
finalFile.close()

if(whichpath==0):
	os.system("C:")
	os.chdir('C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/bin')
	os.system("vbsp.exe -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.vmf\"")
	os.system("vvis.exe -fast -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.bsp\"")
	os.system("vrad.exe -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.bsp\"")
	os.system("copy \"E:\/rng csg active\RNG Level Creator\\de_random_map.bsp\" "+compilepath0+"csgo\\maps")
	os.system("del /P "+compilepath0+"csgo\\maps\\de_random_map.nav")
else:
	os.system("E:")
	os.chdir(r'E:\Gayms\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\bin')
	os.system("vbsp.exe -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.vmf\"")
	os.system("vvis.exe -fast -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.bsp\"")
	os.system("vrad.exe -game ..\\csgo \"E:/rng csg active/RNG Level Creator/de_random_map.bsp\"")
	os.system("copy \"E:\/rng csg active\RNG Level Creator\\de_random_map.bsp\" "+compilepath1+"csgo\\maps")
	os.system("del /P "+compilepath1+"csgo\\maps\\de_random_map.nav")
#subprocess.call(vbsp)
#subprocess.call(vvis)
#subprocess.call(vrad)