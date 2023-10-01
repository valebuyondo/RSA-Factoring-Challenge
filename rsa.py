import sys

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize(number):
    factors = []
    if number <= 1:
        return factors
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                if is_prime(number):
                    print(f"{number}={number}*1")
                else:
                    factors = factorize(number)
                    p = factors[0]
                    q = factors[-1]
                    print(f"{number}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

