import mcpi.block as block
import mcpi.minecraft as iminecraft
mc=minecraft.Minecraft.creat()
pos=mc.player.getTilePos()
x=pos.x+2
y=pos.y
z=pos.z

333 house();
midx=x=SIZE/2
midx=y=SIZE/2
mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIA,Z+SIZE,Block,COBBLESTONE.id)
mc.setBlocks(x+1,y,z+1.,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.Glass.id)
mc.setBlocks(x,y+SIZE,z,x+SIZE,y+SIZE,z+SIZE,block.Wood.id)
mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,block.WOOL.id)
for x in range(5):
    houes()
    x=x+SIZE
    
