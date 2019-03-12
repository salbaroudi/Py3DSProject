### About this Project:

This is a simple project directory specifically designed for small to mid-level projects using python3.3+

It is structured as follows:

/PROJECTNAME:

|---/env: this folder contains a venv environment for sandboxed development.

|---/test: pytest scripts live here.

|---/code:

|------/classes: put Object Classes here, all in one place.

|------/source: the main code for the project is stored here.

|---requirements.txt: used with pip3 to install Development and Data Science Libraries Quickly.

|---readme.MD: you are reading this file right now.  


**Note:** The directories are supposed to be empty, but [git won't keep them around][link1]. A hidden _.keep_ file
is put in every directory at risk of being ignored. Just delete these files after cloning. 

 
To do sandboxed python3 devleopment (with venv), do the following:

1. Clone this directory.
2. Enter the directory. Run _"python3.Y -m venv /env"_
3. Activate venv environment with _"source /env/bin/activate"_
4. Run _"pip3 install -r req.txt"_
5. Run _"git init"_ to start version control.

And you are ready to go. 

A more detailed explanation for this setup is detailed [here][link2]

[link1]: https://stackoverflow.com/questions/115983/how-can-i-add-an-empty-directory-to-a-git-repository
[link2]: https://www.cumulativeparadigms.com/wordpress
