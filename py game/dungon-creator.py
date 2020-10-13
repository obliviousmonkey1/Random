import random 

CHARACTER_TILES = {'stone': ' ',
                   'floor': '.',
                   'wall': '#'}

numb_rooms = 10
min_room_xy = 5
max_room_xy = 10
width = 64
height = 64
room_list = []
level = []
connected = True
wall_front = 0
wall_end = 0

############################################# Room Maker ###############################################

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

########################################################################################################



    
########################################### Dunegon Canvas #############################################

for i in range(height+1):
        level.append(CHARACTER_TILES['stone'] * width)

########################################################################################################




############################################# Grid Layout ##############################################

#Appends rooms to the level
for i in (room_list):
    for c in range((i[3])):
        level[i[1]+1] = level[i[1]][0:i[0]] + (CHARACTER_TILES['floor'] * (i[2])) +  level[i[1]][i[0]+i[2]: -1]
        i[1]+=1


########################################################################################################




############################################# Wall Layout ##############################################
        
for x in range(height):
    try:
        wall_front = [pos for pos, char in enumerate(level[x]) if char == '.'][0]
        wall_end = [pos for pos, char in enumerate(level[x]) if char == '.'][-1]
        #wall_end +=1

        # if you want rooms not to be connected if they are on the same row
        if connected == False:
            level[x] = level[x][0:wall_front] + CHARACTER_TILES['wall'] + level[x][wall_front: wall_end] + CHARACTER_TILES['wall'] + level[x][wall_end+1: -1]
        
        #If you want rooms sharing the same row to be conected
        elif connected == True:
            level[x] = level[x][0:wall_front] + CHARACTER_TILES['wall'] + (CHARACTER_TILES['floor'] *(wall_end - wall_front )) + CHARACTER_TILES['wall'] + level[x][wall_end+1: -1]
        
    except:
        pass

    #print(wall_control_front,wall_control_end)   

########################################################################################################



                                                
############################################### Length #################################################

for i in range(len(room_list)):
    for x in range(height):
            if len(level[x]) < width:
                
                add_walls = width - len(level[x])
                level[x] = level[x] + (CHARACTER_TILES['stone'] * add_walls)
            
                
########################################################################################################                

print('List of rooms: ', room_list)

a = 0
for i in range(height+1):
    print(level[i], f'{a}')
    a+=1
            


