from django.shortcuts import render


def privacy(request):
    return render(request, 'templates/privacy.html', {})
