# Basic Example
def div_func(n, m):
    try:
        res = n / m
    except ZeroDivisionError:
        print("Exception: Check if m is zero")
    except ValueError:
        print(f"Received n = {n} & m = {m}, Both n & m must be valid numbers")
    else:
        return res
    finally:
        print("Execution complete") # Note that the entire function gets executed first, before the return is passed out.

def multiple_exceptions():
    a = ["10", "twenty", 30] # list of strings and integers
    try:
        total = int(a[2]) + int(a[1])
    except (ValueError, TypeError) as e:
        print("Error", e)
    except IndexError:
        print("Index out of range")
    else:
        return total
    
def catch_all_handlers(n, m):
    try:
        res = n / m
    except ArithmeticError:
        print("Arithmetic Issue")
    except ZeroDivisionError:
        print(f"Ensure m is non-zero, received m = {m}")
    except TypeError:
        print(f"TypeError: Check dtype compatibility. Received n as {type(n)} & m as {type(m)}")
    else:
        return res
    finally:
        print("Execution complete")
    
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative. Received age as {age}")

class AgeError(Exception):
    pass

def set_age_custom(age):
    if age < 0:
        raise AgeError(f"Age cannot be negative. Received age as {age}")

if __name__ == "__main__":
    # res1 = div_func(10, 2)
    # print(res1)
    # res2 = div_func(4, 0)
    # print(res2)
    # total = multiple_exceptions()
    # print(total)
    # res1 = catch_all_handlers(10, 2)
    # print(res1)
    # res2 = catch_all_handlers("10", 2.0)
    # set_age(-5) # throws an exception, an error & breaks the code from running.
    # try:
    #     set_age(-5)
    # except ValueError as e: # The exception raised is caught here - doesn't break the code but flags the issue.
    #     print(e)
    # set_age_custom(-5) # throws an exception, an error & breaks the code from running.
    try:
        set_age_custom(-5)
    except AgeError as e: # The exception raised is caught here - doesn't break the code but flags the issue.
        print(e)

