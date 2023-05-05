from rest_framework import serializers
from .models import User
import re

# Check if data contains numbers


def is_alpha(value):
    return bool(value.replace(" ", "").isalpha())


# Remove extra spaces


def remove_extra_spaces(value):
    return re.sub(" +", " ", value.strip())


# Validate the data for register


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_first_name(self, value):
        if not is_alpha(value):
            raise serializers.ValidationError(
                f"First name {value} can't include numbers."
            )
        else:
            first_name = remove_extra_spaces(value).title()
            return first_name

    def validate_last_name(self, value):
        if not is_alpha(value):
            raise serializers.ValidationError(
                f"Last name {value} can't include numbers."
            )
        else:
            last_name = remove_extra_spaces(value).title()
            return last_name

    def validate_email(self, value):
        email = value.replace(" ", "").lower()
        is_duplicated = User.objects.filter(email=email).exists()
        if not is_duplicated:
            return email
        else:
            raise serializers.ValidationError(f"Email {email} is already registered.")

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must contain at least 8 characters."
            )
        else:
            password = value
            return password

    def validate_address(self, value):
        address = remove_extra_spaces(value).title()
        return address

    def validate_telephone(self, value):
        telephone = remove_extra_spaces(value).title()
        return telephone


# Validate the data for login


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_email(self, value):
        email = value.replace(" ", "").lower()
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            return email
        else:
            raise serializers.ValidationError(f"Email {email} doesn't exist.")

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must contain at least 8 characters."
            )
        else:
            password = value
            return password
