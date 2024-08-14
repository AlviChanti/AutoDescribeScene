

Alwi Gelagaew (https://github.com/AlviChanti)
Austria  
09.08.2024

"Describe Scene"
Program Overview: 
"Describe Scene" is a software application designed to assist visually impaired individuals by utilizing the ChatGPT-4o's ability to describe images. The program takes a screenshot of a film or any video, sends it to ChatGPT-4's image input feature, and requests a content description.

Requirements:  
An active ChatGPT-4o account with image input capabilities.
A maximized ChatGPT-4o window open behind the video window you are currently watching.

Setup Instructions:

1. First Activation:  
   Upon the first activation of the `SetClickPoints.exe` file, you will need to set up your action sequence. Each textbox will save the X and Y coordinates where you move the cursor and click. Attention: fill all 8 boxes with coordinates value. Even if you'll find there extra, unnessesary, mouse cursor moves! Otherwise python script won't work.

2. Saving Coordinates: 
   After setting the coordinates, they will be saved in the 'coordinates.txt' file. You will not need to set them again unless changes are necessary. If desired, you can start the program directly using `main.exe` after the initial setup.

3. Backup Coordinates:  
   Be sure to copy your X and Y coordinates from 'coordinates.txt' to 'coordinates copy.txt' for backup. If you accidentally delete the original coordinates, you can restore them from `coordinates_copy.txt`.



Working Sequence:

1. Pause the video at the desired moment by pressing the spacebar.
2. Press 'Ctrl+Alt+T' to take a screenshot and upload the image to AI.
3. Wait for the scene description.
4. The program will automatically return to the video tab, overlapping the ChatGPT window.
5. Resume the video by pressing the spacebar.

Notes:

Shortcut Differences:  
  There are two distinct shortcuts:  
  'Ctrl+Alt+T': For brief, standard descriptions (faster execution).  
  'Ctrl+Alt+D': For detailed descriptions.

Cursor Positioning:  
  The cursor positions in the PowerShell script are upscaled, not physical ones! They are upscaled by a factor of 1.25 in the Python script. Depending on your screen resolution and other factors, adjustments may be needed in both Python scripts! Be aware of this effect!

