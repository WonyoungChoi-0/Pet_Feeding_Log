from django.shortcuts import render
from feeding.forms import Feeding_Entry_Form, Pet_Form, User_Form, User_Login
from feeding.models import Feeding_Entry, Pet
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    pets = Pet.objects.order_by('name')
    pets = pets.filter(user=request.user)
    return render(request, 'feeding/index.html', {'pets':pets})

@login_required
def feeding_schedule(request, pk):

    pet = Pet.objects.get(pk=pk)
    form = Feeding_Entry_Form()

    if 'form' in request.POST:
        form = Feeding_Entry_Form(request.POST)
        form.instance.pet_id = pk
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('feeding:feeding_schedule', kwargs={'pk':pk}))
        else:
            print('ERROR FORM INVALID')
    feeding_entries = Feeding_Entry.objects.filter(pet=pk)
    feeding_entries = feeding_entries.order_by('-date')

    return render(request, 'feeding/feeding_schedule.html', {'pet':pet,'feeding_form':form, 'feeding_entries':feeding_entries})

@login_required
def delete(request, pk):
    if request.method == 'POST':
        if 'delete_entry' in request.POST:
            entry = Feeding_Entry.objects.get(pk=pk)
            entry.delete()
            return HttpResponseRedirect(reverse('feeding:feeding_schedule', kwargs={'pk':entry.pet.id}))
    else:
        pet = Pet.objects.get(pk=pk)
        pet.delete()

    return HttpResponseRedirect(reverse('feeding:index'))

@login_required
def edit_pet(request, pk):

    pet = Pet.objects.get(pk=pk)
    form = Pet_Form(instance=pet)

    if request.method == "POST":
        form = Pet_Form(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            if 'profile_pic' in request.FILES:
                form.profile_pic = request.FILES['profile_pic']
            form.save(commit=True)
            return HttpResponseRedirect(reverse('feeding:index'))
        else:
            print('ERROR FORM INVALID')
    return render(request, 'feeding/edit_pet.html', {'form':form, 'pet':pet})

@login_required
def edit_entry(request, pk):
    entry = Feeding_Entry.objects.get(pk=pk)
    form = Feeding_Entry_Form(instance=entry)

    if request.method == "POST":
        form = Feeding_Entry_Form(request.POST, instance=entry)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('feeding:feeding_schedule', kwargs={'pk':entry.pet.id}))
        else:
            print('ERROR FORM INVALID')
    return render(request, 'feeding/edit_entry.html', {'form':form, 'entry':entry, 'pet':entry.pet})

@login_required
def register_pet(request):

    if request.method == "POST":
        form = Pet_Form(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            if 'profile_pic' in request.FILES:
                form.profile_pic = request.FILES['profile_pic']
            form.save(commit=True)
            return HttpResponseRedirect(reverse('feeding:index'))
        else:
            print(form.errors)
    else:
        form = Pet_Form()

    return render(request, 'feeding/register_pet.html', {'form':form})

def register(request):

    registered = False

    if request.method == "POST":
        user_form = User_Form(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            auth = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, auth)
            return HttpResponseRedirect(reverse('feeding:index'))

        else:
            print(user_form.errors)

    else:
        user_form = User_Form()

    return render(request, 'feeding/registration.html',
                                {'user_form':user_form, 'registered':registered})

def user_login(request):
    form = User_Login()
    if request.method == 'POST':

        user_login = User_Login(data=request.POST)

        if user_login.is_valid():
            username = user_login.cleaned_data['email']
            password = user_login.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('feeding:index'))
                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')

            else:
                print(user_login.errors)
                messages.error(request,'email or password not correct')
                return HttpResponseRedirect(reverse('feeding:user_login'))
        else:
            messages.error(request,'email or password not correct')

    return render(request, 'feeding/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('feeding:user_login'))
