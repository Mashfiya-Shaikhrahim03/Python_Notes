# strings =>
# str = '''shaikh'''
# print(len(str))
# print(str)

# concatenation

# str_2 = "hello" + " " + "world"
# print("lenth of string : " , len(str_2))

# indixing
# str = "tony_shark"
# print(str[-1])

# slicing 

# str_2 = "Batman"
# str_3 = "spider_man"
# print(str_3[1 : len(str_3)])
# print(str_2[0 : 2])  # last index is not include as you see


# string functions

# str = "i am learning python"
#str.endsWith("") return true if string ends with substring
# print(str.endswith("on"))

#str.capatilize() => capitalize 1st cahr
# name = str.capitalize()
# print(str)
# print(name)

#str.replace(old,new) => replace all ocurance of old with new
# str = "i am a coder"

# print(str.replace('a' , 'T'))

#str.find(word) => return 1st index of 1st ocurance
# str = " i am a artificial engg."
# print(str.find('g'))


# str.count(word) => counts the occurance of substring in str

# str = "Alice in boderLand"
# print(str.count('a'))

# Name = input("Enter your name : ")
# print("your name length is : " , len(Name))

# str = "i $am fr$m ca$ad$"
# print(str.count('$'))


# Conditional statements
# ligth = "yellow"

# if(ligth == "red") :
#     print("STOP")
# elif(ligth == "yellow") :
#     print("LOOK")
# elif(ligth == "green") :
#     print("GO") 
# else :
#     print("ligth is broken")
#     print("---end of code---")    

# age = 15
# if(age >= 18) :
#     print("we can vote!")
# else :
#     print("cannot VOTE!")    


# marks = int (input("Enter your marks : "))
# print("you entered :" ,  marks)

# if(marks >= 90) :
#     grade = "A"
# elif(marks >= 80 and marks < 90) :
#     grade = "B"
# elif(marks >= 70 and marks < 80) :
#     grade = "C"
# else :
#     grade = "D"

# print("Grade of the sudent -> " , grade)            
# print("--- code execude---")

# nesting conditions

# age = 93
# if(age >= 18) :
#     if(age >= 90) :
#         print("cannot drive")
#     else :  
#      print("can drive")
# else :
#     print("cannot drive")

# check whether even or odd

# num = int(input("Enter num : "))

# if( num % 2 == 0 ) :
#     print("even num")
# else :
#     print("odd num")


# find greatest num

# a = int (input("enter 1st num : "))
# b = int (input("enter 2nd num : "))
# c = int (input("enter 3rd num : "))

# if(a >= b and a>= c) :
#     print("greates 1st num" , a)
# elif (b >= c) :
#     print(" greatest 2nd num " , b)    
# else :
#     print("greatest 3rd num " , c)    

# multiple of num

# x = int(input("enter a num : "))

# if(x % 7 == 0) :
#     print("multiple of 7")
# else :
#     print("not multiple of 7")    


a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : "))
c = int(input("enter 3rd number : "))
d = int(input("enter 4th number : "))

if(a >= b and a >= c and a >= d) :
    print("greatest num is 1st -> " , a)
elif(b >= c and b >= d) :
    print("greates num is 2nd -> " , b)    
elif(c >= d) :
    print("greatest num is 3rd -> " , c)
else :
    print("greatest num is 4th ->" , d)        