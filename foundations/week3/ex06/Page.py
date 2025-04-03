from elem import Elem, Text
from elements import H1, Body, Title, Html, Head, Img

class Page:
    VALID_TAGS = {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'Text'}

    def __init__(self, root_element):
        self.root_element = root_element

    def is_valid(self, element=None):
        if element is None:
            element = self.root_element

        if isinstance(element, Text):
            return

        # Check if the element's tag is valid
        if element.tag not in Page.VALID_TAGS:
           return False

        # Validate specific structures
        if element.tag == 'html':
            children_tags = [child.tag for child in element.content]
            if children_tags != ['head', 'body']:
                return False

        if element.tag == 'head':
            if len(element.content) != 1 or element.content[0].tag != 'title':
                return False

        if element.tag in {'body', 'div'}:
            allowed_children = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'Text'}
            for child in element.content:
                if isinstance(child, Text):
                    continue  # Text is always valid in these contexts
                if child.tag not in allowed_children:
                    return False

        if element.tag in {'title', 'h1', 'h2', 'li', 'th', 'td'}:
            if len(element.content) != 1:
                return False
            if isinstance(element.content[0], Text):
                pass  # Valid if content is a single Text object
            else:
                return False

        if element.tag == 'p':
            if len(element.content) != 1 or not isinstance(element.content[0], Text):
                return False

        if element.tag == 'span':
            allowed_children = {'Text', 'p'}
            for child in element.content:
                if isinstance(child, Text):
                    continue  # Text is always valid in span
                if child.tag not in allowed_children:
                    return False

        if element.tag in {'ul', 'ol'}:
            if not all(child.tag == 'li' for child in element.content):
                return False

        if element.tag == 'tr':
            children_tags = {child.tag for child in element.content}
            if children_tags - {'th', 'td'}:
                return False
            if 'th' in children_tags and 'td' in children_tags:
                return False

        if element.tag == 'table':
            if not all(child.tag == 'tr' for child in element.content):
                return False

        # Recursively validate all children
        return all(self.is_valid(child) for child in element.content)

    def __str__(self):
        if self.root_element.tag == 'html':
            return '<!DOCTYPE html>\n' + str(self.root_element)
        return str(self.root_element)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


if __name__ == "__main__":
    html = Html([
        Head([
            Title(Text('"Hello ground!"'))
        ]),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])

    page = Page(html)
    print(page.is_valid())
    print(page)
    page.write_to_file('output.html')
