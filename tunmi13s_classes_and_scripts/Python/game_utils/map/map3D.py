#map3D, tunmi13
#A basic low-end map class for constructing 3D maps with an x, y and z axis, with x being left to right in length, y being back to front in width, and z being bottom to top in height.
#This class does not hold any sort of rawdata / parsing functions, or any additional sound or TTS functions. You are in control of that.
class map3D:
 def __init__(self,*args,**kwargs):
  """Initializes the classes with default parameters, the parameters are as follows.
   min_x (int): The left edge of your map. Default is 0, which means you cannot go past 0.
   max_x (int): The right edge of your map. Default is 50, which means you cannot go past 50.
   min_y (int): The back edge of your map. Default is 0, which means you cannot go past 0.
   max_y (int): The front edge of your map. Default is 50, which means you cannot go past 50.
   min_z (int): The bottom edge of your map. Default is 0, which means you cannot go past 0.
   max_z (int): The top edge of your map. Default is 50, which means you cannot go past 50.
   default_surface(str): A string containing the name of the surface you are going to use, such as grass, concrete, gravel, etc. By default this is blank, so no surface will exist on your map, and the list of surfaces will remain blank until you decide to add one.
  """
  self.min_x = kwargs.get("min_x",0)
  self.min_y = kwargs.get("min_y",0)
  self.min_z = kwargs.get("min_z",0)
  self.max_x = kwargs.get("max_x",50)
  self.max_y = kwargs.get("max_y",50)
  self.max_z = kwargs.get("max_z",50)
  #Class list. These are in separate classes.
  self.surfaces = [] #List of surfaces.
  self.zones = [] #List of zones. Zones signify areas of importance on a map.
  #Check if a surface has been specified.
  if "default_surface" in kwargs:
   #If it exists, append it to the list of surfaces.
   sf = ""
   kwargs.get("default_surface",sf)
   #This surface has been placed on the bottom of the map.
   self.surfaces.append(surface(self.min_x,self.max_x,self.min_y,self.max_y,self.min_z,self.min_z,sf))
 def add_surface(self,min_x,max_x,min_y,max_y,min_z,max_z,name):
  """Creates a surface on your map.
  Properties
   min_x (int): The left edge of the surface.
   max_x (int): The right edge of the surface.
   min_y (int): The back edge of the surface.
   max_y (int): The front edge of the surface.
   min_z (int): The bottom edge of the surface.
   max_z (int): The top edge of the surface.
   name (str): The name of the surface, such as concrete.
  Consider this the shortcut to creating a surface."""
  self.surfaces.append(surface(min_x,max_x,min_y,max_y,min_z,max_z,name))
 def get_surface(self,x,y,z):
  """If you are planning to use step sounds, or you just want to get the name of the surface in an area, use this function.
  Properties
   x (int): The x coordinate you would like to retrieve the surface name from.
   y (int): The y coordinate you would like to retrieve the surface name from.
   z (int): The z coordinate you would like to retrieve the surface name from.
  Returns
   A string containing the name of the surface, or a blank string on failure."""
  sfname = ""
  #To retrieve the platform as quickly as possible, especially if using a map with several surfaces, it's best to go backward.
  for i in reversed(self.surfaces):
   if x < i.min_x: continue
   if y < i.min_y: continue
   if z < i.min_z: continue
   if i.min_x <=x and i.max_x >= x and i.min_y <= y and i.max_y >= y and i.min_z <= z and i.max_z >= z: sfname = i.name
  return sfname
 def add_zone(self,min_x,max_x,min_y,max_y,min_z,max_z,text):
  """Creates an area of text on your map to signify an important area, such as outside a house or inside a house. You could create something to get the zone in the user's current area, as that is not provided here.
  Properties
   min_x (int): The left edge of the zone.
   max_x (int): The right edge of the zone.
   min_y (int): The back edge of the zone.
   max_y (int): The front edge of the zone.
   min_z (int): The bottom edge of the zone.
   max_z (int): The top edge of the zone.
   text (str): The text of the zone, such as my car, my house, etc.
  Consider this the shortcut to creating a zone."""
  self.zones.append(zone(min_x,max_x,min_y,max_y,min_z,max_z,text))
#Classes for map2D class.
class surface:
 def __init__(self,min_x,max_x,min_y,max_y,min_z,max_z,name):
  self.min_x = min_x
  self.max_x = max_x
  self.min_y = min_y
  self.max_y = max_y
  self.min_z = min_z
  self.max_z = max_z
  self.name = name

class zone:
 def __init__(self,min_x,max_x,min_y,max_y,min_z,max_z,text):
  self.min_x = min_x
  self.max_x = max_x
  self.min_y = min_y
  self.max_y = max_y
  self.min_z = min_z
  self.max_z = max_z
  self.text = text
