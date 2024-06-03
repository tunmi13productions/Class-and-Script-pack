import inventory as i
inv = i.inventory()
#Let's just make a basic lunch.
inv.give("cookie",5)
inv.give("can of sprite",1)
inv.give("sandwich",1)
def main():
 action = input("Type n for next, p for previous.")
 if action == "n":
  inv.cycle()
  print(f"{inv.itemstring}, {inv.itemamount}, {inv.position+1} of {inv.length}")
 if action == "p":
  inv.cycle(0)
  print(f"{inv.itemstring}, {inv.itemamount}, {inv.position+1} of {inv.length}")
 main()
main()