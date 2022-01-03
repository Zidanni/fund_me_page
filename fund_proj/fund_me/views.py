from django.shortcuts import render
from django.http import HttpResponse
from .models import donations


def say_hello(request):
    context = {"name": "DUDE"}
    return render(request, "hello_page.php", context)


def create_post(request):
    if request.method == "POST":
        if (
            request.POST.get("first_name")
            and request.POST.get("last_name")
            and request.POST.get("quantity")
            and request.POST.get("note")
        ):
            donation = donations()
            donation.first_name = request.POST.get("first_name")
            donation.last_name = request.POST.get("last_name")
            donation.quantity = request.POST.get("quantity")
            donation.note = request.POST.get("note")
            donation.save()

            first_50_donations = donations.objects.all().order_by("id")[50]
            return first_50_donations


# Create your views here.
