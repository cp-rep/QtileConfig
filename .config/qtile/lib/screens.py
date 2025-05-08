## screens.py
from libqtile import bar
from libqtile.config import Screen
# my modules
from .colors import colors
from .widgets import init_widgets_list


def init_screens():
    """
    Defines the screens and sets the top bar for each screen. This assumes a two
    monitor setup but will still function correctly with one monitor.
    """
    return [
        # SCREEN 0
        Screen(
            top = bar.Bar(
                widgets = init_widgets_list(),
                size= 27,
                background = colors[0]
            )
        ),
        # SCREEN 1
        Screen(
            top = bar.Bar(
                widgets = init_widgets_list(),
                size= 27,
                background = colors[0]
            )
        )
    ]


screens = init_screens()
