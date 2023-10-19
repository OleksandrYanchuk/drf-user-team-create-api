from django.urls import path
from .views import (
    TeamListCreateView,
    TeamRetrieveUpdateDeleteView,
    TeamMemberDestroyView,
    TeamMemberCreateView,
    TeamMemberListView,
)

app_name = "team"


urlpatterns = [
    path("teams/", TeamListCreateView.as_view(), name="team-list-create"),
    path(
        "teams/<int:pk>/",
        TeamRetrieveUpdateDeleteView.as_view(),
        name="team-retrieve-update-delete",
    ),
    path(
        "teams/<int:team_id>/members/",
        TeamMemberCreateView.as_view(),
        name="team-member-create",
    ),
    path(
        "team-members/<int:pk>/",
        TeamMemberDestroyView.as_view(),
        name="team-member-destroy",
    ),
    path("team-members/", TeamMemberListView.as_view(), name="team-member-list"),
]
