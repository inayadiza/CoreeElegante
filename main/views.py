from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name' : 'Waode Inaya Diza Mainah',
        'Price': 'Rp. 120.000',
        'Description': 'White Shirt'
    }

    return render(request, "main.html", context)