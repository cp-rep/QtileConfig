# keys.py
from libqtile.config import Key, Group, Drag, Click
from libqtile.lazy import lazy


# LOCAL VARIABLES
mod = "mod4"
mod1 = "alt"
mod2 = "control"
mod3 = "shift"


@lazy.function
def win_to_prev_group(qtile):
    """
    Moves the currently focused window to the previous group workspace.

    Checks if a window is currently focused and then determines the index of the
    current group and sends the window to the group that comes before it in the
    list.  Wraps around from modulus.
    """
    # Ensure a currently focused window
    if qtile.current_window is not None:
        # Get index of currently active group in list
        i = qtile.groups.index(qtile.current_group)

        # Get index of previous group, wrap around if needed
        prev_index = (i - 1) % len(qtile.groups)

        # Move focused window to previous group
        qtile.current_window.togroup(qtile.groups[prev_index].name)


@lazy.function
def win_to_next_group(qtile):
    """
    Moves the currently focused window to the next group workspace.

    Checks for a focused window and then moves it to the group that comes after
    the current one in the groups list. Wraps around from modulus.
    """
    if qtile.current_window is not None:
        # Get index of currently active group in list
        i = qtile.groups.index(qtile.current_group)

        # Get index of next group, wrap around if needed
        next_index = (i + 1) % len(qtile.groups)

        # Move focused window to next group
        qtile.current_window.togroup(qtile.groups[next_index].name)


@lazy.function
def swap_screens(qtile):
    """
    Swaps the active groups between screen 0 and screen 1.

    Exchanges the workspaces currently displayed on the first two screens, and
    then restores focus to the screen that was active before the swap.
    """
    # Get current screens 0 and 1
    screen0 = qtile.screens[0]
    screen1 = qtile.screens[1]

    # Get currently displayed screens 0 and 1
    group0 = screen0.group
    group1 = screen1.group

    # Store currently focused screen index
    active_screen = qtile.current_screen.index

    # Switch focus to screen 0
    qtile.cmd_to_screen(0)
    qtile.groups_map[group1.name].toscreen(toggle=False)

    # Switch focus to screen 1
    qtile.cmd_to_screen(1)
    qtile.groups_map[group0.name].toscreen(toggle=False)

    # Return focus to whichever screen was active before swap
    qtile.cmd_to_screen(active_screen)


@lazy.function
def toggle_screen_focus(qtile):
    """
    Toggle window focus bewteen two screens

    Checks which screen is currently focused and shifts focus to the other screen
    assuming a dual monitor setup.
    """
    # Get index of currently focused screen
    current = qtile.current_screen.index

    # Toggle focus between the the screens
    target = 1 if current == 0 else 0

    # Switch focus to screen at target index
    qtile.cmd_to_screen(target)


def win_to_next_screen(qtile, switch_group=False, switch_screen=False):
    """
    Move currently focused window to the next screen's group with wrap around.

    Moves the focused window to the group on the next screen.  If the current
    screen is the last index, it wraps around and moves the window it wraps wraps
    around and moves the window to the first screens group.
    """
    # Get index of currently focused screen
    current_index = qtile.screens.index(qtile.current_screen)

    # Get index of the next screen, wrap around if at last screen
    next_index = (current_index + 1) % len(qtile.screens)

    # Get name of group assigned to next screen
    target_group = qtile.screens[next_index].group.name

    # Move currently focused window to target group, switch group if
    # switch_group evaluates true
    qtile.current_window.togroup(target_group, switch_group = switch_group)

    # Change focus to next screen if switch_screen evalutes true
    if switch_screen:
        qtile.cmd_to_screen(next_index)


def win_to_prev_screen(qtile, switch_group=False, switch_screen=False):
    """
    Moves currently focused window to previous screen's group with wrap
    around.

    Finds the previous screen of the currently focused screen and wraps
    around when needed and focuses window of that screens group.
    """
    #Get index of currently focused screen
    current_index = qtile.screens.index(qtile.current_screen)

    # Get index of previous screen, wrap around if at first screen
    prev_index = (current_index - 1) % len(qtile.screens)

    # Get name of group assigned to previous screen
    target_group = qtile.screens[prev_index].group.name

    # Move currently focused window to target group, switch group if
    # switch_group evaluates true
    qtile.current_window.togroup(target_group, switch_group = switch_group)

    # Change focus to previous screen if switch_screen evaluates true
    if switch_screen:
        qtile.cmd_to_screen(prev_index)


## GROUP CONFIGURATION
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0"]
group_layouts = ["monadtall"] * 10
groups = [Group(name=n, label=l, layout=lay) for n, l, lay in zip(group_names, group_labels, group_layouts)]


## KEY CONFIGURATION
keys = [
    # LAUNCH TERMINAL
    Key([mod], "Return", lazy.spawn("alacritty"), desc = "Launch terminal"),

    # KILL WINDOW
    Key([mod], "q", lazy.window.kill(), desc = "Kill window"),

    # FULL SCREEN WINDOW
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc = "Toggle fullscreen"),

    # RESTART QTILE
    Key([mod, "shift"], "r", lazy.restart(), desc = "Restart Qtile"),

    # CHANGE WINDOW FOCUS
    Key([mod], "k", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "j", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "h", lazy.layout.left(), desc = "Move focus left"),
    Key([mod], "l", lazy.layout.right(), desc = "Move focus right"),

    # MOVE WINDOWS
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING WINDOW
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc = "Toggle floating"),

    # SWAP SCREEN 0 AND SCREEN 1
    Key([mod], "i", swap_screens, desc = "Swap screens"),

    # CHANGE FOCUS SCREEN 0 SCREEN 1
    Key([mod], "u", toggle_screen_focus, desc = "Toggle screen focus"),

    # SWAP SCREEN 0 SCREEN 1
    Key([mod, "shift"], "Right", lazy.function(win_to_next_screen, switch_screen = True)),
    Key([mod, "shift"], "Left", lazy.function(win_to_prev_screen, switch_screen = True)),

    # MOVE WINDOW GROUPS
    Key([mod, "control"], "Left", win_to_prev_group, desc = "Move win to prev group"),
    Key([mod, "control"], "Right", win_to_next_group, desc = "Move win to next group")
]


for group in groups:
    keys.extend([
        # SWITCH GROUP 0-9
        Key([mod], group.name, lazy.group[group.name].toscreen()),

        # MOVE CURRENT SCREEN TO SCREEN GROUP 0-9 AND FOLLOW
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name), lazy.group[group.name].toscreen()),

        # MOVE CURRENT SCREEN TO SCREEN GROUP 0-9 AND DONT FOLLOW
        Key(["mod1", "shift"], group.name, lazy.window.togroup(group.name)),
    ])


## MOUSE CONFIGURATION
mouse = [
    # TOGGLE FLOATING WINDOW
    Drag([mod], "Button1", lazy.window.set_position_floating(), start = lazy.window.get_position()),

    # RESIZE FLOATING WINDOW
    Drag([mod], "Button3", lazy.window.set_size_floating(), start = lazy.window.get_size())
]

# Disable the mouse dictating which window is active. i.e. must click to activate window
follow_mouse_focus = False

# Disable dynamic group keybinding
dgroups_key_binder = None

# Assign applications to dynamic groups. (none)
dgroups_app_rules = []

# Don't assign any window as the "main" window for Qtile
main = None
