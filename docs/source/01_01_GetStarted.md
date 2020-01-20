# Installation

## Check for an Existing Installation
You may already have Python installed, so check this first. Finding out whether Python is installed, can be done by:

- opening a Command Prompt on your Machine (Command Prompt in Windows; Terminal in Mac/OSX; bash shell or similar in other machines)-
- running the following command: ```python```

![pythoncmdlinecheckversion](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_01/1.png?raw=true)

Make sure that you have a version of Python 3 installed (e.g. 3.7).
Note that it is possible to have a version 2 and 3 installed side by side.

If you have only a version 2 installed, or you want to upgrade your version 3 installation,
please check "Fresh Install" below.

## Fresh Install
You can install the newest version of Python from <https://www.python.org/downloads/>.
Please follow the provided instructions.

If you already have a version 3 installation, this one will be overwritten by the new version.

![Installation](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_01/2.png?raw=true)

## Useful Commands in the Command Prompt
To install new modules, packages or Python versions, you will need to use the Command Prompt / Terminal / Bash Shell.
Although the name of this interface differes for each operating system (Windows/Linux/etc.), 
the functionality is very similar.

The *regular command prompt window* always lists the current Path in which you are. In the previous image, the path is "C:\Users\pipauwel\Python". All commands are executed at that location.

On Windows, ```dir``` provides a list of all files and folders at the current location.
For Linux based systems (e.g. OSX from Apple), the ```ls``` command is used instead.

On most operating systems, you can use the following commands to change directory:

- ```cd foldername```: moves to folder with particular foldername, located at the current location
- ```cd path/to/dir```: moves to folder specified by a path
- ```cd ..```: moves to upper directory (the folder that contains the folder you are currently at)
- ```mkdir```: creates a new folder