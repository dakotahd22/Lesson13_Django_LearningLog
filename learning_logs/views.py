
from django.shortcuts import render


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show the topics page."""
    return render(request, 'learning_logs/topics.html')
