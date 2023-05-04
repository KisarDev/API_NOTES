from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CreateUserView, MyTokenObtainPairView, addNote, deleteNote,
                    getNotes, getRoutes, readNoteById, updateNote)

urlpatterns = [
    path('', getRoutes, name="routes"),

    path('token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),

    path('notes/', getNotes, name='notes'),
    path('notes/add/', addNote, name='add_note'),
    path('notes/update/<int:pk>/', updateNote, name='update_note'),
    path('notes/delete/<int:pk>/', deleteNote, name='delete_note'),
    path('note/<int:note_id>/', readNoteById, name='get_note_by_id'),
    path('users/create', CreateUserView.as_view(), name='create_user'),
]