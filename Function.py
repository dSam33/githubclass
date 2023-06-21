# # #function declaration and function call
# # #function()

# # # Arg return
# # # No     No
# # # yes    No
# # # No 

# # def adding(): # without arguments
# #     print("Hello inside function")


# # adding()


# # def adding(a): # with argument with no return value
# #     print("Hello inside function with argument ", a)

# # adding(5)


# # def adding(a): # with argument with return value
# #     print("Hello inside function with argument ", a)
# #     return a**a
# # val = adding(5)
# # print(val)

# # # predefined variables
# # a=5
# # # b=6
# # # print(f"{a} is less than {b}") # formated print
# # # print("{} is less than {}".format(a,b))
# # # # WAF to show use case of combination of return value and argument.
# # # # there are two type of variables
# # # # * Global
# # # # * Local


# # #WAF to print even numbe between 2 and 50 also perform addition of those even number.
# sum=0
# for i in range(2,51):
   
#     if i%2 ==0:
#         sum += i
# print(sum)

# # #WAF to print odd numbe between 2 and 50 also perform addition of those odd number.
# sum=0
# for i in range(2,51):
#    if i%2 !=0:
#         sum += i
# print(sum)


# #WAF to check if given nuymber is prime or not.

# def check_prime(a):
#     for i in range(2,int(a/2)+1):
#         if a%i==0:
#             return False
#     return True
# if check_prime(11):
#     print("prime")
# else:
#     print("not prime")


# #WAp to give the multiplication table of 5, 10, 17
# num = int(input('Enter the number:'))
# #num =11
# for i in range(1,11):
#     print(num ,'X' ,i, '=' ,num*i)

# # Anup Kafle 
# my_string='This is aws restart program'
# print(my_string[0]) # indexing
# print(my_string[-7])
# print(my_string[4:19])# slicing

# # WAp that prompts the user to enter their name and their favorite color. Then, create a message that combines their name and favorite color to forrm a personalized message.. Finally, print the message on the console
# user_name=str(input("What is your name?"))
# fav_color=str(input("What is you favorite color?"))
# print(f"Hi {user_name}, Your favorite color is {fav_color}")


# #WAP that prompts the user to enter a sentence. Count and display the number of words in the sentence.
# user_set=str(input("Write a sentence"))
# splitted_word = user_set.split(" ")
# print(len(splitted_word))

# #WAP that prompts the user to enter their fuill name( full name and last name) convert the name to uppsercase and display it in reverse order with a comma separating the last name and the first name.
# full_name= str(input("Enter your full name"))
# f_name,l_name=full_name.split(" ")
# upp_fname=f_name.upper()
# upp_lname=l_name.upper()
# #upper_fname = f_name.upper
# print(f"{upp_lname}, {upp_fname}")
# print(f"{l_name.upper()}, {f_name.upper()}")

# #WAP that take a sentence as input and replaces all occurances of specific word with another word.Prompt the user to enter the original sentence. The word to be replace and and replacement word
# sentence=str(input("Enter the sentence"))
# replace=str(input("What do you want to replace?"))
# replacement=str(input("What do you want to replace with?"))
# replaced=sentence.replace(replace,replacement)
# print(replaced)

# list
#
#fruits_list=[]
# tuple

# my_tuple =(99,12,1,2,3,4,5)
# # print(my_tuple[0])
# # count in tuple
# count_1 = my_tuple.count(1)
# print(count_1)
# new_tuple=sorted(my_tuple)
# print(tuple(new_tuple))
#dictinary
# my_dist={
#     "Name":"Surbir",
#     "Age": 16,
#     "Address":{
#         "address1":"Newroad",
#         "zip":1234
#     }
# }

# my_dist["college"]="KMC"
# print(my_dist)
# print(my_dist["Address"]["address1"])
# pop_value=my_dist.pop("Name")
# print(my_dist)
# print(pop_value)
# WAP to show multiplication table of first 20 prime numbers using nested for loop.
# for x in range(5,21):
#         for i in range(2,int(x/2)+1):
#             if x%i==0:
#                  break
#         else:
#             for y in range(1,11):
#                 print(x, "x",y , "=", x*y)
     



# for i in range(1,20):
#    count = 0
#    for x in range(2, (i//2+1)):
#       if(i%x==0):
#          count = count +1
#          break
#     if (count == 0 and i!=1):
#        print("%d" %i, end ='')


# def check_prime(a):
#     for i in range(2,int(a/2)+1):
#         if a%i==0:
#             return False
#     return i
# if check_prime(11):
#     print("prime")
# else:
#     print("not prime")

# list=[]
# for j in range(20,30):
#      prime=1
#      for i in range(2,j):
#           if j%i==0:
#                prime=0
#                break
#      if prime==1:
#         list.append(j)
# print(list)

#Wap to find the simpel interest
# principal=int(input("Enter the principal amount "))
# rate=float(input("Enter the rate %"))
# time=float(input("Enter the time in year"))
# Interest= (principal*time*rate)/100
# print(f"the interest is: {Interest}")

#WAP to find the peremiter of a rectangular body

#WAP to find the volume of irregular body.
#WAP to calculate volume of cube.
#WAP to find square root of a number.
# WAP to find the error % 


# WAP to find area of the circle with radius 7.5, 8.97, 20.39,100, 129, 139,600, 1000, 5.6, 8.9, 12.7
#11.12,12.13

# radius =[7.5, 8.97, 20.39,100, 129, 139,600, 1000, 5.6, 8.9, 12.7,11.12,12.13]
# pie=3.14
# for i in range(len(radius)):
#     print(f" The area of the circle with radius {radius[i]} is {pie*radius[i]**2}")
#radius =[7.5, 8.97, 20.39,100, 129, 139,600, 1000, 5.6, 8.9, 12.7,11.12,12.13]
# pie=3.14
# for i in (7.5, 8.97, 20.39,100, 129, 139,600, 1000, 5.6, 8.9, 12.7,11.12,12.13):
#     print(f" The area of the circle with radius {i} is {3.14*i**2}")

# radius =[7.5, 8.97, 20.39,100, 129, 139,600, 1000, 5.6, 8.9, 12.7,11.12,12.13]
# pie=3.14
# for i in radius:
#     print(f" The area of the circle with radius {i} is {pie*i**2}")

# deep Copy
# lis_a=[1,2,3,4,5]
# lis_b=lis_a
# lis_b[0]="ram"
# print("list b",lis_b)
# print('list a', lis_a)
# import copy
# lis_a=[1,2,3,4,5]
# lis_b=copy.deepcopy(lis_a)
# lis_b[0]="ram"
# print("list b",lis_b)
# print('list a', lis_a)


# from copy import deepcopy
# lis_a=[1,2,3,4,5]
# lis_b=deepcopy(lis_a)
# lis_b[0]="ram"
# print("list b",lis_b)
# print('list a', lis_a)


# t_list=(1,2,3,4,5,6)
# for j,i in enumerate(t_list):
#     print(j,i)
# print(j,i)



# list=[1,2,3,4,5,1,2,3,4,5]
# print(list)
# print(set(list))
# list comprihension

a=[[1+a[i][j] for j in range(3)] for i in range(0,3)]

list=[2,3,4,5,6]
a=(x**2 for x in list)
print(a)
a=[]
for x in list:
    a.append(x**2)
print(a)