from django.shortcuts import render
from .models import Character

# Create your views here.
def index(request):
    return render(request, "characters/index.html", {
        "characters": Character.objects.all()
    })

def character(request, char_name):
    student = Character.objects.filter(name=char_name)
    if student:
        return render(request, "characters/character.html",{
            "character": student[0]
        })
    else:
        return render(request, "characters/error.html")

