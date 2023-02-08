import logging
import xml.etree.cElementTree as xml
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    nodoPrincipal = xml.Element('WebService')
    xml.SubElement(nodoPrincipal,'Mensaje').text = 'Hola Mundo!'
    xmlResponse = xml.ElementTree(nodoPrincipal)

    return func.HttpResponse(
            'Hola mundo!',
            status_code=200
    )