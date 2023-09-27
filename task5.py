#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
item=["food", "water","rope", "torch", "sack", "wood", "iron","steel", "ginger", "garlic", "fish", "stone", "wool"]
itemN=[]
for i in item:
    itemN.append(0)

item1={}
item1=dict(zip(item,itemN))

a=str(input("get or remove or finish : "))
while a!= "finish":
    if a=="get":
        b=str(input("what item : "))
        c=int(input("amount of items : "))
        item1[b]+=c
        a=str(input("get or remove or finish : "))
    elif a=="remove":
        b=str(input("what item : "))
        print("\n")
        print(f"you have ({b} : {item1[b]}) now")
        print("\n")
        c=int(input("amount of items : "))
        item1[b]-=c
        a=str(input("get or remove or finish : "))
print(item1)

"""while item1[b]<c:
            print(f"you cannot remove {c} of {b} item")
            c=int(input("re-enter amount of items or put 0 cancel the removing item: "))
            if c==0:
                break"""