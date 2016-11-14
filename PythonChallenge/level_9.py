import re
import utils
from PIL import Image, ImageDraw


def level_9(text):
    """Find the coordinates in the comments and draw the lines."""
    mo = re.search(r'first:((\d*,?)*)', text.replace('\n', ''))
    if mo:
        first_pat = mo.group(1)
        first = [int(num) for num in first_pat.split(',')]
        im = Image.new('RGBA', (max(first) + 10, max(first) + 10))
        draw = ImageDraw.Draw(im)
        draw.line(first)

    mo = re.search(r'second:((\d*,?)*)', text.replace('\n', ''))
    if mo:
        second_pat = mo.group(1)
        second = [int(num) for num in second_pat.split(',')]
        draw.line(second)
        im.show()


if __name__ == '__main__':
    comments = utils.get_comments(
        'http://www.pythonchallenge.com/pc/return/good.html', user='huge')
    if comments:
        for comment in comments:
            level_9(comment)
    else:
        print(" [*] No comments found.")
