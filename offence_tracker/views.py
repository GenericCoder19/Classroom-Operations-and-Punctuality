from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import OffenceForm, UserForm
from .models import Offence
from django.contrib.auth.models import User
from django.shortcuts import render, redirect , Http404
import pytz
from django.contrib import messages
import datetime
from datetime import date
# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'offence_tracker/login.html')
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/archive')
    else:
        return redirect('/report')

def report(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = OffenceForm(request.POST)
        if form.is_valid():
            offence = form.save(commit=False)
            user_id = request.user
            user_obj = User.objects.get(username= user_id)
            offence.reporter = user_obj.first_name + " " + user_obj.last_name
            render(request, 'offence_tracker/archive.html', {'form': form})
            offence.save()
            messages.success(request, 'Success')
    return render(request, 'offence_tracker/report_form.html', {'form' : form})

def login_u(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/report')
            else:
                return render(request, 'offence_tracker/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'offence_tracker/login.html', {'error_message': 'Invalid login'})
    return render(request, 'offence_tracker/login.html')

def logout_u(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'offence_tracker/login.html', {'form' : form})

def archive(request):
    if not request.user.is_authenticated():
        return render(request, 'offence_tracker/login.html')
    if request.user.is_staff or request.user.is_superuser:
        context = {
            'offences': Offence.objects.order_by('date').reverse().filter(date__date = date.today()),
            'isStaff': True,
        }
        return render(request, 'offence_tracker/archive.html', context)
    else:
        user_id = request.user
        user_obj = User.objects.get(username=user_id)
        reporter = user_obj.first_name + " " + user_obj.last_name
        context = {'offences': Offence.objects.filter(reporter = reporter).order_by('date').reverse().filter(date__date = date.today())}
        return render(request, 'offence_tracker/archive.html', context)

def delete_offence(request, id):
        offence = Offence.objects.get(pk=id)
        offence.delete()
        return redirect('/archive')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'offence_tracker/register.html', context)

def archive_date(request,day,month,year):
    if not request.user.is_authenticated():
        return render(request, 'offence_tracker/login.html')
    if request.user.is_staff or request.user.is_superuser:
        context = {
            'offences': Offence.objects.order_by('date').reverse().filter(date__contains=datetime.date(int(year), int(month), int(day))),
            'isStaff': True,
        }
        return render(request, 'offence_tracker/archive.html', context)
    else:
        user_id = request.user
        user_obj = User.objects.get(username=user_id)
        reporter = user_obj.first_name + " " + user_obj.last_name
        context = {
            'offences': Offence.objects.filter(reporter = reporter).order_by('date').reverse().filter(date__contains=datetime.date(int(year), int(month), int(day)))
        }
        return render(request, 'offence_tracker/archive.html', context)

def archive_all(request):
    if not request.user.is_authenticated():
        return render(request, 'offence_tracker/login.html')
    if request.user.is_staff or request.user.is_superuser:
        context = {
            'offences': Offence.objects.order_by('date').reverse(),
            'isStaff': True,
        }
        return render(request, 'offence_tracker/archive.html', context)
    else:
        user_id = request.user
        user_obj = User.objects.get(username=user_id)
        reporter = user_obj.first_name + " " + user_obj.last_name
        context = {
            'offences': Offence.objects.filter(reporter = reporter).order_by('date').reverse()
        }
        return render(request, 'offence_tracker/archive.html', context)

def archive_block(request,BLOCK):
    if not request.user.is_authenticated():
        return render(request, 'offence_tracker/login.html')
    if request.user.is_staff or request.user.is_superuser:
        context = {
            'offences': Offence.objects.order_by('date').reverse().filter(block=BLOCK),
            'isStaff': True,
        }
        return render(request, 'offence_tracker/archive.html', context)
    else:
        user_id = request.user
        user_obj = User.objects.get(username=user_id)
        reporter = user_obj.first_name + " " + user_obj.last_name
        context = {
            'offences': Offence.objects.filter(reporter = reporter).order_by('date').reverse()
        }
        return render(request, 'offence_tracker/archive.html', context)
