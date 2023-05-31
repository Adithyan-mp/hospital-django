from django.shortcuts import render
from .models import Departments, Doctors, Booking
from .forms import BookingForm
from .models import contact
# Create your views here.


def login(request):
    return render(request, 'admin/')


def home(request):
    return render(request, 'home.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conf.html')

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def contact_view(request):
    dic_contact = {
        'contacts': contact.objects.all()
    }
    return render(request, 'contact.html', dic_contact)


def department(request):
    dic_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dic_dept)


def doctors(request):
    dic_doctors = {
        'doctor': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dic_doctors)
