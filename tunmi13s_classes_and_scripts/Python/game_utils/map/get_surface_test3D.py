import map3D as md
m = md.map3D(max_x = 10,max_y = 10,max_z = 10)
m.add_surface(0,5,0,5,0,0,"tile")
m.add_surface(6,10,6,10,0,0,"carpet")
m.add_surface(0,5,0,5,5,5,"wood")
m.add_surface(6,10,6,10,5,5,"marble")
print(f"On floor 1, {m.get_surface(3,3,0)}, and {m.get_surface(6,6,0)}.")
print(f"On floor 2, {m.get_surface(3,3,5)}, and {m.get_surface(6,6,5)}.")
