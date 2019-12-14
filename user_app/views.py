from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.
def loginauth(request):
    if request.method == "POST":
        e = request.POST.get("email")
        p = request.POST.get("pass")

        user = UserModel.objects.filter(email=e, password=p)

        if user.count() > 0:
            for user in user:
                request.session["email"] = user.email
                request.session["id"] = user.id
                request.session["name"] = user.name
                return redirect("question")
        else:
            return HttpResponse("Wrong Credentials")

    else:
        return render(request, "login.html")


def logout(request):
    request.session.flush()
    return redirect('login')

