import pytest
from factories import MessageBoxCreator
from utils import MessageBox


def test_creator_creates_message_box():
    """Test that factory returns MessageBox instance"""
    creator = MessageBoxCreator()
    mb = creator.create_success_message()
    assert isinstance(mb, MessageBox)


def test_client_can_customize_box():
    """Test that factory is customizable"""
    width = 200

    data = {
        "title": "title",
        "body": "body"
    }

    creator = MessageBoxCreator(box_width=width)
    factory_mb = creator.create_success_message(**data)

    data.update({"width": width, "color": "green"})

    custom_mb = MessageBox(**data)

    assert factory_mb == custom_mb


def test_body_required_for_warning_and_info():
    """Test that warning and info is required for """
    pass
