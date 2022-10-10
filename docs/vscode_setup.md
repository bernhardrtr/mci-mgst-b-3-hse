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
- Install the extensions `Python` + `Pylance` (Press `Ctrl`+`Shift`+`X` to get to extension in VS Code, search for the extensions and install them)

#### Extension PyMakr

As PyMakr is a key extension setting it up correctly is further explained here.

- Install the extension PyMakr within VS Code. (Press `Ctrl`+`Shift`+`X` to get to extension in VS Code, search for PyMakr)
- After installation click on the dropdown menu at the `Uninstall` button and select `Install Another Version...`. Select version **v1.1.18**.
- Edit the global settings (Press `Ctrl`+`Shift`+`P` -> `Pymakr > Global settings`).
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

- Create a folder that contains all your micropython projects in VS Code by following the given steps:
  - Click on File -> Add folder to workspace...
  - Within the pop up window click rights and make a new folder
  - Name the folder as you want, here it is named 'MyMicroPythonProjects'
  - Click the Add button, so the folder 'MyMicroPythonProjects' is added to the workspace of VS Code
- Open a new terminal (Press `Ctrl`+`Shift`+`ö`)
- Clone the [micropython-stubs](https://github.com/Josverl/micropython-stubs) repository into the folder that will contain all your micropython projects with pasting `git clone https://github.com/Josverl/micropython-stubs.git` into the terminal command line and hit the enter key

  Example folder structure:
  ```
  MyMicroPythonProjects/
  |-- micropython-stubs/
  |-- mpy_project_01/
  |-- mpy_project_02/
  |-- ...
  ```

Now we have completed the setup of VS Code to create, develop and test micropython projects within VS Code. It is time to create a micropython project within the given workspace 'MyMicroPythonProjects'

# Micropython Project Setup

As a first step, create a project folder that contains all the files of your project within the 'MyMicroPythonProjects' workspace. Follow the steps to do so:
- Activate the workspace folder 'MyMicroPythonProjects' with a click on File -> Add folder to workspace... and then choosing the folder 'MyMicroPythonProjects'
- Press `Ctrl`+`Shift`+`E` to navigate to the explorer within VS Code
- Press `Ctrl`+`K` to tell VS Code that a command follows and immediatly press `Ctrl`+`O` afterwards (This is the short cut to create a new folder within the workspace)
- Name the folder as you would like. Here it is named 'mpy_project_01'

## Python Environment

Since the project folder is now created, the project and the environment of the project have to be set, so a development with micropython is possible. As the needs of a project are highly depending on the projects requirements, it is reasonable to create an environment specifically for every project. Therefore, a virtual environment is part of all our micopython projects. In the next section a virtual environment is created.

### Virtual environment

To create a new virtual environment for your project, follow the steps:
- Open the terminal (Press `Ctrl`+`Shift`+`ö`)
- Change the directory to your project folder e.g. by typing `cd .\mpy_project_01\`
- Then type `python -m venv venv` to create the virtual environment
- Select the interpreter `Ctrl`+`Shift`+`P` -> `Python: Select Interpreter` from the virtual environment (If not listed, enter the interpreter path: `.\mpy_project_01\venv\Scripts\python.exe`).

### Install Requirements

You will need the following packages within the virtual environment:
- `esptool`
- `pylint`

Open the terminal (Press `Ctrl`+`Shift`+`ö`) and activate the environment by typing `venv\Scripts\activate`.
Install the packages via `pip install pylint esptool`.

### Link the MicroPython Stubs

- Copy the files from the floder `micropython-stubs/docs/samples` to your project root folder (e.g. 'mpy_project_01').
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

## Firmware

Download the device firmware from [MicroPython](https://micropython.org/download/) to your project root directory.

## Files and Folder

Add the following files to your project root directory:
- `boot.py`
- `main.py`

Add the following folder to your project root directory:
- `lib` for additional modules.

Example project structure:
```
mpy_project_01/
|-- .vscode/
|   |-- extensions.json
|   |-- settings.json
|   |-- tasks.json
|-- lib/
|-- venv/
|-- .pylintrc
|-- boot.py
|-- esp32-20220117-v1.18.bin
|-- main.py
```

The project structure is ready for coding now. You have reached the second of three milestones.

# Project Deployment

## Flash the Firmware

Open the terminal (Press `Ctrl`+`Shift`+`ö`) and activate the environment by typing `venv\Scripts\activate`.
Flash the firmware by following the instructions for your device on [MicroPython](https://micropython.org/download/).
If you have an ESP32 you can perform following steps:
1. `python -m esptool --chip esp32 --port $COM-PORT$ erase_flash`
2. `python -m esptool --chip esp32 --port $COM-PORT$ --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin`

## Upload and Run Project

Follow the steps to get the minimal code example to test if VS Code was set up correctly.
- Copy this
  ```
  from time import sleep

  while True:
    print("Congratulations, you have set up VS Code for Micropython Projects with ESP32 correctly")
    sleep(1)
  ```
  into 'main.py'
- Upload your MicroPython project via the Pymakr `Upload` button or via `STRG`+`SHIFT`+`P` -> `Pymakr > Upload project`
- Click the Run Button in the PyMakr toolstrip or via `STRG`+`SHIFT`+`P` -> `Pymakr > Run project`
