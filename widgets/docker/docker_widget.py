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
        self.update(self.get_docker_containers())

    def get_docker_containers(self):
        
        containers = str(check_output('docker container ps -a', shell=True)).split('\\n')
        containers = containers[1:len(containers) - 1]
        return str(len(containers))
