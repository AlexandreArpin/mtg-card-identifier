import json
import os

from django.shortcuts import render
from django.views.generic import View

from mtg_card_identifier_core.opencv_mtg_identifier import identify_file
from mtg_card_identifier_web.forms import UploadImageForm

BASE_DIR = os.path.dirname(__file__)
LATEST_DIR = os.path.join(BASE_DIR, "../mtg_card_identifier_core/static/latest")
DEBUG_FILE = os.path.join(LATEST_DIR, "latest_debug.json")

class IndexView(View):

    def get(self, request):
        context = {
            "form": UploadImageForm(),
        }

        return render(request, "mtg_card_identifier_web/index.html", context)

    def post(self, request):
        context = {
            "result": None,
        }
        form = UploadImageForm(request.POST, request.FILES)
        context["form"] = form

        if form.is_valid():
            card = identify_file(request.FILES['image'].file.name, True)
            context["result"] = json.dumps(card, indent=4, sort_keys=True)
            context["card"] = card

        return render(request, "mtg_card_identifier_web/index.html", context)


class DebugView(View):

    def get(self, request):
        context = {}

        with open(DEBUG_FILE) as data_file:
            data = json.load(data_file)

        context["debug_data"] = json.dumps(data, indent=4, sort_keys=True)

        return render(request, "mtg_card_identifier_web/debug.html", context)
