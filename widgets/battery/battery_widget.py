from subprocess import check_output
import subprocess

from libqtile import widget

class BatteryWidget(widget.base.InLoopPollText):
    defaults = [
        ('update_interval', 60.0, 'Refresh interval')
    ]
    def __init__(self, colorscheme, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.add_defaults(BatteryWidget.defaults)

        self.colorscheme = colorscheme
        


    def tick(self):
        self.update(self._get_battery_percent())

    def _get_battery_percent(self):
        acpi = str(check_output("acpi", shell=True))
        adapter = True if str(check_output("acpi -a", shell=True)).split(" ")[2][0:2] == "on" else False
        
        

        

        percent = int(acpi.split(" ")[3].split("%")[0])
        
        if percent < 20:
            self.color = self.colorscheme.status_color_bad
        elif percent < 80:
            self.color = self.colorscheme.status_color_ok
        else:
            self.color = self.colorscheme.status_color_good

        self.layout = self.drawer.textlayout(
            self.formatted_text,
            self.color,
            self.font,
            self.fontsize,
            self.fontshadow,
            markup=self.markup,
        )

        percent = str(percent)
        res = percent + "" if adapter else percent+"%"
        return res


