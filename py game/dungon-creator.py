import random 

CHARACTER_TILES = {'stone': ' ',
                   'floor': '.',
                   'wall': '#'}

numb_rooms = 15
min_room_xy = 5
max_room_xy = 10
width = 64
height = 64
room_list = []
level = []

def room(min_room_xy, max_room_xy, width, height):
    x, y, w, h = 0, 0, 0, 0

    w = random.randint(min_room_xy, max_room_xy)
    h = random.randint(min_room_xy, max_room_xy)
    x = random.randint(1, (width - w - 1))
    y = random.randint(1, (height - h - 1))
    #       0, 1, 2, 3
    return [x, y, w, h]



for i in range(numb_rooms):
    room_list.append(room(min_room_xy, max_room_xy, width, height))
   


for i in range(height+1):
        level.append(CHARACTER_TILES['stone'] * width)


############################################# Grid Layout ##############################################

#Appends rooms to the level
for i in (room_list):
    for c in range(i[3]):
            level[i[1]] = level[i[1]][0:i[0]] + (CHARACTER_TILES['floor'] * i[2]) + level[i[1]][i[0]+i[2]: -1]
            i[1]+=1


######################################################################################################## 

# Before 
a = 0
for i in range(height):
    print(level[i], f'{a}')
    a+=1

#################################### Checks if tiles missing from grid #################################

for i in range(len(room_list)):
    for x in range(height):
            if len(level[x]) < width:
                
                add_walls = width - len(level[x])
            if room_list[i][0]:
                add_walls = width - len(level[x])
                
                level[x] = level[x] + (CHARACTER_TILES['stone'] * add_walls)
                
######################################################################################################## 

# after 
print('List of rooms, {x, y, w, h}',room_list)
a = 0
for i in range(height):
    print(level[i], f'{a}')
    a+=1
