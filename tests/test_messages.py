import shutil

import pytest

from bot.messages import find_reply, load_data, regex_from_file

LOAD_DATA_EXPECTED = {
    "firsttest|[fF][iI][rR][sS][tT][ ]*[tT][eE][sS][tT]|testfirst|[tT][eE][sS][tT][fF][iI][rR][sS][tT]": "This is the reply to 'first test' and 'testfirst'",
    "secondtest|[sS][eE][cC][oO][nN][dD][ ]*[tT][eE][sS][tT]": "This is the reply to 'second test'",
    "thirdtest|[tT][hH][iI][rR][dD][ ]*[tT][eE][sS][tT]": "This is the reply to 'third test'",
}


@pytest.fixture(autouse=True)
def change_test_dir(monkeypatch, tmp_path):
    # create bot/data in the tmp_path
    d = tmp_path / "bot" / "data"
    d.mkdir(parents=True)
    # and copy the test files in it
    f = d / "test_messages.json"
    shutil.copy("tests/test_data/test_messages.json", f)

    monkeypatch.chdir(tmp_path)


def test_load_data():
    test_data = load_data("test_messages")
    assert test_data == LOAD_DATA_EXPECTED


def test_find_reply():
    pass


def test_regex_from_file():
    pass
