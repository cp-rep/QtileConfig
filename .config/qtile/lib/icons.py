from libqtile.widget import TextBox
from typing import List
from random import sample, shuffle
from libqtile import qtile


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
        foreground = _ICON_COLORS[index % len(_ICON_COLORS)],
        fontsize = 9,
        padding = 9
    )

    icon_pool = []

    def get_next_icon():
        nonlocal icon_pool

        if not icon_pool:
            icon_pool = _ICONS.copy()
            shuffle(icon_pool)

        return icon_pool.pop()

    def update_icon():
        if hasattr(icon, "update"):
            icon.update(get_next_icon())
            
        qtile.call_later(interval, update_icon)

    icon.text = get_next_icon()
    qtile.call_later(interval, update_icon)

    return icon
