def tea_order(customer_name, tea_type,*args, **kwargs): 
    print(f"{customer_name} ordered a {tea_type}.")
    for arg in args:
        print("- Add :", arg)
    for key,value in kwargs.items():
        print("- Add", key, ":", value)

tea_order("Alice","chamomile") 
tea_order("Bob", "black", milk = "oat")
tea_order("Tony", "black", "oat", sweetener = "honey")
# can only accept a finite number of arguments for finite number of parameters
# *args allows for an indefinite amount of argumemts since it continously creates new parameters
# *args acts as empty tuple, unable to handle keyword arguments (ex. milk = "oat")
# **kwargs allows for keyword arguments, acts as empty dictionary
# can have both *args and **kwargs in code, but *args must come first (positional arguments before keyword arguments)




# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    sum = 0
    for num in args:
        sum += num**2
    return sum

print(sum_squares(2,4,5)) 
print(sum_squares(2,6,5,2))

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    sum = 0
    for num in args:
        sum += abs(num)
    return sum

print(absolute_sum(-2,35,-4))
print(absolute_sum(1,-34,23,5))

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum = 0
    for num in args:
        sum += num
    print(f"{name}, the sum of your numbers is {sum}.")

personal_numbers("Alice", 2, 5, 34)