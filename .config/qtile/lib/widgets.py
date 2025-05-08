#widgets.py
from libqtile import widget
from qtile_extras.widget import Battery
import os
# my modules
from .icons import make_icon_widget
from .colors import colors

currTerminal = "alacritty"


# CLASS FOR DYNAMICALLY CHANGING THE BATTERY COLOR
class DynColorBattery(widget.Battery):
    def __init__(self, **config):
        config["markup"] = True
        config.setdefault("format", "{percent:2.0%} {char}   ")
        config.setdefault("update_interval", 10)
        super().__init__(**config)
    def update(self, status):
        # Default values if battery doesn't read
        percent = 0
        color = "#ffffff"
        char = '!'

        # Try to extract percentage from the string
        if isinstance(status, str):
            import re
            if "FULL" in status or "Full" in status:
                percent = 100
            else:
                match = re.search(r"(\d+)%", status)
                if match:
                    percent = int(match.group(1))

        # choose color
        if percent <= 25:
            color = "#ff0000"
            char = ''
        elif percent <= 50:
            color = "#ffaa00"
            char = ''
        elif percent <= 75:
            color = "#ffff00"
            char = ''
        else:
            color = "#00ff00"
            char = ''

        # Set the markup language
        self.markup = True

        # Define the text variable to conatain the markup conversion
        text = f'<span foreground="{color}">{percent:.0f}% {char}</span>'

        # Update the text
        super().update(text)


widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=0,
    background=colors[0],
)

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        # WINDOW NUMBERS
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize = 14,
            margin_y = 5,
            borderwidth = 3,
            active = colors[8],
            inactive = colors[1],
            highlight_color = colors[0],
            highlight_method = "line",
            this_current_screen_border = colors[7],
            this_screen_border = colors[4],
            other_current_screen_border = colors[7],
            other_screen_border = colors[4],
            rounded = False,
            diable_drag = True,
            padding = 1
        ),
        widget.TextBox(
            font = "Ubuntu Bold",
            fontsize = 16,
            text = " ",
            foreground = colors[1],
        ),

        # CURRENT OPEN PROGRAM/FILE
        widget.WindowName(
            text = "Centered text",
            font = "Ubuntu Bold",
            fontsize = 16,
            foreground = colors[6],
            padding = 10,
            max_chars = 130
        ),

        # HEADSET DETECTION
        #HeadsetDetector(),

        # NETWORK 
        widget.Net(
            font = "Ubuntu Bold",
            fontsize = 14,
            foreground = colors[8],
            format = '<span rise = "-14000"> {down:.2f}  {up:.2f}<span size = "8000">{up_suffix}</span></span>',
            padding = 8
        ),

        # ICON SPACER
        make_icon_widget(index = 0, interval = 10),

        # CPU 
        widget.CPU(
            font = "Ubuntu Bold",
            fontsize = 14,
            foreground = colors[3],
            format = '<span rise = "-14000"> CPU: {load_percent}<span size = "8000">%</span></span>',
            padding = 8,
            update_interval = 2
        ),

        # SPACER
        make_icon_widget(index = 1, interval = 10),

        # MEMORY 
        widget.Memory(
            font ="Ubuntu Bold",
            fontsize = 14,
            foreground = colors[4],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(currTerminal + ' -3 htop')},
            format = '<span rise = "-14000"> Mem: {MemUsed: .0f}<span size = "8000">{mm}</span></span>',
            padding = 8
        ),

        # ICON SPACER
        make_icon_widget(index = 2, interval = 10),

        # HARD DISK  
        widget.DF(
            font = "Ubuntu Bold",
            fontsize = 14,
            update_interval = 60,
            foreground = colors[7],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(currTerminal + ' -e df')},
            partition = '/',
            format = '<span rise = "-14000"> Disk: {uf}<span size = "8000">{m}</span></span>',
            padding = 8,
            visible_on_warn = False
        ),

        # ICON SPACER
        make_icon_widget(index = 3, interval = 10),

        # CLOCK  
        widget.Clock(
            font = "Ubuntu Bold",
            foreground = colors[5],
            fontsize = 14,
            format = '<span rise = "-14000"> %-I:%M<span size = "8000">%p</span></span>',
            padding = 8
        ),
    ]
    if os.path.exists("/sys/class/power_supply/BAT0"):(
            widgets_list.append(
                DynColorBattery(
                    font = "Ubuntu Bold",
                    fontsize = 16,
                    markup = True,
                    update_interval = 10
                )
            )
    )
    return widgets_list
