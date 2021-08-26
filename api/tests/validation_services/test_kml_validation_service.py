import pytest

from api.services.validation_services import XMLValidationService
from api.services.xml_extensions import XMLExtensions
from api.tests.utils import get_scrapper_fixture_dir


@pytest.fixture
def cruces_kml():
    fixture_dir = get_scrapper_fixture_dir(__file__)
    with open(f'{fixture_dir}/cruces.kml', 'rb') as content:
        kml = content.read()
    return kml


def test_xml_validation_service_not_empty_is_true(cruces_kml):
    kml_validation_service = XMLValidationService(extension=XMLExtensions.kml.value)
    is_empty = kml_validation_service.not_empty(cruces_kml)

    assert is_empty == True


def test_xml_validation_service_not_empty_false():
    kml_validation_service = XMLValidationService(extension=XMLExtensions.kml.value)
    is_empty = kml_validation_service.not_empty('')

    assert is_empty == False

    is_empty = kml_validation_service.not_empty(3)

    assert is_empty == False
