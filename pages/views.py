from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm, ContactForm
# Create your views here.


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'pages/index.html', context)


def register(request):
    return render(request, 'pages/register.html')


def calculate(subtotal, no_of_signs, sign_permit, engineering, other_fees, discount, cash_discount):
    total = subtotal + (sign_permit * no_of_signs) + engineering + other_fees
    if discount > 0:
        total = total * discount
    elif cash_discount > 0:
        total -= cash_discount
    return total


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


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'pages/add_project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'project': project}
    return render(request, 'pages/delete.html', context)
