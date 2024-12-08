from django.shortcuts import render

def game_platform(request):
    return render(request, "third_task/platform.html")

# Create your views here.

def game(request):
    games = {
        "first": "Atomic Heart",
        "second": "Cyberpank",
        "third": "PayDay 2"

    }
    return render(request, "third_task/games.html", context=games)


def cart(request):
    return render(request, "third_task/cart.html")