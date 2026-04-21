import pint
import pytest
from volume import volume, _si


def test_volume_for_plain_numbers():
    result = volume(2, 3, 4)

    assert result.to(_si.m**3).magnitude == pytest.approx(24.0)


def test_volume_converts_units_properly():
    result = volume(
        2 * _si.m,
        50 * _si.cm,
        1000 * _si.mm,
    )

    assert result.check("[length] ** 3")
    assert result.to(_si.m**3).magnitude == pytest.approx(1.0)


def test_volume_raises_error_for_negative_input():
    with pytest.raises(ValueError):
        volume(-2, 3, 4)


def test_volume_rejects_wrong_units():
    with pytest.raises(pint.errors.DimensionalityError):
        volume(2 * _si.kg, 3 * _si.m, 4 * _si.m)