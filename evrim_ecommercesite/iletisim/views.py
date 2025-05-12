from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Yeni Mesaj - {name}",
                message=message,
                from_email=email,
                recipient_list=["ozzencben@gmail.com"],
            )
            return render(request, 'homepage/contact_thanks.html', {"name": name})
    else:
        form = ContactForm()
    return render(request, 'iletisim/iletisim.html', {"form": form})
