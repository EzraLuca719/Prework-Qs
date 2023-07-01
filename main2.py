# # Prework Assignment

def hello_name(user_name):
    print ("Hello_" + user_name + " !")

hello_name('USERNAME')


# # 2 - Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
     for i in range(0,101):
         if i % 2 !=0:
             print(i)
first_odds()


        

    


# 3 #Write a Python function max_num_in_list that returns the max number in a given list

def max_num_in_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [20, 40, 60, 80, 100]
print(max_num_in_list(a_list))
    


    




# # 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year%4 == 0:
        return True
    else:
        return False
a_year = int(input())

print(is_leap_year(a_year))


# # 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [4,5,6,7,8,9]
print(is_consecutive(a_list))


