from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from django.views.decorators.http import require_http_methods

from . import models
from . import forms


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


@require_http_methods(['GET', 'POST'])
def add_meter_data(request):

    if request.method == 'POST':
        form = forms.MeterForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse(status=204)


    return render(request, template_name='app/form.html')


@require_http_methods(['GET', 'POST', 'DELETE'])
def add_control_data(request):
   
    if request.method == 'POST':
        form = forms.ControlForm(request.POST)
    
        if form.is_valid():
            form.save()
   
            return HttpResponse(status=204)

    results = models.Control.objects.all()

    return render(request, template_name='app/fixed_sidebar.html', context={'data': results})


@require_http_methods(['POST'])
def delete_control_data(request, control_id):

    member = models.Control.objects.filter(control_id=control_id)
    member.delete()
    return redirect('add-control-data')


@require_http_methods(['POST', 'GET'])
def delete_meter(request):

    meter_id = request.POST.get('meter_id', '')
    print("Meter: ", request.POST)
    if meter_id:
        member = models.Meter.objects.filter(meter_id=meter_id)
        member.delete()

    results = models.Meter.objects.all()

    return render(request, template_name='app/form_advanced.html', context={"data": results})


def showdata(request):
    results = models.Meter.objects.all()
    
    return render(request, template_name='app/index4.html', context={"data": results})
