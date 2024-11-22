door1 = True
door2 = False
door3 = False

doors = [door1, door2, door3]

print(f"There are {len(doors)} doors.\n")
choice = int(input("Please Pick a door: "))

opened_door = None
for i in range(len(doors) -1, -1, -1):
    if i + 1 != choice and doors[i] != True:
        opened_door = i + 1
        break #Stops after 1 door

print(opened_door)

