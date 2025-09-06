import grid_printer
import contextlib, io


def validate(actual, expected):
    actual_lines = actual.strip().split('\n')
    for idx, line in enumerate(expected.strip().split('\n')):
        if actual_lines[idx].strip() != line.strip():
            print('here')
            print(actual_lines[idx].strip(), line.strip())
            return False
    return True


expected_grid1 = \
    """+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""

f = io.StringIO()
with contextlib.redirect_stdout(f):
    grid_printer.print_grid1()
assert validate(f.getvalue(), expected_grid1)

expected_grid2 = \
    """+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
"""
f = io.StringIO()
with contextlib.redirect_stdout(f):
    grid_printer.print_grid2(3)
print(f.getvalue())
print(expected_grid2)
assert validate(f.getvalue(), expected_grid2)


expected_grid3 = \
    """+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
"""
f = io.StringIO()
with contextlib.redirect_stdout(f):
    grid_printer.print_grid3(3, 4)
assert validate(f.getvalue(), expected_grid3)
