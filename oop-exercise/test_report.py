"""
test code for the Report class(es)
"""

from report import Row, Report


def example_report():
    """
    utility function to provide a fresh report to test with
    """
    report = Report(limit=4)

    populate_report(report)
    return report


def populate_report(report):
    """
    utility function to populate an existing Report with
    some additional data

    :param report: the report object to populate

    The Report will be populated in place
    """
    report.add_row(Row("Natasha", "Smith", "WA"))
    report.add_row(Row("Devin", "Lei", "WA"))
    report.add_row(Row("Bob", "Li", "CA"))
    report.add_row(Row("Tracy", "Jones", "OR"))
    report.add_row(Row("Johnny", "Jakes", "WA"))
    report.add_row(Row("Derek", "Wright", "WA"))
    report.add_row(Row("Jordan", "Cooper", "WA"))
    report.add_row(Row("Mike", "Wong", "WA"))


def test_row_init():
    """
    test that a new row has the proper attributes initialized
    """
    row1 = Row("Joe", "Camel", "WA")

    assert row1.fname == "Joe"
    assert row1.lname == "Camel"
    assert row1.state == "WA"


def test_row_id_unique():
    """two Rows should have unique IDs"""
    row1 = Row("Joe", "Camel", "WA")
    row2 = Row("Bob", "Camel", "WA")

    assert row1.row_id != row2.row_id


def test_report_length():
    """
    test report size method
    """
    report = example_report()

    # the test data has 8 rows
    assert report.size() == 8


def test_number_of_pages():
    """
    check that the number of pages is correct
    """
    report = example_report()

    assert report.get_number_of_pages() == 2


def test_add_row():
    """validate row1 is added to report"""
    row1 = Row("Joe", "Camel", "WA")
    report = example_report()
    report.add_row(row1)
    test = any(row.row_id == row1.row_id for row in report.rows)
    assert test == True


def test_remove_row():
    """validate test_row is removed from report"""
    report = example_report()
    test_row = report.rows[1]
    report.remove_row(test_row.row_id)
    test = any(row.row_id == test_row.row_id for row in report.rows)
    assert test == False


def test_size():
    """validate example_report has 8 rows"""
    report = example_report()
    assert report.size() == 8


def test_get_number_of_pages():
    """validate example_report has 2 pages"""
    report = example_report()
    assert report.get_number_of_pages() == 2


def test_get_paged_rows():
    """validate example_report returns 4 known rows"""
    report = example_report()
    test_list = report.get_paged_rows("lname", 1)
    print(f"test_list: {test_list}")
    print(f"known_list: {report.rows[:4]}")
    assert test_list == report.rows[:4]
