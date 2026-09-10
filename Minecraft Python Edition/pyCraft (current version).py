from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor, abs
import time
from ursina.audio import Audio
from ursina import duplicate
import cProfile

#the game is more like a horror game, its more like the days of minecraft 1.7.2
#you can build you have caves etc. but there is new mobs and its more like survival horror game.
    
app = Ursina()
buildmode=0
# Window
window.title = "Cave Game"
window.borderless = False
window.color = color.black
window.exit_button.visible = 0
window.entity_counter.visible = 0
window.collider_counter.visible = 0
window.fps_counter.enabled = 1
window.fullscreen = 0
window.vsync = 1

preTime = time.time()
# Fog
scene.fog_color = color.black
scene.fog_density = 0.25

# blocks
class BlockSelect:
    grass= 'Grass_Block_TEX.png'
    wood= 'oak-plank.png'

blockType=None

# Models and Entities
steveModel = 'minecraft_steve.obj'
bte = Entity(model='cube',texture='2.png')

def first_(): #hand
    hand = Entity(
        model='quad', 
        texture='hand.png', 
        parent=camera.ui
    )
    hand.position = Vec2(0.5, -0.4)
    hand.scale = 0.4


def BuildingTool():
    bte.position = round(player.position + camera.forward *3 )
    bte.y +=2
    bte.y =round (bte.y)
    bte.z =round (bte.z)
    bte.x =round (bte.x)

def build(block_type):
    e = duplicate(bte)
    e.collider = 'cube'
    e.texture = block_type
    e.shake(duration=0.3,speed=0.01)

#guy = Entity(model=steveModel, scale=0.1, x=22, z=20, y=3,
             #texture='guy skin.png', double_sided=True)

#girl = Entity(model=steveModel, scale=0.1, x=22, z=16, y=1.1,
    #          texture='girl skin.png', double_sided=True)
def update(): 
    global preX, preZ, preTime, shake_start_time, shake_intensity
    
    if abs(player.z - preZ) > 1 or abs(player.x - preX) > 1:
        generate_shell()
    if time.time() - preTime > 0.5:
        generate_subsets()
        # saftey 
    if player.y < -amp+1:
        player.y = player.height + floor((noise([player.x / freq, player.z / freq])) * amp) + 1
        player.land()

    if buildmode==1:
        BuildingTool()
    elif buildmode==0:
        bte.x = 1000*35

    #mobs #function to look at player
    #guy.look_at(player,'forward') 
    #guy.rotation_x = 0
# Terrain  
terrain = Entity(model=None, collider=None)
subsets_array = []
subcubes = []
terrainWidth = 24  # Adjust width for simplicity
subwidth = terrainWidth
sci = 0
current_subset = 0
# Instantiate our ghost subset cubes
for i in range(subwidth):
    block = Entity(model='cube')
    subcubes.append(block)

# Instantiate our empty subsets
# Ensure the number of subsets is enough for the terrain
num_subsets = (terrainWidth * terrainWidth) // subwidth
for i in range(num_subsets):
    block = Entity(model='cube', color=color.green)  # Assign a simple model to each subset
    block.parent = terrain
    subsets_array.append(block)

def generate_subsets():
    global sci, current_subset, freq, amp
    if current_subset >= len(subsets_array): 
        finish_terrain()
        return
    
    
    for i in range(subwidth):
        x = subcubes[i].x = floor((i % terrainWidth) + sci) 
        z = subcubes[i].z = floor((i // terrainWidth) + sci)
        y = subcubes[i].y = floor((noise([x / freq, z / freq])) * amp)
        
        subcubes[i].parent = subsets_array[current_subset]  # Proper parenting

        subcubes[i].color = color.black
        subcubes[i].visible= 0
    sci += subwidth
    current_subset += 1
# Noise setup
noise = PerlinNoise(octaves=3, seed=2021)
amp = 24  # Elevation (height)
freq = 100  # Frequency (detail)

# Rendering grid - a smaller grid of blocks will be rendered dynamically
render = []
render_width = 24

for i in range(render_width * render_width):  # Pool of blocks for rendering

    block = Entity(model='cube', collider='box', texture='Grass_Block_TEX.png')
    block.visible = 0  # Initially invisible
    render.append(block)

def generate_shell():# Function to generate the terrain around the player
    global render_width, amp, freq
    render_distance = 32  # Blocks around the player to render
    
    for i in range(len(render)):
        x = render[i].x = floor((i % render_width) + player.x - 0.5 * render_width)
        z = render[i].z = floor((i // render_width) + player.z - 0.5 * render_width)

        if abs(x - player.x) > render_distance or abs(z - player.z) > render_distance:
            render[i].visible = 1  # Hide blocks too far from the player
        else:
            render[i].y = floor(noise([x / freq, z / freq]) * amp)
            render[i].visible = 1  # Show blocks close to the player

#Player and camera and sky
skybox_image = load_texture("sky.png")
Sky(texture=skybox_image)
player = FirstPersonController()
player.position = (5, 12, 5)
player.cursor.visible = 1
player.cursor.color = color.white
player.cursor.texture='co.png'
player.cursor.rotation = 0
#player.cursor.scale = 0.1
player.y = 12
player.gravity = 0.5
player.speed = 5
camera.fov = 120
camera.mouse_sensitivity = Vec2(100, 100)
player.fall_after = .35
player.jump_height = 1.5
preX = player.x
preZ = player.z

#sounds

# Finish rendering
def finish_terrain():
    for i, subset in enumerate(subsets_array):
        if subset.model is None:
            return  
    # Combine terrain chunks (make it all one mesh for performance)
    terrain.combine()
def input(key):
    global blockType,buildmode
    if key=='q':
        quit()
    if key=='w':
        pass
        #Audio('Footsteps Grass Sound Effect.mp3', loop=1, autoplay=True)

    if key=='shift': #run
        if player.speed ==7:
            player.speed =5
            camera.fov = 120

        elif player.speed ==5:
            player.speed =7
            camera.shake(duration=1,speed=1)
            camera.fov = 121
            
    if key=='control': #sneak
        if player.speed ==5:
            player.speed =3
        elif player.speed ==7:
            player.speed =3
        elif player.speed ==3:
            player.speed =5
            
    if key=='1': #block selection
        blockType = BlockSelect.grass
    elif key=='2':
        blockType = BlockSelect.wood

    if key=='right mouse up':# place block
        if blockType == None:
            print("( * ) ---> + no block selected!")
        else:
            build(blockType)
    if key=='left mouse up':# break
        e = mouse.hovered_entity # if there was a block
        destroy(e)
    if key=='b':
        if buildmode==1:
            buildmode=0
        elif buildmode ==0:
            buildmode =1  

first_()
generate_shell()
app.run()