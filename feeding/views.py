from django.shortcuts import render
from feeding.forms import Feeding_Entry_Form, Pet_Form
from feeding.models import Feeding_Entry, Pet
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    pets = Pet.objects.order_by('name')
    return render(request, 'feeding/index.html', {'pets':pets})

def feeding_schedule(request, pk):

    pet = Pet.objects.get(pk=pk)
    form = Feeding_Entry_Form()

    if 'form' in request.POST:
        form = Feeding_Entry_Form(request.POST)
        form.instance.pet_id = pk
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('feeding:feeding_schedule2', kwargs={'pk':pk}))
        else:
            print('ERROR FORM INVALID')
    feeding_entries = Feeding_Entry.objects.filter(pet=pk)
    feeding_entries = feeding_entries.order_by('-date')

    return render(request, 'feeding/feeding_schedule.html', {'pet':pet,'feeding_form':form, 'feeding_entries':feeding_entries})

def delete(request, pk):
    if request.method == 'POST':
        if 'delete_entry' in request.POST:
            entry = Feeding_Entry.objects.get(pk=pk)
            entry.delete()
            return HttpResponseRedirect('/feeding_schedule/')
        if 'delete_pet' in request.POST:
            pet = Pet.objects.get(pk=pk)
            pet.delete()
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/feeding_schedule/')

def edit_pet(request, pk):

    pet = Pet.objects.get(pk=pk)
    form = Pet_Form(instance=pet)

    if request.method == "POST":
        form = Pet_Form(request.POST, instance=pet)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print('ERROR FORM INVALID')
    return render(request, 'feeding/edit_pet.html', {'form':form, 'pet':pet})

def edit_entry(request, pk):
    entry = Feeding_Entry.objects.get(pk=pk)
    form = Feeding_Entry_Form(instance=entry)

    if request.method == "POST":
        form = Feeding_Entry_Form(request.POST, instance=entry)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/feeding_schedule/')
        else:
            print('ERROR FORM INVALID')
    return render(request, 'feeding/edit_entry.html', {'form':form, 'entry':entry})

def register_pet(request):

    form = Pet_Form(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            if 'profile_pic' in request.FILES:
                form.profile_pic = request.FILES['profile_pic']
                print('success')
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

    return render(request, 'feeding/register_pet.html', {'form':form})
