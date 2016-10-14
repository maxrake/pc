import zipfile
import os
import utils

ZIPFILE = 'channel.zip'


def level_6(nothing_value):
    """Given a starting value for the 'nothing' value, follow the chain."""
    filename = nothing_value + '.txt'
    comments = []
    
    with zipfile.ZipFile(ZIPFILE) as zip:
        while True:
            print(" [*] Contents of {}:".format(filename))
            with zip.open(filename) as f:
                contents = f.read()
                print("    [+] {}".format(contents))
                comments.append(zip.getinfo(filename).comment)
                if not contents.startswith(b'Next nothing is'):
                    break
                filename = contents.decode().split()[-1] + '.txt'
    
    print(b''.join(comments).decode())


if __name__ == '__main__':
    utils.save_file_from_url('http://www.pythonchallenge.com/pc/def/channel.zip', ZIPFILE, 'wb')
    level_6('readme')
    level_6('90052')
    if os.path.exists(ZIPFILE):
        os.remove(ZIPFILE)
