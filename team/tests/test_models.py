from django.test import TestCase
from user.models import User
from team.models import Team, TeamMember


class TeamMemberModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@user", password="testpassword")
        self.team = Team.objects.create(name="Test Team")
        self.team_member = TeamMember.objects.create(
            user=self.user, status="Developer", team=self.team
        )
