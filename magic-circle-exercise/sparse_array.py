#!/usr/bin/env python
"""
Requirements
    Emulate a built-in 1d list class
    Initialize with a sequence of values
    Any value = to 0 will be dropped, but the position will be retained
    Must support:
        len(sparse_array)       : returns len as if 0s were stored
        get element by index    :returns 0 for any index with a NULL value
                                :negative indexes return values from the end of the list
        set element by index
        deletion by index       :reduces the len(sparse_array) by 1 instead of replacing the value with a 0
        raise IndexError if attempting to access a value beyond the defined index range
        append(value)           :increments the len by 1 and populates the index with the appended value
                                :allow empty append to generate a sparse index value
        slicing[v1:v2:step]     :all fields are optional and manage slice behavior
                                :supports negative numbers
        reversing

Stretch goal: extend to support 2d lists
"""


class SparseArray(list):
    """Emulates lists where 0 values are not stored in memory"""

    def __init__(self, *input_values):
        if not input_values:
            self.sa = {}
        else:
            input_values = list(input_values)
            input_values = [None if i == 0 else i for i in input_values]
            self.sa = {index: value for index, value in enumerate(input_values)}

    def __str__(self):
        return f"Sparse Array {list(self.sa.values())}"

    def __repr__(self):
        return f"Sparse Array {list(self.sa.values())}"

    def __len__(self):
        return max(self.sa.keys(), default=-1) + 1

    def __getitem__(self, key):
        try:
            if key < 0:
                key += len(self.sa)
            if key < 0 or key >= len(self.sa):
                raise IndexError
            return self.sa.get(key, 0)
        except IndexError:
            print(f"IndexError: index of {key} out of range for Sparse Array")
            return None

    def __setitem__(self, key, value):
        try:
            if key < 0:
                key += len(self.sa)
            if key < 0:
                raise IndexError
            if value == 0:
                if key in self.sa:
                    del self.sa[key]
                else:
                    self.sa[key] = value
        except IndexError:
            print(f"IndexError: index of {key} out of range for Sparse Array")

    def __delitem__(self, key):
        try:
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError(f"Index {key} out of range")
            self.sa.pop(key)
        except IndexError:
            print(f"IndexError: index of {key} out of range for Sparse Array")

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self.sa):
            result = self.sa[self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration


"""
    def __reversed__(self):
        pass

    def __contains__(self, item):
        pass

    def __index__(self):
        pass
"""

if __name__ == "__main__":
    a = SparseArray(0, 1, 0, 2, 0, 3, 0)
    print(f"a = {a}")
    print(f"len(a) = {len(a)}")
    print(f"a[0] = {a[0]}")
    print(f"a[1] = {a[1]}")
    print(f"a[2] = {a[2]}")
    print(f"a[3] = {a[3]}")
    print(f"a[4] = {a[4]}")
    print(f"a[5] = {a[5]}")
    print(f"a[6] = {a[6]}")
    print(f"a[7] will generate an error")
    print(a[7])
    print("set a[6] to 22")
    a[6] = 22
    print(f"a = {a}")
    print("set a[99] to 1 will generate an error")
    a[99] = 1
    print(f"a = {a}")
    print("delete a[0]")
    del a[0]
    print(f"a = {a}")
    print("loop through a and print key value pair")
    for i in range(len(a)):
        print(f"Index {i} = {a[i]}")
