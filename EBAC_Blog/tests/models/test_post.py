import pytest

from blog.factories import PostFactory
from django.urls import reverse

@pytest.fixture

def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
    
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == 'Test'