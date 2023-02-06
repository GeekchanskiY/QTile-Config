class Colorscheme:
    """ Colorscheme dataclass """
    __slots__ = ('primary_color', 'secondary_color', 'status_color_bad',
            'status_color_good', 'status_color_ok')

    def __init__(self, primary_color: str, secondary_color: str, status_color_bad: str,
            status_color_good: str, status_color_ok: str):
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.status_color_ok = status_color_ok
        self.status_color_good = status_color_good
        self.status_color_bad = status_color_bad
        
