import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
f=open("mc.txt","r")
nameList=f.readlines()
xCounter=0
for line in nameList:
	digitalList=line.split(",")
	zCounter=0
	for digitalSingle in digitalList:
		if digitalSingle=='1':
			mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,block.DIAMOND_BLOCK.id)
		else:
			mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,block.WOOD.id)
		zCounter+=1
	xCounter+=1
