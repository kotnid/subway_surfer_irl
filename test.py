import pyautogui
import time
import win32gui

# First, get a handle to the window you want to focus
handle = win32gui.FindWindow(None, "BlueStacks App Player")

# Next, set the focus to the window
win32gui.SetForegroundWindow(handle)

pyautogui.press("t")
while True:
    pyautogui.press("left")
    time.sleep(1)
    pyautogui.press("right")