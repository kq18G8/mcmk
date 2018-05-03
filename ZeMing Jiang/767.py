import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for a in range(30):
    mc.setBlock(pos.x+a, pos.y, pos.z, block.GLASS.id)
for a in range(30):
    mc.setBlock(pos.x+a, pos.y, pos.z+29, block.GLASS.id)
for a in range(28):
    mc.setBlock(pos.x, pos.y, pos.z+1+a, block.GLASS.id)
for a in range(28):
    mc.setBlock(pos.x+29, pos.y, pos.z+1+a, block.GLASS.id)
for y in range(30):
    for a in range(30):
        mc.setBlock(pos.x+a, pos.y+y, pos.z, block.GLASS.id)
        mc.setBlock(pos.x+a, pos.y+y, pos.z+29, block.GLASS.id)
    for a in range(28):
        mc.setBlock(pos.x, pos.y+y, pos.z+1+a, block.GLASS.id)
        mc.setBlock(pos.x+29, pos.y+y, pos.z+1+a, block.GLASS.id)
for x in range(30):
    for z in range(30):
        mc.setBlock(pos.x+x, pos.y, pos.z+z, block.COBBLESTONE.id)
for x in range(30):
    for z in range(30):
        mc.setBlock(pos.x+x, pos.y+29, pos.z+z, block.WOOL.id)
                
