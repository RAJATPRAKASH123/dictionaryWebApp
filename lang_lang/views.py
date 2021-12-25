from collections import defaultdict
from typing import DefaultDict
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import csv
from pathlib import Path
from lang_lang.models import LanguageLanguage

from .forms import LanguageLanguageForm

# Create your views here.
def home_view(request, *args, **kwargs): # /search/
    # return HttpResponse("<h1>Hello World</h1>")# actual html response of some kind
    '''
    context = DefaultDict()
    count = 1
    for i in LanguageLanguage.objects.all():
        print(i.lang1, i.lang2)
        context["home"] = "chilling"
        count += 1
    print(context)
    '''
    # query set
    qs = LanguageLanguage.objects.all()
    context = {"object_list": qs}

    # query = request.GET.get('q')
    # context["query"] = query

    return render(request, "home.html", context)


def language_detail_view(request, id):
    obj = None
    try:
        obj = LanguageLanguage.objects.get(id = id)
    except LanguageLanguage.DoesNotExist:
        raise Http404 # render html page, with HTTP status code 404
    # return HttpResponse(f"Translation from {obj.lang1} to {obj.lang2} ")
    context = DefaultDict()
    context["object"] = obj
    print(obj.lang1)
    words = []
    # templates/data/EnglishEnglish.csv
    path = str(Path(__file__).resolve().parent.parent) + "/templates/"
    print(path)
    with open(path + "data/" + obj.lang1 + obj.lang2 +".csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row:
                words.append(row)
            # print(row)
    context["word_list"] = words
    word_meaning = defaultdict(list)
    for i in words:
        word_meaning[i[0]] = [i[1], i[2]]
    # print(context)
    # print(request.POST)
    # print(request.GET)

    # if request.method == "POST":
    #     post_data = request.POST or None
    #     if post_data != None:
    #         my_form = LanguageLanguageForm(request.POST)
    #         # print(my_form.is_valid())
    #         if my_form.is_valid():
    #             if post_data['word'] in word_meaning:
    #                 print(word_meaning[post_data['word']])
    #             print("post_data", post_data['word']) # not the method we want to use
    form = LanguageLanguageForm(request.GET or None)
    context["form"] = form
    if form.is_valid():
        print(form.cleaned_data)
        cur = form.cleaned_data['word']
        if cur in word_meaning:
            print(word_meaning[cur])
            context["cur_res"] = [cur] + word_meaning[cur]
    return render(request, "lang/detail.html", context )

def language_api_detail_view(request, id):
    try:
        obj = LanguageLanguage.objects.get(id = id)
    except LanguageLanguage.DoesNotExist:
        return JsonResponse({"message":"Not found"}) # render html page, with HTTP status code 404

    return JsonResponse({"translation": obj.lang1 + " to " + obj.lang2})
