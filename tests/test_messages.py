import shutil

import pytest

from bot.messages import find_reply, load_data, regex_from_file


@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch, tmp_path):
    d = tmp_path / "bot" / "data"
    d.mkdir(parents=True)
    f = d / "test_messages.json"
    shutil.copy("tests/test_data/test_messages.json", f)
    monkeypatch.chdir(d)


def test_load_data(monkeypatch):
    # test_data = load_data("test_messages")
    # assert test_data == ""
    pass


def test_find_reply():
    pass


def test_regex_from_file():
    pass
