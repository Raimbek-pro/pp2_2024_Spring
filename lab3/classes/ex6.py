def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
numbers = [2, 3, 4,6,7,12,13]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Original list:", numbers)
print("Prime numbers:", prime_numbers)