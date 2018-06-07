while True:
    time.sleep(0.1)
    
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import randon

mc=minecraft.Minecraft.create()

def placeTreasure():
    global treasure_x,treasure_y,treasure_z
    pos=mc.player.getTilePos()
    treasure_x=random.randint(pos.x,pos.x+RAGE)
    treasure_y=random.randint(pos.y+z,pos.y+RANGE)
    treasure_z=random.randint(pos.z,pos.z+RANGE)
    mc.setBlock(treasure_x,treasure_y,treasure_z block DIAMOND BLOCK.id)

    def homingBeacon():
        global score pos = mc.player.getTilePos()
        b = mc.getBlock(pos.x,pos.y-1,pos.z)
        if treasure_x == None:
            if len(bridge)>o:
                coorinate = bridge

                
