import map2D as md
m = md.map2D(max_x = 10,max_y = 10)
m.add_surface(0,5,0,5,"tile")
m.add_surface(6,10,6,10,"carpet")
print(m.get_surface(3,3))
print(m.get_surface(6,6))
