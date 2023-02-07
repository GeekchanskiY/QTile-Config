from libqtile import widget

from subprocess import check_output

def get_memory_usage() -> dict:
    """ Gets current memory usage with free command """
    usage = str(check_output("free", shell=True)).split("\\n")[1].split("     ")
    total = usage[1].strip()
    used = usage[2].strip()
    free = usage[3].strip()
    return {
        "used": used,
        "free": free,
        "total": total,
    }



class MemoryStatus(widget.base.InLoopPollText):
    defaults = [
        ('update_interval', 1.0, 'Refresh interval'),
        ("foreground", "ffffff", "Foreground colour"),
    ]
    def __init__(self, colorscheme, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.colorscheme = colorscheme
        self.add_defaults(MemoryStatus.defaults)
        
    def tick(self):
        self.update(self._get_memory_usage())

    def _get_memory_usage(self):

        # TODO: check other color change solutions

        memory_usage = get_memory_usage()
        usage_percent = round((int(memory_usage["free"])/int(memory_usage["total"])) * 100, 1)
        if usage_percent > 80:
            self.color = self.colorscheme.status_color_good
        elif usage_percent > 50 and usage_percent <= 80:
            self.color = self.colorscheme.status_color_ok
        else: 
            self.color = self.colorscheme.status_color_bad

        self.layout = self.drawer.textlayout(
            self.formatted_text,
            self.color,
            self.font,
            self.fontsize,
            self.fontshadow,
            markup=self.markup,
        )
        return "Mem: " + str(usage_percent) + "%"


