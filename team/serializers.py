from rest_framework import serializers

from .models import Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ("id", "user", "status", "team")

    def create(self, validated_data):
        member = TeamMember.objects.create(**validated_data)
        return member

    def __str__(self):
        return self.user


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "about", "members")
