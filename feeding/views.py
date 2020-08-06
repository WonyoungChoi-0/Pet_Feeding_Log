from django.shortcuts import render
from feeding.forms import Feeding_Entry_Form
from feeding.models import Feeding_Entry
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'feeding/index.html')

def feeding_schedule(request):

    form = Feeding_Entry_Form()

    if 'form' in request.POST:
        form = Feeding_Entry_Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/feeding_schedule/')
        else:
            print('ERROR FORM INVALID')

    feeding_entries = Feeding_Entry.objects.order_by('-date')

    return render(request, 'feeding/feeding_schedule.html', {'feeding_form':form, 'feeding_entries':feeding_entries})

def delete_entry(request, pk):
    if request.method == 'POST':
        entry = Feeding_Entry.objects.get(pk=pk)
        entry.delete()
    return HttpResponseRedirect('/feeding_schedule/')
