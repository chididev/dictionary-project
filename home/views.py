from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyDictionary import PyDictionary
# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'home/home.html')

@csrf_exempt
def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    translations = dictionary.translate(search, 'french')
    context = {
        'search':search,
        'meaning':meaning,
        'synonyms':synonyms,
        'antonyms':antonyms,
        'translations': translations,
    }
    return render(request, 'home/word.html', context)
