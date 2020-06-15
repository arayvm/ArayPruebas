from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .forms import UploadFileForm
from .extraccionKml import extraction
# from .extraccion import testFunc

def index(request):
    template = loader.get_template('api/index.html')
    cont = dict()
    if request.GET.get('view', False):
        content = {
            'Caller': request.path,
            'Query': [x for x in request.GET.keys()],
            'Method': request.method,
            'Content Type': request.content_type
        }
        cont.update({'action': content})
    else:
        cont.update({'action': 'home'})
    return HttpResponse(template.render(cont, request))


def load(request):
    template = loader.get_template('api/conteiner.html')
    action = {'action': 'load'}
    return HttpResponse(template.render(action, request))



def procesing(request):
    template = loader.get_template('api/prosesing.html')
    #body = request.body
    #schema = request.schema
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        try:
            fileRequest = request.FILES['file']
        except :
            return HttpResponse(template.render({'action': 'No se recibio archivo'}, request))
        action = False
        actionDetails = {
            'name':fileRequest.name,
            'path': request.path,
            'pattInf': request.path_info,
            'method': request.method,
            'encoding': request.POST.encoding,
            'contentType': request.content_type,
            'request.FILES': request.FILES.keys(),
            'meta': request.META,
            'headers': request.headers,
            'readed': request.FILES['file'].read(),
            'typeRead': type(request.FILES['file'].read()),
            'choiceFile': request.POST['fileType']
        }
        if not action:
            action = {extraction(actionDetails['readed'],  filename=actionDetails['name'], validExt=actionDetails['choiceFile'])}
    return HttpResponse(template.render({'action':action}))

'''
def procesing(request):
    template = loader.get_template('api/prosesing.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # fileType = form.fileType
        action = {'name': request.FILES['file'].name, 'attrs':request.POST['fileType']}
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponse(template.render(action, request))
    else:
        form = UploadFileForm()
        action = {'name': 'Error en la carga del archivo'}
    return HttpResponse(template.render(action, request))
'''