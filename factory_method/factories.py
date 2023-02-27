from utils import Graphic, MessageBox
from utils import ParamtersRequiredError

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


def body_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('body') is None:
            raise ParamtersRequiredError(
                "body must be given to show the message")
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
            self, title=SUCCESS_TITLE, body=SUCCESS_BODY, color=SUCCESS_COLOR):
        return self._create(title, body, color)

    @body_required
    def create_warning_message(
            self, title=WARNING_TITLE, body=None, color=WARNING_COLOR):
        return self._create(title, body, color)

    def create_error_message(self, title=ERROR_TITLE,
                             body=ERROR_BODY, color=ERROR_COLOR):
        return self._create(title, body, color)

    @body_required
    def create_info_message(self, title=INFO_TITLE,
                            body=None, color=INFO_COLOR):
        return self._create(title, body, color)
