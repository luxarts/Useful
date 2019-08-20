# Install pynput
# pip install pynput

from pyntput.keyboard import Key, KeyCode, Listener

# Functions to call for each hotkey
def func1():
  print("I'm function 1!")

def func2():
  print("I'm function 2!)

# Keys combinations
combinations = {
  frozenset([Key.ctrl_l, KeyCode(char="f")]): func1,            # CTRL+F
  frozenset([Key.ctrl_l, Key.alt_l, KeyCode(char="f")]): func2, # CTRL+ALT+F
}

# Current pressed keys
currentKeys = set()

# Callbacks
def onPress(key):
  # Add to set object
  currentKeys.add(key)
  if frozenset(currentKeys) in combinations:
    # If current set is a valid hotkey
    combinations[frozenset(currentKeys)]()

def onRelease(key):
  # Remove from set object
  currentKeys.remove(key)

# Start to listen
with Listener(on_press=onPress, on_release=onRelease) as listener:
  listener.join()

print("Press Ctrl+f to execute func1 or Ctrl+Alt+f to execute func2")
