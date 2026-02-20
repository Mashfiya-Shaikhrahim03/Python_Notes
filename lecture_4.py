# Dictionary

# student = {
#     "name" : "xyz" ,
#     "is_pass" : True ,
#     "cgpa" : 80.5 ,
#     "topics" : {
#         "phy" : 90 ,
#         "chem" : 81 ,
#         "math" : 87 ,
#     }
# }

# print(student["topics"]["phy"])


# dictionary methods ->
# myDic.key -> return only keyValues

# menu = {
#     "pizzza" : 190 ,
#     "momos" : 80 ,
#     "nodals" : 60 ,
#     "coffee" : 60 ,
# }

# print(menu.keys())

# myDic.values -> return only values

# print(menu.values())

# myDic.items -> return all [vlues , keys] pair as tuples

# print(type(list(menu.items())))
# print(type(menu.items()))

# myDic.get("key") -> return the key acording to value

# print(menu.get("pizza"))
# print(menu["pizza"])
# print("hello")

# myDic.update(newDic) -> insert the specific items to the dictionary

# menu_change = {
#     "veg_nudals" : 120 ,
#     "samosa" : 20 ,
#     "dosa" : 45 ,
# }

# menu.update(menu_change)
# print(menu)

# SET in python #
# num_1 = {1, 2, 3, 4}
# num_2 = {2, 5, 6, 7}

# Null_set = set()
# null_set = set()
# print(null_set)
# print(type(null_set))

# set methods #
# set.add(element)
# empty_set = set()

# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(3)
# empty_set.add(4)
# empty_set.add(5)
# print(empty_set)

# set.remove(element)

# empty_set.remove(4)
# print(empty_set)

# set.clear() -> return empty set
# empty_set.clear()
# print(empty_set)

# set.pop() -> delete random element
# empty_set.pop()
# print(empty_set)

# empty_set.pop()
# print(empty_set)

# empty_set.pop()
# print(empty_set)

# empty_set.pop()
# print(empty_set)




# practice problem

# dic = {
#     "table" : "a piece of furniture" + "list of facts & figures" ,
#     "cat" : " a small animal"

# }

# print(dic)

# set = {"python" , "java" , "c++" , "python" , "javascript" , "java" , "python" , "java" , "c++" , "c"}
# print(set)
# print("length of set is -> " , len(set))

# marks = {}

# mark_1 = int(input("enter your phys mark -> "))
# marks.update({"phy" : mark_1})

# mark_2 = int(input("enter your chem mark -> "))
# marks.update({"chem" : mark_2})

# mark_3 = int(input("enter your math mark -> "))
# marks.update({"math" : mark_3})


# print(marks)
# print(type(marks))


# set = {"9" , 9.0}
# print(set)

set = {
    ("float" , 9) ,
    ("int" , 9.0) ,
}

print(set)