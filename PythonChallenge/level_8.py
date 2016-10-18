import bz2


def level_8(text):
    """Return the bzip2 decompressed version of the provided text."""
    return bz2.decompress(bytes(text, 'latin-1'))


if __name__ == '__main__':
    # from comments in source
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!' +\
        '\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]' +\
        '\xc9\x14\xe1BBP\x91\xf08'
    print(' [+] Username: {}'.format(level_8(un)))
    print(' [+] Password: {}'.format(level_8(pw)))
