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

> The minimum required PyMakr version is `v2.22.5`
>
- Press `Ctrl`+`Shift`+`X` to get to extension in VS Code
- Search for PyMakr
- Click the `install` button

### Git

- If not already installed, install [git](https://git-scm.com/downloads/) on you computer. Otherwise you cannot clone repositories with git.

# Micropython Project Setup

Now we have completed the setup of VS Code to create, develop and test micropython projects within VS Code. It is time to create a micropython project within the given workspace `MyMicroPythonProjects`.

- Create a folder that contains all your micropython projects in VS Code by following the given steps:
  - Click on File -> Add folder to workspace...
  - Within the pop up window click rights and make a new folder
  - Name the folder as you want, here it is named `MyMicroPythonProjects`
  - Click the Add button, so the folder `MyMicroPythonProjects` is added to the workspace of VS Code
- Open a new terminal (Press `Ctrl`+`Shift`+`ö`)
- Initialize version control by typing the command `git init`
- Copy the file `.gitignore` from this repository root folder into `MyMicroPythonProjects`
- Add the [micropython-stubs](https://github.com/Josverl/micropython-stubs) repository as a submodule to the folder that will contain all your micropython projects with pasting `git submodule add https://github.com/Josverl/micropython-stubs.git` into the terminal command line and hit the enter key.
- Your `MyMicroPythonProjects` folder now should look like this:

  ```
  MyMicroPythonProjects/
  |-- .git/
  |-- micropython-stubs/
  |-- .gitignore
  |-- .gitmodules
  ```

As a next step, create a project folder that contains all the files of your project within the `MyMicroPythonProjects` workspace. Follow the steps to do so:
- Press `Ctrl`+`Shift`+`E` to navigate to the explorer within VS Code
- Hover your mouse over the workspace title bar and click the new folder button
- Name the folder as you would like. Here it is named `mpy_project_01`
- Now copy all content from this repository `template` folder into your `mpy_project_01`

## Python Environment

Since the project folder is now created, the project and the environment of the project have to be set, so a development with micropython is possible. As the needs of a project are highly depending on the projects requirements, it is reasonable to create an environment specifically for every project. Therefore, a virtual environment is part of all our micopython projects. In the next section a virtual environment is created.

### Virtual environment

To create a new virtual environment for your project, follow the steps:
- Open the terminal (Press `Ctrl`+`Shift`+`ö`)
- Then type `python -m venv venv` to create the virtual environment
- Select the interpreter `Ctrl`+`Shift`+`P` -> `Python: Select Interpreter` from the virtual environment (If not listed, enter the interpreter path: `.\venv\Scripts\python.exe`).

### Install Requirements

You will need the following packages within the virtual environment:
- `esptool`
- `pylint`

Open the terminal (Press `Ctrl`+`Shift`+`ö`) and activate the environment by typing `venv\Scripts\activate`.
Install the packages via `pip install pylint esptool`.

### Link the MicroPython Stubs

> If you don't use the template project and create a new clean project, you have to copy the files from the folder `micropython-stubs/docs/samples` into your project.

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
	"../micropython-stubs/stubs/micropython-v1_19_1-frozen/esp32/GENERIC",
	"../micropython-stubs/stubs/micropython-v1_19_1-esp32"
    ],
    "python.analysis.extraPaths": [
	"lib",
	"../micropython-stubs/stubs/cpython_core-pycopy",
	"../micropython-stubs/stubs/micropython-v1_19_1-frozen/esp32/GENERIC",
	"../micropython-stubs/stubs/micropython-v1_19_1-esp32"
    ]
  }
  ```
- Edit the line `init-hook=...` in the file `.pylintrc`.
  ```
	  init-hook='import sys;sys.path[1:1] = ["lib", "../micropython-stubs/stubs/cpython_core-pycopy", "../micropython-stubs/stubs/micropython-v1_19_1-frozen/esp32/GENERIC", "../micropython-stubs/stubs/micropython-v1_19_1-esp32",];'
  ```

### PyMakr Configuration

Before you can upload your project to a controller, you must configure PyMakr initially. This requires the following steps:

- Add the file `pymakr.conf` in your project root directory.
- Add following content. Change `mpy_project_01` in the line `name` to your project name.
  ```
  {
    "py_ignore": [
      ".vscode",
      "doc",
      "firmware",
      "env",
      "venv",
      ".env",
      ".venv",
      ".pylintrc",
      "pymakr.conf",
      "README.md",
      ".gitignore",
      ".git",
      "project.pymakr",
      "micropython-stubs"
    ],
    "name": "mpy_project_01"
  }
  ```

## Firmware

Download the device firmware from [MicroPython](https://micropython.org/download/) to your project firmware directory.

## Files and Folder

> This step is only necessary if you are setting up a new clean project and not using the template project.

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
|-- doc/
|-- firmware/
|   |-- esp32-20220117-v1.19.1.bin
|-- lib/
|-- venv/
|-- .pylintrc
|-- boot.py
|-- main.py
|-- pymakr.conf
|-- README.md
```

The project structure is ready for coding now. You have reached the second of three milestones.

# Project Deployment

## Flash the Firmware

Open the terminal (Press `Ctrl`+`Shift`+`ö`) and activate the environment by typing `venv\Scripts\activate`.
Flash the firmware by following the instructions for your device on [MicroPython](https://micropython.org/download/).
If you have an ESP32 you can perform following steps:
1. `python -m esptool --chip esp32 --port $COM-PORT$ erase_flash`
2. `python -m esptool --chip esp32 --port $COM-PORT$ --baud 460800 write_flash -z 0x1000 $NAME_OF_YOUR_MICROPYTHON_FIRMWARE$.bin`

## Upload and Run Project

Follow the steps to get the minimal code example to test if VS Code was set up correctly.
- Copy this
  ```
  from time import sleep

  while True:
    print("Congratulations, you have set up VS Code for Micropython Projects with ESP32 correctly")
    sleep(1)
  ```
  into `main.py`
- Switch to the PyMakr extension.
- Your project should be shown within the projects view.
- In your project, click on `ADD DEVICES` and select your device.
- Your device is now connected to the project and you can click connect (lightning icon) while hovering the mouse over the device.
- Afterwards click on `Sync project to device`.
- If this button is inactive, you should first click the `Stop all busy devices` button on your project.
- Upload your MicroPython project via the Pymakr `Upload` button or via `STRG`+`SHIFT`+`P` -> `Pymakr > Upload project`
- Now perform a device reset.
- Your program will now start and you should see the output in the terminal now.
