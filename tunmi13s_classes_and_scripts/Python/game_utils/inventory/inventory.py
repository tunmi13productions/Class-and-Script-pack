#A simple inventory class.
class inventory:
 #Constructor
 def __init__(self):
  #The list holding the items.
  self.items = []
  #The position in the items list.
  self.position = -1

 #Management functions and properties.
 #We can use this to quickly get the size of the inventory without having to continuously use len(self.items)-1. The reason we have to use -1 is that the index will be out of range if we use the actual length.
 @property
 def size(self):
  return len(self.items)-1
 #Gets the actual size of the inventory item list, without using -1.
 @property
 def length(self):
  return len(self.items)

 #Returns the item (str) under the position.
 @property
 def itemstring(self):
  if self.position < 0 or self.position > self.size: return ""
  else: return self.items[self.position].name

 #Returns the amount of an item (int) under the position.
 @property
 def itemamount(self):
  if self.position < 0 or self.position > self.size: return ""
  else: return self.items[self.position].amount

 #Check if an item exists by searching its name (str) and getting its index (or position) (int) in the list.
 def get_item_index(self,name):
  for i in range(0,self.length):
   if self.items[i].name == name: return i
  return -1

 #For those who prefer handles. Check if an item exists by searching its name (str) and getting the class directly.
 def get_item(self,name):
  for i in self.items:
   if i.name == name: return i
  return None

 #This function outputs the inventory in an INI format, which can then be read, copied, pasted, etc etc.
 @property
 def to_ini(self):
  if self.size <= 0: return ""
  else:
   liststring = ""
   for i in range(0,self.length):
    if i == self.size: liststring += f"{self.items[i].name}={self.items[i].amount}"
    else: liststring += f"{self.items[i].name}={self.items[i].amount}\n"
   return liststring

 #Edit Functions
 #Takes an INI string (liststring) and imports it as an inventory.
 def from_ini(self,liststring,reset = False):
  #Set reset to True if you would like the inventory to rid itself of all items.
  if reset: self.items.clear()
  #First, split the string into lines, which can be cycled through.
  lines = liststring.split("\n")
  #Loop through the lines.
  for i in range(0,len(lines)):
   #Use the = (equals sign) as the delimiter, by splitting things between each sign.
   listing = lines[i].split("=")
   #Check if the item is valid before parsing it. No more or less than 2.
   if len(listing) == 2:
    #Prepare our variables. Keep in mind that lists start from 0. This means if you have 4 items, it is 0, 1, 2, 3.
    name = listing[0]
    #To play it safe, make the variable an int instead of str.
    amount = int(listing[1])
    #Also to play it safe, we will just skip this item if the amount is less than or equal to 0.
    if amount <= 0: continue
    #Check if the item exists.
    index = self.get_item_index(name)
    if index > -1:
     #It does, so just add the amount.
     self.items[index].amount += amount
    else:
     #Create a new item and append it to the list of items.
     self.items.append(inventory_item(name,amount))

 #Finally, the functions you've been waiting for! You must be thinking, about time! As these functions are mostly self explanatory, the comments have been reduced to occasional ones, and mostly doc strings are used.
 def cycle(self,direction = 1):
  """Cycles through the inventory.
  Parameters:
   direction (int): The direction that you want to cycle in. 1 is forward, 0 is backward.
  """
  if direction == 1:
   if self.position >= self.size: self.position = 0
   else: self.position += 1
  if direction == 0:
   if self.position <= 0: self.position = self.size
   else: self.position -= 1
 def give(self,name,amount):
  """Adds or removes an item in the inventory, depending on how it is used.
  Parameters:
   name (str): The name of the item.
   amount (int): The amount you would like to give. Using negative values will subtract from the existing item, and if it is at or below 0 the item will be removed completely.
   Returns: True if the item was added or removed, False otherwise.
  """
  if not name or amount == 0: return False
  i = self.get_item(name)
  if i:
   i.amount += amount
   if i.amount <= 0: self.items.remove(i)
   return True
  else:
   if amount <= 0: return False
   else: self.items.append(inventory_item(name,amount))
   return True
  return False

#This class is for inventory items. The reason it is a class is because you could add parameters to it. Examples include useable, item type, etc.
class inventory_item:
 def __init__(self,name,amount):
  """Creats an item.
  Parameters:
   name (str): The name of the item.
   amount (int): The amount of the item.
  """
  self.name = name
  self.amount = amount
