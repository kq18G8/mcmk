import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

f=open("mc.txt",'r')
nameList=f.readlines()
xCounter=0
for line in nameList:
    print(line)
    digitalList=line.split(',')
 #   print(digitalList)
    zCounter=0
    for digitalSingle in digitalList:
      #  print('1')
        if digitalSingle=='1':
            mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,57)
        else:
            mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,46)
        zCounter+=1
    #print('\n')
    xCounter+=1
