# layouts.py
from libqtile import hook, layout, bar, widget, qtile
# my modules
from .colors import colors


def init_layout_theme():
    """
    Defines the window tile colors and dimensions.
    """
    return {
        "border_width": 3,
        "margin": 6,
        "border_focus": colors[8],
        "border_normal": colors[0]
    }


layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Tile(
        shift_windows = True,
        border_width = 0,
        margin = 0,
        ratio = 0.335
    ),
    layout.Max(
        border_width = 0,
        margin = 0
    ),
]
