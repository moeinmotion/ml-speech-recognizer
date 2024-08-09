# ml-speech-recognizer

JARVIS is a Voice-Based AI assistant which is developed using Python and OpenAI.



Demo Video showcasing AI Assistant:

https://github.com/user-attachments/assets/f48aa817-2986-4dcb-81d2-f8d0593b56dd




# How to Install Virtual Environent

Virtualenv is a tool to set up your Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. You can install venv to your host Python by running this command in your terminal:


pip3 install virtualenv



To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:



 python<version> -m venv <virtual-environment-name>

 
Like so:




 mkdir (project-name)
 
 cd (project-name)
 
 python -m venv env




When you check the new project-name folder, you will notice that a new folder called env has been created. env is the name of our virtual environment, but it can be named anything you want.

If we check the contents of env for a bit, on a Mac you will see a bin folder. You will also see scripts that are typically used to control your virtual environment, such as activate and pip to install libraries, and the Python interpreter for the Python version you installed, and so on. (This folder will be called Scripts on windows).

The lib folder will contain a list of libraries that you have installed. If you take a look at it, you will see a list of the libraries that come by default with the virtual environment.

# How to Activate the Virtual Environment
Now that you have created the virtual environment, you will need to activate it before you can use it in your project. On a mac, to activate your virtual environment, run the code below:

source env/bin/activate

This will activate your virtual environment. Immediately, you will notice that your terminal path includes env, signifying an activated virtual environment.
