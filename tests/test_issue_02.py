import pytest
import morse


@pytest.mark.parametrize('encoded,decoded', [
    ('... --- ...', 'SOS'),
    ('.-. ..- ... ... .. .-', 'RUSSIA'),
    ('.--. -.-- - .... --- -.', 'PYTHON'),
    ('.- ...- .. - ---', 'AVITO')
])
def test_decode(encoded, decoded):
    assert morse.decode(encoded) == decoded
