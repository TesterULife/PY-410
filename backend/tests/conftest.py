import pytest
import tempfile

from django.conf import settings


@pytest.fixture(autouse=True)
def temp_media_root(settings):
    with tempfile.TemporaryDirectory() as temp_dir:
        settings.MEDIA_ROOT = temp_dir

        yield