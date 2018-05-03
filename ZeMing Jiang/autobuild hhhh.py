import mcpi.minecraft as minecraft
import mcpi.block as block 
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y"+str(pos.y)+" z="+str(pos.z))
x=pos.x+2
y=pos.y
z=pos.z

SIZE=60

def rua():
    print("hey")
    mc.postToChat("Silly B")
    midx=x+SIZE/2
    midy=y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.TNT.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS_PANE.id)
    mc.setBlocks(midx+1,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS_PANE.id)
    mc.setBlocks(x,y+SIZE,z,x+SIZE,y+SIZE,z+SIZE,block.LAVA.id)
    mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WATER.id)

for xx in range(10000):
    rua()
    x=pos.x+xx*SIZE+20




