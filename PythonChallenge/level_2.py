from collections import Counter


def level_2(text):
    """Find the characters in the input text string that only appear once."""
    count_dict = dict(Counter(text).most_common())
    return ''.join(letter for letter in text if count_dict[letter] == 1)


if __name__ == '__main__':
    with open(r'extras\level_2.txt') as f:
        print(level_2(f.read()))
