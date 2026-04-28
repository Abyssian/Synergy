from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import UserName


def index(request):
    greeting = ""
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name == "":
            error = "Поле имени не должно быть пустым"
        else:
            UserName.objects.create(name=name)
            greeting = f"Привет, {name}!"

    return render(request, "greetings/index.html", {
        "greeting": greeting,
        "error": error
    })