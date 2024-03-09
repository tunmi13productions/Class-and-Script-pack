#Testing both 2D and 3D maps.
from map2D import Map2D, Tiles
from map3D import Map3D
#World1 is 2D and world2 is 3D.
world1 = Map2D(11, 11)
world2 = Map3D(11, 11, 11)
#Fill the bottom left of world1 wiht carpet.
world1.fill_range(0, 5, 0, 5, Tiles.carpet)
#Fill the bottom left of world2 wiht carpet.
world2.fill_range(0, 5, 0, 5, 0, 0, Tiles.carpet)
#Print the tiles of both. We will use 3 3 as the example point. Notice that there is .name. This is the bring out the string of it. If it weren't there, it would just print Tiles.carpet.
print(f"Round 1. World1 has {world1.get_tile(3, 3).name}, and world2 has {world2.get_tile(3, 3, 0).name}.")
#Now let's break the carpet in both. We'll use air.
world1.set_tile(3, 3, Tiles.air)
world2.set_tile(3, 3, 0, Tiles.air)
#Now, reprint.
print(f"Round 2. World1 has {world1.get_tile(3, 3).name}, and world2 has {world2.get_tile(3, 3, 0).name}.")