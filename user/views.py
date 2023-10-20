from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """
    View for creating a new user.
    """

    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating the user's own information.
    """

    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> "User":
        """
        Get the user object associated with the current request.
        """
        return self.request.user


class DeleteUserView(generics.DestroyAPIView):
    """
    View for deleting the user's own account.
    """

    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> "User":
        """
        Get the user object associated with the current request.
        """
        return self.request.user
