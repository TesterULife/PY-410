import logging
import uuid
from pathlib import Path

from django.shortcuts import render

from .forms import UploadFileForm
from .models import Files, Logs


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "services.log"

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

logger = logging.getLogger(__name__)


def upload_img(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']

            new_file_name = f"{uuid.uuid4()}_{file.name}"

            handle_upload_file(file, new_file_name)

            save_file = Files.objects.create(
                file_name=new_file_name,
                file_type=file.content_type,
                file_path=f'uploads/{new_file_name}'
            )



            logger.info(
                f'Файл {new_file_name} успешно загружен'
            )
            Logs.objects.create(
                file=save_file,
                status='upload',
            )

    else:
        form = UploadFileForm()

    data = {
        'title': 'Загрузка изображений',
        'inf': 'Пожалуйста, перетащите изображения с вашего пк',
        'form': form,
    }

    return render(request, 'images/upload_image.html', data)


def handle_upload_file(f, new_file_name):
    with open(f'uploads/{new_file_name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def get_img(request):
    data = {
        'title': 'Получение изображений',
        'inf': 'Введите id изображения, которое вы хотите увидеть',
    }

    return render(request, 'images/get_image.html', data)


def delete_img(request):
    data = {
        'title': 'Удаление изображений',
        'inf': 'Введите id изображения, которое вы хотите удалить',
    }

    return render(request, 'images/delete_image.html', data)


def db_model(request):
    dats = {
        'title': 'Модель базы данных',
        'inf': 'База данных была описана следующим образом',
    }

    return render(request, 'images/db_model.html', dats)
