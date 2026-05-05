import uuid

from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView

from .forms import UploadFileForm
from .models import Files


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

    else:
        form = UploadFileForm()

    data = {
        'title': 'Загрузка изображений',
        'inf': 'Пожалуйста, перетащите изображения с вашего пк',
        'form': form,

    }

    return render(request, 'images/upload_image.html', data)


def get_img(request):
    image_id = request.GET.get('image_id')

    if image_id:
        return redirect(f'/get/{image_id}')

    show_info = Files.objects.order_by('-created_at')[:3]
    data = {
        'title': 'Получение изображений',
        'inf1': 'Последние добавленные изображения',
        'inf2': 'Здесь вы можете получить изображения введя id',
        'show_info': show_info,
    }

    return render(request, 'images/get_image.html', data)


class GetImgDetailView(DetailView):
    model = Files
    template_name = 'images/get_detail_image.html'
    context_object_name = 'getting_img'


def delete_img(request):
    image_id = request.GET.get('image_id')

    if image_id:
        return redirect(f'/delete/{image_id}')

    data = {
        'title': 'Удаление изображений',
        'inf': 'Введите id изображения, которое вы хотите удалить',
    }

    return render(request, 'images/delete_image.html', data)


class DeleteImgDetailView(DeleteView):
    model = Files
    success_url = '/delete'
    template_name = 'images/delete_detail_image.html'
    context_object_name = 'deleting_img'


def db_model(request):
    dats = {
        'title': 'Модель базы данных',
        'inf': 'База данных была описана следующим образом',
    }

    return render(request, 'images/db_model.html', dats)
