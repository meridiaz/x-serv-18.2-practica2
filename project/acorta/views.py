from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import UrlsAcortada


def index(request):
    if request.method == "GET":
        url_list = UrlsAcortada.objects.all()
        context = {'url_list': url_list}
        return render(request, 'acorta/index.html', context)

    elif request.method == "POST":
        valor = request.POST['valor']
        if valor == "":
            return HttpResponseNotFound("Introduce una url para acortar")

        if not(valor.startswith('http://') or
                valor.startswith('https://')):
            requested_item = valor
            valor = 'http://' + valor
        else:
            requested_item = valor[valor.index('/') + 2:]

        try:
            c = UrlsAcortada.objects.get(url=requested_item)
        except UrlsAcortada.DoesNotExist:
            c = UrlsAcortada(url = requested_item)
            c.save()

        context = {'urlPedida': c}
        return render(request, 'acorta/url_pinchable.html', context)

@csrf_exempt
def get_content(request, llave):
    url = get_object_or_404(UrlsAcortada, id=llave).url
    return redirect("http://" + url)
