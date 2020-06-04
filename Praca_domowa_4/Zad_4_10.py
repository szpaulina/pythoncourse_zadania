"""Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown.
Stwórz klasę bazową Element zawierającą podstawową implementację metody render()
oraz kilka jej klas pochodnych. Stwórz klasę Document umożliwiającą wyrenderowanie dodanych elementów.
Przykład użycia:
> document = Document()
> document.add_element(HeaderElement('Header'))
> document.add_element(LinkElement('ABC', 'abc.com'))
> document.add_element(Element('Simple'))
> document.render()
Header
======
(ABC)[http://abc.com]
Simple"""

from abc import ABC, abstractmethod

class Element(ABC):
    def __init__(self, interior: str, link=""):
        self.interior = interior
        self.link = link

    @abstractmethod
    def render(self):
        pass

class HeaderElement(Element):
    def render(self):
        return f"{self.interior}\n" \
               f"======"

class LinkElement(Element):
    def render(self):
        return f"({self.interior})[http://{self.link}]"

class Element(Element):
    def render(self):
        return f"{self.interior}\n"

class Document:
    def __init__(self):
        self._elements = []

    def add_element(self, element: Element):
        self._elements.append(element)

    def render(self):
        for element in self._elements:
            print(element.render())

document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()

