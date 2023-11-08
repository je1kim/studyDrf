from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request):

    photos = Photo.objects.all()
    print(photos)

    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):

    photo = get_object_or_404(Photo, pk=pk) # get_objecet_or_404()는 모델로부터 데이터를 찾아보고 만약 찾는 데이터가 없다면 404 에러를 반환하는 함수

    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_post(request):
     
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()     # 저장 
            return redirect('photo_detail', pk=photo.pk)  #  photo_detail 페이지로 이동
    else:
        form = PhotoForm()

    return render(request, 'photo/photo_post.html', {'form': form})
def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)   # instance는 설정하므로 수정 대상이 될 데이터 설정
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()     # 저장 
            return redirect('photo_detail', pk=photo.pk)  #  photo_detail 페이지로 이동
    else:
        form = PhotoForm(instance=photo)

    return render(request, 'photo/photo_post.html', {'form': form})    