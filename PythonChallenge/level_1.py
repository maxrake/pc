from string import ascii_lowercase
import textwrap


def level_1(text):
    """Decode input text using an alpha+2 substitution cipher."""
    table = str.maketrans(ascii_lowercase, ascii_lowercase[2:] + 'ab')
    return text.translate(table)


if __name__ == '__main__':
    input = """\
        g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc 
        dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm 
        jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
        """
    
    print(level_1(textwrap.dedent(input)))
    print(level_1('map'))
