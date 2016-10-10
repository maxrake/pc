from collections import Counter


def level_2(text, num_least_common):
    """Find the rare characters in the input text string."""
    return Counter(text).most_common()[:-num_least_common-1:-1]


if __name__ == '__main__':
    with open(r'extras\level_2.txt') as f:
        source = f.read().strip()
        print(level_2(source, 10))
