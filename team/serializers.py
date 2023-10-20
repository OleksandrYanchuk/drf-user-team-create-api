from rest_framework import serializers

from .models import Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    """
    Serializer for the TeamMember model.
    """

    class Meta:
        model = TeamMember
        fields = ("id", "user", "status", "team")

    def create(self, validated_data: dict) -> TeamMember:
        """
        Create and return a new TeamMember instance using the validated data.
        """
        member = TeamMember.objects.create(**validated_data)
        return member

    def __str__(self) -> str:
        """
        String representation of the serializer, showing the associated user.
        """
        return str(self.user)


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model.
    """

    class Meta:
        model = Team
        fields = ("id", "name", "about", "members")
