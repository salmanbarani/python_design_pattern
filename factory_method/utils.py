from abc import ABC, abstractmethod
from colored import fg, bg, attr


class ParamtersRequiredError(Exception):
    """
        This exception is raised when paramter is not given
    """
    pass


class Graphic(ABC):
    """
        Interface that concrete classes must extend from
    """
    @abstractmethod
    def show(self): pass


class MessageBox(Graphic):
    """
        shows a message on the terminal
    """

    def __init__(self, width: int, title: str, body: str, color: str, border="*") -> None:
        self._width = width
        self._title = title
        self._body = body
        self._color = color
        self.border = border

    def _build_box(self):
        title = "".center(self._width, self.border) + "\n" + self.border + \
            self._title.center((self._width - 2), " ") + self.border + \
            "\n" + "".center(self._width, self.border) + "\n"

        body = self.border + self._body.center((self._width - 2), " ") + \
            self.border + "\n" + self.border + "".center(self._width - 2, " ") + self.border + \
            "\n" + "".center(self._width, self.border) + "\n"

        return f"{fg(self._color)}{title}" + f"{fg(self._color)}{ body}"

    def __eq__(self, other: object) -> bool:
        self_attrs = (self._width, self._title,
                      self._body, self._color, self.border)
        other_attrs = (other._width, other._title,
                       other._body, other._color, other.border)

        return self_attrs == other_attrs

    def show(self):
        print(self._build_box())
