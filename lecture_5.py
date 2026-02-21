# loops -> loops are used to repeat instructions...

# while loops => 

# pQ 
# n = int(input("enter number -> "))
# i = 1 
# while i <= 10 :
#   print(i*n)
#   i += 1

  # pQ

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 12  # 2

# i = 0
# while i < len(nums) :
#     if(nums[i] == x) :
#      print("found idx at " , i)
#     i += 1
# else :
#    print("not found")
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# if 100 in nums :
#   print("foun at idx -> " , nums.index(100))

# else :
#   print("not found")  

# PQ

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(list) :
#    print(list[idx])
#    idx += 1

# continue statement - > terminates execution in the current iteration & continue of the loop with next iterater

# i = 0
# while i <= 10 :
#     if( i == 5) :
#         i += 1
#         continue  # 1 , 2 , 3 , 4 , 6 , 7 , 8 , 9 , 10
#     print(i)
#     i += 1


# Break statement = > used to terminate the loop when enconuted

# i = 1
# while i <= 5 :
#   print(i)
#   if i == 3 :
#     break
#   i += 1
# else :
#   print("END loop")

# i = 1 
# while i <= 10 :
#     if ( i % 2 != 0) :
#         i += 1
#         continue 
#     print(i)
#     i += 1



# for loops -> loops are used for sequential traverse for travelling list , string tuples etc .

# list = [1 , 2 , 3 , 4 , 5]

# for val in list :
#     print(len(val))

# tup = ("ironman" , "spiderman" , "batman" , "Alice" , "stranger")
# for val in tup :
#     print(val)

# name = "starnger_things"

# for char in name :
#     print(char)
# else :
#     print("end loop...")    

# nums = [ 1, 20 , 45 , 67 , 48 , 9 , 20]
# for val in nums :
#     print(val)

# num = [ 1, 20 , 45 , 67 , 48 , 9 , 20]

# x = 45
# idx = 0
# for el in num :
#     if(el == x) :
#         print("found" , idx)
#     idx += 1


# range

# for el in range(100 , 0 , -1) :
#     print(el)

# n = int(input("enter a number -> "))

# for val in range (1 , 11 , 1) :
#     print(val*n)


# sum = 0
# i = 0
# while i <= 5 :
#     sum = sum + i
#     print(sum)
#     i = i + 1

# n = int(input("enter number -> "))
# sum = 0
# for i in range(1 , n+1) :
#     sum = sum + i
# print("total sum -> " , sum)

n = int(input("enter number - >"))

fact = 1

for i in range( 1 , n + 1) :
 fact *=  i
 i+=1
print("factorial -> " , fact)