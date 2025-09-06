def fizz_buzz(n):
    """Prints numbers from 1 to n with Fizz/Buzz/FizzBuzz substitutions.

    Args:
        n (int): Upper bound of the range (inclusive).
    """
    for i in range(1, n + 1):
        if (
            i % 3 == 0 and i % 5 == 0
        ):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def elegant_fizzbuzz(n):
    for i in range(1, n + 1):
        print("Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i)


if __name__ == "__main__":
    upper_limit = 100
    print(f"Basic FizzBuzz implementation to {upper_limit}:")
    fizz_buzz(upper_limit)
    print("\nElegant FizzBuzz Solution:")
    elegant_fizzbuzz(upper_limit)
