from django.shortcuts import render,redirect
from .models import *
import uuid
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        request.session['username']=username

        if role == 'customer':
            customer_obj = Customer.objects.filter(username=username,password=password).first()
            if customer_obj:
                if customer_obj.is_verified: 
                    return redirect('customer')
                else :
                    messages.error(request,'Account is not verified check your mail')
            else :
                messages.error(request,'Invalid Username or Password')
        else:
            labour_obj = Labour.objects.filter(username=username,password=password).first()
            if labour_obj:
                if labour_obj.is_verified : 
                    return redirect('labour')
                else:
                    messages.error(request,'Account is not verified check your mail')
            else:
                messages.error(request,'Invalid Username or Password')

    return render(request,"login.html")

def register_customer(request):
    alert_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        auth_token = str(uuid.uuid4())
        customer_obj=Customer(username=username,password=password,name=name,phone_number=phone_number,address=address,auth_token=auth_token)
        exsist_customer = Customer.objects.filter(username=username).first()
        if exsist_customer:
            messages.error(request,'Username is already taken')
        else:
            customer_obj.save()
            alert_flag = True

        send_mail_after_registration(username,auth_token)


    return render(request,"register_customer.html", {'alert_flag': alert_flag})


def register_labour(request):
    alert_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        profession = request.POST.get('profession')
        place = request.POST.get('place')
        fees = request.POST.get('fees')
        other_profession = request.POST.get('other_profession')
        image = request.FILES['image']  # Access the uploaded file

        auth_token = str(uuid.uuid4())
        exsist_labour = Labour.objects.filter(username=username).first()
        if exsist_labour:
            messages.error(request, "Username is already taken")
        else:
            # Check for 'other' profession and save the labour
            profession_to_save = other_profession if profession == 'other' else profession
            labour_obj = Labour(
                username=username,
                password=password,
                name=name,
                phone_number=phone_number,
                profession=profession_to_save,
                place=place,
                fees=fees,
                image=image,  # Directly save the image field
                auth_token=auth_token
            )
            labour_obj.save()
            alert_flag = True
            send_mail_after_registration(username, auth_token)

    return render(request, "register_labour.html", {'alert_flag': alert_flag})


def customer(request):
    username = request.session.get('username')
    cust_obj=Customer.objects.filter(username=username)
    labour_obj=Labour.objects.all()
    return render(request,"customer.html",{'labour_obj':labour_obj,'cust_obj':cust_obj})

def labour(request):
    username = request.session.get('username')
    
    labour_obj = Labour.objects.filter(username=username).first()
    if labour_obj:
        # Change the query to use the `labour_username` field in the `Book` model
        data = Book.objects.filter(labour_username=labour_obj.username)  # Filter based on labour's username
    else:
        data = None
    
    return render(request, "labour.html", {'data': data, 'labour_obj': labour_obj})

def send_mail_after_registration(username, token):
    subject = 'Click the link for your account verification'
    message = f'Hi past the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [username]
    send_mail(subject,message,email_from,recipient_list)

def verify(request, auth_token):
    # Check for a profile in both Customer and Labour models
    profile_obj = Customer.objects.filter(auth_token=auth_token).first() or Labour.objects.filter(auth_token=auth_token).first()

    if profile_obj:
        profile_obj.is_verified = True
        profile_obj.save()
        # Redirect based on the type of profile (Customer or Labour)
        if isinstance(profile_obj, Customer):
            return redirect('customer')
        elif isinstance(profile_obj, Labour):
            return redirect('labour')
    else:
        messages.error(request, 'Invalid verification link')
        return redirect('index')
    
def book(request, customer_id, labour_id):
    cust_obj = Customer.objects.get(id=customer_id)
    labour_obj = Labour.objects.get(id=labour_id)

    if request.method == 'POST':
        booking_time_str = request.POST.get('booking_time')
        booking_time = datetime.strptime(booking_time_str, '%Y-%m-%dT%H:%M')

        book_obj = Book(
            book=cust_obj,  # This is the customer object
            labour_username=labour_obj.username,  # Save labour's username
            booking_time=booking_time,
            status=False
        )
        book_obj.save()

        messages.success(request, 'Booking successful!')
        return redirect('customer')  # Redirect after saving

    return render(request, 'customer.html', {'labour_obj': Labour.objects.all()})
    # cust_obj = Labour.objects.get(id=id)
    # cust_username = request.session.get('username')

    # if request.method == 'POST':
        # Get the booking time from the form
        # booking_time_str = request.POST.get('booking_time')

        # Convert the booking_time to a datetime object
        # booking_time = datetime.strptime(booking_time_str, '%Y-%m-%dT%H:%M')

        # Create the Book object
        # book_obj = Book(
        #     book=cust_obj,
        #     cust_username=cust_username,
        #     booking_time=booking_time,
        #     status=False  # Default status can be set to False initially
        # )
        # book_obj.save()

        # Optionally, you can add a success message here
    #     messages.success(request, 'Booking successful!')
    #     return redirect('customer')

    # return render(request, 'customer.html', {'labour_obj': Labour.objects.all()})

def lab_cart(request):
    return render(request,"lab_cart.html")
