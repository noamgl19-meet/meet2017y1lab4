#asking the user if it is raining
print("is it rainning? (y/n)")
#getting an input
rain = input()
if str(rain) == "n" or str(rain) == "no":
    print("just walk you lazy")
#checking with the user the train iption
print("when does the next train coming?(in minutes)")
#taking an input of the next train
next_train = input()\
#calculating the best way
if (int(next_train) > 15 and str(rain) == "y" or str(rain) == "yes"):
    print("take a texi")
if (str(rain) == "yes" or str(rain) == "y" and int(next_train) <= 15):
    print("wait for the train")

    
    
    
