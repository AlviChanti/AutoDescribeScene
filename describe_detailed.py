import pyautogui
import os
import time
import ctypes
import sys
from ctypes import wintypes

# Constants
CURSOR_SHOWING = 0x00000001
TARGET_CURSOR_HANDLE = 65567  # The handle to detect
# Define the CURSORINFO structure
class CURSORINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("hCursor", wintypes.HANDLE),
        ("ptScreen", wintypes.POINT)
    ]
# Get cursor information
def get_cursor_info():
    cursor_info = CURSORINFO()
    cursor_info.cbSize = ctypes.sizeof(CURSORINFO)
    ctypes.windll.user32.GetCursorInfo(ctypes.byref(cursor_info))
    return cursor_info

# Define the directory to save the screenshots
save_directory = r"C:\Users\User_1\Pictures\Saved Pictures"

# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Function to read coordinates from a file
def read_coordinates(file_path):
    coordinates = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    parts = line.strip().split(',')
                    x_value = int(parts[0].split(':')[1].strip())
                    y_value = int(parts[1].split(':')[1].strip())
                    coordinates.append((x_value, y_value))
    return coordinates

# Define necessary Windows API calls
user32 = ctypes.WinDLL('user32', use_last_error=True)
LOGPIXELSX = 88
LOGPIXELSY = 90

def get_scaling_factor():
    # Assuming a uniform scaling factor for simplicity
    # Retrieve DPI settings for the primary monitor
    hdc = user32.GetDC(None)
    dpi_x = ctypes.windll.gdi32.GetDeviceCaps(hdc, LOGPIXELSX)
    dpi_y = ctypes.windll.gdi32.GetDeviceCaps(hdc, LOGPIXELSY)
    user32.ReleaseDC(None, hdc)
    
    # Standard DPI is 96, so scaling factor is dpi/96
    scaling_factor_x = dpi_x / 96.0
    scaling_factor_y = dpi_y / 96.0
    
    return scaling_factor_x, scaling_factor_y

def scaled_to_physical(scaled_x, scaled_y):
    scale_x, scale_y = get_scaling_factor()
    physical_x = int(scaled_x * scale_x)
    physical_y = int(scaled_y * scale_y)
    return physical_x, physical_y

# Path to the coordinates file
coordinates_file_path = os.path.join(os.path.dirname(__file__), 'coordinates.txt')

# Read coordinates from the file
coords = read_coordinates(coordinates_file_path)

# Convert scaled coordinates to physical coordinates
coords = [scaled_to_physical(x, y) for x, y in coords]

# Assign coordinates to global variables
(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8) = coords[:8]

# Print values for debuggin purposes
# print(f"x1: {x1}, y1: {y1}")
# print(f"x2: {x2}, y2: {y2}")
# print(f"x3: {x3}, y3: {y3}")
# print(f"x4: {x4}, y4: {y4}")
# print(f"x5: {x5}, y5: {y5}")
# print(f"x6: {x6}, y6: {y6}")
# print(f"x7: {x7}, y7: {y7}")
# print(f"x8: {x8}, y8: {y8}")

# Initialize frame counter
frame_counter = 1

def take_screenshot():
    global frame_counter

    # Format the filename for the screenshot
    file_path = os.path.join(save_directory, f"frame{frame_counter}.png")

    # Take the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the specified directory
    screenshot.save(file_path)

    # Activate the window behind the first one (ChatGPT4 window)
    # time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

    # Move cursor to image input point and click
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()
    time.sleep(2)

    # Type the path to the image
    pyautogui.write(r'frame1.png')
    time.sleep(2)
    pyautogui.press('enter')

    time.sleep(3)
    # Click inside the input text area
    pyautogui.moveTo(x3, y3)
    pyautogui.click()
    # time.sleep(1)
    
    # Write the defined string
    # defined_string = "Describe image content. Provide only one version of the response, not double or redundant responses!"
    # pyautogui.write(defined_string)

    # Read the string from the file
    with open('prompt_detailed.txt', 'r') as file:
        defined_string = file.read().strip()
    # Write the string read from the file
    pyautogui.write(defined_string)
    time.sleep(2)


    pyautogui.moveTo(x4, y4)
    pyautogui.click()
    time.sleep(1)  # Allow some time for cursor movement
    pyautogui.moveTo(x5, y5)
    time.sleep(0.5)  # Allow some time for cursor movement
    pyautogui.moveTo(x6, y6)
    time.sleep(0.5)  # Allow some time for cursor movement
    pyautogui.moveTo(x7, y7)
    time.sleep(0.5)  # Allow some time for cursor movement
    pyautogui.moveTo(x8, y8)
    time.sleep(1)  # Allow some time for cursor movement
    # pyautogui.scroll(-500)

    while True:
        cursor_info = get_cursor_info()
        time.sleep(1)  # Allow some time for cursor movement
        if cursor_info.flags == CURSOR_SHOWING:
            if cursor_info.hCursor == TARGET_CURSOR_HANDLE:
                # print(f"Detected Target Cursor Handle: {cursor_info.hCursor}")
                break    
        time.sleep(1)

    time.sleep(1)  
    pyautogui.click()

    # Get back to the previous window 
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    # Exit programme
    sys.exit()

def on_hotkey():
    take_screenshot()

def main():
    on_hotkey()

if __name__ == "__main__":
    main()

