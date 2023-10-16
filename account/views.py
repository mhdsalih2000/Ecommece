
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout
from Ecom import views

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_number=request.POST['Mobile_Number']
        date_of_birth = request.POST['Date']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            # Create a new user
            user = CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                mobile_number=mobile_number,   
                date_of_birth=date_of_birth,           
                last_name=last_name,
                password=password
            )
            auth_login(request,user) 
             # Log the user in
            return redirect('Ecom:home')  # Redirect to the home page upon successful registration
        else:
            error_message = "Passwords do not match."
            return render(request, 'Register.html', {'error_message': error_message})
    else:
        return render(request, 'Register.html')





def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if  user is not None:
            auth_login(request,user)
            return redirect("Ecom:home")
        else:
            error_message='Somthing Went Wrong'
            return render(request,'login.html',{'error_message': error_message})
    else:
        return render(request,'login.html')
   
    
        

def logout_view(request):
    logout(request)
    return redirect('login')
