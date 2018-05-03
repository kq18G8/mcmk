#coding=utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
x=pos.x+2
y=pos.y
z=pos.z
SIZE=20
def house():
    midx=x+SIZE/2
    midy=y+SIZE/2
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
    mc.setBlocks(x+1,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE,z,x+SIZE,midy+3,z,block.GLASS.id)
    mc.setBlocks(x,y+SIZE,z,x+SIZE,y+SIZE,z+SIZE,block.WOOD.id)
    mc.setBlocks(x+1,y-1,z-1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
for xx in range(5):
    house()
    x=pos.x+xx*SIZE
