from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from api.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
)
from django.contrib.auth import authenticate
from api.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),  # type: ignore
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "msg": "Registration Successful"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")  # type: ignore
            password = serializer.data.get("password")  # type: ignore
            user = authenticate(email=email, password=password)
            print(user)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response(
                    {"token": token, "msg": "Login Successful"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["Email or Password is not Valid"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

from rest_framework_simplejwt.exceptions import TokenError
class UserLogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response("Success")
    
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Changed Successfully"}, status=status.HTTP_200_OK
        )

#-----------------------------------------Tokenization - RemovingStopWords - Lemmenization ------------------------------------------#
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TokenizeSentence(APIView):
    def post(self, request):
        sentence = request.data.get('sentence')
        tokenized_sentence = word_tokenize(sentence)
        return Response({"tokenized_sentence": tokenized_sentence})

class RemoveStopwords(APIView):
    def post(self, request):
        sentence = request.data.get('sentence')
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(sentence)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        return Response({"filtered_sentence": filtered_sentence})

class LemmatizeWords(APIView):
    def post(self, request):
        sentence = request.data.get('sentence')
        lemmatizer = WordNetLemmatizer()
        word_tokens = word_tokenize(sentence)
        lemmatized_words = [lemmatizer.lemmatize(w) for w in word_tokens]
        return Response({"lemmatized_words": lemmatized_words})