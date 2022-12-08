:exclamation: If you are using a ZIP file, skip Step 1 and step 3, but not Step 2.

:exclamation: In case of you using ZIP file, venv file will already be in the project repo.

1. Clone this repo

2. Go to repo: 

```
cd <absolute path to the project directory>
```

3. Create a virtual environment. To do that run the command:

```
python -m venv venv   
```

:exclamation: If you got the error like "virtualenv : command not found" - that means you don't have the virtualenv package installed. Install it with the command `pip install virtualenv` and go to the start of this step.

4. Then activate your venv:

```
venv\Scripts\activate.bat 
```

:exclamation: Make sure that there's a "(venv)" title at the start of a terminal path line - that means you've succeeded at venv-activation.

5. Install requirements: 

```
pip install -r requirements.txt
```

6. Activate program:

```
python main.py 
```

:exclamation: Make sure that there's a .ma file opened either in Maya or Notepad. # there is a file in a project directory for program testing as a fail safe. 
:exclamation: If you have niether Maya nor Notepad, just run the program without opening the .ma file.

Have fun!
