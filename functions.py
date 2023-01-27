# write a function that will take a list as a perimeter and return boolean if any number is even in that list

def check_for_even_number(number_list):
    for num in number_list:
        if num % 2 == 0:
            return True
    return False


# print(check_for_even_number([1, 3, 5, 7, 9, 11, 13, 15, 2]))

# write function to return all the even number in a list in sorted order of ascending

def return_all_even_number(number_list):
    ans_list = []
    for num in number_list:
        if num % 2 == 0:
            ans_list.append(num)
    ans_list.sort()
    return ans_list


print(return_all_even_number([1, 3, 3, 8, 2, 6, 2, 6]))
