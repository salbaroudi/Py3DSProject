### About this Project:

This is a simple project directory specifically designed for small to mid-level projects using python3.

It is structured as follows:

/PROJECTNAME:

|---/test: pytest scripts live here.

|---/data: project data is kept here. Iris and Mtcars sample datasets are included. **Note:** This folder is not ignored by .gitignore. You will have to uncomment outside the line, later on.

|---/notebooks: put jupyter notebooks here.

|- /sql: for sql scripts to pull/insert query data. I use this to construct databases with DataGrip.

|---/notes&logs: put personal notes, to do lists, etc here.

|---/web:

|------/{css,js,img,index.html}: webpage directories for flask or other python webservers.

|---/code:

|------/classes: put object classes here, all in one place.

|------/mods: Commonly used script code put here. 

|------req.txt: used with pip3 to install Development and Data Science Libraries Quickly.

|---readme.MD: you are reading this file right now.  

|---Makefile: use make command to run automated scripted tasks (launch servers, run test suites, cleanup, etc).

|---.gitignore: OS directory files, and the /env folder are ignored.

In addition to a test directory, and a jupyter notebook directory, I also add a make file and a small web-directory for a http.server instance.
This allows the user to quickly demonstrate their project online. Inspiration for this comes from [this project][link3].

Out of personal preference, I keep my venv /env folder outside the project directory. It sits one level above, as i use the same
libraries for all data science projects. 

**Note:** The directories are supposed to be empty, but [git won't keep them around][link1]. A hidden _.keep_ file
is put in every directory at risk of being ignored. Just delete these files after cloning. 

To do sandboxed python3 devleopment (with venv), do the following:

1. Clone this directory.
2. Enter the directory. Run _"python3.Y -m venv /env"_
3. Activate venv environment with _"source /env/bin/activate"_
4. Run _"pip3 install -r req.txt"_
5. Run _"git init"_ to start version control.

And you are ready to go. 

A more detailed explanation for this setup is [here][link2]

[link1]: https://stackoverflow.com/questions/115983/how-can-i-add-an-empty-directory-to-a-git-repository
[link2]: http://www.cumulativeparadigms.org/wordpress/index.php/2019/03/13/building-a-simple-python-environment-for-data-science-and-development/
[link3]: https://github.com/tdhopper/pythonplot.com
