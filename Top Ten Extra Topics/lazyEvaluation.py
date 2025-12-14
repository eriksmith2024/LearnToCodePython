def get_prime(n):
    candidate = n + 1
    while True:
        for i in range(2, candidate):
            if candidate % i == 0:
                break
        else:
            return candidate
        candidate += 1


def list_of_primes():
    next = 1
    while True:
        next_prime = get_prime(next)
        next = next + 1
        yield next_prime


def nth_prime(n):
    count = 0
    for prime in list_of_primes():
        count = count + 1
        if count == n:
            return prime


print("\nThe 5th prime is:", nth_prime(5), "\n")

