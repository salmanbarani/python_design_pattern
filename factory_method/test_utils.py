from utils import MessageBox, Graphic


def creat_sample_message_boxy():
    return MessageBox(
        width=100,
        title="sample title",
        body="sample body",
        color="green"
    )


def test_that_message_box_is_instance_of_graphic():
    mb = creat_sample_message_boxy()
    assert issubclass(mb.__class__, Graphic)


def test_that_messag_gox_creates_message_to_show():
    mb = creat_sample_message_boxy()
    assert type(mb._build_box()) == str
    assert len(mb._build_box()) > 0
