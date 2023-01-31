"""
    Volume change controls
"""

from os import walk
from subprocess import check_output, run

#mute_command = 'amixer -D pulse sset Master 0%'


def set_volume(volume: int) -> None:
    """ Set volume % """
    
    if volume > 100 or volume < 0:
        return

    command = f'amixer -D pulse sset Master {volume}%'
    
    run(command, shell=True)

    return

def mute() -> None:
    """ Mute function """

    set_volume(0)

    return


def check_volume() -> int:
    """ Return volume int from amixer """
    command = 'amixer -D pulse sget Master'
    data = str(check_output(command, shell=True))
    volume = int(data.split("\\n")[-2].split("[")[1].split("]")[0]\
            .replace("%", ""))
    return volume
        
def increace_volume(percent: int) -> None:
    """ Increase volume by percent """
    
    set_volume(check_volume()+percent)

    return

