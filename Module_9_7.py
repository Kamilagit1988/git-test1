def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_ = func(*args, **kwargs)
        is_prime = True
        for i in range(2, sum_):
            if sum_ % i == 0:
                is_prime = False
        if is_prime == True:
            return (f'{sum_} Простое')
        else:
            return (f'{sum_} Составное')
    return wrapper
@ is_prime
def sum_three(*value):
    sum_ = sum(value)
    return sum_

result = sum_three(2, 3, 6)
print(result)