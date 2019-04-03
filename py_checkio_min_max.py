# In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in functions min and max. Some builtin functions are closed here: import, eval, exec, globals. Don't forget you should implement two functions in your code.
#
# max(iterable, *[, key]) or min(iterable, *[, key])
# max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])
#
# Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
#
# If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.
#
# The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).
#
# If multiple items are maximal (minimal), the function returns the first one encountered.
#
# -- Python Documentation (Built-in Functions)
#
# Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.
#
# Output: The largest item for the "max" function and the smallest for the "min" function.
#
# Example:
#
# max(3, 2) == 3
# min(3, 2) == 2
# max([1, 2, 0, 3, 4]) == 4
# min("hello") == "e"
# max(2.2, 5.6, 5.9, key=int) == 5.6
# min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
#
# How it is used: This task will help you understand how some of the built-in functions work on a more precise level.
#
# Precondition: All test cases are correct and functions don't have to raise exceptions.

def min(*args, **kwargs):
    smallest = None
    key = kwargs.get("key", None)
    if key:
        if len(args) == 1:
            min_list = list(args[0])
            smallest = min_list[0]
            for arg in range(len(min_list)):
                if key(min_list[arg]) < key(smallest):
                    smallest = min_list[arg]
        else:
            smallest = args[0]
            for arg in range(len(args)):
                if key(args[arg]) < key(smallest):
                    smallest = args[arg]
    else:
        if len(args) == 1:
            min_list = list(args[0])
            smallest = min_list[0]
            for arg in range(len(min_list)):
                if min_list[arg] < smallest:
                    smallest = min_list[arg]
        else:
            smallest = args[0]
            for arg in range(len(args)):
                if args[arg] < smallest:
                    smallest = args[arg]
    return smallest


def max(*args, **kwargs):
    largest = None
    key = kwargs.get("key", None)
    if key:
        if len(args) == 1:
            max_list = list(args[0])
            largest = max_list[0]
            for arg in range(len(max_list)):
                if key(max_list[arg]) > key(largest):
                    largest = max_list[arg]
        else:
            largest = key(args[0])
            for arg in range(len(args)):
                if key(args[arg]) > key(largest):
                    largest = args[arg]
    else:
        if len(args) == 1:
            max_list = list(args[0])
            largest = max_list[0]
            for arg in range(len(max_list)):
                if max_list[arg] > largest:
                    largest = max_list[arg]
        else:
            largest = args[0]
            for arg in range(len(args)):
                if args[arg] > largest:
                    largest = args[arg]
    return largest


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum)
