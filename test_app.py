from app import add, app


def test_home():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, Vybhava World!"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0