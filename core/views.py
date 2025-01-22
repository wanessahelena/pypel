from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def main(request):
    return render(request, "main.html")