from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from words.forms import WordForm
from words.models import Word


def index(request):
    """
    Renders the home
    :param request:
    :return:
    """
    return redirect('/home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/home')
    else:
        return render(request, 'words/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/login')


def home(request):
    return redirect(reverse(words))
    return render(request, 'words/home.html')


def word(request):
    """
    If the method is GET, we render the add-word view.
    If the method is POST we create a new word.
    :param request:
    :return:
    """
    return HttpResponse(status=404)
    if request.method == "GET":
        form = WordForm()
        return render(request, 'words/addword.html', {'form': form})
    else:
        return HttpResponse(status=409)

    #if request.method == "POST":
    #    form = WordForm(request.POST)

    #    if form.is_valid():
    #        model = Word(
    #            **form.cleaned_data
    #        )
    #        model.save()
    #        messages.add_message(request, messages.SUCCESS, "Added word")
    #    return render(request, 'words/addword.html', {'form': form})
    #else:
    #    return HttpResponse(status=409)


def word_individual(request, id):
    word = get_object_or_404(Word, pk=id)

    if request.method == "GET":
        return render(request, 'words/word_detail.html', {'word': word})

    return redirect(reverse(words))


def word_delete(request, id):
    return HttpResponse(status=404)

    if request.method != "POST":
        return 409

    word = get_object_or_404(Word, pk=id)

    if word.owner != request.user:
        messages.add_message(request, messages.ERROR, "You don't have access to delete this word")
        return 403

    word.delete()
    messages.add_message(request, messages.SUCCESS, "Message deleted")
    return redirect(reverse(words))


def word_update(request, id):
    return HttpResponse(status=409)
    if request.method != "POST":
        return 409

    word = get_object_or_404(Word, pk=id)

    form = WordForm(request.POST)

    if form.is_valid():
        word.word = form.cleaned_data['word']
        word.wordExample = form.cleaned_data['wordExample']
        word.freeTrans = form.cleaned_data['freeTrans']
        word.freeTransExample = form.cleaned_data['freeTransExample']
        word.freeTrans2 = form.cleaned_data['freeTrans2']
        word.freeTrans2Example = form.cleaned_data['freeTrans2Example']
        word.save()

    messages.add_message(request, messages.SUCCESS, 'Word updated')

    return redirect('/my-words')


def words(request):
    """
    Renders an overview over my words, with pagination
    :param request:
    :return:
    """
    search_query = request.GET.get('q')
    words_all = Word.objects\
        .order_by('word')

    if search_query:
        words_all = words_all.filter(
            Q(word__contains=search_query) |
            Q(POS__contains=search_query) |
            Q(gloss__contains=search_query) |
            Q(tone__contains=search_query) |
            Q(dialect__contains=search_query)
        )

    paginator = Paginator(words_all, 25)
    page = request.GET.get('page')

    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        words = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        words = paginator.page(page)

    min_page = max(1, int(page)-3)
    max_page = min(min_page + 6, paginator.num_pages)
    paginator_template_range = range(min_page, max_page+1)

    return render(request, 'words/mywords.html', {
        'words': words,
        'num_pages': paginator.num_pages,
        'page': int(page),
        'is_filtered': search_query is not None,
        'range': paginator_template_range,
        'search_query': search_query
    })
