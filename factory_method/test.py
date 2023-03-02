import pytest

from utils import (Graphic, MessageBox, MessageBoxCreator,
                   ParamtersRequiredError)


def creat_sample_message_box():
    return MessageBox(
        width=100, title="sample title", body="sample body", color="green"
    )


def test_creator_creates_message_box():
    """Test that factory returns MessageBox instance"""
    creator = MessageBoxCreator()
    mb = creator.create_success_message()
    assert isinstance(mb, MessageBox)


def test_client_can_customize_box():
    """Test that factory is customizable"""
    width = 200

    data = {"title": "title", "body": "body"}

    creator = MessageBoxCreator(box_width=width)
    factory_mb = creator.create_success_message(**data)

    data.update({"width": width, "color": "green"})

    custom_mb = MessageBox(**data)

    assert factory_mb == custom_mb


def test_body_required_for_warning_and_info():
    """Test that warning and info is required for"""
    mb = MessageBoxCreator()
    with pytest.raises(ParamtersRequiredError):
        mb.create_info_message()

    with pytest.raises(ParamtersRequiredError):
        mb.create_warning_message()


def test_that_message_box_is_instance_of_graphic():
    mb = creat_sample_message_box()
    assert issubclass(mb.__class__, Graphic)


def test_that_messag_gox_creates_message_to_show():
    mb = creat_sample_message_box()
    assert type(mb._build_box()) == str
    assert len(mb._build_box()) > 0
