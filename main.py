# In computer programming, control flow refers to the exact order in which individual statements
# instructions, or function calls are executed within a program.

# 3 types of control flows or structure

# - sequence
# - selection/conditional
# - Iterations/Repetition

# name1 = "Obinna"
# name2 = "Paul"
# name3 = "John"
# age = 20 
# age2 = 25
# age3 = 30

# print(age3)
# print(age2)
# print(age)
# print(name3)
# print(name2)
# print(name1)

# if, else, elif, 


# name1 = "Obinna"
# name2 = "Paul"
# name3 = "John"
# amount = 5000
# amount2 = 1000
# no_amount = 0

# my_money = int(input("How much do you have:"))

# if my_money >= amount:
#     print("Buy Ozu okuko")
# elif my_money  >= amount2 and my_money < amount:
#     print("Buy ugu make we cook")
# else:
#     print("Nothing to buy")


# Iteration/Repetition

# for loop
# List1 = ["name", "paul", 1, 100, 100]


# for i in List1:
#     print(i)

# while loop 
# i = 0

# while i < 10:
#     print(i)
#     i += 1   

# listofbooks = ["Python", "Java", "C++", "Javascript", "C#"]

# for i in listofbooks:
#     if "c" in i.lower():
#         print(i.lower())
#     else:
#         print(i.upper())        


# listofbooks = ["python", "java", "c++", "javascript", "c#"]

# bookprices = [500, 1000, 1500, 2000, 2500]

# bookinterest = input("what book are you interested in:")


# bookandprices = dict(zip(listofbooks, bookprices))
# # print(bookandprices)

# if bookinterest in listofbooks:
#     amount = int(input("How much do you have: "))
#     if amount >= bookandprices.get(bookinterest):
#         print("you can  make payment")
#     else:  
#         print("Your money is not enough")
# else:
#     print("Book is not available")          


# loop control statements 
# break, continue, pass



# listofnumbers = [1,2,3,4,5,6,7,8,9,10]

# for i in listofnumbers:
#     if i == 6:
#         break
#     print(i)


listofnumbers = list(input("enter your list of names: "))

for i in listofnumbers:
    if i == "m":
        continue
    print(i)

combine if with loops 