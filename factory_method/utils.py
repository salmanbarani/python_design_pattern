from abc import ABC, abstractmethod

from colored import attr, bg, fg

SUCCESS_TITLE = "Success"
WARNING_TITLE = "Warning"
ERROR_TITLE = "Error"
INFO_TITLE = "Info"

SUCCESS_BODY = "Your action was successful"
ERROR_BODY = "There was an error"

SUCCESS_COLOR = "green"
WARNING_COLOR = "yellow"
ERROR_COLOR = "red"
INFO_COLOR = "#FF5F9E"


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
    def show(self):
        pass


class MessageBox(Graphic):
    """
    shows a message on the terminal
    """

    def __init__(
        self, width: int, title: str, body: str, color: str, border="*"
    ) -> None:
        self._width = width
        self._title = title
        self._body = body
        self._color = color
        self.border = border

    def _build_box(self):
        title = (
            "".center(self._width, self.border)
            + "\n"
            + self.border
            + self._title.center((self._width - 2), " ")
            + self.border
            + "\n"
            + "".center(self._width, self.border)
            + "\n"
        )

        body = (
            self.border
            + self._body.center((self._width - 2), " ")
            + self.border
            + "\n"
            + self.border
            + "".center(self._width - 2, " ")
            + self.border
            + "\n"
            + "".center(self._width, self.border)
            + "\n"
        )

        return f"{fg(self._color)}{title}" + f"{fg(self._color)}{ body}"

    def __eq__(self, other: object) -> bool:
        self_attrs = (self._width, self._title, self._body, self._color, self.border)
        other_attrs = (
            other._width,
            other._title,
            other._body,
            other._color,
            other.border,
        )

        return self_attrs == other_attrs

    def show(self):
        print(self._build_box())


def body_required(func):
    """
    Decorator to make sure that wrapped function has Not-None body parameter
    """

    def wrapper(*args, **kwargs):
        if kwargs.get("body") is None:
            raise ParamtersRequiredError("body must be given to show the message")
        return func(*args, **kwargs)

    return wrapper


class MessageBoxCreator:
    """
    Abstract class to create message boxs
    """

    def __init__(self, box_width=50) -> None:
        self._box_width = box_width

    def _create(self, title, body, color):
        return MessageBox(width=self._box_width, title=title, body=body, color=color)

    def create_success_message(
        self, title=SUCCESS_TITLE, body=SUCCESS_BODY, color=SUCCESS_COLOR
    ):
        return self._create(title, body, color)

    @body_required
    def create_warning_message(
        self, title=WARNING_TITLE, body=None, color=WARNING_COLOR
    ):
        return self._create(title, body, color)

    def create_error_message(
        self, title=ERROR_TITLE, body=ERROR_BODY, color=ERROR_COLOR
    ):
        return self._create(title, body, color)

    @body_required
    def create_info_message(self, title=INFO_TITLE, body=None, color=INFO_COLOR):
        return self._create(title, body, color)
