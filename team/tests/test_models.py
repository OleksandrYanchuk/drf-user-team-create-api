from django.test import TestCase

from team.models import Team, TeamMember
from user.models import User


class TeamMemberModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@user", password="testpassword")
        self.team = Team.objects.create(name="Test Team")
        self.team_member = TeamMember.objects.create(
            user=self.user, status="Developer", team=self.team
        )

    def test_team_member_creation(self):
        team_member = TeamMember.objects.get(id=self.team_member.id)
        self.assertEqual(team_member.user, self.user)
        self.assertEqual(team_member.status, "Developer")
        self.assertEqual(team_member.team, self.team)

    def test_team_member_str_method(self):
        expected_str = f"({self.team.name}){self.user.first_name} {self.user.last_name}"
        self.assertEqual(str(self.team_member), expected_str)


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team", about="Test description")

    def test_team_creation(self):
        team = Team.objects.get(id=self.team.id)
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(team.about, "Test description")

    def test_team_str_method(self):
        self.assertEqual(str(self.team), "Test Team")
