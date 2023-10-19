from django.test import TestCase
from rest_framework.exceptions import ErrorDetail

from team.models import Team
from team.serializers import TeamSerializer, TeamMemberSerializer
from user.models import User


class TeamMemberSerializerTest(TestCase):
    def test_valid_data(self):
        user = User.objects.create(
            email="test@example.com", password="testpassword", is_staff=False
        )
        team = Team.objects.create(name="Development Team", about="Development Team")
        data = {
            "id": 1,
            "user": user.id,
            "status": "Developer",
            "team": team.id,
        }
        serializer = TeamMemberSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_missing_required_field(self):
        data = {
            "user": 1,
            "status": "Developer",
            "team": 1,
        }
        serializer = TeamMemberSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["user"],
            [
                ErrorDetail(
                    string='Invalid pk "1" - object does not exist.',
                    code="does_not_exist",
                )
            ],
        )


class TeamSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            "id": 1,
            "name": "Development Team",
            "about": "A great team of developers",
        }
        serializer = TeamSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_missing_required_field(self):
        data = {
            "about": "A great team of developers",
        }
        serializer = TeamSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {"name": [ErrorDetail(string="This field is required.", code="required")]},
        )
