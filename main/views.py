from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name' : 'Brown Cardigan',
        'Price': 'Rp. 180.000',
        'Description': 'A brown cardigan is a cozy, versatile layering piece, made from soft materials like wool or cotton.'
    }

    return render(request, "main.html", context)