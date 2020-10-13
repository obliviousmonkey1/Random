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
This example has 4 rooms:
  >  '.' is equivalent to 5ft, most races the character can play can move 30ft on their turn.
  > ' ' or blank is equivalent to stone walls (i.e the areas you cant go).
  > Corridors will be added soon to connect the rooms as well as doors, an exit and loot.
  > Each list that you can see contains the coordinates for that singular room. x = x-axis,
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

At the moment i am not focused on this aspect of the game. However i will talk about my targets for how the enemies act and behave.
