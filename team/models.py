from django.db import models

from user.models import User


class TeamMember(models.Model):
    """
    Model representing a team member and their role within a team.
    """

    class StatusChoices(models.TextChoices):
        TeamLead = "TeamLead"
        ProjectManager = "ProjectManager"
        QA = "QA"
        Developer = "Developer"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    team = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
        related_name="team",
    )

    class Meta:
        unique_together = ("user", "team")

    def __str__(self) -> str:
        """
        String representation of the team member, showing their name and team.
        """
        return f"({self.team.name}){self.user.first_name} {self.user.last_name}"


class Team(models.Model):
    """
    Model representing a team.
    """

    name = models.CharField(max_length=255)
    about = models.CharField(max_length=510, blank=True, null=True)
    members = models.ManyToManyField(User, through=TeamMember)

    def __str__(self) -> str:
        """
        String representation of the team, showing its name.
        """
        return self.name
