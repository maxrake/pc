import pickle
import requests


def level_5():
    """Solve level 5 of the Python Challenge."""
    r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
    r.raise_for_status()

    unpickled = pickle.loads(r.content)

    # after much trial and error, it was determined that the unpickled
    # content represents a series of rows in an ASCII art image
    for row in unpickled:
        for character, length in row:
            print(character * length, end='')
        print()


if __name__ == '__main__':
    level_5()
