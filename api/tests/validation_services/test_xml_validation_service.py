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


def test_xml_validation_service_is_empty_false(cruces_kml):
    kml_validation_service = XMLValidationService()
    is_empty = kml_validation_service.is_empty(cruces_kml)

    assert is_empty == False


def test_xml_validation_service_is_empty():
    kml_validation_service = XMLValidationService()
    is_empty = kml_validation_service.is_empty('')

    assert is_empty == True


def test_xml_validation_service_has_valid_extension():
    kml_validation_service = XMLValidationService()
    valid_extension = kml_validation_service.has_valid_extension('cruces.kml')

    assert valid_extension == True

    valid_extension = kml_validation_service.has_valid_extension('cruces.osc')

    assert valid_extension == True


def test_xml_validation_service_has_not_valid_extension():
    kml_validation_service = XMLValidationService()
    valid_extension = kml_validation_service.has_valid_extension('cruces.txt')

    assert valid_extension == False

