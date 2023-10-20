from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from team.models import Team, TeamMember
from team.permissions import IsAdminOrIfAuthenticatedReadOnly
from team.serializers import TeamSerializer, TeamMemberSerializer


class TeamListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating teams.
    """

    queryset = Team.objects.prefetch_related("members").all()
    serializer_class = TeamSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TeamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a team.
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TeamMemberCreateView(generics.CreateAPIView):
    """
    View for creating a team member.
    """

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def perform_create(self, serializer):
        team_id = self.kwargs.get("team_id")
        team = Team.objects.get(pk=team_id)
        serializer.save(team=team)


class TeamMemberDestroyView(generics.DestroyAPIView):
    """
    View for deleting a team member.
    """

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TeamMemberListView(generics.ListAPIView):
    """
    View for listing team members with optional filtering.
    """

    serializer_class = TeamMemberSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        team_id = self.request.query_params.get("team_id")
        queryset = TeamMember.objects.select_related("user", "team").all()

        if team_id:
            queryset = queryset.filter(team=team_id)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "team_id",
                type=OpenApiTypes.INT,
                description="Filter by team ID",
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        team_id = request.query_params.get("team_id")
        queryset = TeamMember.objects.all()

        if team_id:
            queryset = queryset.filter(team=team_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
