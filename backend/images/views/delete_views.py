from django.shortcuts import render, redirect, reverse
from django.views.generic import DeleteView

from ..models import Files


def delete_img(request):
    image_id = request.GET.get('image_id')

    if image_id:
        image = Files.objects.filter(id=image_id).first()

        if image:
            return redirect(f'/delete/{image_id}')

        return render(request, 'images/not_found.html', {
            'message': 'Попробуйте ещё раз',
            'redirect_url': reverse('delete')
        })

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