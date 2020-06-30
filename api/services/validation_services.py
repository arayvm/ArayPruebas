

class XMLValidationService:
    def __init__(self, extension: str):
        self._extension = extension
    
    def not_empty(self, xml_file: bytes) -> bool:
        try:
            return len(xml_file) > 1
        except TypeError:
            return False

    def validate_file_extension(self, xml_file: bytes) -> bool:
        import ipdb; ipdb.set_trace()
        # https://docs.python.org/3/library/pathlib.html

