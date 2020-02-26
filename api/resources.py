from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization
class NoteResources(ModelResource):
  class Meta:
    queryset = Note.objects.all()
    resource_name = 'note'
    authorization = Authorization()
    fields = ['title', 'body']