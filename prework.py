#prework questions for Coding Temple course

#Question 1 - print hello user
def hello_name(user_name):
    print("Hello, " + user_name)

hello_name("Sam")

#Question 2 - print the first 100 odd numbers
i = 1
while i < 200:
    print(i)
    i += 2

#Question 3 - return the max number in a list
def max_num_in_list(a_list):
    print(max(a_list))
    return max(a_list)

max_num_in_list([2,3,6,7,12])

#Question 4 - write a function to return if the given year is a leap year
def is_leap_year(a_year):
    if a_year%4 == 0:
        if a_year%100 == 0:
            if a_year%400 == 0: return True
            else return False
        else return True
    else return False

#Question 5 - check if the numbers in a list are consecutive
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i]+1 != a_list[i+1]:
            return False
    return True

print(is_consecutive([2,3,4,5,6]))
print(is_consecutive([3,6,7,4]))