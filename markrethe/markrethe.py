from .base import Base
from .basic import BasicSyntax
from .extended import ExtendedSyntax


class Markrethe(Base, BasicSyntax, ExtendedSyntax):
    def __call__(self, text: str) -> None:
        """Call the instance as a function to write a paragraph.

        Args:
            text: The text to write as a paragraph.
        """
        self.paragraph(text)
