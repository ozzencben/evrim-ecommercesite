from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages  


def login_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) 
            return redirect("product")  
        else:
            
            messages.error(request, "Hatalı şifre veya kullanıcı adı!")
    return render(request, "account/login.html")


def logout_request(request):
    logout(request)
    return redirect("product") 


def register_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        
        if not username or not email or not password1 or not password2:
            messages.error(request, "Lütfen tüm alanları doldurduğunuzdan emin olun.")
            return redirect("register")
        
        if password1 != password2:
            messages.error(request, "Parola eşleşmiyor.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı kullanılıyor.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email zaten sistemde kayıtlı.")
            return redirect("register")

        
        user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password1)
        messages.success(request, "Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
        return redirect("login")

    return render(request, "account/register.html")
