import os
import unittest
from html.parser import HTMLParser

class H1Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_texts = []
        self._recording = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'h1':
            self._recording = True

    def handle_endtag(self, tag):
        if tag.lower() == 'h1':
            self._recording = False

    def handle_data(self, data):
        if self._recording:
            text = data.strip()
            if text:
                self.h1_texts.append(text)

class TestIndexHTML(unittest.TestCase):
    def test_h1_contains_hi(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        index_path = os.path.join(repo_root, 'index.html')
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        parser = H1Parser()
        parser.feed(content)
        self.assertIn('Hi', parser.h1_texts)

if __name__ == '__main__':
    unittest.main()
