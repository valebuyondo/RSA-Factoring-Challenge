import sys

def factorize(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
        if number == 1:
            break
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                if len(factors) == 2:
                    p, q = factors
                    print(f"{number}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

