import pytest

from images.models import Files

@pytest.mark.django_db
def test_get_page(client):
    response = client.get('/get')

    assert response.status_code == 200


@pytest.mark.django_db
def test_success_get_image(client):
    image = Files.objects.create(
        file_name='test.png',
        file_type='image/png',
        image='uploads/test.png'
    )

    response = client.get(f'/get/{image.id}')

    assert response.status_code == 200


@pytest.mark.django_db
def test_getting_image_not_found(client):
    image_id = 999_999_999

    response = client.get(f'/get/{image_id}')

    assert response.status_code == 404


@pytest.mark.django_db
def test_success_redirect_after_get(client):
    image = Files.objects.create(
        file_name='test.png',
        file_type='image/png',
        image='uploads/test.png'
    )

    response = client.get(
        '/get',
        {'image_id': image.id}
    )

    assert response.status_code == 302

    assert response.url == f'/get/{image.id}'