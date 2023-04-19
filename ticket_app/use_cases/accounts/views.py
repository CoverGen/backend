# this file contains user basic validation and logic when login or register user
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm, ValidationError
from ticket_app.models import User, Planner
from django.contrib.auth.hashers import check_password
import re

# user register validation
# function that check if first or last name has numbers in it.


def has_numbers(name_input):
    return bool(re.search(r"\d", name_input))


class registerForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "address",
            "telephone",
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if has_numbers(first_name):
            raise ValidationError(f"First name {first_name} cant include numbers.")
        else:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if has_numbers(last_name):
            raise ValidationError(f"Last name {last_name} cant include numbers.")
        else:
            return last_name

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            User.objects.get(email=email)
        except Exception as error:
            error = error  # only to pass lint
            return email
        raise ValidationError(f"Email {email} is already registered.")

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise ValidationError("Password must contain at least 8 characters.")
        else:
            return password


class loginForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            User.objects.get(email=email)
        except Exception as error:
            raise ValidationError(f"Email {email} not exist, with message: {error}")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise ValidationError("Password must contain at least 8 characters.")
        else:
            return password


# views

# don't search for HTTPS cookie


@csrf_exempt
# Register user
def register(request):
    if request.POST:
        try:
            newUser = registerForm(request.POST)
            if newUser.is_valid():
                newUser.save()
                email = newUser.cleaned_data["email"]
                user = User.objects.get(email=email)
                newPlanner = Planner(id_planner=user)
                newPlanner.save()
                return render(request, "response.html", {"msg": "Registrado"})
            else:
                return render(request, "response.html", {"msg": newUser.errors})
        except Exception as error:
            return render(request, "response.html", {"msg": error})
    else:
        return render(request, "response.html", {"msg": "Register endpoint."})


# login user

# don't search for HTTPS cookie


@csrf_exempt
def login(request):
    if request.POST:
        try:
            user = loginForm(request.POST)
            if user.is_valid():
                email = user.cleaned_data["email"].lower()
                password = user.cleaned_data["password"]
                hashed_password = User.objects.get(email=email).password
                if check_password(password, hashed_password):
                    return render(
                        request, "response.html", {"msg": f"User {email} logged in."}
                    )
                else:
                    return render(request, "response.html", {"msg": "Wrong Password."})
            else:
                return render(request, "response.html", {"msg": user.errors})
        except Exception as error:
            return render(request, "response.html", {"msg": error})
    else:
        return render(request, "response.html", {"msg": "Login endpoint"})
