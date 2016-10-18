import os
import re
import utils
from PIL import Image

IMAGE = 'oxygen.png'


def level_7():
    """Find the message in the image."""
    im = Image.open(IMAGE)
    
    print(' [*] Getting all gray pixels from the middle row of the image...')
    gray_pixels = [im.getpixel((x, int(im.height / 2)))[0] for x in range(im.width)]
    
    print(' [*] The gray pixels repeat every 7 pixels. Reducing the data set...')
    message = ''.join(chr(pix) for pix in gray_pixels[::7])
    print(' [*] The hidden message is:')
    print('    [+] {}'.format(message))

    print(' [*] Finding sub-message within message by converting all numbers to characters...')
    sub_message = re.findall(r'\d+', message)
    next_level = ''.join(map(chr, map(int, sub_message)))
    print('    [+] The next level is: {}'.format(next_level))


if __name__ == '__main__':
    utils.save_file_from_url('http://www.pythonchallenge.com/pc/def/oxygen.png', IMAGE, 'wb')
    level_7()
    if os.path.exists(IMAGE):
        os.remove(IMAGE)
