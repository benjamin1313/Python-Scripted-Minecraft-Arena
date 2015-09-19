#! python2
from mcpi import minecraft
import pygame

'''
BUGS:
1. traps can be used outside of the arena

TODO:
1. add TNT
2. add a way to make walls and pillars
3. make a funktion to check how the arena looks like
4. add option to make the floor generate by it self over time
'''
#connecting to the minevraft server IP in prems
mc = minecraft.Minecraft.create() #to local server on your machine
#mc = minecraft.Minecraft.create("123.456.7.89") #if you wanna join an external server


ArenaPos = (100,0,100) #these are the main cordinates for the arena
           # x  y  z

#loads imagers to display in GUI
cobblestoneIMG = pygame.image.load('pics/cobblestone.png')
iceIMG = pygame.image.load('pics/ice.png')
cobwebIMG = pygame.image.load('pics/web.png')
lavaIMG = pygame.image.load('pics/lava.png')
tntIMG = pygame.image.load('pics/tnt.png')
blankTileIMG = pygame.image.load('pics/blankTile.png') #blanks tiles are plased were there are air blocks
playerTileIMG = pygame.image.load('pics/playerTile.png')

#icons for the menu.
icon1 = pygame.image.load('pics/pitIcon.png')
icon2 = pygame.image.load('pics/iceIcon.png')
icon3 = pygame.image.load('pics/webIcon.png')
icon4 = pygame.image.load('pics/lavaIcon.png')


#minecraft Blocks
air = 0
stone = 1
cobblestone = 4
planks = 5
lava = 11
gravel = 13
cobweb = 30
tnt = 46 # use 0 or 1 to set as active or not
ice = 79

#pygame colors
white = (255,255,255)
gray = (150,150,150)
lightGray = (170,170,170)
black = (0,0,0)

pygame.init()
height = 512 #height of the GUI window
width = 848 #width of the GUI window
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Arena Panel')
fps = pygame.time.Clock()

mc.postToChat("Arena program is now open")

#function for creating and restoring the arena
def create_arena():
    #makes the arena floor
    x = ArenaPos[0]
    y = ArenaPos[1]
    z = ArenaPos[2]
    lenghtX = 0
    lenghtZ = 0
    while lenghtX <= 50:
        mc.setBlock(x,y,z,cobblestone)
        while lenghtZ <= 25:
            mc.setBlock(x,y,z,cobblestone)
            z = z+1
            lenghtZ = lenghtZ + 1
        x = x + 1
        lenghtZ = 0
        z = ArenaPos[2]
        lenghtX = lenghtX + 1

    #makes the arena sides
    x = ArenaPos[0]-1
    y = ArenaPos[1]
    z = ArenaPos[2]-1
    h = 0
    while h <= 5:
        lenghtX = 0
        lenghtZ = 0
        while lenghtX <= 51:
            mc.setBlock(x,y,z,planks)
            x = x + 1
            lenghtX = lenghtX + 1
        while lenghtZ <= 26:
            mc.setBlock(x,y,z,planks)
            z = z + 1
            lenghtZ = lenghtZ + 1
        lenghtX = 0
        lenghtZ = 0
        while lenghtX <= 51:
            mc.setBlock(x,y,z,planks)
            x = x - 1
            lenghtX = lenghtX + 1
        while lenghtZ <= 27:
            mc.setBlock(x,y,z,planks)
            z = z - 1
            lenghtZ = lenghtZ + 1
        x = ArenaPos[0]-1
        z = ArenaPos[2]-1
        y = y + 1
        h = h + 1

    #clears the air in the arena
    x = ArenaPos[0]
    y = ArenaPos[1] + 1
    z = ArenaPos[2]
    lenghtX = 0
    lenghtZ = 0
    h = 0
    while h <= 4:
        while lenghtX <= 50:
            mc.setBlock(x,y,z,air)
            while lenghtZ <= 25:
                mc.setBlock(x,y,z,air)
                z = z+1
                lenghtZ = lenghtZ + 1
            x = x + 1
            lenghtZ = 0
            z = ArenaPos[2]
            lenghtX = lenghtX + 1
        lenghtX = 0
        lenghtZ = 0
        x = ArenaPos[0]
        z = ArenaPos[2]
        h = h + 1
        y = y + 1

    #crates the lavapit under the arena
    x = ArenaPos[0]
    y = ArenaPos[1] - 1
    z = ArenaPos[2]
    lenghtX = 0
    lenghtZ = 0
    depthY = 0
    while depthY <= 10:
        while lenghtX <= 50:
            mc.setBlock(x,y,z,air)
            while lenghtZ <= 25:
                mc.setBlock(x,y,z,air)
                z = z+1
                lenghtZ = lenghtZ + 1
            x = x + 1
            lenghtZ = 0
            z = ArenaPos[2]
            lenghtX = lenghtX + 1
        lenghtX = 0
        lenghtZ = 0
        x = ArenaPos[0]
        z = ArenaPos[2]
        depthY = depthY + 1
        y = y - 1

    depthY = 0
    while depthY <= 5:
        lenghtX = 0
        lenghtZ = 0
        x = ArenaPos[0]
        z = ArenaPos[2]
        while lenghtX <= 50:
            mc.setBlock(x,y,z,lava)
            while lenghtZ <= 25:
                mc.setBlock(x,y,z,lava)
                z = z+1
                lenghtZ = lenghtZ + 1
            x = x + 1
            lenghtZ = 0
            z = ArenaPos[2]
            lenghtX = lenghtX + 1
        depthY = depthY + 1
        y = y - 1

    #the walls around the lavapit
    x = ArenaPos[0] - 1
    y = ArenaPos[1] - 1
    z = ArenaPos[2] - 1
    depthY = 0
    while depthY <= 15:
        lenghtX = 0
        lenghtZ = 0
        while lenghtX <= 51:
            mc.setBlock(x,y,z,stone)
            x = x + 1
            lenghtX = lenghtX + 1
        while lenghtZ <= 26:
            mc.setBlock(x,y,z,stone)
            z = z + 1
            lenghtZ = lenghtZ + 1
        lenghtX = 0
        lenghtZ = 0
        while lenghtX <= 51:
            mc.setBlock(x,y,z,stone)
            x = x - 1
            lenghtX = lenghtX + 1
        while lenghtZ <= 27:
            mc.setBlock(x,y,z,stone)
            z = z - 1
            lenghtZ = lenghtZ + 1
        x = ArenaPos[0]-1
        z = ArenaPos[2]-1
        y = y - 1
        depthY = depthY + 1

