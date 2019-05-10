''' This script solves the problem of calculating maximum sum 
    of the non-neighbours in a list and provide the elements 
    making this maximum sum along with the sum.
    This script works for mixed (positive and negative) number list
    
    Script doesn't do of the input parameters
    It takes input from the user
'''
__version__="1.0.0"
__author__="Jayaprakash Nevara"

def list_has_negative_numbers_only(num_list):
    '''This function checks if the given input list 
       num_list has only negative numbers
       returns - True, if it has only negative numbers
                 False, if not
    '''
    ele_count = 0
    for item in num_list:
        if item < 0:
            ele_count += 1

    if ele_count == len(num_list):
        return True
    else:
        return False


def get_max_sum_list(num_list):
    '''This function takes num_list a number list as input 
    processes the list to find the maximum sum of the 
    non-neighbour numbers and the numbers that make this sum
    Input  : num_list - a number list 
    Output : (max_sum, max_sum_list) - a tuple with maximum sum
             and the numbers list that make up this sum
    '''
    if not isinstance(num_list, list):
        raise ValueError("Expecting list as input")

    incl_list = []
    excl_list = []
    index = 0
    for num in num_list:
        if num > 0:
            incl = num
            incl_list.append(num)
            break
        index += 1

    excl = 0
    for num in num_list[index + 1:]:
        if num > 0:
            temp = incl
            if incl < excl + num:
                temp_list = incl_list.copy()
                incl_list = excl_list.copy()
                incl_list.append(num)
                excl_list = temp_list.copy()
                incl = excl + num
            excl = temp
            if incl == excl:
                excl_list = incl_list.copy()
        else:
            temp = incl
            incl = max(incl, excl + 0)
            excl = incl
            excl_list = incl_list.copy()
    return max(incl, excl), incl_list


def main():
    number_of_elements = int(input("Enter number of elements in the list?"))
    print("Enter list elements(only integer data allowed)")
    index = 0
    num_list = []
    while index < number_of_elements:
        try:
            element = int(input())
        except Exception as exp:
            print("Invalid input, enter integer only")
            continue
        num_list.append(element)
        index += 1
    if not list_has_negative_numbers_only(num_list):
        max_sum, sum_list = get_max_sum_list(num_list)
        print("Maximum sum : ", max_sum)
        print("Elements making maximum sum")
        print(sum_list)
    else:
        print("Maximum sum : ", max(num_list))
        print("Elements making maximum sum")
        print("[" + str(max(num_list)) + "]")


main()
