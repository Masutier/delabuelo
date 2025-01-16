from django.contrib import messages
from .views import clean_basket


def total_basket(request):
    total = 0
    if request.user.is_authenticated:
        if "basket" in request.session.keys():
            for key, value in request.session["basket"].items():
                total += int(value["accumulated"])
    else:
        clean_basket(request)
        messages.success(request, f"No hay Vendedor Activado")
        if "basket" in request.session.keys():
            for key, value in request.session["basket"].items():
                total += int(value["accumulated"])
    return {'total_basket': total}

