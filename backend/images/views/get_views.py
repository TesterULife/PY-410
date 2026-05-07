from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView

from ..models import Files


def get_img(request):
    image_id = request.GET.get('image_id')

    if image_id:
        image = Files.objects.filter(id=image_id).first()

        if image:
            return redirect(f'/get/{image_id}')

        return render(request, 'images/not_found.html', {
            'message': 'Попробуйте ещё раз',
            'redirect_url': reverse('get')
        })

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
