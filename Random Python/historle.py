#data which is event followed by the year
data = ["Paul Devine's birth", 1983]

print (type(data))
#Ask for user input and take the first bit of data from list

print("When did this event occur?")
print(data[0])

guess = int(input())
tries = 5

while guess == True:

    if guess == (data[1]):
        print("That's right")
    if guess < (data[1]):
        print("Too low sorry")
        continue
    else:
        print("Too high")
        continue


#need to tell user if high or low
