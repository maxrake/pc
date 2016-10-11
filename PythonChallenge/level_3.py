import re
import utils


def level_3(text):
    """Find the lowercase letters in text that are surrounded by exactly 3 uppercase letters."""
    pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
    return ''.join(pattern.findall(text))


if __name__ == '__main__':
    comments = utils.get_comments('http://www.pythonchallenge.com/pc/def/equality.html')
    if comments:
        for comment in comments:
            print(level_3(comment))
    else:
        print(" [*] No comments found.")