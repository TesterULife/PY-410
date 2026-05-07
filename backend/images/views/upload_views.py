import uuid

from django.shortcuts import render, redirect

from ..forms import UploadFileForm
from ..models import Files


def upload_img(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']

            new_file_name = f"{uuid.uuid4()}_{file.name}"

            file.name = new_file_name

            Files.objects.create(
                file_name=new_file_name,
                file_type=file.content_type,
                image=file
            )
            return redirect('success_add')

    else:
        form = UploadFileForm()

    data = {
        'title': 'Загрузка изображений',
        'inf': 'Пожалуйста, перетащите изображения с вашего пк',
        'form': form,

    }

    return render(request, 'images/upload_image.html', data)
