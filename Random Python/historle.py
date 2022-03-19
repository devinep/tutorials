#data which is event followed by the year
data = ["Paul Devine's birth", 1983]

#Ask for user input and take the first bit of data from list

print("When did this event occur?")
print(data[0])

guess = input

if guess == (data[1]):
    print("That's right")
elif guess < (data[1]):
    print("Too low sorry")
else:
    print("Too high")


#need to tell user if high or low
