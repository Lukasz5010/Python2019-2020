#Wysylam to co mam, niestety nie udalo mi sie tego do koc zrobic
class Element:
    def __init__(self, content):
        self.content=content

    def render(self):
        pass

class Document:
    def __init__(self):
        self.elements=[]

    def add_element(self, element:Element):
        self.elements.extend(element)

    def render(self):
        return '\n'.join(self.elements)


class HeaderElement(Element):
    def render(self):
        print(self.content)
        print()
        print('='*len(self.content))



class LinkElement(Element):
    def __init__(self, napis, link):
        self._link=link
        self._napis=napis


    def render(self):
        print(f'({napis})[http://{link}]')


 document = Document()
 document.add_element(HeaderElement('Header'))
 document.add_element(LinkElement('ABC', 'abc.com'))
 document.add_element(Element('Simple'))
 document.render()