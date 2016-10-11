from collections import Counter
import utils


def level_2(text):
    """Find the characters in the input text string that only appear once."""
    count_dict = dict(Counter(text).most_common())
    return ''.join(letter for letter in text if count_dict[letter] == 1)


if __name__ == '__main__':
    comments = utils.get_comments('http://www.pythonchallenge.com/pc/def/ocr.html')
    if comments:
        for comment in comments:
            print(level_2(comment))
    else:
        print(" [*] No comments found.")
