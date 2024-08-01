from django.shortcuts import render, redirect, get_object_or_404
from .models import Vocabulary, DailyPrompt, DailyWriteUp
from django.contrib.auth.decorators import login_required
import random
from .utils import fetch_daily_prompt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def home(request):
    return render(request, 'vocab_app/home.html')


@login_required
def vocabulary_list(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        definition = request.POST.get('definition')
        example_sentence = request.POST.get('example_sentence')
        Vocabulary.objects.create(word=word, definition=definition, example_sentence=example_sentence)
        return redirect('vocabulary_list')  
    vocabularies = Vocabulary.objects.all()
    return render(request, 'vocab_app/vocabulary_list.html', {'vocabularies': vocabularies})

@login_required
def submit_write_up(request):
    prompt = fetch_daily_prompt()
    vocabularies = random.sample(list(Vocabulary.objects.all()), 3)
    if request.method == 'POST':
        write_up = request.POST.get('write_up')
        DailyWriteUp.objects.create(user=request.user, write_up=write_up)
        return redirect('view_write_ups')
    return render(request, 'vocab_app/submit_write_up.html', {'vocabularies': vocabularies, 'prompt': prompt})

@login_required
def view_write_ups(request):
    write_ups = DailyWriteUp.objects.filter(user=request.user).order_by('-date')
    return render(request, 'vocab_app/view_write_ups.html', {'write_ups': write_ups})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def delete_write_up(request, write_up_id):
    write_up = get_object_or_404(DailyWriteUp, id=write_up_id, user=request.user)
    if request.method == 'POST':
        write_up.delete()
        return redirect('view_write_ups')
    return render(request, 'vocab_app/confirm_delete.html', {'write_up': write_up})


@login_required
def delete_vocab(request, vocab_id):
    word = get_object_or_404(Vocabulary, id=vocab_id)
    if request.method == 'POST':
        word.delete()
        return redirect('vocabulary_list')
    return render(request, 'vocab_app/confirm_delete.html', {'write_up': word})

