"""level 10

Find len(sequence[30])
Given the sequence = [1, 11, 21, 1211, 111221, ...]
This is the 'Look and Say' sequence:
https://en.wikipedia.org/wiki/Look-and-say_sequence
"""


def level_10(num):
    """Return the next number in the 'see-and-say' sequence, given a number.
    
    The next number in the sequence is found by saying the count of each digit,
    in order, in the current number.
    """
    # ensure the input is a number as a string
    num_as_str = str(num)
    
    count = 0
    current_digit = num_as_str[0]
    next_num_as_str = ''

    for digit in num_as_str:
        if digit == current_digit:
            count += 1
        else:
            next_num_as_str += '{}{}'.format(count, current_digit)
            count = 1
            current_digit = digit
    else:
        next_num_as_str += '{}{}'.format(count, current_digit)
    
    return next_num_as_str


if __name__ == '__main__':
    sequence = ['1']
    for x in range(30):
        sequence.append(level_10(sequence[x]))
    print('\n [+] len(sequence[30]): {}'.format(len(sequence[30])))
