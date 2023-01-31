from libqtile import widget
#from libqtile import manager
from .volume_utils import check_volume, increace_volume, mute, set_volume

class VolumeStatus(widget.TextBox):
    '''Widget that displays network status
       if theme_path is set it draws the
       widget as an icon'''
 
    defaults = (
    #    ("font", "Arial", "Text font"),
    #    ("fontsize", None, "Font pixel size. Calculated if None."),
        ("padding", 3, "Padding left and right. Calculated if None."),
    #    ("background", None, "Background colour."),
        ("color", "#000000", "Foreground colour."),
    #    ("theme_path", None, "Path of the icons"),
    #    ("update_interval", 0.2, "Update time in seconds."),
    )
    def __init__(self, **config):
        self.volume = check_volume()
        super().__init__(f"{self.volume}%", **config)
        self.name = "VolumeStatus"

    def plus_volume(self, value=10):
        increace_volume(value)
        self.update(f"{check_volume()}%")

    def minus_volume(self, value=10):
        increace_volume(-value)
        self.update(f"{check_volume()}%")
