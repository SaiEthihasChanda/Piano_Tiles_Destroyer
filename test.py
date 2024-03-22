from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import math

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Flag to indicate if the game has started
game_started = False
start_button_center = None
left_extreme = None
right_extreme = None

while True:
    try:
        # Look for the gamedetailsbar on the screen
        #gamedetailsbar_location = pyautogui.locateOnScreen('gamedetailsbar.png', confidence=0.8)

        # If the game details bar is found, store its bounding limits
        if not game_started:
            gamedetailsbar_location = pyautogui.locateOnScreen('gamedetailsbar.png', confidence=0.8)

            if gamedetailsbar_location:
                left_extreme = gamedetailsbar_location.left
                right_extreme = gamedetailsbar_location.left + gamedetailsbar_location.width
                print("Game details bar found at:", gamedetailsbar_location)
                print("Left extreme:", left_extreme)
                print("Right extreme:", right_extreme)

        # If the game has not started yet, look for the start button
        if not game_started:
            start_button_location = pyautogui.locateOnScreen('start.png', confidence=0.8)
            if start_button_location is not None:
                s_left, s_top, s_width, s_height = start_button_location
                print("Start button found at:", start_button_location)
                # Click on the start button
                click(int((s_left + s_width) * 0.9), int((s_top + s_height) * 0.9))
                # Calculate the center position of the start button
                start_button_center = (s_top + s_height)*0.9
                print("Start button center:", start_button_center)
                game_started = True

        # Once the game has started, look for black pixels along the same horizontal line as the start button center
        else:
            if start_button_center is not None:
                screen_width, screen_height = pyautogui.size()
                for x in range(left_extreme, right_extreme, (right_extreme-left_extreme)//5):
                    # Get the color of the pixel at the same horizontal line as the start button center
                    color = pyautogui.pixel(int(x), int(start_button_center))
                    #print("Color at", x, ",", start_button_center, ":", color)
                    # Check if the color is black
                    if color == (0, 0, 0):
                        # Click on the black pixel
                        click(int(x), int(start_button_center))
                        #print("Clicked on black pixel at:", x, ",", start_button_center)
                    else:
                        pass

    except ImageNotFoundException as e:
        print("Image not found:", e)
