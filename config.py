# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell


#
#       GeekanskiY's QTile Config
#

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

from widgets.volume.volume_widget import VolumeStatus, increace_volume
from widgets.memory.memory_widget import MemoryStatus


import os
import subprocess


mod = "mod4"
terminal = "kitty"
browser = "google-chrome"

second_monitor = True


groupbox_colors = {
    "this_current_screen_border": "A50113",
    "this_other_screen_border": "211D21",
    "active": "FFFFFF",
    "inactive": "808080",
    "spacing": 15,
    "rounded": False

}

group_settings = {
        "": 0
}



@hook.subscribe.startup
def autostart():
    home=os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen(home)


keys = [

    Key([mod, 'shift'], "q",
       lazy.to_screen(0)),
    Key([mod, 'shift'], "w",
      lazy.to_screen(1)),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]


#
#   Widget settings and shortcuts
#

# Keyboard

keyboard = widget.KeyboardLayout(configured_keyboards=['us', 'ru'])
keys.extend([
    Key([mod,], "space", lazy.widget["keyboardlayout"].next_keyboard(),   desc="Next keyboard layout"),
 ])

# Volume Mixer

volume = VolumeStatus()

@lazy.function
def increace_volume(qtile):
    volume.plus_volume()

@lazy.function
def decrease_volume(qtile):
    volume.minus_volume()
    

keys.extend([
    Key([mod], "f", increace_volume, desc="Decrease_volume"),
    Key([mod], "d", decrease_volume, desc="Add volume"),
])





group_keys = [i for i in "1234567"]
group_names = ["main", "code", "browser", "messages", "work", "music", "stuff"]
group_icons = ["", "", "", "", "", "", ""]


groups = [Group(name=group_names[i], label=group_icons[i]) for i in range(len(group_keys))]

for name, key in zip(group_names, group_keys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                key,
                lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                key,
                lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="#fff", border_width=2, margin=2), # type: ignore
    # layout.Max(), # type: ignore
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=3),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/a.png",
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                keyboard,
                volume,
                MemoryStatus(),
                #widget.CurrentLayout(),
                widget.GroupBox(**groupbox_colors),
                widget.Prompt(),
                widget.WindowName(),
                widget.Battery(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("GeekanskiY's config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),
                widget.Clock(format="%H:%M"),
                widget.QuickExit(),
            ],
            30,
            background="211D21"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"


if second_monitor:
    screens.append(
        Screen(
        wallpaper="~/Pictures/a.png",
        wallpaper_mode='fill',

        top=bar.Bar([
            widget.GroupBox(**groupbox_colors),
            widget.WindowName(),
        ], 30),
        )

    )

