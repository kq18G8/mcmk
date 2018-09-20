import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for a in range(100):
   mc.setBlock(pos.x+a, pos.y, pos.z,46)
   mc.setBlock(pos.x+a, pos.y, pos.z+9,46)
for a in range(100):
    mc.setBlock(pos.x, pos.y, pos.z+1+a,46)
    mc.setBlock(pos.x+9, pos.y, pos.z+1+a,46)
for y in range(10):
    for a in range(10):
        mc.setBlock(pos.x+a, pos.y+y, pos.z, 46)
        mc.setBlock(pos.x+a, pos.y+y, pos.z+9, 46)
    for a in range(8):
        mc.setBlock(pos.x, pos.y+y, pos.z+1+a, 46)
        mc.setBlock(pos.x+9, pos.y+y, pos.z+1+a, 46)
for x in range(10):
    for z  in range(10):
        mc.setBlock(pos.x+x, pos.y, pos.z+z,46 )
for x in range(10):
    for z  in range(10):
        mc.setBlock(pos.x+x, pos.y+9, pos.z+z, 46)
