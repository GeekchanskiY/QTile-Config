from libqtile import widget
from subprocess import check_output

class DockerStatus(widget.base.InLoopPollText):
    defaults = [
        ('update_interval', 10.0, 'Refresh interval')
    ]
    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.add_defaults(DockerStatus.defaults)
        
    def tick(self):
        self.update(self.get_memory_usage())

    def get_memory_usage(self):
        
        return str(len(str(check_output('docker container ps -a', shell=True)).split('\\n')))
