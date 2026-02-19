# ---LISTS---
# declaration of list

# marks = [87 , 34 , 56 , 78 , 45]
# print(marks[0] ) 
# print(marks[2])
# print(marks)
# print(len(marks))
# print(type(marks))

# student = ["Karan" , 87 , "mumbai" , 20]
# print(student)

# slicing in list
# marks = [87, 45, 60, 30, 50]
# print(marks[0 : ]) 
# print(marks[ : 4 ]) # lst idx not included

# list methods

# list = [23, 45, 32, 90, 59]
#append -> adds one element at the end
# print(list)
# list.append(10)
# print(list)

# sorting -> ascending order
# list.sort()
# print("ASCENDING ORDER -> ", list)
# # sorting in descending order -> list.sort(reverse=True)
# list.sort(reverse=True)
# print("DESCNDIG ODER -> " , list)

# reverse a string

# list.reverse()
# print(list)

# remove 1st ocurrance element 
# nums = [12 , 2 , 4 , 1, 2 , 2]
# nums.remove(2)
# print(nums)

# # pop == delete -> delete element at index
# nums.pop(1)
# print(nums)

# names = ["apples" , "orange" , "graps" , "banana"]
# names.sort()
# print(names)

#---TUPLES---

# tups = (21, 45, 34, 90, 10)
# print(tups)
# print(type(tups))

# tups = (1,)
# print(tups)
# print(type(tups))


# tuples methods

# tups = (2 , 4 , 5, 8 , 1 , 10)

# # tups.indx(element) -> return index of first ocurance

# print(tups.index(1))

# tups.count(element) -> return counts total no of ocurances

# tups = (1, 3,2, 1, 2, 1, 2)
# print(tups.count(1))

# m1 = input("enter your favorite movie_1 -> ")
# m2 = input("enter your favorite movie_2 -> ")
# m3 = input("enter your favorite movie_3 -> ")

# list = [m1 , m2 , m3]
# print(list)

# movies = []
# movies.append(input("enter 1st movie -> "))
# movies.append(input("enter 2nd movie -> "))
# movies.append(input("enter 3rd movie -> "))
# print(movies)


# x = [1 , 2 , 3 , 2 , 4]

# if (x[0] == x[4] and x[1] == x[3]) :
#     print("palindrome number")
# else :
#     print("NOT palindrome number")    


# y = [1 , "abc" , "abc" , 2]

# if(y[0] == y[3] and y[1] == y[2]) :
#     print("yes")
# else :
#     print("NO")    


# list = ["a" , "m" , "m" , "a"]
# list_copy = list.copy()
# list_copy.reverse()

# if(list == list_copy) :
#     print("TRUE")
# else :
#     print("FALSE")    


grade = ["C", "D" , "A" , "B" , "B" , "A"]
grade.sort()
print(grade)

