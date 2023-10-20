from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from team.models import Team, TeamMember
from user.models import User


class TeamListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="admin1@admin.com",
            password="1234admin",
            is_staff=True,
        )

        self.team_data = {"name": "Test Team", "about": "This is a test team"}
        self.team = Team.objects.create(name="Test Team", about="This is a test team")

    def test_create_team(self):
        counter = Team.objects.count()
        self.client.force_authenticate(user=None)
        response = self.client.post("/api/team/teams/", self.team_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/team/teams/", self.team_data, format="json")
        counter += 1
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), counter)

    def test_list_teams(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/team/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamRetrieveUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="admin1@admin.com",
            password="1234admin",
            is_staff=True,
        )

        self.team = Team.objects.create(name="Test Team", about="This is a test team")

    def test_update_team(self):
        self.client.force_authenticate(user=None)
        updated_data = {
            "name": "Updated Team Name",
            "about": "This is an updated team description",
        }
        response = self.client.put(
            f"/api/team/teams/{self.team.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f"/api/team/teams/{self.team.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, "Updated Team Name")
        self.assertEqual(self.team.about, "This is an updated team description")

    def test_delete_team(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(f"/api/team/teams/{self.team.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/team/teams/{self.team.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Team.objects.filter(id=self.team.id).exists())


class TeamMemberCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="admin1@admin.com",
            password="1234admin",
            is_staff=True,
        )
        self.team = Team.objects.create(name="Test Team", about="This is a test team")

    def test_create_team_member(self):
        self.client.force_authenticate(user=None)
        team_member_data = {
            "user": self.user.id,
            "status": "Developer",
            "team": self.team.id,
        }
        response = self.client.post(
            f"/api/team/teams/{self.team.id}/members/", team_member_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            f"/api/team/teams/{self.team.id}/members/", team_member_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        team_member = TeamMember.objects.get(user=self.user, team=self.team)
        self.assertEqual(team_member.status, "Developer")


class TeamMemberDestroyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="admin1@admin.com",
            password="1234admin",
            is_staff=True,
        )
        self.team = Team.objects.create(name="Test Team", about="This is a test team")
        self.team_member = TeamMember.objects.create(
            user=self.user, status="Developer", team=self.team
        )

    def test_destroy_team_member(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(f"/api/team/team-members/{self.team_member.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/team/team-members/{self.team_member.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(TeamMember.objects.filter(id=self.team_member.id).exists())


class TeamMemberListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
            email="user10@user.com",
            password="1234user",
        )
        self.user2 = User.objects.create(
            email="user20@user.com",
            password="1234user",
        )

        self.team = Team.objects.create(name="Test Team", about="This is a test team")
        self.team_member1 = TeamMember.objects.create(
            user=self.user1, status="Developer", team=self.team
        )
        self.team_member2 = TeamMember.objects.create(
            user=self.user2, status="QA", team=self.team
        )

    def test_get_team_members_without_filter(self):
        counter = TeamMember.objects.count()
        response = self.client.get("/api/team/team-members/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), counter)

    def test_get_team_members_with_filter(self):
        team_id = self.team.id
        response = self.client.get(f"/api/team/team-members/?team_id={team_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_team_members_with_invalid_filter(self):
        invalid_team_id = 999
        response = self.client.get(f"/api/team/team-members/?team_id={invalid_team_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
