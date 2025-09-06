#!/usr/bin/env python

"""
Series 1
* Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
* Display the list. Plain old print() is fine.
* Ask the user for another fruit and add it to the end of the list.
* Display the list.
* Ask the user for a number and display the number back to the user and the fruit corresponding to that number, using 1 as the first number. Remember that Python uses zero-based indexing, so you will need to correct for that.
* Add another fruit to the beginning of the list using “+” and display the list.
* Add another fruit to the beginning of the list using insert() and display the list.
* Display all the fruits that begin with “P”, using a for loop.

Series 2
Using the list created in series 1 above:
* Display the list.
* Remove the last fruit from the list.
* Display the list.
* Ask the user for a fruit to delete, find it and delete it.
* Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

Series 3
Again, using the list from series 1:
* Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list, making the fruit all lowercase.
* For each “no”, delete that fruit from the list.
* For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
* Display the list.

Series 4
Once more, using the list from series 1:
* Make a new list with the contents of the original, but with all the letters in each item reversed.
* Delete the last item of the original list. Display the original list and the copy.
"""


def setup():
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit_list)
    return fruit_list


def series_1(list):
    """Prompts user to extend and modify a list of fruits. Handles display, indexing, and filtering by first letter."""
    response = input("Enter a fruit > ")
    list.append(
        response.title()
    )  # normalize formatting of new fruit string to title case
    print(list)

    top_of_list_range = len(list)  # determine how long the list is
    print(
        "Pick an item from the list of fruits. Enter a number between 1 and "
        + str(top_of_list_range)
    )
    output = series_1_get()  # call the function to get the numeric input from the user
    while (
        (output > top_of_list_range) or (output < 1) or (not isinstance(output, int))
    ):  # validate the user entered a valid integer in the range
        print("You entered a value that is out of range. Try again.")
        output = series_1_get()
    print("You picked ")
    print(list[output - 1])

    response = input("Enter another fruit > ")
    list = [response.title()] + list
    print(list)

    response = input("Enter another fruit > ")
    list.insert(0, response.title())
    print(list)

    user_letter = input("Enter a letter > ")
    new_list = []
    for i in list:
        if (i.find(user_letter.title())) == 0:
            new_list.append(i)
    print(new_list)


def series_1_get():
    """Helper function to collect list value"""
    response_index = input(" > ")
    try:
        get_output = int(response_index)

        return get_output
    except ValueError as e:
        return 0


def series_2(list):
    """
    Function to manipulate a list of fruits.
    Pop from initial list
    Create new list that duplicates original
    Doubles the values in the new list
    """
    print(list)
    list.pop()
    new_list = list[:]
    new_list *= 2
    while new_list == list * 2:
        # keep looping until we've removed at least one matching fruit
        new_list = series_2_get(new_list)
    print(new_list)


def series_2_get(list):
    """Helper function to remove a fruit from the list"""
    print(list)
    bad_fruit = input("Enter a fruit to remove from the list > ")
    new_list = []
    for i in list:
        if not i == bad_fruit.title():
            new_list.append(i)
    return new_list


def series_3(list):
    """
    Function to collect a list of fruit the user likes/dislikes.
    Handles invalid responses.
    """
    like_fruit_answer = []
    for i in list:
        answer = ""
        while answer == "":
            answer = input(f"Do you like {i}? Type Y or N > ").strip().lower()
            print("Answer = " + answer)
            if (not answer == "Y") and (not answer == "N"):
                print("You must enter Y or N.")
                answer = ""
        like_fruit_answer.append(answer)

    new_list = list[:]

    counter = len(list)
    for i in range(counter):
        if like_fruit_answer[i] == "N":
            new_list.remove(list[i])

    if not new_list:
        print("You don't like any of these fruit!")
    else:
        print(new_list)


def series_4(list):
    """
    Function to reverse a list and pop 1 item
    """
    new_list = list[:]
    new_list2 = []
    for i in new_list:
        i = i[::-1]
        new_list2.append(i)
    print(new_list2)

    list.pop()
    print(f"Original List: {list}")
    print(f"New List: {new_list2}")


if __name__ == "__main__":
    setup_result = setup()
    series_1(setup_result)
    series_2(setup_result)
    series_3(setup_result)
    series_4(setup_result)
