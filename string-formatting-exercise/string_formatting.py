"""
String Formatting Exercise by uriah McKinney

Objective: Complete 6 assigned tasks and the bonus task
"""


def task_1():
    """
    Task 1: Write a format function that will take 4 values in a tuple and return a formatted string:
    * First string inserts a number to the string "file_00x" where x is the number
    * Second string presents a float rounded to the 2nd sig fig
    * Third and fourth strings each present a number in scientific notation

    Returns:
        formatted_string: string that is formatted as per instructions
    """
    formatted_string = "file_{:03} :  {:.2f}, {:.2e}, {:.2e}".format(
        2, 123.4567, 10000, 12345.67
    )

    return formatted_string


def task_2():
    """
    Task 2 is to replicate Task 1, but using an alternate method for formatting the strings.

    Returns:
        formatted_string2: string that is formatted as per instructions
    """
    initial_tuple = (2, 123.4567, 10000, 12345.67)
    formatted_string2 = f"file_ {initial_tuple[0]:03} :  {initial_tuple[1]:.2f}, {initial_tuple[2]:.2e}, {initial_tuple[3]:.2e}"

    return formatted_string2


def task_3(input_tuple):
    """
    Create a string formatted that accepts a tuple of arbitrary length and presents the data
    in the following pattern:
        the X numbers are A, B, C, ..., N

    Args:
        input_tuple: tuple containing the values to be formatted

    Returns:
        output_string: formatted string
    """
    tuple_count = len(input_tuple)
    string1 = f"the {tuple_count} numbers are: "
    string2 = ""
    for item in input_tuple:
        string2 += str(item)
        if item != input_tuple[tuple_count - 1]:
            string2 += ", "
    output_string = string1 + string2

    return output_string


def task_4():
    """
    Using string formatting, given a 5 element tuple:
        1. Swap the 4th element with the 1st element
        2. Swap the 5th element with the 2nd element
        3. Pad all number to as least 2 digits

    Returns:
        output_string: formatted string
    """
    input_tuple = (4, 30, 2017, 2, 27)
    output_string = f"{input_tuple[3]:02} {input_tuple[4]:02} {input_tuple[2]:02} {input_tuple[0]:02} {input_tuple[1]:02}"

    return output_string


def task_5():
    """
    Given a 4 element list ['oranges', 1.3, 'lemons', 1.1]
    Write an fstring that will display
        The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Then display the fruit names in upper case and the weights at 120%

    Returns:
        output_string: formatted string
    """
    input_list = ["oranges", 1.3, "lemons", 1.1]
    output_string = f"The weight of an {trim_s(input_list[0])} is {input_list[1]} and the weight of a {trim_s(input_list[2])} is {input_list[3]}"
    print("Initial string: \n" + output_string)
    output_string2 = f"The weight of an {trim_s(input_list[0]).upper()} is {input_list[1] * 1.2} and the weight of a {trim_s(input_list[2]).upper()} is {input_list[3] * 1.2}"
    print("Updated string: \n" + output_string2)


def trim_s(term):
    """
    Trims the last letter of a string if it ends in 's'
    This was needed because there was a mismatch between the list provided in the homework and the required output

    Args:
        term: word to be evaluated

    Returns:
        term: if it ends in 's', trimmed
    """
    if term.endswith("s"):
        return term[:-1]
    return term


def task_6():
    """
    Write some Python code to print a table of several rows,
    each with a name, an age and a cost.
    Make sure some of the costs are in the hundreds and thousands
    to test your alignment specifiers.
    """
    input_table = [
        # ["Name", "Age", "Cost"],
        ["Bob", 42, 1000],
        ["Nancy", 30, 500],
        ["Jorge", 38, 750],
        ["Marisol", 25, 1500],
        ["Umar", 31, 10900],
    ]

    # define format structure
    row = "| {name:<8s} | {age:3d} | ${cost:6}".format

    for i in input_table:
        print(row(name=i[0], age=int(i[1]), cost=int(i[2])))


def task_7():
    """
    And for an extra task, given a tuple with 10 consecutive numbers,
    can you work how to quickly print the tuple in columns that are 5 characters wide?
    It can be done on one short line!
    """
    input_tuple = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    print(*[str(item).ljust(5) for item in input_tuple], end="")


if __name__ == "__main__":
    print("Task 1: " + task_1())
    print("Task 2: " + task_2())
    print("Task 3: " + task_3((1, 2, 3)))
    print("Task 3: " + task_3((1, 2, 3, 4, 5, 6)))
    print("Task 4: " + task_4())
    print("Task 5:")
    task_5()
    print("Task 6:")
    task_6()
    print("Task 7:")
    task_7()
