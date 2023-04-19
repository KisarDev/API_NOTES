from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Note

from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        '/api/token/refresh'
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Atualizar Note.
@api_view(['POST'])
def updateNote(request, pk):
    Note = Note.objects.get(id=pk)
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
    return Response(serializer.data)
#delete Note.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    Note = Note.objects.get(id=pk)
    if Note == None:
        return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
    Note.delete()

    return Response('O item foi deletado!')
