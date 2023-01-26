temp_list = [1, 2, 3, 4, 5, 6]

boolean = 3 in temp_list

print(boolean)

# list comprehensions

stringTemp = 'hello'

temp_list = [i for i in stringTemp]

print(temp_list)

temp_list = [i for i in stringTemp if i == 'e' or i == 'l']

print(temp_list)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

newTuple = zip(list1, list2)

for a, b in newTuple:
    print(a, b)

# 2d list

list3 = [list1, list2]

for _ in list3:
    for num in _:
        print(num, end=" ")
    print()
