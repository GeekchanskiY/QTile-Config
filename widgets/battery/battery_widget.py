from subprocess import check_output
import subprocess

from libqtile import widget

class BatteryWidget(widget.base.InLoopPollText):
    defaults = [
        ('update_interval', 60.0, 'Refresh interval')
    ]
    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.add_defaults(BatteryWidget.defaults)
        


    def tick(self):
        self.update(self._get_battery_percent())

    def _get_battery_percent(self):
        acpi = str(check_output("acpi", shell=True))
        adapter = True if str(check_output("acpi -a", shell=True)).split(" ")[2][0:2] == "on" else False
        percent = acpi.split(" ")[3].split("%")[0]
        res = percent + "%+" if adapter else percent+"%"
        return res


