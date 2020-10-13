# RPG Roguelike game
An adventure, dungeon crawling loot game!
. A single dungeon will contain many floors(levels), within those levels will be serious of rooms connected by corridors. 

## Dungeon levels:

**Dungeons(rooms)**
``` 
> Contain an exit door
> enemys(turnbased)
> loot, chests, ect 
```

**Objects Table:**
```
> ' # ' wall 
> " ' " door
> ' . ' floor
> ' $ ' chest 
> ' ! ' enemy
> ' / ' exit door
> '   ' stone
```


#################### WHAT A LEVEL LOOKS LIKE AT THE MOMENT ####################
```
This example level has 4 rooms:
  >  '.' is equivalent to 5ft, most races the player can choose can move up to 30ft on their turn.
  > ' ' or blank is equivalent to stone walls (i.e the areas you cant go).
  > Corridors will be added soon to connect the rooms. As well as doors, an exit and loot.
  > Each list that you can see contains the coordinates for that singular room: x = x-axis, 
    y = y-axis, w = width and h = height.

The Variables for this room:
 > numb_rooms = 4
 > min_room_xy = 5
 > max_room_xy = 10
 > width = 64
 > height = 64
 > room_list = []
 > level = []
 > wall_front = 0
 > wall_end = 0

  x   y   w  h    x   y   w  h     x   y   w  h    x  y   w  h
[[22, 16, 7, 6], [51, 22, 7, 10], [53, 42, 8, 9], [3, 60, 7, 9]]
                                                                 0
                                                                 1
                                                                 2
                                                                 3
                                                                 4
                                                                 5
                                                                 6
                                                                 7
                                                                 8
                                                                 9
                                                                 10
                      #.......#                                  11
                      #.......#                                  12
                      #....................................#     13
                      #....................................#     14
                      #....................................#     15
                      #....................................#     16
                      #....................................#     17
                      #....................................#     18
                      #....................................#     19
                      #....................................#     20
                      #....................................#     21
                      #....................................#     22
                                                                 23
                                                                 24
                                                                 25
                                                                 26
                                                                 27
                                                                 28
                                                                 29
                                                                 30
                                                                 31
                                                                 32
                                                                 33
                                                     #........#  34
                                                     #........#  35
                                                     #........#  36
                                                     #........#  37
                                                     #........#  38
                                                     #........#  39
                                                     #........#  40
                                                     #........#  41
                                                     #........#  42
                                                                 43
                                                                 44
                                                                 45
                                                                 46
                                                                 47
                                                                 48
                                                                 49
                                                                 50
                                                                 51
   #.......#                                                     52
   #.......#                                                     53
   #.......#                                                     54
   #.......#                                                     55
   #.......#                                                     56
   #.......#                                                     57
   #.......#                                                     58
   #.......#                                                     59
   #.......#                                                     60
                                                                 61
                                                                 62
                                                                 63
                                                                 64
```                                                                 

## Enemies

At the moment I am not focused on this aspect of the game. However I will talk about my targets for how I want the enemies act and behave.
```
 > Enemies will have a FOV (Field Of View), Each enemy type(race) will have a diffrent one. Factors that will effect base FOV:
   > Race
   > Class (i.e, Warrior or Wizard)
   > Height 
   > Wisdom 
   
   There are also environmental factors to take into consideration:
   > How dark or light an area is (If their are tourches in a room or you are holding one then you will be easier to spot, but so are your enemies).
   > If anything is obscuring their view or if something is obscuring the players character. 
   
   My plan at the moment is as it is turn based even out of combat (for now). Each enemey will have a set of data telling them what they know about the area.
   If you get into an enemies FOV, (Their FOV will be shown on the screen at all times), Then the enemey will note the positon that you are in depending if
   its fellow allies are in a certain radius to them it will give them that coord and they will go and search the area as well. using A* pathfinding it will traverse that 
   position and explore around it if the player character has disapered. The enemy will stay in an ALERTED state for a while and then return back to its NORMAL state. If the 
   enemey can still see the player character then they will try and pathfind to the player and attack it. 
   
 > I plan on increasing the enemies diffculty. One: based on how much data they can hold and store about the world, what it can do, and the player character. Two increase the      size of the states availble to it.
```
