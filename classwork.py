#1 if and else

age = int(input("How old are you"))
if age  >= 18:
    print("i am an adult")
else:
    print("i am a minor")    


#2 if, elif and else

numbers = int(input("Enter a number"))
if numbers > 0:
    print("Postive number")
elif numbers < 0:
    print("Negative number")
else:
    print("Zero")


#3 for loop

listofnumbers = [1,2,3,4,5,6,7,8,9,10]

for i in listofnumbers:
    print(i)


#4 while Loop    


listofnumbers = [1,2,3,4,5,6,7,8,9,10]

for i in listofnumbers:
    if i == 6:
        break
    print(i)



#5 Break and Continue
# Break

listofnumbers = [1,2,3,4,5,6,7,8,9,10]

for i in listofnumbers:
    if i == 6:
        break
    print(i)

# continue

listofnumbers = [1,2,3,4,5,6,7,8,9,10]

for i in listofnumbers:
    if i == 6:
        continue
    print(i)

# 6 simple combination

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break
    if number < 0:
        continue

    print("Positive number")