#function that draws rectangles
def draw_rect(x, y, w, h, c): #x,y position. w,h width and hight. c color
    pygame.draw.rect(gameDisplay, c, [x, y, w, h])

# makes the menu for the GUI interface
def menu(item): #item is the selected menu item
    draw_rect(0, 0, width, 64, gray)

    #marks selected item
    if item == 1:
        draw_rect(10, 0, 64, 64, lightGray)
    elif item == 2:
        draw_rect(84, 0, 64, 64, lightGray)
    elif item == 3:
        draw_rect(158, 0, 64, 64, lightGray)
    elif item == 4:
        draw_rect(232, 0, 64, 64, lightGray)
    elif item == 5:
        draw_rect(306, 0, 64, 64, lightGray)
    elif item == 6:
        draw_rect(380, 0, 64, 64, lightGray)
    elif item == 7:
        draw_rect(454, 0, 64, 64, lightGray)
    elif item == 8:
        draw_rect(528, 0, 64, 64, lightGray)
    elif item == 9:
        draw_rect(602, 0, 64, 64, lightGray)
    
    #draws the icons on the menu
    gameDisplay.blit(icon1, (10,0))
    gameDisplay.blit(icon2, (84,0))
    gameDisplay.blit(icon3, (158,0))
    gameDisplay.blit(icon4, (232,0))

#makes the arena background for the GUI interface
def background():
    x = 16
    y = 80
    lenghtX = 0
    lenghtY = 0
    while lenghtX <= 50:
        gameDisplay.blit(cobblestoneIMG, (x,y))
        while lenghtY <= 25:
            gameDisplay.blit(cobblestoneIMG, (x,y))
            y = y + 16
            lenghtY = lenghtY + 1
        x = x + 16
        lenghtX = lenghtX + 1
        lenghtY = 0
        y = 80

def tileToIngameCod(x,y):
    x = x - 16
    y = y - 80
    codX = x//16
    codY = y//16
    BlockCodX = ArenaPos[0] + codX
    blockCodY = ArenaPos[2] + codY
    return BlockCodX, blockCodY

def ingameToTileCod(x,z):
    blockX = x - ArenaPos[0]
    blockZ = z - ArenaPos[2]
    screenX = blockX*16+16
    screenY = blockZ*16+80
    return screenX, screenY

