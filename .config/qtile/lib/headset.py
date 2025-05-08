# headset.py
import re
import subprocess
from libqtile.widget.textbox import ThreadPoolText
from libqtile.hook import subscribe
from libqtile import qtile
from libqtile.utils import Timer


## HEADSET DETECTION CLASS
class HeadsetDetector(ThreadPoolText):
    def __init__(self, **config):
        super().__init__(text="", **config)
        self.update_interval = 5
        self.headset_name = "Arctis Pro Wireless Game"
        self.headset_icon = ""

    def poll(self):
        try:
            result = subprocess.run(
                ["pactl", "list", "sinks"],
                capture_output=True,
                text=True
            )

            sinks = result.stdout.split("Sink #")
            for sink in sinks:
                if self.headset_name.lower() in sink.lower():
                    match = re.search(r"State:\s+(\w+)", sink)
                    if match and match.group(1).lower() != "suspended":
                        return self.headset_icon

        except Exception:
            pass
        return ""

# def is_headset_connected():
#     output = subprocess.check_output(['pactl', 'list', 'sinks'], text=True)
#     return 'bluez_output' in output.lower()

# def update_headset_widget(widget):
#     connected = is_headset_connected()
#     widget.visible = connected
#     widget.bar.draw()
#     Timer(10, lambda: update_headset_widget(widget)).start()

# @subscribe.startup_once
# def start_headset_monitor():
#     # Import your actual widget instance from config.py (or call this manually)
#     pass
