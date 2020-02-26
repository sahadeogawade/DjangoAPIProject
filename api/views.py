from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Note, Friend, Belonging, Borrowed
from .serializers import NoteSerializer, FriendSerializer,BelongingSerializer,BorrowedSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView


import logging
# Create your views here.


class NoteAPIView(APIView):

  def get(self, request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many= True)
    return JsonResponse(serializer.data, safe= False)

  def post(self, request):
    data = JSONParser().parse(request)
    serializer = NoteSerializer(data= data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


class NoteDetailAPIView(APIView):

  def get_object(self, id):
    try: 
      return Note.objects.get(id=id)

    except Note.DoesNotExist:
      return HttpResponse(status=404)

  def get(self, request, id):
    note = self.get_object(id)
    serializer = NoteSerializer(note)
    return JsonResponse(serializer.data)

  
  def put(self, request, id):
    note = self.get_object(id)
    serializer = NoteSerializer(note, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400,data={"message":"Data doesn't exist"})

  def delete(self, request, id):
    note = self.get_object(id)
    note.delete()
    return HttpResponse(status=204)

@csrf_exempt

def note_list(request):
  logging.log(request)
  print("***request",request)

  if request.method == 'GET':
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many= True)
    return JsonResponse(serializer.data, safe= False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = NoteSerializer(data= data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def note_detail(request, pk):
  try:
    note = Note.objects.get(pk=pk)

  except Note.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = NoteSerializer(note)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400,data={"message":"Data doesn't exist"})

  elif request.method == 'DELETE':
    note.delete()
    return HttpResponse(status=204)