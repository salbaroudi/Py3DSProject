### About this Project:

This is a simple project directory specifically designed for small to mid-level projects using python3.


### Setting up a Python Environment:

Before you can run this project, you must have Python3, venv and a variety of libraries installed. The tutorial that follows is setup for an Ubuntu 18+ install. This has not been tested for Windows or Mac.

As Ubuntu's default python distribution typically lags behind the latest versions available, we need to build one from source and perform an altinstall. We don't want to upgrade python and install a number of packages for the default system python, as this put other user space programs at risk.

Firstly, download a python3.X distribution from the [Python website][pythonSite]:

Before you configure and compile a python altinstall, there a number of Ubuntu packages you might need. These are largely C/C++ libraries that
python packages wrap and reference. If these are not installed, you may encounter errors setting up your venv environment for this project. There are quite
a few potential packages to install [1][pack1] [2][pack2] [3][pack3]:

```
sudo apt-get install libbz2-dev
sudo apt-get install libffi-dev
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
```

Once this is installed, refer to the following [tutorial][link2] to setup venv and install all of the necessary libraries.

Out of personal preference, I keep my venv /env folder outside the project directory. It sits one level above, as I use the same
libraries for all data science projects. 

To do sandboxed python3 devleopment (with venv), do the following:

1. Clone this directory.
2. Enter the directory. Run _"python3.Y -m venv /env"_
3. Activate venv environment with _"source /env/bin/activate"_
4. Run _"pip3 install -r req.txt"_
5. Run _"git init"_ to start version control.

And you are ready to go. 

### Project Structure:

/PROJECTNAME:

|---/test: pytest scripts live here.

|---/data: project data is kept here. Iris and Mtcars sample datasets are included. **Note:** This folder is not ignored by .gitignore. You will have to uncomment outside the line, later on.

|---/notebooks: put older jupyter notebooks, and generated notebook presentations here.

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

|---.gitignore: used to exclude files and directories from git commit.

|---Start.ipynb: Basic template notebook to start project.

**Note:** The directories are supposed to be empty, but [git won't keep them around][link1]. A hidden _.keep_ file
is put in every directory at risk of being ignored. Just delete these files after cloning. 


## Notable Project Features:

### Python Flash for Simple Web Development:

This consists of a make file and a small web-directory for a http.server instance.
This allows the user to quickly demonstrate their project online. 

Inspiration for this comes from [this project][link3].

### Generating Project Presentations:

After experimenting/coding phase, it is a pain to start a new notebook and clean up the results. To speed up the process, cell-tagging and a cell extraction script is used to generate a hand selected iPython notebook. This can be processed by nbconvert to generate a results documents to share with others. To use this feature, run the following commands:

1. In your notebook, tag all cells you wish to select for a summary document. Any cell with a **non-empty** tag will be selected by the cell extraction script.
2. Run the following script: 

```

./src/pulltagcells.py ./<notebookname>ipynb ./<newnotebookname>.ipynb

```

3. Use nbconvert to convert the new notebook to a format of your choice:

```

jupyter nbconvert <yournotebook>.ipynb --to <html/pdf> --output <newnotebookname>.ipynb

```

### Citations:

The [cite2c module][citelink] provides this functionality. This module queries Zotero to find references to various works. Follow the instructions
on the project page to activate.


**END**


[pythonSite]: https://www.python.org/downloads/
[citelink]: https://github.com/takluyver/cite2c
[pack1]: https://stackoverflow.com/questions/12806122/missing-python-bz2-module
[pack2]: https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul
[pack3]: https://stackoverflow.com/questions/57743230/userwarning-could-not-import-the-lzma-module-your-installed-python-is-incomple
[link1]: https://stackoverflow.com/questions/115983/how-can-i-add-an-empty-directory-to-a-git-repository
[link2]: http://www.cumulativeparadigms.org/wordpress/index.php/2019/03/13/building-a-simple-python-environment-for-data-science-and-development/
[link3]: https://github.com/tdhopper/pythonplot.com
