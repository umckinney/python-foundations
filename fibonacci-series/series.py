"""
This is my attempt at creating a generic function that calculates a value based on the fibinacci series.
My original approach is straightforward. Simply loop through the range(n) and update the counting and total values.
Due to my approach where I deal with the initial values before my loop, I only execute the loop n-3 times.

When evaluating my solution, I saw several potential issues for a more generic approach:
1. It doesn't prevent invalid series lengths (i.e., n >= 0).
2. It doesn't allow us to easily extend the function if we needed to select a non-n sum (e.g., select the 2nd value from a list with length 200)
3. It uses multiple lines of code for actions that can be done in a single line of code (e.,g., updating the variables tracking the series values)

While it is more complex code, I believe my generic solution is more functional and robust.

Original solution for sum_series function
~~~~
def sum_series(n, n0=0, n1=1):
    total = n0+n1
    for i in range(n-3):
        n0 = n1
        n1 = total
        total = n0 + n1

"""


def fibonacci(n, n0=0, n1=1):
    """
    Application of sum_series to generate fibonacci sequence
    """
    return sum_series(n, n0, n1)


def lucas(n, n0=2, n1=1):
    """
    Application of sum_series to generate lucas sequence
    """
    return sum_series(n, n0, n1)


def sum_series(n, n0=0, n1=1):
    def sum_series(n, n0=0, n1=1):
    """Return a list of the first n terms in a generalized additive series.

    Args:
        n (int): Number of terms to return.
        n0 (int): First seed value. Default is 0 (Fibonacci).
        n1 (int): Second seed value. Default is 1 (Fibonacci).

    Returns:
        list or dict: List of series values, or error dict for invalid input.
    """
    series = [n0, n1]
    if n < 0:
        error_value = {
            "error code": "001",
            "error message": "Your sequence must be greater than or equal to 0.",
        }
        #        raise ValueError("Your sequence must be greater than or equal to 0.")
        return error_value
    for i in range(n - 2):  # Generate the remaining numbers
        n0, n1 = n1, n0 + n1
        series.append(n1)
    return series


# Main execution block
if __name__ == "__main__":
    series_length = 4
    series_output = fibonacci(series_length)
    print(
        series_output[series_length - 1]
    )  # Print the last value in the series_output list

    series_output = lucas(series_length)
    print(
        series_output[series_length - 1]
    )  # Print the last value in the series_output list

    series_output = sum_series(series_length, 11, 22)
    print(
        series_output[series_length - 1]
    )  # Print the last value in the series_output list

# Testing block
assert (
    fibonacci(10, 0, 1)[0] == 0
)  # validate fibonacci function returns expected values for first 10 items in series
assert fibonacci(10, 0, 1)[1] == 1
assert fibonacci(10, 0, 1)[2] == 1
assert fibonacci(10, 0, 1)[3] == 2
assert fibonacci(10, 0, 1)[4] == 3
assert fibonacci(10, 0, 1)[5] == 5
assert fibonacci(10, 0, 1)[6] == 8
assert fibonacci(10, 0, 1)[7] == 13
assert fibonacci(10, 0, 1)[8] == 21
assert fibonacci(10, 0, 1)[9] == 34
assert (
    lucas(10, 2, 1)[0] == 2
)  # validate lucas function returns expected values for first 10 items in series
assert lucas(10, 2, 1)[1] == 1
assert lucas(10, 2, 1)[2] == 3
assert lucas(10, 2, 1)[3] == 4
assert lucas(10, 2, 1)[4] == 7
assert lucas(10, 2, 1)[5] == 11
assert lucas(10, 2, 1)[6] == 18
assert lucas(10, 2, 1)[7] == 29
assert lucas(10, 2, 1)[8] == 47
assert lucas(10, 2, 1)[9] == 76
assert (
    sum_series(10, 0, 1)[0] == fibonacci(10, 0, 1)[0]
)  # validate sum_series function returns expected values when constructed as fibonacci series
assert sum_series(10, 0, 1)[1] == fibonacci(10, 0, 1)[1]
assert sum_series(10, 0, 1)[2] == fibonacci(10, 0, 1)[2]
assert sum_series(10, 0, 1)[3] == fibonacci(10, 0, 1)[3]
assert sum_series(10, 0, 1)[4] == fibonacci(10, 0, 1)[4]
assert sum_series(10, 0, 1)[5] == fibonacci(10, 0, 1)[5]
assert sum_series(10, 0, 1)[6] == fibonacci(10, 0, 1)[6]
assert sum_series(10, 0, 1)[7] == fibonacci(10, 0, 1)[7]
assert sum_series(10, 0, 1)[8] == fibonacci(10, 0, 1)[8]
assert sum_series(10, 0, 1)[9] == fibonacci(10, 0, 1)[9]
assert (
    sum_series(10, 2, 1)[0] == lucas(10, 2, 1)[0]
)  # validate sum_series function returns expected values when constructed as lucas series
assert sum_series(10, 2, 1)[1] == lucas(10, 2, 1)[1]
assert sum_series(10, 2, 1)[2] == lucas(10, 2, 1)[2]
assert sum_series(10, 2, 1)[3] == lucas(10, 2, 1)[3]
assert sum_series(10, 2, 1)[4] == lucas(10, 2, 1)[4]
assert sum_series(10, 2, 1)[5] == lucas(10, 2, 1)[5]
assert sum_series(10, 2, 1)[6] == lucas(10, 2, 1)[6]
assert sum_series(10, 2, 1)[7] == lucas(10, 2, 1)[7]
assert sum_series(10, 2, 1)[8] == lucas(10, 2, 1)[8]
assert sum_series(10, 2, 1)[9] == lucas(10, 2, 1)[9]

# test edge case where series length is less than 0
assert sum_series(-10, 11, 22) == {
    "error code": "001",
    "error message": "Your sequence must be greater than or equal to 0.",
}
