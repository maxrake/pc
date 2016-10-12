import requests


def level_4(nothing_value):
    """Given a starting value for the 'nothing' parameter, follow the chain.
    
    The result text will be analyzed for the string pattern 'and the next nothing is'.
    If that pattern is found, then the next nothing parameter will be assumed to be at
    the end of the string and the search will continue.
    Otherwise, stop searching and ask the user what parameter they would like to try next.
    """
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url =  base_url + nothing_value
    
    while True:
        print(" [*] Getting text for {} ...".format(url), end='')
        r = requests.get(url)
        r.raise_for_status()
        print("Done")
        print("    [+] {}".format(r.text))
        if not r.text.startswith('and the next nothing is'):
            return
        url = base_url + r.text.split()[-1]


if __name__ == '__main__':
    try:
        while True:
            nothing_value = input("Enter a value for the nothing parameter to follow: ")
            level_4(nothing_value)
    except KeyboardInterrupt:
        print("\n\n [*] All done. I hope you found what you were looking for...")
