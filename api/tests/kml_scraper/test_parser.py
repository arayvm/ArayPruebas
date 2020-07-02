import pytest
from api.tests.utils import get_scrapper_fixture_dir
from api.services.kml_scraper_service import KmlParser



@pytest.fixture
def cruces_kml():
    fixture_dir = get_scrapper_fixture_dir(__file__)
    with open(f'{fixture_dir}/cruces.kml', 'rb') as content:
        kml = content.read()
    return kml


def test_asd(cruces_kml):
    parser = KmlParser()
    parser.extract_values(cruces_kml)