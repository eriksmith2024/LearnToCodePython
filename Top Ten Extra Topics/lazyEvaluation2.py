def get_prime(n):
    # Simple version so we can see output clearly
    num = n + 1
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            return num
        num += 1


def list_of_primes():
    next = 1
    while True:
        next_prime = get_prime(next)
        print("list_of_primes generated:", next_prime)
        next = next + 1
        yield next_prime


def nth_prime(n):
    count = 0
    for prime in list_of_primes():
        count = count + 1
        print("nth_prime saw:", prime)

        if count == n:
            print("nth_prime returning:", prime)
            return prime


print("Calling nth_prime...")
result = nth_prime(5)
print("Result:", result)
