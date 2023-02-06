from .memory_utils import get_memory_usage 

from libqtile import widget


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
        self.update(self.get_memory_usage())

    def get_memory_usage(self):

        # TODO: check other color change solutions

        memory_usage = get_memory_usage()
        usage_percent = round((int(memory_usage["free"])/int(memory_usage["total"])) * 100, 2)
        if usage_percent > 80:
            self.color = self.colorscheme.status_color_bad
        elif usage_percent > 50 and usage_percent <= 80:
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
        return str(usage_percent)


