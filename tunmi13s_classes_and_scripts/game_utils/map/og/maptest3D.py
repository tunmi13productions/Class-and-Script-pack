import map3D as md
m = md.map3D(max_x = 10,max_y = 10,max_z = 10)
m.add_surface(0,10,0,10,0,0,"tile")
m.add_zone(0,10,0,10,0,0,"room")
def surfaces_to_str():
 ret = ""
 for i in m.surfaces: ret+= i.name+". "
 return ret
def zones_to_str():
 ret = ""
 for i in m.zones: ret+= i.text+". "
 return ret
print(f"Platforms: {surfaces_to_str()}")
print(f"Zones: {zones_to_str()}")