def removeIfTileExist(tile):
    if tile in blackTiles:
        blackTiles.remove(tile)
    if tile in iceTiles:
        iceTiles.remove(tile)
    if tile in lavaTiles:
        lavaTiles.remove(tile)

blackTiles=[]
def addBlackTile(x,y):
    x = x - 16
    y = y - 80
    X = x//16
    Y = y//16
    tileCodX = X * 16 + 16
    tileCodY = Y * 16 + 80
    tileCods = (tileCodX,tileCodY)
    removeIfTileExist(tileCods)
    blackTiles.append(tileCods)

iceTiles = []
def addIcePad(x,y,z):
    mc.setBlock(x,y,z, ice)
    tileX, tileY = ingameToTileCod(x,z)
    tileCods = (tileX, tileY)
    removeIfTileExist(tileCods)
    iceTiles.append(tileCods)
    blackTiles.append(tileCods)

webTiles = []
def addCobweb(x,y,z):
    mc.setBlock(x,y+1,z, cobweb)
    tileX, tileY = ingameToTileCod(x,z)
    tileCods = (tileX, tileY)
    webTiles.append(tileCods)

lavaTiles = []
def addLava(x,y,z):
    mc.setBlock(x,y,z, lava)
    tileX, tileY = ingameToTileCod(x,z)
    tileCods = (tileX, tileY)
    removeIfTileExist(tileCods)
    lavaTiles.append(tileCods)


def drawBlackTiles():
    for x,y in blackTiles:
        gameDisplay.blit(blankTileIMG, (x,y))

def drawIceTiles():
    for x,y in iceTiles:
        gameDisplay.blit(iceIMG, (x,y))

def drawWebTiles():
    for x,y in webTiles:
        gameDisplay.blit(cobwebIMG, (x,y))

def drawLavaTiles():
    for x,y in lavaTiles:
        gameDisplay.blit(lavaIMG, (x,y))

def resetTiles():
    blackTiles[:] = []
    iceTiles[:] = []
    webTiles[:] = []
    lavaTiles[:] = []

def showPlayers():
    players = mc.getPlayerEntityIds()
    for player in players:
        x,y,z = mc.entity.getPos(player)
        blockX = x - ArenaPos[0]
        blockZ = z - ArenaPos[2]
        screenX = (blockX*16+16)-8 #the -8 is to make the center of the red tile the player posetion
        screenY = (blockZ*16+80)-8
        gameDisplay.blit(playerTileIMG, (screenX,screenY))

def close():
    pygame.quit()
    exit()

def main():
    create_arena()
    menuItem = 1 #selected menu item selected
    trap = "pit" #the trap that is usede when you click with the mouse
    while True:
        gameDisplay.fill(black)
        menu(menuItem)
        background()
        drawBlackTiles()
        drawIceTiles()
        drawLavaTiles()
        drawWebTiles()
        showPlayers()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    close()

                if event.key == pygame.K_1:
                    trap = 'pit'
                    menuItem = 1
                if event.key == pygame.K_2:
                    trap = 'ice'
                    menuItem = 2
                if event.key == pygame.K_3:
                    trap = 'cobweb'
                    menuItem = 3
                if event.key == pygame.K_4:
                    trap = 'lava'
                    menuItem = 4
                if event.key == pygame.K_5:
                    menuItem = 5
                if event.key == pygame.K_6:
                    menuItem = 6
                if event.key == pygame.K_7:
                    menuItem = 7
                if event.key == pygame.K_8:
                    menuItem = 8
                if event.key == pygame.K_9:
                    menuItem = 9

                #rebuilds the arena
                if event.key == pygame.K_r:
                    create_arena()
                    resetTiles()
                    mc.postToChat('The Arena is now rebuild')

                #teleports all players to the arena
                if event.key == pygame.K_t:
                    entityIds = mc.getPlayerEntityIds()
                    for entity in entityIds:
                        mc.entity.setPos(entity,ArenaPos[0]+1,ArenaPos[1]+1,ArenaPos[2]+1)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x,z=tileToIngameCod(pos[0],pos[1])
                y = ArenaPos[1]
                if trap == 'pit':
                    mc.setBlock(x,y,z, gravel)
                    addBlackTile(pos[0],pos[1])
                if trap == 'ice':
                    addIcePad(x,y,z)
                if trap == 'cobweb':
                    addCobweb(x,y,z)
                if trap == 'lava':
                    addLava(x,y,z)




        pygame.display.update()
        fps.tick(60)

main()
