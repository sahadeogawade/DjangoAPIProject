from django.urls import path
from .views import note_list, note_detail,NoteAPIView, NoteDetailAPIView

urlpatterns = [
  # path('note/',note_list),
  path('note/',NoteAPIView.as_view()),
  # path('note_details/<int:pk>/',note_detail),
  path('note_details/<int:id>/',NoteDetailAPIView.as_view()),
]