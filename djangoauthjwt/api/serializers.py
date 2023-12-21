from dataclasses import fields
from rest_framework import serializers
from api.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # For Password confirmation
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password does not match!"
            )
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)  # type: ignore
