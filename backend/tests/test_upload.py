import pytest
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
from images.models import Files


def test_upload_page(client):
    response = client.get('/upload')

    assert response.status_code == 200


@pytest.mark.django_db
def test_success_upload_image(client):
    image_path = Path('tests/test_files/test_pic.png')

    with open(image_path, 'rb') as img:
        test_file = SimpleUploadedFile(
            name='test_pic.png',
            content=img.read(),
            content_type='image/png'
        )

    response = client.post(
        '/upload',
        {'file': test_file}
    )

    assert response.status_code == 302


@pytest.mark.django_db
def test_upload_duplicate_image(client):
    image_path = Path('tests/test_files/test_pic.png')

    with open(image_path, 'rb') as img:
        image_content = img.read()

    first_file = SimpleUploadedFile(
        name='test_pic.png',
        content=image_content,
        content_type='image/png'
    )

    second_file = SimpleUploadedFile(
        name='test_pic.png',
        content=image_content,
        content_type='image/png'
    )

    response_1 = client.post(
        '/upload',
        {'file': first_file}
    )

    response_2 = client.post(
        '/upload',
        {'file': second_file}
    )

    assert response_1.status_code == 302
    assert response_2.status_code == 302

    assert Files.objects.count() == 2

    files = Files.objects.all()

    first_name = files[0].file_name
    second_name = files[1].file_name

    assert first_name != second_name


@pytest.mark.django_db
def test_upload_not_image(client):
    file_path = Path('tests/test_files/test_file.txt')

    with open(file_path, 'rb') as file:
        file_content = file.read()

    fake_file = SimpleUploadedFile(
        name='test_file.txt',
        content=file_content,
        content_type='text/plain'
    )

    response = client.post(
        '/upload',
        {'file': fake_file}
    )

    assert response.status_code == 200

    assert Files.objects.count() == 0


@pytest.mark.django_db
def test_success_redirect_after_upload(client):
    image_path = Path('tests/test_files/test_pic.png')

    with open(image_path, 'rb') as img:
        test_file = SimpleUploadedFile(
            name='test_pic.png',
            content=img.read(),
            content_type='image/png'
        )

    response = client.post(
        '/upload',
        {'file': test_file}
    )

    assert response.status_code == 302

    assert response.url == '/upload/success'