from libqtile.widget import TextBox
from typing import List
from random import sample
from threading import Timer


_ICONS =  [
    # Font Awesome Icons
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "",  "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", ""
]


_ICON_COLORS: List[str] = [
    # Icon colors that get applied to the icons between the system widgets
    "#50fa7b", # green,
    "#f1fa8c", # yellow
    "#bd93f9", # purple
    "#ffb15f", # orange
]


def make_icon_widget(index: int, interval: int = 30) -> TextBox:
    """
    Creates a dynamic TextBox widget that displays a randomly chosen icon from the
    predefined list _ICONS.

    The displayed icon updates at the specified time interval in widgets.py. The
    default update duration is 30 seconds.
    """
    icon = TextBox(
        text = sample(_ICONS, 1)[0],
        font = "Ubuntu Bold",
        foreground = _ICON_COLORS[index % len(_ICON_COLORS)],
        fontsize = 9,
        padding = 9
    )

    def updateIcon():
        icon.update(sample(_ICONS, 1)[0])
        t = Timer(interval, updateIcon)
        t.daemon = True
        t.start()

    updateIcon()
    return icon
