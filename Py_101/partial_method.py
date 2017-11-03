import wx
from functools import partial


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def run(func):
    print(func())


def main():
    a1 = partial(add, 1, 2)
    a2 = partial(add, 1)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(a2(2))
    run(m1)


class MainFrame(wx.Frame):
    """
    This app shows a group of buttons
    """

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super(MainFrame, self).__init__(parent=None, title='Partial')
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn_labels = ['one', 'two', 'three']
        for label in btn_labels:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, partial(self.onButton, label=label))
            sizer.Add(btn, 0, wx.ALL, 5)

        panel.SetSizer(sizer)
        self.Show()

    def onButton(self, event, label):
        """
        Event handler called when a button is pressed
        """
        print("Your pressed: " + str(label))


if __name__ == "__main__":
    main()

    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
