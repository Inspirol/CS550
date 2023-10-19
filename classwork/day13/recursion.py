def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    
# result = factorial(999)

# print(result)

stored_fib_values = {}

def fibonachi(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n in stored_fib_values:
            return stored_fib_values[n]
        else:
            result = fibonachi(n - 1) + fibonachi(n - 2)
            stored_fib_values[n] = result
            return result
    
# for i in range(10000):
#     print(fibonachi(i))

# print(fibonachi(10000))

