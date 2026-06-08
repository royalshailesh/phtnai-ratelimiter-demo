from src.app import create_app


def test_health_ok():
    client = create_app().test_client()
    assert client.get("/health").status_code == 200


def test_rate_limit_trips():
    client = create_app().test_client()
    last = None
    for _ in range(7):
        last = client.get("/ping")
    assert last.status_code == 429
