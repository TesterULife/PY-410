"""
Повторное удаление
"""
import pytest

from images.models import Files


def test_get_page(client):
    response = client.get('/delete')

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_deleting_img(client):
    image = Files.objects.create(
        file_name='test.png',
        file_type='image/png',
        image='uploads/test.png'
    )

    response = client.get(f'/delete/{image.id}')

    assert response.status_code == 200


@pytest.mark.django_db
def test_deleting_image_not_found(client):
    image_id = 999_999_999

    response = client.get(f'/delete/{image_id}')

    assert response.status_code == 404


@pytest.mark.django_db
def test_success_delete_image(client):
    image = Files.objects.create(
        file_name='test.png',
        file_type='image/png',
        image='uploads/test.png'
    )

    response = client.post(f'/delete/{image.id}')

    assert response.status_code == 302

    assert Files.objects.count() == 0


@pytest.mark.django_db
def test_duplicate_delete_image(client):
    image = Files.objects.create(
        file_name='test.png',
        file_type='image/png',
        image='uploads/test.png'
    )

    first_response = client.post(f'/delete/{image.id}')

    assert first_response.status_code == 302

    assert Files.objects.count() == 0

    second_response = client.post(f'/delete/{image.id}')

    assert second_response.status_code == 404