from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the custom user model.
    """

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "password",
            "is_staff",
            "profession",
            "skills",
            "first_name",
            "last_name",
        )
        read_only_fields = ("is_staff",)
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
            "profession": {"required": False, "allow_null": True},
            "skills": {"required": False, "allow_null": True},
            "first_name": {"required": True, "allow_null": False},
            "last_name": {"required": True, "allow_null": False},
        }

    def create(self, validated_data: dict) -> get_user_model():
        """
        Create and return a new user instance using the validated data.
        """

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data: dict) -> get_user_model():
        """
        Update and return an existing user instance using the validated data.
        """

        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user
