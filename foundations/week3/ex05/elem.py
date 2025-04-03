class Elem:
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        attrs = ''.join([f' {key}="{value}"' for key, value in self.attr.items()])
        if self.tag_type == 'double':
            content = ''.join([str(c) for c in self.content])
            return f"<{self.tag}{attrs}>{content}</{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag}{attrs} />"

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if isinstance(content, Text):
            self.content.append(content)
        elif type(content) == list:
            self.content += [c for c in content if c != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (type(content) == list and all(isinstance(c, Elem) or isinstance(c, Text) for c in content)))

class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '<').replace('>', '>')

if __name__ == "__main__":
    html = Elem(tag='html', content=[
        Elem(tag='head', content=Elem(tag='title', content=Text('"Hello ground!"'))),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('"Oh no, not again!"')),
            Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])

    print(html)
