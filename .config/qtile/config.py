# config.py
from libqtile import hook, qtile
import subprocess
# my modules
from lib.keys import keys, groups, follow_mouse_focus, dgroups_key_binder
from lib.keys import dgroups_app_rules, main
from lib.screens import init_screens, screens
from lib.widgets import init_widgets_list, widget_defaults, extension_defaults
from lib.layouts import init_layout_theme, layouts, layout_theme
#from lib.headset import Headset_Detector


@hook.subscribe.startup_once
def assign_monitor_2_to_group():
    """
    Assign group '0' to screen index 1(monitor 2) on startup.This ensures that
    the workspace group labeled '0' is displayed on the second monitor when Qtile
    starts.

    Runs once per session from the '.startup_once' hook.
    """
    qtile.groups_map["0"].toscreen(1)


@hook.subscribe.startup
def set_mouse():
    """
    Ensures the mouse cursor is set to the standard 'left_ptr' using the xsetroot
    command.  This is useful for avoiding odd cursor shapes that can persist
    from display managers.

    Runs every time Qtile starts or restarts.
    """
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
