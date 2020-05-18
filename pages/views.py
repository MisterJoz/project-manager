from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users
from .models import *
from .forms import ProjectForm, ContactForm, CreateUserForm
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'pages/index.html', context)


@unauthenticated_user
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # associate user with admin group upon registration
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'pages/register.html', context)


# @unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrenct')
    context = {}
    return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def calculate(subtotal, no_of_signs, sign_permit, engineering, other_fees, discount, cash_discount):
    total = subtotal + (sign_permit * no_of_signs) + engineering + other_fees
    if discount > 0:
        total = total * discount
    elif cash_discount > 0:
        total -= cash_discount
    return total


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form_copy = request.POST.copy()
        # get data used to calculate total
        subtotal = int(form_copy['subtotal'])
        number_of_signs = int(form_copy['number_of_signs'])
        sign_permit = int(form_copy['sign_permit'])
        engineering = int(form_copy['engineering'])
        other_fees = int(form_copy['other_fees'])
        # project can have discount OR cash discount
        discount = (float(form_copy['discount']) * .01)
        cash_discount = int(form_copy['cash_discount'])
        # total after discount applied
        discount_total = int(form_copy['discount_total'])
        deposit_amount = int(form_copy['deposit_amount'])
        completion_amount = int(form_copy['completion_amount'])
        # calculate total price
        form_copy['final_total'] = calculate(
            subtotal, number_of_signs, sign_permit, engineering, other_fees, discount, cash_discount)
        form = ProjectForm(form_copy)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'pages/add_project_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addContact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'pages/add_contact_form.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project, }
    return render(request, 'pages/project.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    print('Project...', project)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'pages/add_project_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'project': project}
    return render(request, 'pages/delete.html', context)
