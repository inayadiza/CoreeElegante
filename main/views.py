from django.shortcuts import render, redirect
from main.forms import ClothingEntryForm
from main.models import ClothingEntry 
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    clothing_entries = ClothingEntry.objects.all()  # Fetch all clothing items

    context = {
        'Name': 'Brown Cardigan',
        'Price': 'Rp. 180.000',
        'Description': 'A brown cardigan is a cozy, versatile layering piece, made from soft materials like wool or cotton.',
        'clothing_entries': clothing_entries,  # Pass clothing items to the template
    }

    return render(request, "main.html", context)

def create_clothing_entry(request):
    form = ClothingEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_clothing_entry.html", context)

def show_xml(request):
    data = ClothingEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ClothingEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ClothingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ClothingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
