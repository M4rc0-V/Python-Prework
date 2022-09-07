#Q1 'hello_USERNAME'
from operator import truediv


username = input("What's you username?")
print ("Hello " + username)

#Q2 'first_odds'
current_number = 0
while current_number < 100:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Q3 'max_num_in_list'
def max_num_in_list(a_list):
    return max(a_list)


#Q4 'leap_year'
leap_year = (int(input("What Year is it?")))
if leap_year % 400 == 0 or leap_year % 4 == 0:
    print ("It is a leap year!")
else:
    print ("It is not a leap year")     
     

#Q5 'consecutive_numbers'
a_list = [2,3,4,5,3,7]
i = 0
def is_consecutive(list):
    while i in range(len(a_list)-1):
        if a_list[i]+1==a_list[i+1]:
            return True
        else:
            return False

print(is_consecutive(a_list))








