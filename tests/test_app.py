from app import create_app

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Us' in response.data

def test_non_existent_page(client):
    response = client.get('/non-existent')
    assert response.status_code == 404