import xml.etree.ElementTree as ET
from json import load, dumps

# <--------- CHECK THIS DEFAULT VALUE --------->
def extensionFileValidor(filename, validExt='kml'):
    try:
        str(filename)
    except:
        return "Error - Input no valido - Se esperaba un string"
    extension = filename.split('.')[-1].strip()
    if not (extension == validExt):
        return False
    else:
        return True


def checkTypeFile(file):
    """
    Esta funcion deberia chequear el tipo de arvhivo
    para este caso si es un xml o un xmls y extrer el prefijo si es xmls
    """
    pass


def readXml(xmlFile):
    # Aqui es donde deberia extraer el namespace si fuece necesario
    try:
        xmlFile = xmlFile.decode()
    except:
        return False 
    return ET.fromstring(xmlFile)


def openFile(pathToFile):
    with open(pathToFile, "r") as kFile:
        xmlR = readXml(kFile.read())
        kFile.close()
        return xmlR



def convertToJson(data):
    try:
        # # <--------- TENGO QUE DECODIFICAR ANTES DE GUARDAR A LA BD ESTO DEBE CAMBIARSE --------->
        dataConverted = dumps(data, ensure_ascii=False)
        return dataConverted
    except:
        return False


def extraccionKml(file, filename = "", fileLocation="", prefix='http://www.opengis.net/kml/2.2'):
    if not len(file):
        return 'Empty file'
    # <-->
    if not extensionFileValidor(filename):
        return 'Error en el tipo de archivo (extension)'
    # <-->
    if not readXml(file):
        return 'Can not decode file'
    else:
        xmlFile = readXml(file)
    # <-->
    # Este es el prefijo del xlmns '{http://www.opengis.net/kml/2.2}'
    # SET THIS BEFORE START <-----------------------------------
    prf = {'prefix': prefix}
    # cooking kml ----> # SET THIS BEFORE START <-----------------------------------
    folders = xmlFile.findall('prefix:Document/prefix:Folder', prf)
    # Loop de extraccion sobre el xml
    dataList = list()
    for f in folders:
        dicDeTransicion = dict()
        places = list()
        folderName = f.find('prefix:name', prf).text.strip()
        folderId = None
        dicDeTransicion.update({'folder': folderName, 'folderId': folderId})
        # <-->
        placeList = f.findall('prefix:Placemark', prf)
        if len(placeList):
            for p in placeList:
                placesDict = dict()
                if p.find('prefix:name', prf).text:
                    placeName = p.find('prefix:name', prf).text.strip()
                else:
                    placeName = None
                #placeDescription = p.find('prefix:description', prf).text.strip()
                lon, lat, z = p.find("prefix:Point", prf)[0].text.strip().split(",")
                placesDict.update({
                    'placeName': placeName, 
                    #'placeDescription': placeDescription, 
                    'lat': lat, 
                    'lon': lon
                    })
                # <-->
                extendedData = p.find('prefix:ExtendedData', prf)
                if len(extendedData):
                    for d in extendedData:
                        atributo = d.attrib["name"]
                        valor = d[0].text
                        placesDict.update({
                            f'{atributo}': valor
                        })
                places.append(placesDict)
        else:
            continue
        dicDeTransicion.update({'places': places})
        dataList.append(dicDeTransicion)

    data = {'data': dataList}
    jsonData = convertToJson(data)
    if not jsonData:
        return 'Error al generar Json'
    else:
        return jsonData