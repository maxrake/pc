from html.parser import HTMLParser
import requests


class MyHTMLParser(HTMLParser):
    comments = []
    def handle_comment(self, data):
        """Append HTML comment data to class attribute as a string with all newlines removed."""
        if data:
            self.comments.append(data.replace('\n', ''))


def get_comments(url):
    """Return a list of HTML comment data given a URL as a string."""
    print(' [*] Parsing {} for comments ...'.format(url), end='')
    r = requests.get(url)
    print('Done')
    r.raise_for_status()

    parser = MyHTMLParser()
    parser.feed(r.text)
    parser.close()

    return parser.comments