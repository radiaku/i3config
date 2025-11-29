#!/usr/bin/env python3

# sudo pacman -S python-pip
# sudo pacman -S python-i3ipc
# chmod +x ~/.config/i3/bin/i3-cycle-window.py
# chmod +x ~/.config/i3/bin/i3-switch-windows.py

import i3ipc

i3 = i3ipc.Connection()
tree = i3.get_tree()

focused = tree.find_focused()
workspace = focused.workspace()

# Collect all windows (both tiled and floating) on this workspace
windows = [w for w in workspace.leaves() if w.type == "con"]

if not windows or len(windows) == 1:
    exit(0)

# Find index of current window
current_index = next((i for i, w in enumerate(windows) if w.id == focused.id), -1)

# Focus the next window
next_index = (current_index + 1) % len(windows)
i3.command('[con_id="{}"] focus'.format(windows[next_index].id))
