#Wysylam to co mam, niestety nie udalo mi sie tego do koc zrobic
class Element:
    def __init__(self, content):
        self.content=content

    def render(self):
        print(self.content)

class Document:
    def __init__(self):
        self.elements=[]

    def add_element(self, element:Element):
        self.elements.append(element)

    def render(self):
        for i in self.elements:
            self.elements=i.__str__()
        return '\n'.join(self.elements)

    def __str__(self):
        return f'{self.content}'

class HeaderElement(Element):
    def __str__(self):
        print(self.content)
        print('='*len(self.content))



class LinkElement(Element):
    def __init__(self, napis, link):
        self._link=link
        self._napis=napis


    def render(self):
        print(f'({self.napis})[http://{self.link}]')


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()