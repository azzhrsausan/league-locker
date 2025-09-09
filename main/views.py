from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'League Locker',
        'name': 'Sausan Farah Azzahra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)