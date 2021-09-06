import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from django_admin_sticky_notes.models import StickyNote


class StickyNoteView(View):
    def get(self, request):
        obj, created = StickyNote.objects.get_or_create(id=1)
        return JsonResponse({"note": obj.body})

    def post(self, request):
        obj = StickyNote.objects.last()
        obj.body = json.loads(request.body)["note"]
        obj.save()
        return HttpResponse(status=200)
