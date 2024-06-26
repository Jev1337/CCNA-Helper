
# PacketTracerLoader
This is a guide on how to build and configure the PacketTracerLoader.
```py
pip install -r requirements.txt
```

## Building the Application
Build the application using PyInstaller. This will create a single executable file with all the dependencies included:
```py
pyinstaller --onefile --windowed --icon icon.ico -n PacketTracerLoader ccna.py
```
Copy the following files into the `dist` folder:
* `settings.json`
* `icon.png`
* `index.html`
* `disp.py`

## Configuring the Application
Configure the application by modifying the `settings.json` file:

* `CCNA_HTML_LOCATION`: Path to the .html file containing the answers (downloaded from the CCNAReponses website).
* `HOTKEY`: Key combination for the Auto Select + Copy + Get Answers function.
* `MANUAL_KEY`: Key combination to copy the selection and get the answers (does not auto select).
* `PANIC_KEY`: Key to close the app.
* `X_TOOLTIP`: X coordinate for the answer tooltip.
* `Y_TOOLTIP`: Y coordinate for the answer tooltip.
* `TOOLTIP_DURATION`: Duration (in milliseconds) for the answer tooltip to stay on the screen.

### Hardcoded Keys
* `F4`: Closes the application.
* `RIGHT CONTROL`: Shows the answer.

## Tested on

Note that this was ONLY tested on <a href="https://ccnareponses.com/ccna-2-examen-final-de-cours-srwe-v7-0-questions-reponses/"> the french version of CCNA 2 SWRE 7.0 on CCNAREPOSNES website</a>. This software can be improved to work with all versions.

## Responsability

I do not take any responsability for missuse of this software/script. This is done only for educational purposes.
