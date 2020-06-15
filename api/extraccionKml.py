import xml.etree.ElementTree as ET
from json import load, dumps


# <--------- CHECK THIS DEFAULT VALUE --------->
def extensionFileValidator(filename, validExt):
    try:
        str(filename)
    except AttributeError:
        return False
    extension = filename.split('.')[-1].strip()
    if not (extension == validExt):
        return False
    else:
        return True


def xmlDecode(xmlFile):
    """
    :param xmlFile: file en memoria subido por el usuario
    :return: booleano False si se no se puede convertir a string True si decode funciona bien
    """
    try:
        xmlFile.decode()
    except:
        return False
    return True

def etParse(file):
    try:
        ET.fromstring(file)
        return True
    except :
        return False


def fileCheckListValidation(file, filename, validExt):
    """
    :param file: Archivo subido por el usuraio :: file type bytes
    :param filename: Este paramentro viene de la lectura de los headers del file subido
    :param validExt: la extencion validad es la extension que el usuario indica para su archivo
    :return: booleano False si no se cumplen las condiciones True si esta bien
    """
    if not len(file):
        return {'status': False, 'error': 'Empty file'}
    # <-->
    if not extensionFileValidator(filename, validExt):
        return {'status': False, 'error': 'Error en el tipo de archivo (extension) - SOLO ARCHIVOS KML SON PERMITIDOS POR AHORA'}
    # <--> check decode bytes into string
    if not xmlDecode(file):
        return {'status': False, 'error': 'Can not decode file'}
    # check library succes parse
    if not etParse(file):
        return {'status': False, 'error': 'Library parse error (xml format - structure)'}
    return {'status': True}


def convertToJson(data):
    try:
        # # <--------- TENGO QUE DECODIFICAR ANTES DE GUARDAR A LA BD ESTO DEBE CAMBIARSE --------->
        dataConverted = dumps(data, ensure_ascii=False)
        return dataConverted
    except:
        return False


def xmlKmlParser(file):
    xmlFile = ET.fromstring(file.decode())
    prefix = "http://www.opengis.net/kml/2.2"
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
                # placeDescription = p.find('prefix:description', prf).text.strip()
                lon, lat, z = p.find("prefix:Point", prf)[0].text.strip().split(",")
                placesDict.update({
                    'placeName': placeName,
                    # 'placeDescription': placeDescription,
                    'lat': lat,
                    'lon': lon
                })
                # <-->
                extendedData = p.find('prefix:ExtendedData', prf)
                try:
                    if len(extendedData):
                        for d in extendedData:
                            atributo = d.attrib["name"]
                            valor = d[0].text
                            placesDict.update({
                                f'{atributo}': valor
                            })
                    places.append(placesDict)
                except TypeError:
                    continue
        else:
            continue
        dicDeTransicion.update({'places': places})
        dataList.append(dicDeTransicion)

    return {'status': True, 'content': {'data': dataList}}


def extraction(file,  filename="", validExt=''):
    # <-->
    checkList = fileCheckListValidation(file, filename, validExt)
    if not checkList['status']:
        return checkList['error']
   #<-->
    data = xmlKmlParser(file)
    if not data['status']:
        return data['error']
    else:
        data = data['content']

    jsonData = convertToJson(data)
    if not jsonData:
        return 'Error al generar Json'
    else:
        return jsonData
