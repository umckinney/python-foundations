#!/usr/bin/env python

"""
A set of classes to facilitate report writing
"""
from typing import List
import math
import operator
from uuid import uuid4


class Row:
    """
    This class represents a single row
    with ID, first name, last name and state attributes
    """

    def __init__(self, fname, lname, state):
        self.row_id = str(uuid4())  # randomly generated unique ID
        self.fname = fname
        self.lname = lname
        self.state = state

    def __str__(self):
        return f"| {self.row_id} | {self.fname + ' ' + self.lname:<15} | {self.state} |"


class Report:
    def __init__(self, limit: int):
        self.limit = (
            limit  # specifies how many records (rows) a report should return by default
        )
        self.rows = []

    def add_row(self, row: Row):
        """Add a row object to the report"""
        self.rows.append(row)
        return True

    def remove_row(self, row_id: str):
        """Remove a row object by the row's ID"""
        for row in self.rows:
            if row_id == row.row_id:
                self.rows.remove(row)
                return True
        return False

    def size(self) -> int:
        """Return how many total rows the report has"""
        return len(self.rows)

    def get_number_of_pages(self) -> int:
        """
        Get how many pages the report has; this will be based on limit variable.
        If your limit=4 and rows list has 6 records then there are two pages:
          page1 has 4 records, page2 has 2 records
        hint: you'll want to round up
        """
        return math.ceil(self.size() / self.limit)

    def get_paged_rows(self, sort_field: str, page: int) -> List[Row]:
        """Return a list of rows for a specific page number
        :param sort_field:  field to sort on, for example "fname" or "-fname" (descending)
        :param page:        specific page for returning data
        :return:            list of row objects for specific page

        Hints:
        1. You'll want to determine if sort is reversed or not (remember that
           sorted() takes in param for that) this is based on if the field
           starts with a minus sign for DESCENDING sort
        2. When sorting on passed in field you can use handy `operator` library
           with `attrgetter` method (look up official docs)
        3. `page` parameter is used to determine what page number you'd like to display.
           In a typical report you commonly see Page 1 of X with a default display size of Y rows per page,
           this design allows a user to page through results without having to load all records in a single page.

           To actually determine what rows belong on the specific page you'll be
           using list slicing (remember the slicing lab?)

           Here is an illustration to help with the code logic:

           If a list has 6 rows => [<row1>, <row2>, <row3>, <row4>, <row5>, <row6>] and limit is set to 4 then
           for page=2 we expect to get => [<row5>, <row6>]
           with slicing you'll want to offset your list by 4 in this case
           (extra hint: we can define offset as `offset = (page - 1) * self.limit`)

        """
        sort_order = True if sort_field[0] == "-" else False
        sort_field = sort_field[1:] if sort_order == True else sort_field
        self.rows.sort(key=operator.attrgetter(sort_field), reverse=sort_order)

        if page > 0 and page <= self.get_number_of_pages():
            offset = (page - 1) * self.limit
            return self.rows[offset : (offset + self.limit)]


def run_report(sort_field):
    print(f"... PAGED REPORT SORTED BY: '{sort_field}'...")
    page = 1
    while True:
        rows = report.get_paged_rows(sort_field, page=page)

        if not rows:
            break

        input(f"Press ENTER to see page {page}")

        print(f"PAGE: {page} of {report.get_number_of_pages()}")
        print("---------------------------------------------------------------")

        for row in rows:
            print(row)

        print("---------------------------------------------------------------")

        page += 1


if __name__ == "__main__":

    report = Report(4)

    report.add_row(Row("natasha", "smith", "WA"))
    report.add_row(Row("devin", "lei", "WA"))
    report.add_row(Row("bob", "li", "CA"))
    report.add_row(Row("tracy", "jones", "OR"))
    report.add_row(Row("johny", "jakes", "WA"))
    report.add_row(Row("derek", "wright", "WA"))

    run_report("fname")

    print(
        "\n\nRemoving student: "
        f"{report.rows[1].fname} [{report.rows[1].row_id}]... \n\n"
    )
    report.remove_row(report.rows[1].row_id)

    run_report("-fname")
