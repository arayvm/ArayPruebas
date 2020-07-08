import xml.etree.ElementTree as ET


class KmlParser:

    def extract_values(self, file: bytes):
        content = ET.fromstring(file.decode())
        import ipdb; ipdb.set_trace()
        # ----> # SET THIS BEFORE START <-----
        # Extraer el prefijo del xml, aqui  se introduce por defecto
        prefix = "http://www.opengis.net/kml/2.2"
        prf = {'prefix': prefix}
        # ----> # SET THIS BEFORE STARTf <-----
