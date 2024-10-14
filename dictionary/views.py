from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from .models import Word

def index_view(request):
    return TemplateResponse(request, "index.html", {
        "words": Word.objects.all()
    })

def word_detail_view(request, word):
    return TemplateResponse(request, "word.html", {
        "word": get_object_or_404(Word, word = word)
    })