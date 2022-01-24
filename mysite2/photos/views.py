from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Photo


def gallery(request):
    photos = Photo.objects.all()

    context = {'photos': photos}
    return render(request, 'photos/gallery.html', context)


def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})



