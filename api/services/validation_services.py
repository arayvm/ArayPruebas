from api.services.xml_extensions import XMLExtensions
from pathlib import Path


class XMLValidationService:

    def validate(self, xml_file: bytes):
        if self.is_empty(xml_file):
            pass

        if self.has_valid_exension(xml_file.name):
            pass

    def is_empty(self, xml_file: bytes) -> bool:
        try:
            return len(xml_file) < 1
        except TypeError:
            return False

    def has_valid_extension(self, filename: str) -> bool:
        fileSuffix = Path(filename).suffix
        validExtensions = [XMLExtensions.kml.value, XMLExtensions.osc.value]
        return (fileSuffix in validExtensions)





