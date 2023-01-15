
def is_prime(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    
    if count == 2:
        print('This number is prime')
    else:
        print('This number not is prime')


is_prime(2)
is_prime(4)
is_prime(8)
is_prime(3)
