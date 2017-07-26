print("how fast did you go?(in numbers[carmi])")
speed = input()
print("is it your birthday? (y/n)")
bd = input()
if bd == "y":
    speed = int(speed) - 5
if int(speed) < 31 :
    print("no ticket")
elif int(speed) > 30 & speed < 51:
    print("small ticket")
elif int(speed) > 50:
    print("big ticked! you don't know how to drive")
