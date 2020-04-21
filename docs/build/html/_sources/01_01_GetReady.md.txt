# Getting Ready (Installing Python & Spyder)

## 1. Installation

### Check for an Existing Installation
You may already have Python installed, so check this first. Finding out whether Python is installed, can be done by:

- opening a Command Prompt on your Machine (Command Prompt in Windows; Terminal in Mac/OSX; bash shell or similar in other machines)-
- running the following command: ```python```

![](../../images/01_01/1.png)

Make sure that you have a version of Python 3 installed (e.g. 3.7).
Note that it is possible to have a version 2 and 3 installed side by side.

If you have only a version 2 installed, or you want to upgrade your version 3 installation,
please check "Fresh Install" below.

### Fresh Install
You can install the newest version of Python from <https://www.python.org/downloads/>.
Please follow the provided instructions.

If you already have a version 3 installation, this one will be overwritten by the new version.

![](../../images/01_01/2.png)

### Useful Commands in the Command Prompt
To install new modules, packages or Python versions, you will need to use the Command Prompt / Terminal / Bash Shell.
Although the name of this interface differs for each operating system (Windows/Linux/etc.), 
the functionality is very similar.

The *regular command prompt window* always lists the current Path in which you are. In the previous image, the path is "C:\Users\pipauwel\Python". All commands are executed at that location.

On Windows, ```dir``` provides a list of all files and folders at the current location.
For Linux based systems (e.g. OSX from Apple), the ```ls``` command is used instead.

On most operating systems, you can use the following commands to change directory:

- ```cd foldername```: moves to folder with particular foldername, located at the current location
- ```cd path/to/dir```: moves to folder specified by a path
- ```cd ..```: moves to upper directory (the folder that contains the folder you are currently at)
- ```mkdir```: creates a new folder

## 2. Executing Python from the Command Prompt

### Starting the Python Shell

You can use the Python Shell to directly execute Python code.
Although this is not the most convenient way to develop and run scripts,
it is very accessible to try out your first commands.

To start the Python shell, you can do the following:

- open a Command Prompt / Terminal / Bash Shell on your Machine
- run the command ```python```
- you will see that a ```>>>``` command line opens, which is a place where you can include and execute Python commands directly.

![](../../images/01_01/3.png)

### Using the Python shell
In the Python shell, you can execute Python code directly. For example, you can execute the following commands:

```python
print("Hello world")
```

```python
(1+4) * 2
```

The result of the command is displayed immediately in the shell.

![](../../images/01_01/4.png)

### Executing python scripts from a command-line interface
You can also include the above Python commands in a file to execute them.
For example, you can use Notepad++ or even a simple text editor, add the command and save the file in a .py format.

- Create file hello.py with contents ```print("Hello world")```
- Execute the script from the Python command prompt:
```python
python path/to/hello.py
```

### Closing the Python shell
To stop using the ```>>>``` Python command prompt, exit python as follows:

- Windows: press Ctrl-Z and Enter
- OS X and Linux: press Ctrl-D
- Run the python command ```exit()```

## 3. Spyder

### What is Spyder?
Spyder is a so-called Integrated Development Environment (IDE). In contrast to basic code editors, it provides autocompletion, debugging and testing functionality. You can use this environment to develop, improve and run your code.

You can download Spyder using Anaconda [Here](https://www.spyder-ide.org/ "Download page").

### How to use Spyder?
After the installation has finished, you can run Spyder. You will see an interface with different panels, each of which is discussed briefly below.

#### The IPython Console

![](../../images/01_01/5.png)

In the console, you will be able to run commands like you would in the Python Shell when we used the command prompt/terminal.
For example, we can type ```print("Hello world")``` and hit enter to run this command.

![](../../images/01_01/6.png)

#### The Editor

![](../../images/01_01/7.png)

In the editor, you are able to write a sequence of commands and save them.
Basically, you will do the same here as we did earlier when we used a text editor to create a .py file.

When you press the small play button in the top menu, your script will be executed.
You will see the output in the console.

![](../../images/01_01/8.png)

#### The Variable Explorer

You can use the Variable Explorer tab to get a quick overview of the variables that you have created.

- Run ```variable = "this is a value"``` to create a variable.
- You will see this variable and the value that you defined in the Variable Explorer tab.

![](../../images/01_01/9.png)

In the next section variables are discussed in greater detail.


