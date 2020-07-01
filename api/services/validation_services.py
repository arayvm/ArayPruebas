from api.services.xml_extensions import XMLExtensions

class XMLValidationService:
    def __init__(self, name='', extension='', length=''):
        self.extension = extension
        self.name = name
        self.length = length
    
    def not_empty(self, xml_file: bytes) -> bool:
        self.length = len(xml_file)
        try:
            return len(xml_file) > 1
        except TypeError:
            return False

    def validate_file_extension(self, filename: str) -> bool:
        extension = filename.split('.')[-1].strip()
        self.extension = extension
        self.name = filename.split('.')[0].strip()
        #testExt = XMLExtensions.kml
        testExt = 'kml'
        res = (extension == testExt)
        return res





