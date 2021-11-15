from django.shortcuts import render

# Create your views here.

def tickets_page(request):


    context = {

    }
    return render(request, 'tickets/tickets.html', context)


