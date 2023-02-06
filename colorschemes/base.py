class Colorscheme:
    """ Colorscheme dataclass """
    __slots__ = ('primary_color', 'secondary_color', 'status_color_bad',
            'status_color_good', 'status_color_ok', 'fatal_color')

    def __init__(self, primary_color: str, secondary_color: str, status_color_bad: str,
            status_color_good: str, status_color_ok: str, fatal_color: str):
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.status_color_ok = status_color_ok
        self.status_color_good = status_color_good
        self.status_color_bad = status_color_bad
        self.fatal_color = fatal_color
        
