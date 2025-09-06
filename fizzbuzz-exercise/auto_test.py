import contextlib
import io
import fizz_buzz

f = io.StringIO()
with contextlib.redirect_stdout(f):
    fizz_buzz.fizz_buzz(16)

output = f.getvalue()

expected_output = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

assert output.lower() == expected_output.lower(), f"Expected output: {expected_output}"
