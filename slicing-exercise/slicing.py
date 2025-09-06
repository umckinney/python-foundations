def exchange_first_last(seq):
    """
    creates a new sequence that is a concat of:
    the last character of the original string,
    the middle N characters in the original string,
    and the first character in the original string
    """
    new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return new_sequence


def every_other_removed(seq):
    """
    creates a new sequence that drops every 2nd character using the slice step function
    """
    new_sequence = seq[::2]
    return new_sequence


def first4_last4_every_other_removed(seq):
    """
    creates a new sequence that drops the first and last 4 characters,
    as well as every other character, in the original string
    """
    new_sequence = seq[4:-4:2]
    return new_sequence


def seq_reversed(seq):
    """
    creates a new sequence that reverses the original sequence using the slice step -1 function
    """
    new_sequence = seq[::-1]
    return new_sequence


def last_third_first_third_mid_third(seq):
    """
    create a new sequence comprised of
    the last third of the original sequence,
    the first third,
    and the middle third
    use the slice function following the same pattern in the exchange_first_last function

    """
    new_sequence = (
        seq[-int(len(seq) / 3) :]
        + seq[: int(len(seq) / 3)]
        + seq[int(len(seq) / 3) : -int(len(seq) / 3)]
    )
    return new_sequence


if __name__ == "__main__":
    original_sequence = "abcdefghijklmnopqrstuvwxyz"
    print("Original Sequence: " + original_sequence)
    print("exchange_first_last: " + exchange_first_last(original_sequence))
    print("every_other_removed: " + every_other_removed(original_sequence))
    print(
        "first4_last4_every_other_removed: "
        + first4_last4_every_other_removed(original_sequence)
    )
    print("seq_reversed: " + seq_reversed(original_sequence))
    print(
        "last_third_first_third_mid_third: "
        + last_third_first_third_mid_third(original_sequence)
    )

    # test block
    assert exchange_first_last("abc") == "cba"
    print("exchange_first_last test passed")
    assert every_other_removed("abcd") == "ac"
    print("every_other_removed test passed")
    assert first4_last4_every_other_removed("abcdefghijk") == "eg"
    print("first4_last4_every_other_removed test passed")
    assert seq_reversed("abcdefg") == "gfedcba"
    print("seq_reversed test passed")
    assert last_third_first_third_mid_third("abcdefghi") == "ghiabcdef"
    print("last_third_first_third_mid_third test passed")
