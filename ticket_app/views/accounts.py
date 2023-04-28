# this file contains user basic validation and logic when login or register user
from django.views.decorators.csrf import csrf_exempt
from ticket_app.models import User, Planner
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ticket_app.serializers import UserRegisterSerializer, UserLoginSerializer

# Allow POST and GET requests


@api_view(["POST", "GET"])
# Don't ask for csrf token
@csrf_exempt
# Register user
def register_user(request):
    if request.method == "POST":
        print(request.data)
        new_user = UserRegisterSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            email = new_user.data["email"]
            user = User.objects.get(email=email)
            new_planner = Planner(id_planner=user)
            new_planner.save()
            return Response(
                {"message": f"Email {email} registered."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "There are some errors.", "errors": new_user.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    else:
        return Response({"message": "Register endpoint."}, status=status.HTTP_200_OK)


# Allow POST and GET requests
@api_view(["POST", "GET"])
# Don't ask for csrf token
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        user_request = UserLoginSerializer(data=request.data)
        if user_request.is_valid():
            email = user_request.data["email"]
            password = user_request.data["password"]
            hashed_password = User.objects.get(email=email).password
            if check_password(password, hashed_password):
                return Response(
                    {"message": f"User with email {email} logged in."},
                    status=status.HTTP_202_ACCEPTED,
                )
            else:
                return Response(
                    {"message": "Wrong password, try again."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        return Response(
            {"message": "There are some errors.", "errors": user_request.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    else:
        return Response({"message": "Login endpoint."}, status=status.HTTP_200_OK)
