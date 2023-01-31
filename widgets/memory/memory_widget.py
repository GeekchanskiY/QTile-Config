from .memory_utils import get_memory_usage

from libqtile import widget


class MemoryStatus(widget.base.InLoopPollText):
    defaults = [
        ('update_interval', 1.0, 'Refresh interval')
    ]
    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.add_defaults(MemoryStatus.defaults)
        
    def tick(self):
        self.update(self.get_memory_usage())

    def get_memory_usage(self):
        memory_usage = get_memory_usage()
        return(str(round((int(memory_usage["free"])/int(memory_usage["total"])) * 100, 2)))


