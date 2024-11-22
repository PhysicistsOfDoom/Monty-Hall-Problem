import random
import time

door1 = True
door2 = False
door3 = False

#Make and Shuffle Doors
doors = [door1, door2, door3]
random.shuffle(doors)

#Introduce the doors
print(f"There are {len(doors)} doors.\n")
choice = int(input("Please Pick a door: "))

#Determine Invalid Answer
if choice > len(doors) or choice < 0:
    print(f"Invalid choice. Please choose a door between 1 and {len(doors)}.")
    exit()

#Host Opens a Door
opened_door = None
for i in range(len(doors) -1, -1, -1):
    if i + 1 != choice and doors[i] != True:
        opened_door = i + 1
        break #Stops after 1 door
print(f"The host opens door #{opened_door}, revealing it is empty (False).")

#Offer to switch to remaining door
remaining_door = [i + 1 for i in range(len(doors)) if (i + 1 != choice and i + 1 != opened_door)][0]
offer_choice = input(f"Would you like to switch to door #{remaining_door}? (y/n): ").lower()

#Determine offer choice
if offer_choice == "y":
    choice = remaining_door
    print(f"You have switched to the door #{choice}")
else:
    print(f"You have chosen to stick with door #{choice}\n")

#Count down to reveal door
# time.sleep(2)
# for x in range(3 - 1, -1, -1):
#     print(f"{x + 1}...")
#     time.sleep(1)

if doors[choice - 1] == True:
    print(f"Congratulations, Door #{choice} is TRUE!")
else:
    print(f"Sorry, Door #{choice} is FALSE!")
