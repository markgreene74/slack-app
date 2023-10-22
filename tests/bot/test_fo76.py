from collections import namedtuple

import pytest
import requests

from slackapp.bot.fo76 import get_updates

Response = namedtuple("Response", "status_code content")

RESPONSE_GOOD = Response(
    200,
    "<p>ALPHA</p>, <p>841 38 947</p>\n<p>BRAVO</p>, <p>676 23 748</p>\n<p>CHARLIE</p>, <p>512 39 897</p>",
)
RESPONSE_BAD = Response(
    200,
    "<p>ALPHA</p>, <p>841  38  947</p>\n<p>BRAVO</p>, <p>676 3 748</p>\n<p>CHARLIE</p>, <p>51239897</p>",
)


@pytest.mark.parametrize(
    "mocked_response,expected",
    [
        (RESPONSE_GOOD, "ALPHA:841 38 947\nBRAVO:676 23 748\nCHARLIE:512 39 897"),
        (RESPONSE_BAD, ""),
    ],
)
def test_get_updates(monkeypatch, mocked_response, expected):
    def mock_get(*args, **kwargs):
        return mocked_response

    monkeypatch.setattr(requests, "get", mock_get)

    content = get_updates(save_file=False)
    assert content == expected
