import inventory as i
inv = i.inventory()
#Let's just make a basic lunch.
inv.give("cookie",5)
inv.give("can of sprite",1)
inv.give("sandwich",1)
#Print it in INI format.
print(inv.to_ini)
#Completely change the inventory with this. I want breakfast now! Remember \n (backslash n) means a line feed.
new_inv = """pancakes=10
bottle of syrup=1
plate of scrambled eggs=1
plate of bacon=1"""
inv.from_ini(new_inv,True)
#Print the new inventory.
print(inv.to_ini)
#Tired of all these pancakes. Let's get rid of some. We'll save the rest for later, I guess.
inv.give("pancakes",-5)
#Could use some more scrambled eggs though.
inv.give("plate of scrambled eggs",2)
#Print Changes
print(f"Got tired of pancakes but got some more eggs! {inv.to_ini}")
