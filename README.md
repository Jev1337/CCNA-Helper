# CCNA Helper

Step 1:
Build with:
```py
pyinstaller --onefile --windowed --icon icon.ico -n PacketTracerLoader ccna.py
```

Step 2: Copy "settings.json" "icon.png" "index.html" "disp.py" inside dist folder.

Step 3: Configure settings in settings.json:

CCNA_HTML_LOCATION : This parameter is to locate where the answers are in .html (downloaded from CCNAReponses website)<br>
HOTKEY : This parameter is the Auto Select + Copy + Get Answers hotkey<br>
MANUAL_KEY : This parameter only Copies the selection and gets the answers (does not auto select)<br>
PANIC_KEY : This parameter allows you to pick another key to close the app<br>
X_TOOLTIP : Where you want the answer to be shown (X coordinates)<br>
Y_TOOLTIP : Where you want the answer to be shown (Y coordinates)<br>
TOOLTIP_DURATION : How long you want the tooltip to stay on the screen for.<br>


HARDCODED Keys:<br>
F4 Button always closes the app<br>
RIGHT CONTROL is the button to use to SHOW answers.
