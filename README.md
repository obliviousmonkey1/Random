# Python game 
A adventure dungeon crawling loot game.
dungeon contains many floors(levels) within those levels are a serious of conected rooms, 1 space is equivalent to 5ft: 


Parameters for a dungeon room:
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 5
MAX_ROOMS = depends avarage 15

Dungeons(rooms)
> Contain an exit door
> enemys(turnbased)
> loot, chests, ect 

Objects Table:
```
> ' # ' wall 
> " ' " door
> ' . ' floor
> ' $ ' chest 
> ' ! ' enemy
> ' / ' exit door
> '   ' stone
```


#################### WHAT ROOM COULD LOOK LIKE ####################
```
 This example has 4 rooms
 
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
                                                                
