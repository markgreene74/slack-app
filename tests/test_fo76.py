import requests

from bot.fo76 import get_updates


class MockResponseGood:
    def __init__(self) -> None:
        self.status_code = 200
        self.content = """
<p>ALPHA</p>, <p>841 38 947</p>
<p>BRAVO</p>, <p>676 23 748</p>
<p>CHARLIE</p>, <p>512 39 897</p>"""


def test_get_updates_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseGood()

    monkeypatch.setattr(requests, "get", mock_get)

    content = get_updates(save_file=False)
    assert content == "ALPHA:841 38 947\nBRAVO:676 23 748\nCHARLIE:512 39 897"


class MockResponseBad:
    def __init__(self) -> None:
        self.status_code = 200
        self.content = """
<p>ALPHA</p>, <p>841  38  947</p>
<p>BRAVO</p>, <p>676 3 748</p>
<p>CHARLIE</p>, <p>51239897</p>"""


def test_get_updates_failed(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponseBad()

    monkeypatch.setattr(requests, "get", mock_get)

    content = get_updates(save_file=False)
    assert content == ""
