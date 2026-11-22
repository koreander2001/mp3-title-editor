"""Launch the MP3 title editor."""

import wx


def main() -> None:
    app = wx.App()
    window = wx.Frame(None, title="MP3タイトル編集")
    app.SetTopWindow(window)
    window.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
