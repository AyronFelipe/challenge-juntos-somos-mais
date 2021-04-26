import pytest  # noqa
from core.models import Phone


def test_phone_transform():

    number = "(86) 9999-9999"
    transformed = Phone.transform(number)
    assert transformed == "+558699999999"


def test_phone_transform_with_nine():

    number = "(86) 99999-9999"
    transformed = Phone.transform(number)
    assert transformed == "+5586999999999"
