from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .models import Car, Offer, Header
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def home(request):
    all_cars = Car.objects.prefetch_related("car_image").filter(is_active=True)
    all_headers = Header.objects.all().filter(default=True)
    all_offers = Offer.objects.all().filter(is_active=True)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            messages.success(request, "Mesajınız başarıyla gönderildi...")
            return redirect("homepage:home")

    form = ContactForm()

    context = {
        "cars": all_cars,
        "all_headers": all_headers,
        "all_offers": all_offers,
        "form": form,
    }
    return render(request, "index.html", context=context)


class ContactSuccessView(TemplateView):
    template_name = 'success.html'


