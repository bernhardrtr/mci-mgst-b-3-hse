# VS Code Setup

## Initial Installation

### Python

- Download and install [Python](https://www.python.org/downloads/). **Node.JS** requires one of the versions 3.7, 3.8, 3.9, 3.10.

### Node.JS

- Download and install [Node.JS](https://nodejs.org/en/).
- Configure Node.js native addon build tool. [See](https://github.com/nodejs/node-gyp#on-windows) for additional information.
  - Install Visual C++ Build Environment: [Visual Studio Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools) (using "Visual C++ build tools" workload) or [Visual Studio Community](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community) (using the "Desktop development with C++" workload)
  - Launch cmd, `npm config set msvs_version 2017`
  - Set the Python executeable path, `npm config set python /path/to/python.exe`

### Visual Studio Code

- Download and install [VS Code](https://code.visualstudio.com/download)
- Install the extensions `Python` + `Pylance`

#### Extension PyMakr

- Install the extension PyMakr within VS Code.
- Edit the global settings (`STRG`+`SHIFT`+`P` -> `Pymakr > Global settings`).
  In `pymakr.json` edit the following lines:
  ```
  ...
  "address": "",
  "username": "",
  "password": "",
  ...
  "py_ignore": [
      "pymakr.conf",
      ".vscode",
      ".gitignore",
      ".git",
      "project.pymakr",
      "env",
      "venv",
      "micropython-stubs"
  ],
  ...
  "autoconnect_comport_manufacturers": [
      "Pycom",
      "Pycom Ltd.",
      "FTDI",
      "Microsoft",
      "Microchip Technology, Inc.",
      "1a86",
      "Silicon Labs"
  ]
  ...
  ```
  If you want to use a specific port, set `"auto_connect": false` and then define the port `"address": "COM4"`.

### Git 

- If not already installed, install [git](https://git-scm.com/downloads/) on you computer. Otherwise you cannot clone repositories with git. 

### MicroPython Stubs

- Clone the [micropython-stubs](https://github.com/Josverl/micropython-stubs) repository next to your MicroPython projects.
  `git clone https://github.com/Josverl/micropython-stubs.git`
  Example folder structure:
  ```
  MyMicroPythonProjects/
  |-- micropython-stubs/
  |-- mpy_project_01/
  |-- mpy_project_02/
  ```

## Project Setup

### Python Environment

#### Virtual environment

- Create a new virtual environment for your project.
  Open the terminal and type `python -m venv venv`
- Select the interpreter `STRG`+`SHIFT`+`P` -> `Python: Select Interpreter` from the virtual environment (`./venv/Scripts/python.exe`).

#### Install Requirements

You will need following packages:
- `esptool`
- `pylint`

Open the terminal and activate the environment by typing `venv\Scripts\activate`.
Install the packages via `pip install pylint esptool`.

#### Link the MicroPython Stubs

- Copy the files from the floder `micropython-stubs/docs/samples` to your project root folder.
- Edit the file `.vscode/settings.json`. This is an ESP32 specific configuration example:
  ```
  {
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.languageServer": "Pylance",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.autoComplete.extraPaths": [
	"lib",
	"../micropython-stubs/stubs/cpython_core-pycopy",
	"../micropython-stubs/stubs/micropython-v1_18-frozen/esp32/GENERIC",
	"../micropython-stubs/stubs/micropython-v1_18-esp32"
    ],
    "python.analysis.extraPaths": [
	"lib",
	"../micropython-stubs/stubs/cpython_core-pycopy",
	"../micropython-stubs/stubs/micropython-v1_18-frozen/esp32/GENERIC",
	"../micropython-stubs/stubs/micropython-v1_18-esp32"
    ]
  }
  ```
- Edit the line `init-hook=...` in the file `.pylintrc`.
  ```
	  init-hook='import sys;sys.path[1:1] = ["lib", "../micropython-stubs/stubs/cpython_core-pycopy", "../micropython-stubs/stubs/micropython-v1_18-frozen/esp32/GENERIC", "../micropython-stubs/stubs/micropython-v1_18-esp32",];'
  ```

### Firmware

Download the device firmware from [MicroPython](https://micropython.org/download/) to your project root directory.

### Files and Folder

Add the following files to your project root directory:
- `boot.py`
- `main.py`

Add the following folder to your project root directory:
- `lib` for additional modules.

Example project structure:
```
mpy_project_01/
|-- .vscode/
|   |-- settings.json
|   |-- tasks.json
|-- venv/
|-- lib/
|-- .pylintrc
|-- boot.py
|-- esp32-20220117-v1.18.bin
|-- main.py
```

## Project Deployment

### Flash the Firmware

Open the terminal and activate the environment by typing `venv\Scripts\activate`.
Flash the firmware by following the instructions for your device on [MicroPython](https://micropython.org/download/).
If you have an ESP32 you can perform following steps:
1. `esptool --chip esp32 --port $COM-PORT$ erase_flash`
2. `esptool --chip esp32 --port $COM-PORT$ --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin`

### Upload Project

Upload your MicroPython project via the Pymakr `Upload` button or via `STRG`+`SHIFT`+`P` -> `Pymakr > Upload project`
