from picture_dir import core


def test_dir_fullpath():
    from pathlib import Path

    root_path = Path("data")
    param = dict(place=str(root_path), year=2022, date="0517", event="テスト")
    assert str(core.dir_fullpath(param, "D90")) == "data/2022年/D90_0517_テスト"
