# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

num = [4, 2, 5, -2, 34, 95]
def all_positives(num):
    for i in range(len(num)):
        if num[i] <= 0 :
            return False
    
    return True

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

nums = [12, -93, 389, 2824, 2, 49]
def sum_less(nums):
    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] < 1000:
            sum += nums[i]
        else:
            continue
    return sum


# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

count = 0
numbers = [23, 4, 11, 44, 298]

def count_even(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            counter +=1
        else:
            continue
    return counter