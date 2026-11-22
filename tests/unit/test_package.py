"""Check that the installed application package exposes its entry point."""

from importlib.metadata import distribution

from mp3_title_editor.__main__ import main


def test_installed_package_has_an_entry_point() -> None:
    assert distribution("mp3-title-editor").metadata["Name"] == "mp3-title-editor"
    assert callable(main)
