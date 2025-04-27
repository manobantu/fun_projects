

name = input("Name your character: ")
print("Hello", name, "to this adventure!")

answer = input("Your on a dirty road, it has come to an end and you can go right or left. What do you choose? ").lower()

if answer =="left":
    answer = input("you come to a river, you can walk around it or swim across. Type 'walk' to work around it and 'swim' to swim across ")

    if answer == "use bridge":
        print("You walked walk for many kilometers, ran out of food and died")

    elif answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come across a bridge, it looks unstable, do you cross or turn back? (cross/back) ")
    if answer == "back":
        print("You go back and come across a troll and it kills you")

    elif answer == "cross":
        answer = input("You cross the bridge and come across a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            answer = input("You talk to the stranger and he hands you a bag. Do you accept(yes/no)")

            if answer == "no":
                print("You reject the bag and leave. Only to come across a pack of wolves and they kill you")

            elif answer == "yes":
                print()
            
            else:
                print()
        

        elif answer == "no":
            print()

        else:
            print("Invalid option. You lose.")     
    
    else:
        print("Not a valid option. You lose.")
    

else:
    print("Not a valid option. You lose")    
