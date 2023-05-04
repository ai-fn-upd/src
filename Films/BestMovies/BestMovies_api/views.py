from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer


class ProfileView(APIView):
    """
    Profile endpoint for user profile
    """
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_surname": request.user.last_name,
                "email": request.user.email,
                "date_joined": request.user.date_joined,
            }
            return Response(data)
        else:
            return Response({"message": "You are not authorized yet"}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    """
    Registrarion endpoint that creates a new user.
    """
    def post(self, request):
        # Get the user data from the request data
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('passsword')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username is already taken"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)


class MovieListView(APIView):
    """
    List view for movie
    """
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        response = {}
        movies = Movie.objects.all()
        serialize_data = MovieSerializer(movies, many=True)
        response["movies"] = serialize_data.data
        return Response(response)


class AuthView(APIView):
    """
    Authenticate endpoint for authenticate users
    """
    def post(self, request):
        # Get the user credentials from the request data
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is authenticated
            login(request, user)
            return Response({'message': "Successfully authenticate"})
        else:
            # If the user is not authenticated
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LikesView(APIView):
    """
    Likes view for set likes
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        try:
            movie = self.get_object(pk=pk)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        if request.user.is_authenticated:
            if movie.likes.filter(pk=request.user.id):
                movie.likes.add(request.user)
                return Response({"message": "Successfully liked movie"})
            else:
                movie.likes.remove(request.user)
                return Response({"message": "Successfully unliked movie"})
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)


class MovieDetailView(APIView):
    """
    Detail view for movie
    """
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            return Response({"movie": MovieSerializer(movie).data})
        except Movie.DoesNotExsist:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

