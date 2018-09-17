***************************************
*** Programming with Python (NOTES) ***
***************************************

		
TIP:
	QUESTIONS TO ASK:
		(None, one, many)?				[None, 1, [1, 2, 3]]
		-CLASS, make sure all the METHODS (are looking in the BASE, root class being used)
		
		
# (I am Dean)(Anagram)(Idea man)	
		
PYTHON (CODE ACADEMY) JUL.17 - OCT.2, 2018 (INTENSIVE)($199)

MODERATOR 
	SHARMEEN (on Slack)

PYTHON 
	-CODE appears to be done in BROWSER
	
PYTHON (VERSION) 
	-go to TERMINAL (POWERSHELL or COMMAND PROMPT) 
	-type (python) 
		-at the TOP it should state the VERSION in the (PYTHON COMMANDLINE)
		************************************************************************************************************
		Python 3.6.0 |Anaconda 4.3.0 (64-bit)| (default, Dec 23 2016, 11:57:41) [MSC v.1900 64 bit (AMD64)] on win32
		Type "help", "copyright", "credits" or "license" for more information.
		************************************************************************************************************
		-I'm using (Python 3.6 VERSION)
	
PYTHON (PUBLISHING)
	https://python-packaging.readthedocs.io/en/latest/minimal.html
		Publishing On PyPI
		setup.py 
		__init__.py
	
COMMANDLINE (HOW USE PYTHON)
	-make sure it is INSTALLED first (*** check the VERSION, Python2 or Python3 are different ***)
	POWERSHELL 
		-run (*.py) by typing (python ex1.py) 
		-execute functions directly to the PYTHON CONSOLE 
			-type (python)(to activate PYTHON CONSOLE) 
	POWERSHELL (-i switch)(to run *.py files)(WITH PYTHON PROMPT)
		-go to folder where (python files are)
		-type 
			python -i startup.py 			#this executes the file (THEN GOES TO PYTHON PROMPT)
	COMMAND LINE (CMD.EXE) 
		-same as POWERSHELL 
		-type (python)(to activate PYTHON CONSOLE) 
	IDLE (?? not sure what this is, an EDITOR?) 
		-Book: Python The Hard Way (he says to NOT USE THIS?) 
		-rightclick TO OPEN (*.py) FILE 
	VS-CODE (Visual Studio Code)
		-use this to EDIT (*.py) files 
		-has AUTOCOMPLETE (add PYTHON extensions) 
	NOTEPAD 
		-don't forget to SAVE 
		-problem here is it can OPEN THE SAME FILE twice 
		-NO COLOR CODING
	NOTEPAD++ 
		-good editor 
		-used for NOTES 
		-does have COLOR CODING HERE
	CODE ACADEMY (ONLINE CONSOLE)
		-just type and run there
		-CON, this only seems to work for THE EXERCISE YOUR DOING 
		-NOT that easy to SAVE FILES 
	ATOM (IDE)(TEXT EDITOR)		https://atom.io/
		INSTALL 	
			"C:\Users\Pythagoras\Downloads\
				AtomSetup-x64.exe"
		DOCUMENTATION 
			https://atom.io/docs
		BOOKMARK (TIP)
			-to move BACK AND FORTH (between TWO PARTS OF CODE)
			-use FIND/REPLACE (FIND ONLY)
			-put in a comment (#**BOOKMARK**)
				-now SEARCH FOR (#**BOOKMARK**) and it will bounce you back and forth :)
	JUPYTER (IDE)(WEB APP TEXT EDITOR)
		-run code in browser
		-save files to (*.ipynb)
	ANACONDA (???) (I think I have a VERSION of this PYTHON installed?)
	PYCHARM (???)(editor?)
	iPYTHON (TERMINAL)
		-open from ANACONDA FOLDER, click on IPYTHON 
		-define a FUNCTION 
		-to SEE THE FUNCTION BODY (type ??)(<func>??)
			def test(aaa):
				return aaa 
			test??
				IPYTHON --------------------
				In [3]: test??
				Signature: test(aaa)
				Source:
				def test(aaa):
					return aaa
				File:      c:\users\pythagoras\documents\<ipython-input-1-4427b3b4ad36>
				Type:      function
				----------------------------
				
ATOM (EDITOR)(SHORTCUTS)
	https://github.com/nwinkler/atom-keyboard-shortcuts
	COMMENTS 		CTRL+/
	AUTO INDENT 	Edit, Line, (Auto Indent)
	FIND/REPLACE 	(to REPLACE a TAB or NEWLINE)
		-turn on REGEX MODE (.*) button 
		-REPLACE \n 	NEWLINE 
		-REPLACE \t 	TAB 
		
PROJECT STRUCTURE 
	TO RUN 
		-go to folder (with *.py files)
		-type 
			python -i startup.py 
			>>> #can run python code here (to test)
		--------
		PS C:\Users\Pythagoras\Documents\000-Code\code academy\python\000-CAPSTONE Project (Tom Rater)> python -i startup.py
		>>> p = Name('Dean', 'Jones')
		>>> p.__dict__
		{'first': 'Dean', 'last': 'Jones', 'fullname': 'Dean Jones'}
		--------
	startup.py 					#STARTUP SCRIPT (to load classes)
		from Name import *
		from Email import *
		from User import *
	User.py 					#CLASS
		from Name import *		#load dependencies (Name.py NAME CLASS)
		from Email import *		#load dependencies (Email.py EMAIL CLASS)
		class User:
			#code...
	Name.py
		class Name():	
			#code...
	Email.py
		class Email():	
			#code...
	
ESCAPE CHARACTERS 
	\\		BACKSLASH 
	\'		QUOTE 
		-TIP: to show a SINGLE QUOTE (')(WITHOUT ESCAPE SLASH) simply use DOUBLE-QUOTE STRING 
			eg. "I'm a single quote WITHOUT ESCAPING"
	\"			DOUBLE QUOTE 
	\a 			ASCII (BELL)(BEL)
	\b			ASCII (BACKSPACE)(BS)
	\f 			ASCII (FORMFEED)(FF)
	\n 			NEW LINE (ASCII LINEFEED)(LF)
	\N{name}	Character named in UNICODE DATABASE (UNICODE ONLY)
			eg. ???
	\r 			CARRIAGE RETURN (CR)
	\t 			TAB 
	\v 			ASCII (VERICAL TAB)(VT)
		
	\uxxxx 		Characer with HEX-VALUE (16-bit) value (xxxx, 4-digits)
			eg. \u0394
	\Uxxxx		Character with HEX-VALUE (32-bit) value (xxxxXXXX, 8-digits)
			eg. \U00000394
	\000 		Character with OCTAL-VALUE (000)
	\xhh 		Character with HEX-VALUE (hh)(replace hh with 0-9 A-F)
			eg. \xFF
	

INSTALL 
	-INSTALL PYTHON 3.6 
	https://www.python.org/downloads/release/python-360/
	-add PATH to ENVIRONMENT VARIABLES (to run from POWERSHELL)
	
INSTALL (JUPYTER)
	-Jupyter, is an open-source web application 
	-PIP (PIP3) (is an INSTALLATION TOOL, for the commandline)
	-(pip3) and (pip) are the same, an alias
	-using (conda) to install
	-AT COMMANDLINE 
		-type (pip install jupyter)(*** NOT FROM PYTHON SHELL ***)
			*************************************************
			PS C:\Program Files\Python36> pip install jupyter
			Requirement already satisfied: jupyter in c:\program files\anaconda3\lib\site-packages
			You are using pip version 9.0.1, however version 18.0 is available.
			You should consider upgrading via the 'python -m pip install --upgrade pip' command.
			*************************************************
	-UPGRADE (PIP)(to latest version pip-18.0)
		-type (python -m pip install --upgrade pip)(*** run as admin (powershell) ***)
			PermissionError: [WinError 5] Access is denied: 'c:\\program files\\anaconda3\\lib\\site-packages\\pip'
			PermissionError: [WinError 5] Access is denied: 'c:\\program files\\anaconda3\\lib\\site-packages\\pip\\basecommand.py'
			*************************************************
			PS C:\WINDOWS\system32> python -m pip install --upgrade pip
			Collecting pip
			Downloading https://files.pythonhosted.org/packages/5f/25/e52d3f31441505a5f3af41213346e5b6c221c9e086a166f3703d2ddaf940/pip-18.0-py2.py3-none-any.whl (1.3MB)
			    100% |...| 1.3MB 232kB/s
				****** NOTE, if you get a (PermissionError)(OPEN POWERSHELL, RUN AS ADMIN) ******
			Installing collected packages: pip
			  Found existing installation: pip 9.0.1
				Uninstalling pip-9.0.1:
				  Successfully uninstalled pip-9.0.1
			Successfully installed pip-18.0
			*************************************************
			
INSTALL ANACONDA (already installed)
	TEST INSTALL type (conda list)
		-PS C:\WINDOWS\system32> conda list			(this should list a bunch of functions)
	INSTALL JUPYTER type (conda install jupyter)
		-PS C:\WINDOWS\system32> conda install jupyter
			Y for YES (to proceed)
	VERIFY VERSION (ANACONDA VERSION)
		-PS C:\WINDOWS\system32> conda --version
			conda 4.3.30
	UPDATE CONDA 
		-PS C:\WINDOWS\system32> conda update conda
			-proceed (y, yes)
			...
			
ANACONDA (CONDA)(ENVIRONMENTS)		https://conda.io/docs/user-guide/getting-started.html
	-ENVIRONMENTS, anaconda allows you to create ENVIRONMENTS that contain (files and package dependencies)
		-sounds like a PROJECT FOLDER? 
	CREATE AN ENVIRONMENT 
		-PATH (C:\Program Files\Anaconda3\envs)
		-name: snowflakes 
		-package: BioPython 
		-type (conda create --name snowflakes biopython)
		-creates environment (project)
			'C:\Program Files\Anaconda3\envs\snowflakes'
	CREATE AN ENVIRONMENT (with different PYTHON VERSION)
		-type (conda create --name snakes python=3.5)
	ACTIVATE ENVIRONMENT 
		-type (activate snowflakes)
	GET (LIST OF) ENVIRONMENTS 
		-type (conda info --envs)
		**************
		conda environments:
			base           /home/username/Anaconda3							#this is DEFAULT
			snowflakes   * /home/username/Anaconda3/envs/snowflakes			#this ACTIVE or current directory with (* asterisk)
		**************
	DEACTIVATE (CHANGE BACK TO BASE ENVIRONMENT)
		-type (deactivate)
	PACKAGES 
		-C:\Program Files\Anaconda3\pkgs 

ANACONDA (INCLUDES)
	NAVIGATOR 
	PROMPT (ANACONDA)
	IPYTHON 
	JUPYTER NOTEBOOK 		(Jupyter Notebook is built off of IPython, an interactive way of running Python code in the terminal using the REPL model (Read-Eval-Print-Loop)
	JUPYTER QT CONSOLE 
	SPYDER 
	
JUPYTER NOTEBOOK 
	TO LAUNCH 
		*************************
		-type (cd ...)(change directory to where you want to SAVE FILES)
		-type (jupyter notebook)			#the program will instantiate a local server at localhost:8888 (or another specified port).
		*************************
		*** THIS SHOULD OPEN A BROWSER, with JUPYTER NOTEBOOK (web app running) ***
			-OTHERWISE, COPY/PASTE URL to browser manually
		-URL (http://localhost:8888/tree?token=d3f837877f8eee81b0dd77f6d1a66e17b70567a05ce31898)
			-The notebooks have a UNIQUE TOKEN since the software uses PRE-BUILT DOCKER CONTAINERS to put notebooks on their own unique path.
		-STOP THE SERVER (QUIT JUPYTER)
			-To stop the server and shutdown the kernel from the terminal, hit control-C twice
				CTRL+C, CTRL+C 
	JUPYTER INTERFACE (GUI, BROWSER) 
		-NOTEBOOKS (SEE notebook icon) or (*.ipynb) file type
	CREATE A NEW NOTEBOOK 
		-in JUPYTER BROWSER, (menu, NEW, PYTHON3 (notebook))
		-or UPLOAD (existing file)(*.ipynb)
		CELL (this is where you WRITE PYTHON CODE)
		RUN CODE (SHFT+ENTER, or click PLAY button)
		MARKDOWN (COMMENT)(change CELL TYPE, with PULLDOWN)
		-can move CELLS UP/DOWN (to organize)
	NOTEBOOK (FILE)(*.ipynb)
		-automatically SAVES 
		-They will exist in your directory as a JSON file with the extension (*.ipynb)
		-RENAME file (using FILE menu, RENAME)
		-EXPORT (to HTML file)
	SAVE FILE 
		-the LOCATION is whatever FOLDER (you START jupyter from...)
	(*.IPYNB)JSON file 
		-"cell_type": "code",		(used for code)
		-"cell_type": "markdown", 	(used for comments)
		
JUPYTER (OTHER FOLDERS)
	C:\Users\Pythagoras\AppData\Roaming\jupyter			#KERNEL
	C:\Users\Pythagoras\.jupyter							
	
PIP VS CONDA 
	PIP (manage python packages)(install)
		eg. (pip install jupyter)
	CONDA (anaconda package manager)(install)

------------------------------------------------
FUNCTIONS (*ARGS, **KWARGS) 
	*ARGS, asterisk form (*args) is used to pass a non-keyworded, variable-length argument list
	**KWARGS, and the double asterisk form is used to pass a keyworded, variable-length argument list.
	*(SINGLE ASTERISK) (returns a LIST)
	**(DOUBLE ASTERISK) (returns a DICTIONARY OBJECT)
	-*ARGS 
		are POSITIONAL (meaning the ORDER matters how you enter them when the FUNCTION IS CALLED)
	-**KWARGS (KEYWORD ARGUMENTS)
		are NOT POSITIONAL (meaning you can enter them in ANY ORDER, because they have a KEY)
	eg. 
		*ARGS
		def test_var_args(farg, *args)
			...
		test_var_args(1, "two", 3)
		---
		def testArgs(*args):
			print(*args)

		testArgs(1, 3, 4)			#1 3 4

		**KWARGS
		def test_var_kwargs(farg, **kwargs):
			... 
		test_var_kwargs(farg=1, myarg2="two", myarg3=3)
		-------------
		>>> def test2(farg, *args, **kwargs):
		...     print('farg: ', farg)
		...     print('*args: ', *args)
		...     for k,v in kwargs.items():
		...             print(k, ': ', v)
		...
		>>> test2(33)
		farg:  33
		*args:
		>>> test2(33, 1, 2, 3)
		farg:  33
		*args:  1 2 3
		>>> test2(33, 1, 2, 3, a=10, b=20, c=30)
		farg:  33
		*args:  1 2 3
		a :  10
		b :  20
		c :  30
		-------------
		ARGUMENTS (AS LIST)(*args)(* single asterisk, returns a LIST)
			-call ARGUMENTS in order, it turns them INTO LIST (behind scenes)
			>>> def test(*mylist):
			...     for x in mylist:
			...             print(x)
			-----
			test([1, 2, 3, 'elijafolukojall'])
			[1, 2, 3, 'elijafolukojall']
			>>> test(1, 2, 3, 'elijafolukojall')
			1
			2
			3
			elijafolukojall
		-------------
		ARGUMENTS (AS DICTIONARY)(**kwargs)(** double asterisk, returns DICTIONARY)
			-call ARGUMENTS as KEYWORD ARGUMENTS
			>>> def test(**my_dict):
			...     for k,v in my_dict.items():
			...             print(k, v)
			...
			>>> test(a=10, b=20, c=30)
			a 10
			b 20
			c 30
		-------------
FUNCTION (OPTIONAL ARGUMENTS)(DEFAULT)
	https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
	def info(object, spacing=10, collapse=1):
		...
		
FUNCTION (ARGUMENTS)(OPTIONAL)
	https://www.python.org/dev/peps/pep-0457/
	Instead, positional-only parameters can be specified in optional "groups". Groups of parameters are surrounded by square brackets, like so...
		def addch([y, x,] ch, [attr,] /):
			...
		Number of arguments	Parameter assignment
			0	raises an exception
			1	ch
			2	ch, attr
			3	y, x, ch
			4	y, x, ch, attr
			5 or more	raises an exception
		
HELP** FUNCTION 
	help() 
	help(int)
	help(list)
	help(len) 
		len(obj, /)
			Return the number of items in a container.
	import datetime 
	help(datetime.time)
		...
	
	help([1,2,3]) 	#will give help on LIST FUNCTIONS 
	lst = [1, 2, 3]
	>>> help(lst)
	Help on list object:

	class list(object)
	 |  list() -> new empty list
	 |  list(iterable) -> new list initialized from iterable's items
	 |
	 |  Methods defined here:
	 |
	 |  __add__(self, value, /)
	 |      Return self+value.
	 |
	 |  __contains__(self, key, /)
	 |      Return key in self.
	 |
	 |  __delitem__(self, key, /)
	 |      Delete self[key].
	 |
	 |  __eq__(self, value, /)
	 |      Return self==value.
	 |
	 |  __ge__(self, value, /)
	 |      Return self>=value.
	 |
	 |  __getattribute__(self, name, /)
	 |      Return getattr(self, name).
	 |
	 |  __getitem__(...)
	 |      x.__getitem__(y) <==> x[y]
	 |
	 |  __gt__(self, value, /)
	 |      Return self>value.
	 |
	 |  __iadd__(self, value, /)
	 |      Implement self+=value.
	 |
	 |  __imul__(self, value, /)
	 |      Implement self*=value.
	 |
	 |  __init__(self, /, *args, **kwargs)
	 |      Initialize self.  See help(type(self)) for accurate signature.
	 |
	 |  __iter__(self, /)
	 |      Implement iter(self).
	 |
	 |  __le__(self, value, /)
	 |      Return self<=value.
	 |
	 |  __len__(self, /)
	 |      Return len(self).
	 |
	 |  __lt__(self, value, /)
	 |      Return self<value.
	 |
	 |  __mul__(self, value, /)
	 |      Return self*value.
	 |
	 |  __ne__(self, value, /)
	 |      Return self!=value.
	 |
	 |  __new__(*args, **kwargs) from builtins.type
	 |      Create and return a new object.  See help(type) for accurate signature.
	 |
	 |  __repr__(self, /)
	 |      Return repr(self).
	 |
	 |  __reversed__(...)
	 |      L.__reversed__() -- return a reverse iterator over the list
	 |
	 |  __rmul__(self, value, /)
	 |      Return value*self.
	 |
	 |  __setitem__(self, key, value, /)
	 |      Set self[key] to value.
	 |
	 |  __sizeof__(...)
	 |      L.__sizeof__() -- size of L in memory, in bytes
	 |
	 |  append(...)
	 |      L.append(object) -> None -- append object to end
	 |
	 |  clear(...)
	 |      L.clear() -> None -- remove all items from L
	 |
	 |  copy(...)
	 |      L.copy() -> list -- a shallow copy of L
	 |
	 |  count(...)
	 |      L.count(value) -> integer -- return number of occurrences of value
	 |
	 |  extend(...)
	 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
	 |
	 |  index(...)
	 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
	 |      Raises ValueError if the value is not present.
	 |
	 |  insert(...)
	 |      L.insert(index, object) -- insert object before index
	 |
	 |  pop(...)
	 |      L.pop([index]) -> item -- remove and return item at index (default last).
	 |      Raises IndexError if list is empty or index is out of range.
	 |
	 |  remove(...)
	 |      L.remove(value) -> None -- remove first occurrence of value.
	 |      Raises ValueError if the value is not present.
	 |
	 |  reverse(...)
	 |      L.reverse() -- reverse *IN PLACE*
	 |
	 |  sort(...)
	 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
	 |
	 |  ----------------------------------------------------------------------

 
RESOURCES** 
	*****************************************************************************************
	ROSETTA CODE (PYTHON)		https://rosettacode.org/wiki/Category:Python
	
	PYTHON 2 TO 3 REFERENCE 	http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html#divingin
	
	DUNDER METHODS 				http://www.diveintopython3.net/table-of-contents.html#special-method-names
								http://www.diveintopython3.net/special-method-names.html
								http://www.diveintopython3.net/special-method-names.html#esoterica
	
	GEEKS FOR GEEKS 			https://www.geeksforgeeks.org/global-local-variables-python/
	
	REAL PYTHON 				https://realpython.com/python-first-steps/			(recommended on Code Academy)
	
	TUTORIAL (W3SCHOOLS)		https://www.w3schools.com/python/default.asp
	
	PYTHON DOCS 				https://docs.python.org/3/contents.html
	PYTHON TUTORIAL 			https://docs.python.org/2/tutorial/
								https://docs.python.org/3.6/tutorial/index.html			PYTHON 3.6
	
	TUTORIALSPOINT				https://www.tutorialspoint.com/python3/index.htm
								https://www.tutorialspoint.com/python/python_functions.htm
								
	SOCKETS 					https://docs.python.org/3/howto/sockets.
								https://docs.python.org/3.4/library/socket.html?highlight=socket#module-socket
								
	*****************************************************************************************

	JUPYTER NOTEBOOK 							http://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html
												http://jupyter.readthedocs.io/en/latest/
												https://try.jupyter.org/
												
	ANACONDA DOCS 								https://conda.io/docs/user-guide/getting-started.html
	***********************************************************************************************
	PYTHON DOCS (*** GOOD REFERENCE ***)		https://docs.python.org/3/reference/datamodel.html
					BUILT-IN FUNCTIONS 			https://docs.python.org/3/library/functions.html
	***********************************************************************************************
	
	JUPYTER NOTEBOOK 			http://jupyter.org/

	YOUTUBE (Corey Schafer Programming)				https://www.youtube.com/user/schafer5
	YOUTUBE (Socratia Python and Math)				https://www.youtube.com/channel/UCW6TXMZ5Pq6yL6_k5NZ2e0Q
	
	YOUTUBE (PyData)			What Does It Take To Be An Expert At Python?
									https://www.youtube.com/watch?v=7lmCu8wz8ro
									
	YOUTUBE (DRAPSTV)(SOCKETS)	https://www.youtube.com/watch?v=XiVVYfgDolU

	BOOKS 						PYTHON 3 - THE HARD WAY (by Zed A. Shaw)
								BLACK HAT PYTHON (by Justin Seitz)
			
	HOME PAGE (CODE ACADEMY)	https://www.codecademy.com/programs/4c4c76bca436123016b333288546648e/items/37140c97d116cc8c0be8d4c442282803

	SLACK SETUP
		-https://pythagoras-drafting.slack.com/messages/CBQR7P5U3/
		
GETTING STARTED 
	SLACK 		-for messaging
				-DOWNLOAD 		https://slack.com/downloads/windows
				-INSTALL 		(SlackSetup.exe)
				-SHORTCUT 		(C:\Users\Pythagoras\AppData\Local\slack\slack.exe)
				
	SLACK (GUIDE)				https://get.slack.help/hc/en-us/categories/200111606
								https://sdhunt.github.io/codecademy-ref/mod/slack-quick-start.html
				
	GITHUB 		-for submitting projects, and getting feedback and reviews
				-MY GITHUB 		https://github.com/deanpjones?tab=repositories
	CHROME 
	
	PYTHON PACKAGES (libraries)			https://pypi.org/
		PYMARC (metadata world)					
			

	
JUL.19 POWERSHELL 
		https://powershell.org/tag/powergui/
		Windows PowerShell ISE 		(command prompt and extra GUI)
		Windows PowerShell 			(looks like command prompt, cmd.exe)
		-commands (have aliases from linux)
		-Windows, search (start bar), type POWERSHELL, click on POWERSHELL ISE 
		-create a shortcut on TASKBAR
		-add PATH to ENVIRONMENT VARIABLES (to run from POWERSHELL)
			-Windows, search ENVIRONMENT VARIABLE, (click SET UP ENVIRONMENT VARIABLES)
			-this opens CONTROL PANEL, SYSTEM PROPERTIES, click button at bottom ENVIRONMENT VARIABLES
				-EDIT (PATH)
				*** to find path SHFT+RIGHTCLICK the TASKBAR ICON, PROPERTIES (this should give you the TARGET PATH of the *.EXE file ***
				"C:\Program Files\Python36\python.exe"
				-NEW, BROWSE... (C:\Program Files\Python36)
				-click OK 
				-*** REBOOT program (for changes to take effect) ***
				
		
		 
		LINUX 		CMD.EXE 		POWERSHELL 			POWERSHELL ALIAS			DESCRIPTION 
		help 		help 			Get-Help <cmd>									-list help syntax 
		cd 			cd 				Set-Location 		sl, cd, chdir				-change directory 
		ls			dir 			Get-ChildItem 		gci, ls, dir				-list directory 
		clear 		cls				Clear-Host 			clear, cls 					-clear screen
		mkdir		mkdir			New-Item			mkdir, ni					-make directory
		cat 											cat 						-view file contents
		
		touch 						echo $null >> <filename>						-create BLANK file (eg. echo $null >> ex5.py)
		-			-				show-command									-command dialog list
		
		cd '.\Program Files\Python36'				-does AUTOCOMPLETE (sweet)
		
		GET ENVIRONMENT VARIABLES 
		Get-ChildItem ENV:PATH
		
		%PATH%		-shortcut to PATH (environment variable)
		%APPDATA%	-APP DATA folder path
		%TEMP% 		-TEMP folder path
		
	
	POWERSHELL (OPEN PROGRAMS)
		explorer		-opens FILE EXPLORER 
		python 			-opens PYTHON (in powershell app)(works from POWERSHELL commandline, *** NOT POWERSHELL ISE ***)
		quit() 			-back to POWERSHELL commandline
		start python	-opens PYTHON (in external application) (from POWERSHELL ISE)
						*** NOTE THIS RUNS FROM ANOTHER LOCATION (C:\Program Files\Anaconda3\python.exe)
		E:				-change to E-DRIVE
		C:				-change to C-DRIVE
		
	POWERSHELL (RUN A (*.PY) PYTHON FILE)
		-in POWERSHELL, go to FOLDER of (*.py)
		-type, (python ex1.py)						#WINDOWS (*** make sure to RUN from POWERSHELL PROMPT, not python prompt ***)
		-type, (python3.6 ex1.py)					#LINUX OR MacOS
		-this should run the file in the TERMINAL
	
	TIPS 
		-CHECK CODE (read it backwards, this with not attach meaning to the code)(helps you to spot mistakes)
	
JUL.16	
LINUX (BASH)(COMMAND PROMPT)
COMMANDLINE (BASH)(LINUX)(on Code Academy)
	*** all commands in LOWERCASE ***
	help				-lists help for all commands
	help pwd 			-prints help for this command
	cp --help 			-prints help for this command
	
	ls 					-lists files and subdirectories
	ls -a 				-all (-a modifier) lists files and folders and...
							. 				root folder 
							.. 				previous folder 
							.preferences 	hidden folders start with (.folder)
	ls -l 				-lists all content in (long format)
							-shows file permission levels 
							-count for hard links (counts directories and files)
							-username of file owner
							-group name
							-file size (bytes)
							-date and time 
							-file or directory name
								----------------------------------------------------------
								$ ls -l
									total 0
									drwxr-xr-x 4 ccuser ccuser 172 Jul  8  2015 action
									drwxr-xr-x 4 ccuser ccuser  77 Jul  8  2015 comedy
									drwxr-xr-x 4 ccuser ccuser  38 Jul  8  2015 drama
									-rw-r--r-- 1 ccuser ccuser   0 Jul  8  2015 genres.txt
								----------------------------------------------------------
	ls -t 				-order files (by time)
	ls <multiple options> 
						*** you can combine options together ***
	ls -alt					eg. ls -a, ls -l, ls -t  ->  combined equal (ls -alt)
	
	ls -1 				-list ONE FILE (per line)
	ls -d 				-list DIRECTORIES
	
	
	dir 				-lists files and subdirectories
	pwd 				-print working directory
	clear 				-clear screen
	
	.					-root directory 
	.. 					-previous directory
	~ 					-users HOME directory
	$					-always used in front of VARIABLE NAMES (echo $USER)
	:					-SEPARATOR ($PATH list of directories)
	cd 					-change directory 
	cd ..				-up a directory 
	cd ../..			-up two directory levels
	cd ../../..			-up three levels
	cd ../feb			-moves back a folder, then to (feb folder)	
	cd mem<press tab>	-this will AUTOCOMPLETE the folder name
	
	<up/down arrows>	-scroll thru last commands typed
	
	CREATE (ADD, NEW)
	mkdir									-make a directory
	mkdir media 							-makes a (media folder) in the current directory
	mkdir startups/disruptors				-makes a subfolder inside the (startups folder)
	touch 									-creates a blank file
	touch keyboard.txt						-creates a blank file (called keyboard.txt)
	touch bmx/tricks.txt					-creates a file in subfolder
	touch startups/disruptors/tech.txt 		-creates file in nested folder (*** note, must be correct path and exist ***)
	cp --help 
	cp [from SOURCE] [to DIRECTORY]			-COPY (FILES OR DIRECTORIES)
	cp frida.txt lincoln.txt 				-COPY (contents of ONE file to ANOTHER FILE)
	cp biopic/cleopatra.txt historical/		-copy file (from)(what file, cleopatra.txt), (to)(historical/ folder)
	cp biopic/ray.txt biopic/notorious.txt historical/		-*** copy MULTIPLE FILES (list files first, the destination folder as last argument) ***
	*										-WILDCARD
	cp * satire/							-copy ALL FILES 
	cp m*.txt scifi/						-copy ALL FILES (start with 'm')(and *.txt files)
	cp f*.txt ../paint/						-copy FILES (start with 'f'.txt)(to specified folder)
	
	UPDATE (EDIT)
	mv 										-move files 
	mv [FILE] [to DIRECTORY]				-MOVE (one file)
	mv superman.txt superhero/				-move (superman.txt) to (superhero/ folder)
	
	mv [FILES...] [to DIRECTORY]			-MOVE (multiple files)
	mv superman.txt batman.txt superhero/	-move (two files) to (superhero/ folder)
	
	mv [existing FILE] [new FILE]			-RENAME FILE (OLD to NEW name)
	mv batman.txt spiderman.txt				-RENAME FILE (renames batman.txt TO spiderman.txt)
	
	DELETE 
	rm 										-REMOVE FILE OR DIRECTORY
	rm [FILE or DIRECTORY]					-remove (ONE FILE
	rm waterboy.txt 						-remove THIS FILE from current directory
	rm -r slapstick/						-remove THIS DIRECTORY (*** and it's contents and subdirectories ***)
	rm --help
	rm media/*								-remove ALL FILES (in this folder)
	
	rmdir 									-remove directory 
	rmdir test 								-remove (test directory)

	echo 									-echo
	echo "Hello"							-echo (takes INPUT "Hello") and (OUTPUTS to terminal "Hello") 
	stdin									-standard INPUT 
	stdout									-standard OUTPUT
	stderr 									-standard ERROR OUTPUT
	
	echo "Hello" > hello.txt				-redirects the "Hello" CONTENTS into a NEW FILE (hello.txt)
	> 										-OVERWRITE (REDIRECTS) (output to a FILE)
	>>										-APPENDS (REDIRECTS) (output to a FILE)
	<										-REDIRECTS (redirects INPUT to a command) (right FILE to left COMMAND)
	|										-PIPE (BAR symbol) (REDIRECTS OUTPUT from ONE COMMAND to another)(takes the OUTPUT on left, and PIPES IT TO... the INPUT on right)
	head 									-PRINTS (first 10 lines only) of file
	wc 										-Print newline, word, and byte counts for each FILE
	sort 									-orders ALPHABETICALLY
	uniq 									-ONLY SHOWS UNIQUE (values of content)(doesn't show duplicates)
	grep 									-GREP (global regular expression print)
	grep [SEARCHES] [FILE CONTENT]			-FIND/SEARCHES (for CONTENTS within a FILE)
	grep -i 								-(-i ignores CASE)
	grep -R 								-searches (ALL FILES IN A DIRECTORY) and outputs filenames and lines containing matched results
	grep -Rl 								-searches the /home/ccuser/workspace/geography directory for the string "Arctic" and outputs filenames
	sed 									-FIND/REPLACE (STREAM EDITOR) (input modifies based on REGULAR EXPRESSION)
												-searches the file and does (FIND and REPLACE on word)
	
	cat 											-display FILE CONTENTS 
	cat hello.txt 									-dislays "Hello" FILE CONTENTS
	cat oceans.txt > continents.txt					-OVERWRITES CONTENTS (FROM ocean.txt file, TO continents.txt file)
	cat glaciers.txt >> rivers.txt					-APPENDS CONTENTS (FROM glacier.txt file, TO rivers.txt file)
	cat < lakes.txt 								-DISPLAY CONTENTS
	cat volcanoes.txt | wc							-OUTPUT the WORD COUNT 
	cat volcanoes.txt | wc | cat > islands.txt		-???
	less 											-DISPLAY FILE (similar to CAT, but displays a page at a time)
	less javanese.txt 
		q 		(to quit)
	
	sort lakes.txt									-SORTS the CONTENTS names in alphabetical order 
	cat lakes.txt | sort > sorted-lakes.txt			-takes the OUTPUT of (lakes.txt), SORTS IT, and PIPES it into the (sorted-lakes.txt) file
	uniq deserts.txt								-show UNIQUE deserts (no duplicates)
	sort deserts.txt | uniq > uniq-deserts.txt		-SORTS contents of file, SHOWING ONLY UNIQUE VALUES, OUTPUTS to a new file (uniq-deserts.txt)
	
	grep Mount mountains.txt							-SEARCHES (for Mount) in this file
	grep -i Mount mountains.txt							-SEARCHES (for Mount)(IGNORING CASE) in this file
	grep -R Arctic /home/ccuser/workspace/geography/	-SEARCHES for (Arctic) in this DIRECTORY?
	grep Japan roster.txt								-SEARCHES (for players from Japan only)
	sed 's/snow/rain/g' forests.txt						-SEARCHES (AND MODIFIES) (and does find replace)
		's'		-substitution 
		'snow'	-search for string 
		'rain' 	-replace string 
		'g' 	-REPLACES (ALL INSTANCES)(otherwise first only)
	ls -l | head > list1.txt						-SAVES THE (COMMAND OUTPUT) from files (SAVES TO A FILE)(for first 10 lines only)
	sort flowers.txt | uniq > uniq-flowers.txt		-SORTS (flower file) with UNIQUE values only, and SAVES TO FILE
	grep -Rl tree .									-SEARCH (current folder)(output only files with match)
	grep -R tree .									-SEARCH (current folder)(output files and matches)
	cat greatest.txt | sort 						-PRINT SORTED FILE
	echo "Aesop Rock" >> greatest.txt				-APPENDS TEXT TO FILE 
	
	nano 											-TEXT EDITOR 
	nano [FILE]
	nano hello.txt 									-opens HELLO.TXT file for EDITING
	nano COMMANDS 
		CTRL+O+ENTER 			WRITE OUT (SAVE)
		CTRL+X					EXIT (goes back to terminal)
	nano ~/.bash_profile		-create script file (welcome screen)
		(in editior)
		echo "Welcome Dean Jones"
		alias pd="pwd"					-creates an alias
		alias hy="history"
		alias ll="ls -la"
		export USER="Dean Jones"		-saves a value to a VARIABLE $USER
		export PS1=">> " 				-changes the COMMAND PROMPT (to the left)
		export LESS="-N" 				-(-N) switch adds LINE NUMBERS (used with LESS command)
		(save and exit)
	~/.bash_profile				(bash_profile, is the file used to store environment settings)
								~ 	home directory 
								.	hidden file
	source ~/.bash_profile		-EXECUTES SESSION FILE (*** refreshes any changes, before you can use any ALIASES ***)
	
	alias 						-SHORTCUT 
	alias [ALIAS]=["COMMAND"]	
	alias pd="pwd"				-creates an alias (type 'pd', to execute 'pwd' command)
	alias hy="history"			-type 'hy' to see 'history' (of commands)
	alias ll="ls -la"			-type 'll' to list contents
	
	export USER="Dean Jones"	-save a ENVIRONMENT VARIABLE 
	echo $USER 					-DISPLAY VARIABLE value
	
	export 
	export [VARIABLE]=["VALUE"]
	export PS1=">> " 			-COMMAND PROMPT (PS1 variable for COMMAND PROMPT style) (to the left)
	export PS1="---\nCommand: "	-CUSTOM (COMMAND PROMPT) (with line break)
	
	echo $HOME 					-HOME DIRECTORY (for user)(/home/ccuser)
	echo $PATH 					-SCRIPT PATHS (directories list)
	/bin/pwd 					-EXECUTE SCRIPT (in the /bin FOLDER)
	/bin 						-FOLDER (holds ALL SCRIPTS)
	ls /bin						-LIST ALL SCRIPTS
	env 						-ENVIRONMENT variables (lists them)
	
JUL.16
BICYCLE WORLD PROJECT (COMMANDLINE BASH LINUX)
	-done navigating folders using commandline, making files and directories, and listing working directory and path using (ls, pwd, mkdir, cd, touch) commands
DAILY BUZZ
	-done 
QUIZ#1 - NAVIGATING THE FILE SYSTEM 
	-100% (8/8)

JUL.16 
MANIPULATION (COPY, MOVE, DELETE FILES USING COMMANDLINE)
	-done using commands (mv, rm, rm -r, cp) for moving, renaming, coping, and deleting (files and folders)
ARTUSI PROJECT 
	-practise using all previous commands (done)
QUIZ#2 VIEWING AND CHANGING THE FILE SYSTEM
	-85% (6/7)
	
JUL.16 
REDIRECTION (INPUT AND OUTPUT)
	-done, >, >>, <, |, grep, sed, cat, sort, uniq, wc, echo
	-??not sure about these (stdin, stdout)
ATHLETICA
	-practise using previous commands 
ECOSYSTEM (REDIRECT FILES)
	-more practise 
QUIZ#3 
	-60% (6/10)
	-100% (10/10)(redone quiz)
	
JUL.16 
ENVIRONMENT (CONFIGURE THE ENVIRONMENT)
	-learn nano editor, how create alias, change the command promt, reload settings, view environment variables 
	-commands (nano, export, alias, echo, env, source)
ATTICA 
	-practise above settings 
LINGUA FRANCA
	-more practise
QUIZ#4 
	-55% (5/9)
	-100% (9/9)
	
--------------------------------------------------------------
JUL.17 (WEEK 1, DAY 1,2,3)
SLACK 
	-accepted invitation through email 
	-CHANNELS 				-messaging 
	-DIRECT MESSAGES 		-one-on-one messages
	
	SHARMEEN 			(MODERATOR)
	#pwp-jul-17-2018	(MAIN CHANNEL)
		1. #pwp-jul-17-2018 is our very own channel for discussion in this cohort. I'll be posting daily here, and I encourage everyone to share resources they find here as well.
		3. There is also a #general channel where I recommend you introduce yourself to the rest of the Programming with Python community!
	SHARMEEN (TIMES EST)
		Monday, Wednesday, Friday - around 10pm - Midnight 
		Tuesday, Thursday, Saturday - around Noon - 2pm
	
	TO POST (BLOCK OF CODE)
		-add (```) back-quotes (three around code)
		-this will show as A BLOCK OF CODE (in SLACK)
		-ONE-LINER or `writing code in-line` you only need single back tics.
	
JUL.17 
PYTHON 
	TIP (TO REDUCE CODE ON RETURN STATEMENT)
	-if the FUNCTION (returns TRUE OR FALSE)
	-------------------
	def less_than_2(n):
	   if n < 2:
		  return True
	   else
		  return False
	-------------------
	def less_than_2(n):
		return n < 2
	-------------------
		
PYTHON HISTORY 
	-1999 didn't have much popularity
	-Python can be connected to the rise of interest in data science.
	-There are over 125,000 third-party Python libraries (why it's more popular than R and SQL)
	-Python has become a go-to language for data analysis. 
	-With data-focused libraries like pandas, NumPy, and matplotlib
	-anyone familiar with Python’s syntax and rules can deploy it as a powerful tool to process, manipulate, and visualize data.
	-great for data analysis and machine learning.
	
JUL.17 
SYNTAX 
	-uses a TEXT FILE that is READ to form a PROGRAM 
	
	FILE TYPE (*.py)
		script.py 			(used for Code Academy coding...)
	
	GLOSSARY 
		{}				CURLY BRACES (PLACEHOLDER)
		{{}}			ESCAPE PLACEHOLDER
		# 				COMMENTS (pound symbol, octothorpe, hash tag)
		#				MULTI-LINE COMMENTS (put # in front of each line)
		=				ASSIGNMENT OPERATOR 
		"<string>"		STRING 
		'<string>'		STRING
		(""" or ''')	MULTI-LINE STRING ("""A multi-line string""")
		+ 				CONCATENATION (string)
		
		+				ADDITION (number)
		-				SUBTRACTION
		*				MULTIPLICATION (asterisk)
		*				??ASTERISK (unpacking arguments) 		https://stackoverflow.com/questions/21617593/python-zip-single-list-element
							eg. 
								>>> args = [3, 6]
								>>> range(*args)            # It's equivalent to range(3, 6)
								[3, 4, 5]
							
		/				DIVISION (forward slash)
		**				EXPONENTS (double-asterisk)
		% 				MODULAR (MOD, MODULO)(REMAINDER)(percent)
		//				DIVISION (whole number, not the remainder (decimal))
		
		<				LESS-THAN 
		>				GREATER-THAN
		<=				LESS-THAN-EQUALS 
		>=				GREATER-THAN-EQUALS 
		
		==				EQUAL-TO
		!=				NOT-EQUAL-TO
		
		NOT				NOT (returns opposite of True/False)(*** similar to (!) in other languages ***)
		AND				AND (both are true, returns true)(*** dont' use (&) ***)
		OR 				OR (if ONE or OTHER or BOTH are True, returns True)
		XOR 			XOR (only if ONE or OTHER is True, returns True)
		
		
		+=				PLUS EQUALS (adds the number, and reassigns the value)
		\\				ESCAPE CHARACTER 
		\n 				NEW LINE 
		\t 				TAB
		\b 				BACKSPACE 
			print('Text: ABC\b\b\bXYZ')	#Text: XYZ
			---
			#THIS DOESN'T WORK?			https://stackoverflow.com/questions/34233285/using-b-in-python-3
			str = 'abcdefghi\b\b\b\b\b\b'
			print(str)			#abcdefghi (THIS DOESN'T WORK RIGHT?)
		\'				SINGLE QUOTE (escaped)
		\"				SINGLE DOUBLE-QUOTE (escaped)
		:				COLON(:) END OF CONDITION, BEFORE FUNCTION BLOCK 
							eg. if <condition>:
									<do this>
							eg. def my_func(arg1):
									<do stuff>
									return <whatever>
									
		REPL model 		(Read-Eval-Print-Loop)
		
	DATA TYPES (CASTING)(CONVERTING)
		int --> str 		str(int)
			my_int = 33 
			str(my_int) 		#'33'
		*** NOTE, (FORMAT) doesn't need casting ***
			>>> int = 33
			>>> str(int)
			'33'
			>>> '{}, {}'.format('test', 33)
			'test, 33'
			
	TEST (IF INT)(IF INTEGER)
		t = 33
		type(t)
			<class 'int'>
		isinstance(t, int)		#True
		
	VALDIATION** 
		#VALIDATION: TEST (FOR NUMBER)(float or int)
		def is_number(s):
			try:
				return float(s)
			except ValueError:
				return False
		#TEST
		is_number('2')      #2.0 (True)
		is_number('2.5')    #2.5 (True)
		is_number('2.5a')   #False

		#VALIDATION: TEST (FOR INTEGER ONLY)(int)
		def is_int(s):
			try:
				return int(s)       #return (value)(can be used in true/false still)
			except ValueError:
				return False
		#TEST
		is_int('2')         #2 (True)
		is_int('2.5')       #False
		is_int('2.5a')      #False

		#VALIDATION: TEST (FOR FLOAT ONLY)(float)
		def is_float(s):
			try:
				if is_int(s):              #will Error or return False
					return False 
				else:
					return float(s)        #if both run it will get to (True)
			except ValueError:
				return False
		#TEST 
		is_float('2')           #False
		is_float('2.5')         #2.5 (True)
		is_float('2.5a')        #False
			
		
	DATA TYPES** (not explicitly called, in other words Python figures this out on its own)
								EXAMPLE
		-------------------------------------------------------------------
		STRING 					"string" or 'string' or '''multi-line'''
			str		
		NUMBER
			int 				33 or 5 (whole number)
			float 				3.14 or 1.414213 (decimals)
		BOOLE (BOOLEAN)
			True				True or False
			False
		NONE (like Null) 
			None 				rating = None 
								type(rating)				#<class 'NoneType'>
								if not rating: 				#this can act as A TEST (without having to use an OPERATOR)(shorter)
									print('do this...')
								versus...
								-------
								rating = 'None' 
								if rating != 'None':
									#...
									
		CLASS (@property getters/setters)
			???
			https://docs.python.org/3/library/functions.html#property
			class Email():
				def __init__(self, address):
					self.address = address
					#self.username = self.address.split('@')[0]              #not using (as change_email) does not update these fields (automatically)?
					#self.domain = self.address.split('@')[1]                #probably need to use (@property getters/setters)
			
		CLASS (DUMP AS DICTIONARY)
			obj.__dict__
				{'b': 1, 'a': 2}
			b1.__dict__
				{'title': 'Harry Potter', 'isbn': ISBN: 978-0-54-501022-1, 'ratings': []}
		CLASS 		
			https://www.w3schools.com/python/python_classes.asp
			-don't need to INSTANTIATE?
			class Test:
				x = 5
				y = 7
			Test.x 	#returns 5	
			Test.y	#returns 7
			type(Test)
					#<class 'type'>
			-----------
			class Person:
			def __init__(self, name, age):
				self.name = name
				self.age = age

			p1 = Person('Dean', 42)
			p2 = Person('Nadine', 41)
			p3 = Person('Vivian', 12)
			p1
				#<__main__.Person object at 0x00000250058B4DD8>
			p1.name		#'Dean'
			p1.age		#42
			type(p1)
						#<class '__main__.Person'>
			-----------
		GLOBAL VARIABLE (GLOBAL)
			-need to CALL GLOBAL (when using a VARIABLE inside a FUNCTION)
			tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
			play = tarot.copy()         #copy deck
			
			#FUNCTION: RESET DECK
			def reset():
				global play                 #need to reference global variable
				play = tarot.copy()         #copy deck
			
		ENUM 
			https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
			https://docs.python.org/3.4/library/enum.html
			from enum import Enum
			class Fruit(Enum):
				apple = 1
				banana = 2
				cupcake = 3
			#access enum
				Fruit.apple				#<Fruit.apple: 1>
			#get name
				Fruit.apple.name		#'apple'
			#get value
				Fruit.apple.value		#returns 1
				
		ENUM 
			# enum (use a DICTIONARY as an ENUM)(because the KEY has to be UNIQUE)
			# ENUM (object works better)
			days_of_week = {'Sunday':0, 'Monday':1, 'Tuesday': 2, 'Wednesday':3, 'Thursday':4, 'Friday': 5, 'Saturday':6}
			days_of_week['Sunday']      #0
			class Days(Enum):
				Sunday = 0
				Monday = 1
				Tuesday =  2
				Wednesday = 3
				Thursday = 4
				Friday =  5
				Saturday = 6

			Days.Sunday         #<Days.Sunday: 0>
			type(Days)          #<class 'enum.EnumMeta'>
			type(Days.Sunday)   #<enum 'Days'>
			dir(Days)
			#['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday', '__class__', '__doc__', '__members__', '__module__']
			dir(Days.Sunday)
			#['__class__', '__doc__', '__module__', 'name', 'value']
			Days.Sunday.name    #'Sunday'
			Days.Sunday.value   #0
			
		CLASS 
			https://www.python.org/dev/peps/pep-0008/#class-names
			-Class names should normally use the CapWords convention.
			
		OBJECT??
		
		OPERATORS (MAPPING OPERATORS TO FUNCTIONS)
			MAPPING OPERATORS TO FUNCTIONS 				https://docs.python.org/3/library/operator.html#mapping-operators-to-functions			
			Operation		Syntax		Function
			Addition		a + b		add(a, b)
			Ordering		a < b		lt(a, b)
			
			import operator
			import operator as o
			o.lt(1,2)					#True
			#same as...
			1 < 2						#True
		
		LIST					https://docs.python.org/3/tutorial/datastructures.html
								https://www.w3schools.com/python/python_lists.asp
								https://www.programiz.com/python-programming/methods/list/	
								
		LIST**					(indexed, ordered, changeable, duplicates)
			my_list = []								#EMPTY LIST (don't know what to put in it yet)
			mixed_data = [33, "string", True]			#(can have MIXED DATA TYPES)
			my_list = list((1,2,3))						#CONSTRUCTOR 						#[1, 2, 3]
			my_list = ["apple", "banana", "cherry"]		#CREATE								#["apple", "banana", "cherry"]
			my_list.append("donut")						#ADD (to end)						#['apple', 'blackberry', 'cherry', 'donut']
			my_list.insert(1, 'banana')					#ADD (by index)						#['apple', 'banana', 'blackberry', 'cherry']
			type(my_list)																	#<class 'list'>
			my_list[1]									#READ								#"banana"
			my_list.index('cherry')						#READ (search value, or errors)		#2
			my_list[1] = "blackberry"					#UPDATE
			my_list[1]																		#"blackberry"
			my_list.remove('donut')						#DELETE (first entry found) 		#['apple', 'blackberry', 'cherry']
			my_list.pop(2)								#DELETE (by index)					#['apple', 'banana', 'cherry']
			my_list.clear()								#DELETE (all items removed)			#[]
			
			l = [16, 8, 4, 2, 1]	
			l.reverse() 								#REVERSE LIST (*** Note, doesn't RETURN a value ***)(RUN function, then call list again)
			l 		#[1, 2, 4, 8, 16]
			l = [16, 8, 4, 2, 1]
			l.sort()									#SORT (*** Note, doesn't RETURN a value ***)(RUN function, then call list again)
			l 		#[1, 2, 4, 8, 16]
			
		LIST (SUBTRACT TWO LISTS)(LIKE OPPOSITE UNION)
			https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
			temp1 = ['One', 'Two', 'Three', 'Four']
			temp2 = ['One', 'Two']
			list(set(temp1) - set(temp2))		#['Three', 'Four']
			
		LIST (2ND MAX)(GET SECOND HIGHEST NUMBER)
			-use SET to remove DUPLICATES 
			-use LIST MANIPULATION to work backwards to SECOND PLACE
			def second_highest(l):
				return list(set(l))[-2]
			l = [2,3,4,4,5]
			second_highest(l)			#returns 4
			
		LIST (GET UNIQUE VALUES)
			-convert LIST to SET (then back to list)
			https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
			t = [1,1,2,3,3,4]
			set(t)				#{1, 2, 3, 4}
			list(set(t))		#[1, 2, 3, 4]
			
		LIST (LENGTH)	
			len(my_list)								#get length 						#3
		LIST (COUNT)		(counts the # of times N-ELEMENT appears) 
			list = ['a', 'a', 'b', 'b', 'b', 'c']
			list.count('a')								#2
			list.count('b')								#3
			list.count('c')								#1
		
		LIST (COUNT)(2D ARRAY)
			pizzas = [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]
			num_two_dollar_slices = sum(x.count(2) for x in pizzas)
				#num_two_dollar_slices:  3
			
		LIST (SORT)(ALPHABETICAL or NUMERICAL)
			#NOTE, sort PERMANENTLY CHANGES THE (ORDER OF THE LIST) 
			#  	and using (=) to save to ANOTHER VARIABLE (this REFERENCE points to the SAME VALUE)
			#   USE <list>.copy() TO CREATE A COPY
			my_list = ["apple", "banana", "cherry", "artichoke"]
			my_list.sort()								#ALPHABETICAL
			my_list										#['apple', 'artichoke', 'banana', 'cherry']
		LIST (SORT)(list = 'None')(*** SORT doesn't RETURN a value, WARNING, if LIST is 'None')
			>>> x = [3,4,2,2,4,5,5,9]
			>>> y = x
			>>> print(x)				#[3, 4, 2, 2, 4, 5, 5, 9]			
			>>> print(y)				#[3, 4, 2, 2, 4, 5, 5, 9]			
			>>> y = x.sort()			#'None'			***WARNING***
			>>> print(x)				#[2, 2, 3, 4, 4, 5, 5, 9]	
			>>> print(y)				#None
			
		LIST (REVERSE)
			-NOTE, this caused me some confusion (DOESN'T CREATE A NEW LIST) just REVERSES (A LIST)
			lst1 = [1, 2, 3]
			lst1.reverse()								#reverse ORDER of list (DOESN'T RETURN ANYTHING)
			lst1 
				#[3, 2, 1]
			
		LIST (REVERSE)(IF YOU NEED A COPY)
			lst = [1, 2, 3]
			#REVERSE LIST 
			lst[::-1]
				#[3, 2, 1]
			--------------
			#FUNCTION: REVERSED LIST 
			def reversed_list(lst1, lst2):
			  return lst1 == lst2[::-1]					#COUNT_BY (ONE) BACKWARDS (NEGATIVE)
			  
			print(reversed_list([1, 2, 3], [3, 2, 1]))	#True
			--------------
				
		LIST (COPY)(my_list.copy())
			https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
			#note, trying to create a (NEW LIST) by using the (=) ASSIGNMENT OPERATOR (doesn't work, it only creates a NEW POINTER)
			#	*** YOU MUST USE (COPY) ***
			list.copy()
				eg.
					>>> x = [3,4,2,2,4,5,5,9]
					>>> y = x.copy()
					>>> y
						[3, 4, 2, 2, 4, 5, 5, 9]
					>>> x
						[3, 4, 2, 2, 4, 5, 5, 9]
					>>> x.sort()
					>>> x
						[2, 2, 3, 4, 4, 5, 5, 9]
					>>> y
						[3, 4, 2, 2, 4, 5, 5, 9]
		LIST (COPY)(SLICE A SUBSET)(CREATES A COPY)
				ref_old_list = old_list 			#this CREATES A REFERENCE ONLY *** DON'T USE THIS TO COPY ***
				new_list = old_list[:]				#this will CREATE A COPY
			eg. 
				>>> x
					[3, 4, 2, 2, 4, 5, 5, 9]
				>>> y = x[:]
				>>> x
					[3, 4, 2, 2, 4, 5, 5, 9]
				>>> y
					[3, 4, 2, 2, 4, 5, 5, 9]
				>>> x.sort()
				>>> x
					[2, 2, 3, 4, 4, 5, 5, 9]
				>>> y
					[3, 4, 2, 2, 4, 5, 5, 9]
		LIST (COPY)(different ways)
			new_list = old_list.copy()		#LIST (copy method)
			new_list = old_list[:]			#SLICE (subset)
			new_list = list(old_list)		#LIST CONSTRUCTOR 
			sorted_list = sorted(old_list)	#CREATES A COPY (of a SORTED LIST)
			
			import copy 
			new_list = copy.copy(old_list)	#COPY METHOD (for older versions)
			
			import copy
			new_list = copy.deepcopy(old_list)	#IF THE LIST (CONTAINS OBJECTS) YOU WANT COPIED
			

		LIST (SQUARES)
			squares = [x**2 for x in range(10)]			#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
		LIST (permutations)
			[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
					#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
			#PERMUTATION (example)(x,y)
			[(x, y) for x in [0,1,2] for y in [0,1,2]]
					#(x,y)
					#[
					(0, 0), 
					(0, 1), 
					(0, 2), 
					(1, 0), 
					(1, 1), 
					(1, 2), 
					(2, 0), 
					(2, 1), 
					(2, 2)
					]
			#NO REPEATS
			[(x, y, z) for x in [0,1,2] for y in [0,1,2] for z in [0,1,2] if x != y and x != z and y != z]
					#[
					(0, 1, 2), (0, 2, 1), 
					(1, 0, 2), (1, 2, 0), 
					(2, 0, 1), (2, 1, 0)
					]
			#PERMUTATION (example)(x,y,z)
			[(x, y, z) for x in [0,1,2] for y in [0,1,2] for z in [0,1,2]]
					#(x,y,z)
					#[
					(0, 0, 0), 
					(0, 0, 1), 
					(0, 0, 2), 
					(0, 1, 0), 
					(0, 1, 1), 
					(0, 1, 2), 
					(0, 2, 0), 
					(0, 2, 1), 
					(0, 2, 2), 
					(1, 0, 0), 
					(1, 0, 1), 
					(1, 0, 2), 
					(1, 1, 0), 
					(1, 1, 1), 
					(1, 1, 2), 
					(1, 2, 0), 
					(1, 2, 1), 
					(1, 2, 2), 
					(2, 0, 0), 
					(2, 0, 1), 
					(2, 0, 2), 
					(2, 1, 0), 
					(2, 1, 1), 
					(2, 1, 2), 
					(2, 2, 0), 
					(2, 2, 1), 
					(2, 2, 2)
					]
			#REPEATS ONLY (x == y)
			list = [(x, y) for x in [0,1,2] for y in [0,1,2] if x == y]
				#[(0, 0), (1, 1), (2, 2)]
			#NO REPEATS (x != y)
			list = [(x, y) for x in [0,1,2] for y in [0,1,2] if x != y]
				#[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
			#ORDER (MATTERS)
			#ORDER (DOESN'T MATTER)(don't need to add any FILTER)
		LIST (MULTIPLY)(* 3)
			 x = [1, 2, 3, 4] * 3			#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
		LIST (CONCATENATION)(+)(COMBINE TWO LISTS)
			items_sold = ['cake', 'cookie', 'bread']
			items_sold_new = items_sold + ['biscuit', 'tarts']		
				#['cake', 'cookie', 'bread', 'biscuit', 'tarts']	
				
		LIST (RANGE)(CREATE A LIST OF CONSECUTIVE NUMBERS)
			SYNTAX 
				range(max)
				range(start, max)
				range(start, max, count_by)
			-this will create a similar (ZIP object)(*** use LIST to display ***)
			-starts (by default) at ZERO
			-count_by (by default) counts by ONE
			-max (one less) than argument
			eg.
				x = range(10)
				print(x)		#range(0, 10)
				print(list(x))	#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]		
			-to set the START VALUE (use TWO ARGUMENTS)
			eg2. 
				SYNTAX 			range(start, max)
				x = range(2, 9)
				list(x)
					#[2, 3, 4, 5, 6, 7, 8]
			eg3. 
				SYTAX 			range(start, max, count_by)
				x = range(2, 9, 2)
				list(x)
					#[2, 4, 6, 8]
		LIST (RANGE)
			-negative range 
				eg. 
					range(-10, 10, 1)			#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]					
			-whole numbers only (COUNT_BY)
				error:
					range(0, 10, 0.1)			#ERRORS 
						TypeError: 'float' object cannot be interpreted as an integer	
				ALTERNATIVES...
					*** NOT GOOD ***
					>>> [x * 0.1 for x in range(0, 10)]
					[0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]
					*** GOOD ***
					>>> [x / 10 for x in range(0, 10)]
					[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
			-reverse list with NEGATIVE 
				eg.
					range(2, -2, -1)			#[2, 1, 0, -1]
					
		LIST (RANGE)(MULTIPLICATION TABLE)
			twos = range(0, 2 * 10, 2)
			list(twos)
			[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
			threes = range(0, 3 * 10, 3)
			list(threes)
			[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
			#FUNCTION: MULTIPLICATION TABLE (for each row)
			def list_multiples(multiplier):
				return list(range(0, multiplier * 10, multiplier)))

			list_multiples(3)		#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
			list_multiples(4)		#[0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
			list_multiples(5)		#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
			
		LIST (select FIRST IN LIST)
			employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
			print("First element:", employees[0])					#First element: Michael
		LIST (LAST IN LIST)
			#NOTE, the (-)(negative) sign indexes in reverse
			print("Last element:", employees[-1])					#Last element: Robert
		LIST (SECOND LAST ELEMENT)
			print("2nd last element:", employees[-2])				#2nd last element: Andy		
		
		LIST (SLICE)(SUBSET)
			#SLICING (breaking up list into PARTS)
			#COLON (:) (TO CREATE A RANGE)(SUBSET OF LIST)
			#SYNTAX (my_list[<start_index>:<one_less_end_index>])
			suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
			------
			beginning = suitcase[0:4]			
			print(beginning)							#['shirt', 'shirt', 'pants', 'pants']

			#new list 
			middle = suitcase[2:-2]
			print("middle two elements: ", middle)		#middle two elements:  ['pants', 'pants']

			test = suitcase[1:-1]
			print(test)									#['shirt', 'pants', 'pants', 'pajamas']
		
		LIST (LIST PART, TO THE END)
			lst = [4, 8, 10, 11, 12, 15]			
			lst = lst[1:]
			lst				#[8, 10, 11, 12, 15]
			lst = lst[1:]
			lst				#[10, 11, 12, 15]
			lst = lst[1:]
			lst				#[11, 12, 15]
			
		
		LIST (SLICE)(OMITTING start or end)
			test = ["one", "two", "three", "four", "five", "six"]
			#when starting at (0 index)(you can OMIT the index)
			print(suitcase[:3])		#first 3 elements							#['one', 'two', 'three']
			print(suitcase[2:])		#start at (2nd element)(to end of list)		#['three', 'four', 'five', 'six']
			print(suitcase[-3:])	#last 3 elements							#['four', 'five', 'six']
		
		LIST (SLICE REMOVE SUBSET)
			def remove_middle(lst, start, end):
				return lst[:start] + lst[end + 1:]
			print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))	#[4, 23, 42]
			
		LIST (GET MIDDLE INT)
			-------------
			#FUNCTION: MIDDLE TERM
			def middle_element(lst):
			  len_lst = len(lst)
			  if len_lst % 2 == 1: 	#odd (get middle element)
				#get middle item
				mid_item = len_lst // 2
				return lst[mid_item]
			  else:									
				#even elements (get average)
				mid2 = len_lst // 2
				mid1 = mid2 - 1
				avg = (lst[mid1] + lst[mid2]) / 2
				return avg

			#TEST
			print(middle_element([5, 2, -4, 4, 5]))				#-4
			print(middle_element([5, 2, -10, -4, 4, 5]))		#-7.0
			-------------
			
		LIST (SLICING)(DOUBLE COLON)
			lst[::]
			lst[<start>:<end>:<count_by>]
			---
			lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			(START AT...)
			(lst[<start>:]
			lst[0:]		#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			lst[:]		#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]		#defaults to (0 ZERO) too
			lst[1:]		#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			lst[2:]		#[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			---
			(END AT...)
			(lst[:<end>])
			lst[:2]		#[1, 2]
			lst[:3]		#[1, 2, 3]
			lst[:4]		#[1, 2, 3, 4]
			---
			(COUNT BY...)
			(lst[::<count_by>])
			lst[::1]		#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			lst[::2]		#[1, 3, 5, 7, 9, 11]
			lst[::3]		#[1, 4, 7, 10]
			---
			(COMBINE ALL THREE...)
			(lst[<start>:<end>:<count_by>])
			lst[2:8:2]
				#[3, 5, 7]
			---
			(COUNT BACKWARDS)(REVERSE LIST)
			lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
			lst[::-1]
				#[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
			
		LIST COMPREHENSION (TWO LISTS)
			-runs the lists (IN PARALLEL)
			-eg. 
				t = [1, 4]
				result = "dogdogdog"
				v = [(x, y) for (x, y) in zip(result, t)]
				RETURN (*** ONLY RETURNS TWO ENTRIES, THE MAXIMUM OF (t) LIST ***)
					[('d', 1), ('o', 4)]
			
		LIST COMPREHENSION** (SHORTHAND for doing some cool stuff!!)
			http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
			-much the same as (lambda, map, filter) functions
			SYNTAX 
				<output> <for X in MY_LIST> <condition_to_test>
			EXAMPLES 
				lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
				#output (even numbers only)
				tmp = [x for x in lst if x % 2 == 0]
				print("tmp: ", tmp)		
					#tmp:  [2, 4, 6, 8, 10]
				#output (x2)(for even numbers only)
				tmp2 = [x * 2 for x in lst if x % 2 == 0]
				print("tmp2: ", tmp2)	
					#tmp2:  [4, 8, 12, 16, 20]
				---------------
				test = [x * 5 for x in range(0, 10) if x % 2 == 0]
					#[0, 10, 20, 30, 40]
					
		LIST COMPREHENSION (ZIP TWO LISTS) 
			-use TWO LAMBDA variables (x, y), same as MAPCAR to ZIP through the two LISTS at same time)
				eg.
					hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
					new_prices = [25, 20, 35, 15, 15, 30, 45, 30]
					cuts_under_30 = [[x, y] for x, y in zip(hairstyles, new_prices) if y < 30]
								#[['bouffant', 25], ['pixie', 20], ['crew', 15], ['bowl', 15]]
								
		LIST COMPREHENSION (NESTED LIST)
			https://stackoverflow.com/questions/18072759/list-comprehension-on-a-nested-list
			daily_transactions_split2 = [['Gail Phelps', '$30.52', 'green&white&blue', '09/15/17'], ['Myrtle Morris', '$22.66', 'green&white&blue', '09/15/17']]
			transactions_clean2 = [[x.strip() for x in y] for y in daily_transactions_split2]
			
		LIST (SORT BY INDEX)(NESTED LIST)
			https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list/4174955
			l = [[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
			l.sort(key=lambda x: x[2])
				#[[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']]
		
		LIST COMPREHENSION (FLATTEN NESTED LIST)		https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
			-(nested_lst) is the list to input (this will get flattened)
			flat_list = [item for sublist in nested_lst for item in sublist]
								
		LIST COMPREHENSION (SEARCH for LETTER IN STRING)
			temp = [x == 'a' for x in 'abcdef']
				#[True, False, False, False, False, False]
			---------
			-other ways...
				'A' in 'abc'						#False
				'a' in 'abc'						#True
				#ignore case
				'A'.upper() in 'abc'.upper()		#True
				#works woth FULL WORDS 
				'blue' in 'blueberry' 				#True
					
		FILTER (applies a TEST CONDITION (predicate) TO A LIST)
			lst = list(range(0, 20))
			lst
				[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
			x = filter(lambda e: e % 2 == 0, lst)
			x
				<filter object at 0x0000029E8B7BEF98>
			list(x)
				[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
			
		MAP (modifies a list)
			z = map(lambda x: x * 5, lst)
			z
				<map object at 0x0000029E8B7D1780>
			list(z)
				[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
			
		MAP and FILTER combined (same as LIST COMPREHENSION)
			map_filter = map(lambda n: n * 5, filter(lambda m: m % 2 == 0, lst))
			map_filter
				<map object at 0x0000029E8B7D16D8>
			list(map_filter)
				[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
			#--------
			#the same with (LIST COMPREHENSION)
			test = [x * 5 for x in lst if x % 2 == 0]
				#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
				
		LAMBDA (ANONYMOUS FUNCTION) 
			x = lambda a : a + 10
			x(5)
				#returns 15
				
		AGGREGATE (SUM)
			>>> sum([x for x in lst])
			10
			>>> sum([1, 2, 3, 4])
			10
		
		REPEAT (A FUNCTION)(N TIMES)(FUNCTION ARGUMENT**)
			def repeat(func, n):
				for x in range(n):
					func()			#need the BRACKETS here
		
			def test():
				print("TEST")
		
			repeat(test, 3)
				TEST
				TEST
				TEST
		
		TUPLE					(like ENUM)(indexed, ordered, NOT changeable, duplicates) 
			tuple				...
			my_tuple = (1, 2, 3)
			#REVERSE TUPLE 
				my_tuple[::-1]		#(3, 2, 1)
		SET 					(NOT indexed, NOT ordered, NO duplicates)
		DICTIONARY				(indexed, NOT ordered, changeable, NO duplicates)
		
	DICTIONARY (GET EVEN ELEMENTS ONLY)
		#FUNCTION: EVEN KEYS 
		def sum_even_keys(my_dictionary):
		  return sum([v for k,v in my_dictionary.items()][1::2])			#*** THIS IS CLEVER USING [::2] to get EVEN ELEMENTS ONLY ***
		
	LOOPS (FOR LOOP)
		for ELEMENT in LIST:
			#do stuff here 
		eg. 
			my_list = [1, 2, 3, 4, 5]
			for x in my_list:
				print("index: ", x)
			#index:  1
			#index:  2
			#index:  3
			#index:  4
			#index:  5
	
	LOOPS (WITH INDEX)(TWO LISTS IN PARALLEL)
		--------------
		#RETURN INDEX
		def same_values(lst1, lst2):
			return [i for i in range(0, len(lst1)) if lst1[i] == lst2[i]]
			
		lst1 = [1, 2, 3, 4, 5, 6]
		lst2 = [4, 4, 4, 4, 5, 6]
		same_values(lst1, lst2)
			#[3, 4, 5]
		--------------
		#RETURN VALUE
		def same_values(lst1, lst2):
			return [[i, lst[i]] for i in range(0, len(lst1)) if lst1[i] == lst2[i]]
			
		lst1 = [1, 2, 3, 4, 5, 6]
		lst2 = [4, 4, 4, 4, 5, 6]
		same_values(lst1, lst2)
			#[20]
		--------------
			
	LOOP (RANGE)
		#LOOP (RANGE)
		promise = "YOU ARE LOVED"

		for i in range(13):
		  print(promise)
		  
	LOOP (ADD ONE LIST TO ANOTHER)
		#print(students_period_B + students_period_A)		#same as concat two lists
		for student in students_period_A:
		  students_period_B.append(student)
		  print(student)
		  
	LOOP (BREAK) (use this to LEAVE the loop)
		dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
		dog_breed_I_want = 'dalmation'

		#LOOP 
		for dog in dog_breeds_available_for_adoption:
		  print(dog)
		  if dog == dog_breed_I_want:
			print('They have the dog I want!')
			break			#STOPS (after finding this element)
		#french_bulldog
		#dalmation
		#They have the dog I want!
		 
	LOOP (CONTINUE) (continue after skipping something)
		ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

		#check age (under 21 to drink)
		for age in ages:
		  if age < 21:
			continue		#SKIPS (this condition)
		  print(age)
		 
	LOOP (WHILE)(use when you DON'T KNOW how many loops are required)
		all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
		students_in_poetry = []

		#WHILE
		num = 0							#need (counter)		
		while num != 6:					#test (counter)
		  students_in_poetry.append(all_students.pop())
		  num += 1						#increment (counter)
		  
		print("Poetry class: ", students_in_poetry)
		print(students_in_poetry)	 
		
	LOOP (NESTED) (LOOP inside a loop)
		sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

		scoops_sold = 0
		for location in sales_data:
		  print(location)
		  for i in location:
			scoops_sold += i
			
		print("How many scoops sold?: ", scoops_sold)
		 
	LOOP (INFINITE LOOP) *** WARNING ***
		-use (CTRL+C) to terminate a loop (that is stuck)
		lst = [1, 2, 3]
		for x in lst:
		  lst.append(1)		#*** WARNING, infinite loop ***
	
	LOOP (PROBLEM WITH FLOATS)
		lst = [0, 1, 2, 3, 4, 6, 7, 8, 9]
		*** PROBLEM ***
			>>> for n in lst:
			...     n * 0.1
			...
			0.0
			0.1
			0.2
			0.30000000000000004
			0.4
			0.5
			0.6000000000000001
			0.7000000000000001
			0.8
			0.9
		*** GOOD ***
			>>> for n in lst:
			...     print('{:10.3f}'.format(n * 0.001))
			...
				 0.000
				 0.001
				 0.002
				 0.003
				 0.004
				 0.005
				 0.006
				 0.007
				 0.008
				 0.009
			
	STRING HANDLING FUNCTIONS 
		STRING (HOW TO INSERT A CHAR INTO A STRING?)
			my_string = 'dogdogdog' 
			my_string.index(4, ' ') 			#this DOESN'T WORK??
			----
			def insert_char(my_string, char, index):
				return my_string[:index] + char + my_string[index:]
				
		STRING (LETTER OR WORD IN WORD)(TEST)
			#FUNCTION: WORD IN WORD (TEST)
			def contains(big_string, little_string):
			  return little_string in big_string

			#TEST
			print(contains("watermelon", "melon")) 	#true
			print(contains("watermelon", "water"))	#true
			print(contains("watermelon", "WATER"))	#false
			print(contains("watermelon", "berry"))	#false

		STRING (COMPARE TWO STRINGS)
			#FUNCTION: COMPARE STRINGS (COMMON LETTERS)
			def common_letters(string_one, string_two):
			  result = []
			  for x in string_one:
				if (x in string_two) and not (x in result):
				  result.append(x)
			  return result

			#TEST 
			print(common_letters('banana', 'cream'))		#['a']
			print(common_letters('Dean Jones', 'Nadine Jones')) #['e', 'a', 'n', ' ', 'J', 'o', 's']
	
	FUNCTIONS 		https://docs.python.org/3/library/functions.html#min
		print()		PRINT TO CONSOLE
		str()		CONVERT NUMBER (to string)
		def()		DEFINE FUNCTION (like defun in AutoLISP)
		len()		LENGTH (OF LIST)
		abs()		ABSOLUTE VALUE (make positive)
		float("inf")		INFINITY(FLOAT VALUE)
		
		type(x)		CHECKS THE TYPE (OF VARIABLE)
			>>> w = 'string'
			>>> x = 33
			>>> y = 33.0
			>>> z = (2, 3)
			
			>>> type(w)
				<class 'str'>
			>>> type(x)
				<class 'int'>
			>>> type(y)
				<class 'float'>			
			>>> type(z)
				<class 'tuple'>
		isinstance(x, str)			RETURNS (BOOL)
			str 		STRING
			int 		INTEGER 
			float 		FLOAT 
			tuple 		TUPLE
			>>> isinstance(x, str)
				False
			>>> isinstance(w, str)
				True
				
		min(arg1, arg2, ...)	RETURN (MINIMUM VALUE)
		max(arg1, arg2, ...)	RETURN (MINIMUM VALUE)
		eval(<string>)			EVALUATES A STRING 
			eval("1 + 2 + 3")	#returns 6
			
		input() 						USER INPUT 
		name = input('What is your name?')
		print(name)
		
		zip() 			https://www.programiz.com/python-programming/methods/built-in/zip
						#(LIST OF LISTS)(PAIRED LIST)
						#This COMBINES (two lists) into an embedded list 
						eg. 
							x = [1, 2, 3]
							y = ["one", "two", "three"]
							result = zip(x, y)		#<zip object at 0x00000282501A7A48>
							result2 = list(result)	#[(1, 'one'), (2, 'two'), (3, 'three')]		#CONVERT TO LIST					
						eg2. 
							#*** WARNING, (if the LISTS are UNEQUAL in length, it will CROP it to the SMALLEST LIST)
							x = [1, 2, 3]
							z = [1, 2, 3, 4, 5]
							test = zip(x, z)
							print(list(test))	#[(1, 1), (2, 2), (3, 3)]
		ZIP (***WARNING***)	
						*** NOTE, that a ZIP file, after (CALLED ONCE) will become (AN EMPTY LIST) ***
						*** SAVE AS, back to LIST, after using ZIP to generate a list ***
						eg. 
							-----------------
							#FUNCTION: ZIP LISTS (COMBINE)(subjects and grades)
							def zip_subjects_and_grades(list_subjects, list_grades):
							  return zip(list_subjects, list_grades)				#SHOULD RETURN (LIST), not ZIP
							  
							#ZIP (subjects with grades)
							gradebook = zip_subjects_and_grades(subjects, grades)


							#gradebook = zip(subjects, grades)
							print_grades("Gradebook: ", list(gradebook))			#*** AFTER THIS IS CALLED, it becomes EMPTY ([]) LIST ***
							-----------------
							****** GOOD FUNCTION ******
							def list_subjects_and_grades(list_subjects, list_grades):
							  #return zip(list_subjects, list_grades)		#***WARNING, causes empty list
							  return list(zip(list_subjects, list_grades))
							-----------------

	KEYBOARD SHORTCUTS (KEYBOARD)
		SHFT+TAB	-(REVERSE TAB direction)(goes to FRONT OF WORD sometimes...)
		CTRL+HOME 	-go to TOP of TEXT FILE 
		SHFT+HOME 	-HIGHLIGHT LINE 
		HOME 		-front of line 
		END 		-end of line
		PGUP 		-PAGE UP, scroll UP A PAGE 
		PGDN 		-PAGE DOWN, scroll DOWN A PAGE
				
	KEYBOARD SHORTCUTS (SYMBOLS)
		-look up CHARACTER MAP (search bar in Windows)
		-ARIAL FONT 
		xº		POWER 0			ALT+0186
		x¹		POWER 1			ALT+0185
		xⁿ 		POWER (nth)		???	
			???	xE2\x82\xAC

		
		x² 		SQUARED 		ALT+0178
		x³		CUBED 			ALT+0179 
		
		°C		DEGREE CELCIUS	ALT+0176
		°F		FARENHEIT
		±		PLUS/MINUS		ALT+0177
		≠		NOT EQUAL 		???
		√		SQUARE ROOT 	??? 		U+221A
		∫		INTEGRAL 		???			U+222B
		≤		LESSTHAN-EQUAL	???			U+2264
		≥		GREATERTHAN-EQUAL			U+2265
		
				
		¼		1/4 FRACTION 	ALT+0188
		½		1/2 FRACTION	ALT+0189
		¾		3/4 FRACTION  	ALT+0190
		⅓
		⅔
		⅛
		⅜
		⅝
		⅞
		
		ɸ		PHI 			???
		65¢		CENTS 			ALT+0162
		÷		DIVISION 		ALT+0247
		50ø		DIAMETER		ALT+0248
		
		♠		SPADES 			???			U+2660
		♣		CLUBS 			???			U+2663
		♥		HEARTS 			???			U+2665
		♦		DIAMONDS 		???			U+2666
		
		
	------------
	my_name = "Dean"
	print("Hello and welcome " + my_name + "!")
	------------
	
	COMMENTS (#)
		# this is a comment in Python
		
	VARIABLE 
		my_variable = 33
		
	VARIABLE (NAMES, NAMING)
		-NO SPACES
		-(_) UNDERSCORES allowed 
		-CANNOT BEGIN with a NUMBER 
	
	VARIABLE (SAVE MULTIPLE VARIABLES AT ONCE)
		 x, y = (2,3)
		 -same as...
		 x = 2
		 y = 3	
		
	PRINT 
		print()
		print("print this output")
		print("Hello World")
		print("Dean")
		print('Jones')
		
	PRINT (USE FORMAT TO IMBED VARIABLES)(*** EASIER THAN CONCATENATION ***)
		https://docs.python.org/3/tutorial/inputoutput.html?highlight=printf
		print("Hello, {}".format("Dean"))	
		print("I am {} years old and my dad is {} years old".format(my_age, dads_age))	
	
	STRING (FORMAT)(WITH KEYWORDS)
		def poem_description(author, title):
		  poem_desc = "The poem {title} by {author}.".format(author=author, title=title)
		  return poem_desc

		my_beard_description = poem_description("Shel Silverstein", "My Beard")
		print(my_beard_description)
		#The poem My Beard by Shel Silverstein.
	
	STRING (F-STRING)		https://www.python.org/dev/peps/pep-0498/
		-use (f'....{varA}....{varB}'
		a = 'Dean'
		b = 'Jones'
		f'this {a} is a {b}'			#'this Dean is a Jones'
	
	PRINT(F)(*** doesn't work in Python 3 ***)
		print(f<string>)			-allows variables to be inserted with {my_var}
		my_name = "Dean"
		print(f"hello {my_name}")	-prints "hello Dean"
		---
		print(f"Total: {customer_one_total}")
		tax_formatted = format(tax * 100, '.2f')
		print(f"Tax: {tax_formatted}%")
		print(f"Grand Total: {customer_one_gtotal}")
		
	PRINT (MULTIPLE TIMES)(WITHOUT LOOP)
		print("poo "*6)		#this will print 'poo ' (6 times) "poo poo poo poo poo poo "
		
	PRINT (COMMA)
		days = "Mon Tue Wed Thu Fri Sat Sun"
		print("Days: ", days)						#Days:  Mon Tue Wed Thu Fri Sat Sun
		
	PRINT (separate by COMMA)
		-STRING CONVERTION is automatic
		-ADDS SPACE automatic
		x = 4.0
		print("aaa", x, "zzzzzzzzz")		#this PRINT doesn't require (str())
		---
		train_force = get_force(train_mass, train_acceleration)
		print( "The GE train supplies", train_force, "Newtons of force.")		#The GE train supplies 226800 Newtons of force.
		
	PRINT (CURLY BRACES)
		-the CURLY BRACES are placeholders, for the TWO FORMAT variables
		print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))	
			#The GE train does 22680000 Joules of work over 100 meters.
		--------------
		-add the INDEX NUMBER 
		print("Sammy the {0} has a pet {1}!".format("shark", "pilot fish"))
			#Sammy the shark has a pet pilot fish!
		print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
			#Sammy the pilot fish has a pet shark!
			
	PRINT (CURLY BRACES LITERAL)
		({}) VS ({{}})
		"{dean}".format(dean="Dean")
			'Dean'
		"{{dean}}".format(dean="Dean")
			'{dean}'
			
	PRINT (%S)(PLACEHOLDER)(SHARMEEN)
		name = "Dean"
		str = "this is a test %s"
		print (str % (name))		#this is a test Dean
		
	PRINT (%r)(similar to {} brackets for formatting)
		>>> a = "one"
		>>> b = "two"
		>>> c = "three"
		>>> print('1: %r, 2: %r, 3: %r' % (a, b, c))
		1: 'one', 2: 'two', 3: 'three'
		
	PRINT (NEWLINE)("\n")
		def newline():
			print("\n")
		newline()
		print("------------------")
		newline()
		---
		print("\nThis is a new line.")
		
	PRINT (PAGE BREAK)
		def page_break(str_len):
			#print("-" * 20)			#--------------------
			print("-" * str_len)
	
	PRINT (REPEATING)
		print("." * 10)		#repeats (x10)
		
	PRINT (SUPPRESS NEWLINE)(end=' ')(ex7.py) 		
		print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
		print(end7 + end8 + end9 + end10 + end11 + end12)	#end = ' ' (suppresses NEWLINE? interesting)
			#Cheese Burger
		print(end1 + end2 + end3 + end4 + end5 + end6)		#end = ' ' (removed)
		print(end7 + end8 + end9 + end10 + end11 + end12)	
			#Cheese 
			#Burger
			
	PRINT (FORMAT)
		my_format = "{} {} {} {}"		#use this STRING to SET FORMAT

		print(my_format.format(1, 2, 3, 4))
		print(my_format.format("one", "two", "three", "four"))
		print(my_format.format(			#use MULTIPLE LINES, for arguments
			"Roses are red", 
			"Violets are blue",
			"I am awesome", 
			"And you are too :)"
		))
		
	PRINT (MULTILINE)(STRING)
		-use THREE QUOTES (beginning and end)(for multi-line text)
		print("""
			This is multi-line text
			Can I INDENT THIS LINE? YES THIS WHOLE PARAGRAPH INDENTS THEN...
			I can type as many lines as I need.
		""")

		print("""
		This is multi-line text
		THIS IS *** NOT INDENTED ***
		I can type as many lines as I need.
		""")
			
	FORMAT STRINGS (Currency)			https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
		'${:,.2f}'.format(1234.5)		#'$1,234.50'
			$		-add currency symbol
			, 		-adds COMMA every 3RD DIGIT 
			.2f}	-rounds to TWO DECIMAL PLACES
			
	FORMAT EXAMPLES 					https://docs.python.org/2/library/string.html	
		BASIC 
			'{0}, {1}, {2}'.format('a', 'b', 'c')
				#'a, b, c'
			'{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
				#'a, b, c'
			'{2}, {1}, {0}'.format('a', 'b', 'c')
				#'c, b, a'
			'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
				#'c, b, a'
			'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
				#'abracadabra'		
		CONVERT BASES 
			"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
				#'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
		THOUSANDS SEPARATOR 
			'{:,}'.format(1234567890)
				#'1,234,567,890'
		PERCENTAGE 
			points = 19.5
			total = 22
			'Correct answers: {:.2%}'.format(points/total)
				#'Correct answers: 88.64%'
		TIME 
			import datetime
			d = datetime.datetime(2010, 7, 4, 12, 15, 58)
			'{:%Y-%m-%d %H:%M:%S}'.format(d)
				#'2010-07-04 12:15:58'
		CURRENT TIME 
			import datetime 
			d = datetime.datetime.now() 
				#				  (	year, 	month, 	day, 	hour, 	minute, 	second, 	microsecond	)	
				#datetime.datetime(	2018, 	8, 		22, 	21, 	52, 		35, 		570705		)
			d.year				#2018
			d.month 			#8 (August)
			d.day				#22 (Aug.22)
			d.weekday()			#returns 2 		(for Wednesday)
			d2.strftime('%A')	#'Wednesday'
			d.hour				#21 (24 hour clock)
			d.minute			#53
			d.second			#33
		CURRENT DATE 
			# d = datetime.date(year=2018, month=9, day=5)
			# d.strftime('%A, %b.%d, %Y')         #'Wednesday, Sep.05, 2018'
			# d.strftime('%A')                    #'Wednesday'
			#SET THE DATE
			d = Date(datetime.date(year=1976, month=6, day=7))
			# Monday, Jun.07, 1976
			#GET THE CURRENT DATE 
			current = Date(datetime.datetime.now())
			# Wednesday, Sep.05, 2018
			
		DATETIME (TIME)(STRFTIME)
			EXAMPLE
			https://docs.python.org/3/library/datetime.html
			SET TIME 
				import datetime 
				---
				12 HOUR CLOCK
				d = datetime.time(hour=11, minute=00)
				d.strftime('%I:%M %p')		#'11:00 AM'
				---
				d = datetime.time(hour=13, minute=00)
				d.strftime('%I:%M %p')		#'01:00 PM'
				---
				24 HOUR CLOCK 
				d.strftime('%H:%M')			#'13:00'
				
			FORMAT CODES
			https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
			%a		weekday (short)				Sun, Mon, Tues...
			%A 		weekday (long) 				Sunday, Monday, Tuesda...
			%w 		weekday (int) 				0-6
			
			%H 		HOUR, 24 hour clock 		01-23
			%I 		HOUR, 12 hour clock 		01-12
			%p		12 hour (am, pm)			AM, PM
			%M		Minute (zero-padded)		00-59
			%S		Second (zero-padded)		00-59
			%Z		Time zone name				MST, CST, EST 
			
			
		TEXT ALIGN 
			'{:<30}'.format('left aligned')
				#'left aligned                  '
			'{:>30}'.format('right aligned')
				#'                 right aligned'
			'{:^30}'.format('centered')
				#'           centered           '
			'{:*^30}'.format('centered')  # use '*' as a fill char
				#'***********centered***********'
		
	STRING (double or single quotes)
		"Hello World"
		'Hello World'
		
	STRING (WITH FORMAT)
		-f (format)(put in front of string)(use CURLY BRACES to embed the VARIABLE)
		x = 100
		f"some string {x}"		#returns ('some string 100')
		
	F-STRING 
		-(f) stands for FORMAT 
		f"some stuff here {a_variable}"	
		
	STRING (UPPERCASE, lowercase)
		'asdf'.upper()
			#'ASDF'
		'ABCDEF'.lower()
			'abcdef'
			
	STRING (CAPITALIZE, TITLE)
		'asdf'.capitalize()
			#'Asdf'
		'asdf zzzzz'.title()
			#'Asdf Zzzzz'
			
	STRING (COUNT)			https://thehelloworldprogram.com/python/python-string-methods/
		>>> ss = "abbccc"
		>>> ss.count("a")
		1
		>>> ss.count("b")
		2
		>>> ss.count("c")
		3
	
	STRING (FIND)
		-returns the INDEX of the FIRST LETTER (0-index to start)
		>>> s = "hello world"
		>>> s.find("world")
		6
		
	STRING (FIND)(DIDN'T FIND ANYTHING?)
		-returns (-1) if it doesn't find anything
		daily_sales.find(':')
			#returns -1
	
	STRING (FIND ALL)(INDEXES OF STRING)
		#THE CONCEPT...
		#test 'ab' in string 'abcdef abcdef'
		# >>> test[0:2]
		# 'ab'
		# >>> test[1:3]
		# 'bc'
		# >>> test[2:4]
		# 'cd'
		# >>> test[3:5]
		# 'de'
		# >>> test[4:6]

		#FUNCTION: FIND ALL (INDEXES OF STRING)(SEARCH)
		def find_all(my_str, str_to_test):
			#variables
			length = len(my_str)                        #length of entire string
			last_index = len(my_str)                    #index of last character
			start = 0                                   #start index
			length_str_to_test = len(str_to_test)       #length of string being tested
			end = start + length_str_to_test            #end char (to iterate thru)
			result = []                                 #save indexes here
			
			while end <= last_index:
				if my_str[start:end] == str_to_test:    #test here
					result.append(start)                #if test matches (add index)
				#update counters
				start += 1
				end += 1
			return result
			
		find_all('abcdef abcdef abcdef', 'ef')          #[4, 11, 18]
		find_all('abcdef abcdef abcdef', 'ab')          #[0, 7, 14]
		
	STRING FIND FIRST (INDEX)
		-dependent on (find_all()) FUNCTION
		#FUNCTION: FIND FIRST (INDEX)
		def find_first(my_str, str_to_test):
			return find_all(my_str, str_to_test)[0]

		#TEST 
		find_first('banana', 'n')                       #returns 2
		find_all('banana', 'n')                         #[2, 4]
		
	STRING (FIND)(FIND ALL OCCURENCES)
		def
		
	STRING (REPLACE)
		-parameters (old_string, new_string)
		>>> s.replace("world", "ttt")
		'hello ttt'
	
	STRING (CHAIN METHODS)(combine REPLACE and TITLE)
		>>> s.replace("world", "Dean").title()
		'Hello Dean'
		
	STRING (BYTES LITERAL)
		str = '...' 			-literals = a sequence of Unicode characters (UTF-16 or UTF-32, depending on how Python was compiled)
		bytes = b'...' 			-literals = a sequence of octets (integers between 0 and 255)
		b"this is a bytes literal"
		B"this is a bytes literal"
		
	STRING (GET A LETTER)(treat a STRING as a LIST of chars)
		>>> str1 = "@coolguy35"
		>>> str1
		'@coolguy35'
		>>> str1[0]
		'@'
		
	STRING (SPLIT)
		'Hello world'.split()					#['Hello', 'world']
		'Hello, world, Dean'.split(',')			#['Hello', ' world', ' Dean']
		
	STRING (SPLITTING)
		authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

		author_names = authors.split(',')
		print(author_names)		
		#['Audre Lorde', ' William Carlos Williams', ' Gabriela Mistral', ' Jean Toomer', ' An Qi', ' Walt Whitman', ' Shel Silverstein', ' Carmen Boullosa', ' Kamala Suraiyya', ' Langston Hughes', ' Adrienne Rich', ' Nikki Giovanni']

		author_first_names = [x.split()[0] for x in author_names]
		#['Audre', 'William', 'Gabriela', 'Jean', 'An', 'Walt', 'Shel', 'Carmen', 'Kamala', 'Langston', 'Adrienne', 'Nikki']
		print(author_first_names)
		author_last_names = [x.split()[-1] for x in author_names]
		print(author_last_names)
		#['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']
		
	STRING (JOIN)
		' '.join(['Hello', 'world'])			#'Hello world
		
	STRING (JOIN)(<delimiter>.join(<list_of_string>))
		-opposite of SPLIT
		-delimitter with argument (as list) of strings
		-good for CSV FILES (COMMA SEPARATED FILE)(COMMA DELIMITTER)
		eg.
			reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
			reapers_line_one = ' '.join(reapers_line_one_words)
			print(reapers_line_one)
			#Black reapers with the sound of steel on stones
		
	STRING (REPLACE)
		'Hello world'.replace('H', 'J')			#'Jello world'
		'Adam, Abel, Andrew'.replace('A', 'J')	#'Jdam, Jbel, Jndrew'
		
	STRING (SPLIP)(removes whitespace)	
		'   Hello world   '.strip()				#'Hello world'	
		-removes SPACES (front and back)
		-also removes ('\n') NEW LINES
	
	STRING (WHITESPACE)(FROM FRONT OF STRING)
		def remove_white_front(my_str):
			for x in my_str:
				if my_str[0] == ' ':			#test to see if FIRST ELEMENT (is a space)
					my_str = my_str[1:]			#if it is (redefine the LIST, without first space)
			return my_str

		remove_white_front('    bad spaces in front')
			#'bad spaces in between'
			
	STRING (WHITESPACE)(FROM BACK OF STRING)
			def remove_white_back(my_str):
				for x in my_str:
					if my_str[-1] == ' ':		#test to see if LAST ELEMENT (is a space)
						my_str = my_str[:-2]	#if it is (redefine the LIST, without last space)
				return my_str

			remove_white_back('bad spaces at end    ')
				'bad spaces at end'
				
	STRING (WHITESPACE)(FROM BACK OF STRING)
		def remove_white_both(my_str):
			for x in my_str:
				#remove FRONT (whitespace)
				if my_str[0] == ' ':			#test to see if FIRST ELEMENT (is a space)
					my_str = my_str[1:]			#if it is (redefine the LIST, without first space)
				#remove BACK (whitespace)
				if my_str[-1] == ' ':			#test to see if LAST ELEMENT (is a space)
					my_str = my_str[:-2]		#if it is (redefine the LIST, without last space)
			return my_str

		remove_white_both('    bad spaces front and back    ')
			'bad front and back'
	
	STRING (BINARY TO STRING)
		b'hello Dean'.encode('ascii') 		#
		
	
	CONVERT(STRING to BYTES)
		<string>.encode('UTF-8')
		'\uFEFF'.encode('UTF-8')
		b'\xef\xbb\xbf'
		
	CONVERT(BYTES TO STRING)
		<bytes>.decode('UTF-8')
		b'\xE2\x82\xAC'.decode('UTF-8')
		'€'			
	
	NUMBERS 
		INTEGER (int)		3
		FLOAT 				1.44				https://docs.python.org/3/tutorial/floatingpoint.html
		my_int = 33
		my_float = 1.44
		
	FLOAT (BINARY)
		-these numbers are EQUAL
		0.125 (has a value 1/10 + 2/100 + 5/1000)
		0.001 (has a value 0/2 + 0/4 + 1/8)
		
	FLOAT (PI 3.14)
		format(math.pi, '.12g')  # give 12 significant digits
			'3.14159265359'
		format(math.pi, '.2f')   # give 2 digits after the point
			'3.14'	
			
	FLOAT (ROUNDING ISSUES)
		https://docs.python.org/3/tutorial/floatingpoint.html
		*** NOTE, there are issues with how FLOATS are stored in BINARY (and could have weird results) ***
			
	OPERATOR (FIND MINIMUM)
		min(a, b, c) 		#min function
		-another way... (use the < > greater-than, or less-than operators to point to it 
			eg. find MIN of THREE VARIABLES 
				*** NOTE, the MIDDLE TERM is always the one that is CORRECT ***
				a = 1, b = 2, c = 3
				-just scoll the VARIABLES to the right, leaving the OPERATORS the same (POINTING TO MIDDLE TERM, as less-than)
				a > b < c	#false 
				c > a < b 	#true 
				b > c < a 	#false 
			eg. fin MAX of THREE VARIABLES 
				a < b > c 	#false
				c < a > b 	#false
				b < c > a  	#true
			-------------
			#works unless ARGUMENTS are EQUAL
			#>>> def my_min(a, b, c):
			#...     if (a > b < c):
			#...             return b
			#...     elif (c > a < b):
			#...             return a
			#...     elif (b > c < a):
			#...             return c
			#...     else:
			#...             return "my_min failed"
			---
			#this works PERFECTLY
			#FUNCTION: MINIMUM (MIN)
			def my_min(a, b, c):
				if (a >= b <= c):
					return b
				elif (c >= a <= b):
					return a
				elif (b >= c <= a):
					return c
				else:
					return "my_min failed"
			-------------
			#FUNCTION: MAXIMUM (MAX)
			def my_max(a, b, c):
				if (a <= b >= c):
					return b
				elif (c <= a >= b):
					return a
				elif (b <= c >= a):
					return c
				else:
					return "my_max failed"
			-------------
			#FUNCTION: MIN (4-TERMS)
			#works perfectly, just funnel the LEFT-MOST TERM, make all the OPERATORS THE SAME)
			>>> def my_min4(a,b,c,d):
			...     if(a <= b <= c <= d):
			...             return a
			...     elif(d <= a <= b <= c):
			...             return d
			...     elif(c <= d <= a <= b):
			...             return c
			...     elif(b <= c <= d <= a):
			...             return b
			...     else:
			...             return "my_min4 failed"
			...
	ERRORS** (^ points to error)
		ASSERTION ERROR 
		AssertionError: The rating argument needs to be a number (int).						<--- *** KEPT SHOWING THIS 
		AssertionError: .........The rating argument needs to be a number (int).			<--- *** SHOULD HAVE LOOKED LIKE THIS (FROM UPDATED CODE)		
			-was fighting with this for a long time (hours)
			-INHERITANCE (apparently with the CONSOLE, and inheritance, I had TWO OBJECTS that DID NOT UPDATE)
			-I changed the ASSERTION ERROR MESSAGE (but for some reason it wasn't changing which was very hard to track down)
				-FIND (in my code could not find this??)
			-It must have been STUCK IN MEMORY or something (not sure)
			-FIX: I took both OBJECTS (where I instantiated them)
				-MAKE SURE TO (UPDATE THE CODE FOR *** ALL INHERITED CLASSES ***)
				-DELETED (THE OBJECTS)
					-del(object_name)
						book1 = tr.create_book("Society of Mind", 1234512345678)
						novel1 = tr.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")
						del(book1)	#this deletes the OBJECT (INSTANCE)
						del(novel) 	#this deletes the OBJECT (INSTANCE)
						novel1.add_rating('None')			#AssertionError: The rating argument needs to be a number (int).	
				-RECREATE THE OBJECTS (INSTANCE)
						book1 = tr.create_book("Society of Mind", 1234512345678)
						novel1 = tr.create_novel("Alice In Wonderland", 1020304030201, "Lewis Carroll")
	
		KEY ERROR 
			KeyError: 'energy' 
			-happens if KEY in DICTIONARY (doesn't exist)
			zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], 
				"air":["Gemini", "Libra", "Aquarius"], "energy2": "Not a Zodiac element"}
				print(zodiac_elements["energy"])
					#CREATES KEY ERROR...
		SYNTAX ERROR 
			-something wrong with the WRITTEN PROGRAM (punctuation)(eg. missing a quote)
			-SyntaxError
			-SyntaxError: invalid syntax
			-bad LOGIC (= instead of ==)
					if user_name = "Dave":
								 ^
				SyntaxError: invalid syntax
			---
			-SyntaxError: unexpected EOF while parsing
				-check INDENTS, MISSING BRACKETS (on functions)
				*** NOTE, may be before the LINE indicated ***
				-print(currency(2.25)		#SyntaxError: unexpected EOF while parsing
				-print(currency(2.25)		#$2.25
			------------
			SyntaxError: invalid syntax
				-improper use of ESCAPE CHARACTERS
				eg. 
					password = "theycallme"crazy"91"		#BAD
					password = "theycallme\"crazy\"91"		#GOOD 
					password2 = 'theycallme"crazy"91'		#GOOD
			------------
			SyntaxError: 'continue' not properly in loop
				-if key_letter == ' ':
					continue					#this causes ERROR 
				-apparently CONTINUE can only be used in WHILE or FOR statements
				
		NAME ERROR 
			-if Python DOESN'T RECOGNIZE A WORD
			-NameError 
			---
			-NameError: name 'raw_input' is not defined
				-RAW_INPUT() was renamed to INPUT()
		DIVIDE BY ZERO
			-dividing a number by zero (eg. 23 / 0)
			-ZeroDivisionError
			-ZeroDivisionError: division by zero
		TAB ERROR 
			-TabError: inconsistent use of tabs and spaces in indentation
			-Python DOESN'T LIKE inconsitently MIXED TABS AND SPACES for indentation
			-*** INDENT, underneath (def) FUNCTION (Python expects this to be indented) ***
		INDEX ERROR
			-IndexError: tuple index out of range
			-this happens if you use an INDEX that is out of range 
				-eg. print("Sammy the {1} has a pet {2}!".format("shark", "pilot fish"))     	#this needs to be INDEX (0 and 1)
			---------
			IndexError: list index out of range
				-index value is TOO HIGH (or low?)
		TYPE ERROR 
			-TypeError: a bytes-like object is required, not 'str'
				"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode('utf-8')
				"STRING".encode('utf-8')
			--------
			-TypeError: 'list' object is not callable
				-the problem here (I created a LIST with the NAME (list))
				-the problem here is (Python lets me do it, without warning, but then later I cannot call the LIST CONSTRUCTOR)
				eg. 	x = list(("one", "two", "three"))		#['one', 'two', 'three']
						#this works fine 
						#create a new list
						list = [1, 2, 3]						#*** WARNING, don't do this!!!, this will not allow the LIST CONSTRUCTOR to work ***
						y = list(("one", "two", "three"))
							#TypeError: 'list' object is not callable
			--------
			TypeError: can only concatenate list (not "int") to list
				-this happens if you are CONCATENATING (+)
				-make sure BOTH ARE LISTS 
					x = [1, 2, 3]
					x + 4 		#TypeError 
					x + [4]		#[1, 2, 3, 4]
			--------
			TypeError: 'str' object does not support item assignment
				-STRING is IMMUTABLE (CANNOT CHANGE) 
				-so we CANNOT reassign the LETTER
					first_name = "Bob"		
					first_name[0] = "R"
			--------
			TypeError: unhashable type: 'list'
				-DICTIONARIES, need to have a KEY (string or int) that is UNCHANGEABLE (otherwise HASH is unreliable...)
				#eg. powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
				#TypeError: unhashable type: 'list'
					
		UNSUPPORTED OPERAND TYPE 
			unsupported operand type(s) for //: 'builtin_function_or_method' and 'int'
			-check VARIABLE NAMES match arguments (don't use KEYWORDS)

		ATTRIBUTE ERROR 
			-AttributeError: 'float' object has no attribute
			AttributeError: 'super' object has no attribute '_NonFiction__init'
				-check the SPELLING
				super().__init(title, isbn)			#ERRORS (missing LAST DOUBLE UNDERSCORE)(__init__)
		PERMISSION ERROR 
			PermissionError: [WinError 5] Access is denied: 'c:\\program files\\anaconda3\\lib\\site-packages\\pip'
			PermissionError: [WinError 5] Access is denied: 'c:\\program files\\anaconda3\\lib\\site-packages\\pip\\basecommand.py'
			-run as admin ???
			
		INDENTATION ERROR
			IndentationError
			-happens a lot (go through code, and *** REDO ALL INDENTS ***)
			-this happens on FUNCTIONS, FOR-LOOP, IF-STATEMENT 
				-if the TABS or SPACES (aren't identical)
				-NOTE, (Code Academy) uses (2 SPACES)
			-*** MAKE SURE TO INDENT (EVEN WITH SPACE IN LONG FUNCTION) ***
			--------------------------
			#FUNCTION: TRIAL AND ERROR (FOR SMALLEST ERROR)
			def find_smallest_error(lst):
				#variables (defaults)
				smallest_error = float("inf")
				best_m = 0
				best_b = 0
															#<-- *** STILL NEEDS INDENT FOR FUNCTION TO STAY CONNECTED ***
				#loop thru all possible combinations
				for m in possible_ms:
					for b in possible_bs:
						test = calculate_all_error(m, b, lst)
						if (test < smallest_error):
							smallest_error = test   #save best (error value)
							best_m = m              #save best (m - value)
							best_b = b              #save best (b - value)
				return [smallest_error, best_m, best_b]
			--------------------------
			IndentationError: unexpected indent
			-*** MAKE SURE (IF-STATMENT) HAS (: COLON) AT THE END... ***
				-this can cause INDENT ERROR
		
		UNBOUND LOCAL ERROR
			UnboundLocalError: local variable 'smallest_error' referenced before assignment
			-this happens with (A VARIABLE) outside of (A FUNCTION) and you are (trying to update it)
				-either (PUT THE VARIABLE INSIDE THE FUNCTION)
				-or use GLOBAL keyword?			https://stackoverflow.com/questions/39911666/why-does-it-say-in-python-unboundlocalerror-local-variable-yes-referenced
				eg.
					----------------
					my_variable += 1
					def myfunc():
						global my_variable
					----------------
				
		ENCODING ERROR	
			-CREATED FILE WITH... (echo $null >> ex5.py) NOW ERRORS...
			*************************************************************
			FIX:
				-create file in NOTEPAD (copy/paste contents)
				-OR SAVEAS in NOTEPAD (change ENCODING at bottom to UTF8)
			*************************************************************
			-CREATE IN (WINDOWS EXPLORER)(ex5.py)(*** this works ***)
				-*** OPEN FILE in HEX EDITOR (the first TWO CHARACTERS are (ff) and (fe) which appear before the first comment (this is the problem that's tripping Python) ***
					-deleting this in HEX EDITOR doesn't fix this (needs upgrade to change ENCODING)
				-https://stackoverflow.com/questions/35507214/python-encoding-error-non-ascii-character-xff-allthough-coding-is-decl
				-Python doesn't support source files encoded with with a fixed-width multi-byte codec such as UTF-16 or UTF-32.
				-Your file is encoded as UTF-16 Little Endian, which means the file starts with a Byte Order Mark; the first two bytes in the file are (hex) FF and FE. Python trips over the first byte.
				-Re-save the file as UTF-8 instead. See the PyCharm documentation, there is a section on changing the encoding.
		
			-Python will default to ASCII as standard encoding if no other encoding hints are given.
			-a magic comment must be placed into the source files either as FIRST OR SECOND LINE 
			-had a comment on the FIRST LINE of (*.py) (caused error)
				--------------------------------------------------------------------------------------------
				SyntaxError: Non-UTF-8 code starting with '\xff' in file ex5.py on line 1, 
				but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
				--------------------------------------------------------------------------------------------
			-??start file with...
				#!/usr/bin/python
				# -*- coding: ascii -*-
				

	CALCULATIONS 
		-if INT and FLOAT are in the same CALCULATIONS (the INT will be CONVERTED AUTOMATICALLY to a float)
		-Python follows ORDER OF OPERATIONS (BEDMAS, brackets, exponents, division/multiplication, addition/subtraction)
			*** NOTE, BEDMAS will do calculations FIRST, then LOGIC statements LAST (eg. if 2 == 4 = 2:) ***
		
		calc = 25 * 68 + 13 / 28
		print(calc)
		
		quilt_width = 8
		quilt_length = 12
		print(quilt_width * quilt_length)
		
		EXPONENTS (**)
			>>> 2 ** 3
				8
			>>> 2 ** 4
				16
			>>> 2 ** 5
				32
		
		-----------------		
		six_quilt = 6
		seven_quilt = 7
		eight_quilt = 8

		num_people = 6
		num_quilts_each = 6

		print(six_quilt ** 2)
		print(seven_quilt ** 2)
		print(eight_quilt ** 2)

		print(six_quilt ** 2 * num_people * num_quilts_each)
		-----------------
	
		MODULO (%)(EVERY NTH-TIME)
			-modulo operator is useful in programming when we want to perform an action EVERY NTH-TIME the code is run
	
		-------------
		person1_team = 1 % 4
		person2_team = 2 % 4
		person3_team = 3 % 4
		person4_team = 0 % 4
		print("Person 1 belongs to team:", person1_team)
		print("Person 2 belongs to team:", person2_team)
		print("Person 3 belongs to team:", person3_team)
		print("Person 4 belongs to team:", person4_team)
		-------------
	
		CONCATENATION
			-use (str()) to CONVERT A NUMBER (to string)
			*** WARNING, cannot cheat with (print(5 + "test")) ***
			------------------------
			string1 = "The wind, "
			string2 = "which had hitherto carried us along with amazing rapidity, "
			string3 = "sank at sunset to a light breeze; "
			string4 = "the soft air just ruffled the water and "
			string5 = "caused a pleasant motion among the trees as we approached the shore, "
			string6 = "from which it wafted the most delightful scent of flowers and hay."
			message = string1 + string2 + string3 + string4 + string5 + string6

			print(message)
			------------------------
	
		PLUS EQUALS (+=)
		----------------------------
		hike_caption = "What an amazing time to walk through nature!"

		# Almost forgot the hashtags!
		hike_caption += " #nofilter"
		hike_caption += " #blessed"
		----------------------------
		total_price = 0
		print(total_price)
		new_sneakers = 50.00

		total_price += new_sneakers
		print(total_price)
		nice_sweater = 39.00
		fun_books = 20.00

		total_price += nice_sweater
		print(total_price)
		total_price += fun_books
		print(total_price)
		----------------------------
	
		MULTI-LINE STRINGS
		----------------------------
		to_you = """
		Stranger, if you passing meet me and desire to speak to me, why
		  should you not speak to me?
		And why should I not speak to you?
		"""
		----------------------------
		
		REVIEW 
		----------------------------
		#variables
		my_age = 42
		half_my_age = my_age / 2
		greeting = "Welcome :)"
		name = "Dean"
		greeting_with_name = "Welcome, " + name
		----------------------------
		
		CLASS (BOOK: Python 3 The Hard Way, p.180)
			-----------------------
			#CLASS
			class Parent(object):
				def override(self):
					print("PARENT override()")

			#CREATE OBJECT
			dad = Parent()
			dad
				#<__main__.Parent object at 0x0000023791B1D748>
				
			#CALL METHOD
			dad.override()
				#PARENT override()
			-----------------------
		
		CLASS (DUPLICATE DATA IN OBJECTS)(*** WARNING ***)
			-when I update data (all the objects had same data?)
			*** BAD WAY ***
			class Book:
				def __init__(self, rating=[]):            
					self.ratings = rating
			*** CORRECT WAY ***
			class Book:
				def __init__(self):
					self.ratings = []
		
		OBJECT (DUMP PROPERTIES AND METHODS)
		---------------------------
		def dump(obj):
			for attr in dir(obj):
				if hasattr( obj, attr ):
					print( "obj.%s = %s" % (attr, getattr(obj, attr)))
		dump(dad)
		---------------------------
		
		DUMP OBJECT METHODS ??? (DIR(x))
			x = 33 
			dir(x)
			#-----------------
			s = 'string'			
			dir(s)				#DUMP METHODS
			['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
				'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
				'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
				'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 
				'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 
				'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
				'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
				'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
				
		GET ATTRIBUTES (FROM FUNCTION)
		def tip(total, percentage):
			return total * percentage
		import inspect 
		inspect.getfullargspec(tip)
			#FullArgSpec(args=['total', 'percentage'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})
		inspect.getfullargspec(tip).args
			#['total', 'percentage']
			
JUL.17 
QUIZ#1 SYNTAX 
	100% (13/13)
	
JUL.17 (WEEK 1, DAY 4,5)
	-------------------------------------
	PROJECT (FURNITURE STORE)(CUSTOMER PRINT RECEIPTS)
	see file... 
		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\01-Syntax\
		01-furniture_store.py"
	-------------------------------------
	
JUL.18 (WEEK 2, DAY 1,2)
	FUNCTIONS
	SYNTAX 
		def function_name():
			#some code
			
	DEF (FUNCTION)
		-in Python, the WHITESPACE tells the compiler what is part of the function (because there are no brackets)
		-make sure to use TABS OR SPACES (to indent)(*** MUST BE THE SAME or you'll get a TabError ***)
		-RETURN (is used to return OUTPUT, or close off function
		--------------------------
		def func(param1, param2, etc):		#PARAMETERS are when creating the function
			#code goes here
			return
			
		func(arg1, arg2, etc)				#ARGUMENTS are when running the function
		--------------------------
	
	FUNCTION (create the function)
	def hello():
		print("Hello world!")
		
	IMPLEMENT FUNCTION (run it)
	hello()
	
	-----------
	def loading_screen():
		print("This page is loading...")
  
	loading_screen()
	-----------
	def mult_two_add_three(number):
		print(number * 2 + 3)
	  
	mult_two_add_three(5)
	mult_two_add_three(-1)
	mult_two_add_three(0)
	-----------
	
	KEYWORD ARGUMENTS (this sets a DEFAULT VALUE to the PARAMETER)
	-can take the ARGUMENT or NOT (it will use the default value)(OPTIONAL)
	-----------
	def create_spreadsheet(title, row_count=1000):
		print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")
	  
	create_spreadsheet("Downloads")
	create_spreadsheet("Applications", 10)
	-----------
	
	FUNCTION (RETURN)
	-----------
	def calculate_age(current_year, birth_year):
		return current_year - birth_year

	my_age = calculate_age(2018, 1993)
	dads_age = calculate_age(2018, 1953)

	print("I am {} years old and my dad is {} years old".format(my_age, dads_age))
	-----------
	
	FUNCTION (MULTIPLE RETURNS)
	-----------
	def func(x, y):
		return x, y
	func(2,3)
		(2, 3)
	-----------
	def get_boundaries(target, margin):
		low_limit = target - margin
		high_limit = target + margin
		return low_limit, high_limit

	low, high = get_boundaries(100, 20)
	print("Low limit: "+str(low)+", high limit: "+str(high))
	-----------
	
	REVIEW 
	-----------
	def repeat_stuff(stuff, num_repeats=10):
		return stuff*num_repeats
	  
	lyrics = repeat_stuff("Row ", 3) + "Your Boat"
	song = repeat_stuff(lyrics)
	print(song)
	-----------
	
JUL.19 QUIZ
	QUIZ#1 FUNCTIONS 
	85% (6/7)
	100% (7/7)
	
JUL.20 PROJECT: GETTING READY FOR PHYSICS CLASS
	-------------------------
	#variables (code academy)
	train_mass = 22680
	train_acceleration = 10
	train_distance = 100

	bomb_mass = 1

	#TEMPERATURE
	#farenheit(f) to celcius(c) convertion
	def f_to_c(f_temp):
	  return (f_temp - 32) * 5 / 9

	print(f_to_c(100))									#37.7777...

	#celcius(c) to farenheit(f) convertion
	def c_to_f(c_temp):
	  return (c_temp * 9 / 5) + 32

	print(c_to_f(37.7777777777777777))	#100.0

	#FORCE
	#calculate force
	def calc_force(mass, acceleration):
	  return mass * acceleration

	train_force = calc_force(train_mass, train_acceleration)
	print( "The GE train supplies", train_force, "Newtons of force.")

	#calculate energy 
	#mass = mass, c = constant(speed of light)
	def calc_energy(mass, c = 3 * 10 ** 8):
	  return mass * c * c

	bomb_energy = calc_energy(bomb_mass)
	print("A 1kg bomb supplies", bomb_energy, "Joules.")

	#calculate work
	def calc_work(mass, acceleration, distance):
	  force = calc_force(mass, acceleration)
	  return force * distance

	train_work = calc_work(train_mass, train_acceleration, train_distance)
	print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))
	-------------------------
	#UNIT CONVERSIONS 
	#INCHES, MILLIMETERS, CENTIMETERS

	#FUNCTION: convert (inches to millimeters)
	def in_to_mm(inches):
		return inches * 25.4

	print(in_to_mm(6.625))

	#FUNCTION: convert (millimeters to inches)
	def mm_to_in(millimeters):
		return millimeters / 25.4

	print(mm_to_in(50.8))

	#---

	#FUNCTION: convert (inches to centimeters)
	def in_to_cm(inches):
		return inches * 2.54

	print(in_to_cm(6.625))

	#FUNCTION: convert (centimeters to inches)
	def cm_to_in(centimeters):
		return centimeters / 2.54

	print(cm_to_in(10))
	-------------------------
	
JUL.20 
	FUNCTIONS 
	-------------------------
	#FUNCTION: average (two numbers)
	def average(num1, num2):
		return (num1 + num2) / 2		
	print(average(1, 100))			# The average of 1 and 100 is 50.5
	print(average(1, -1))			# The average of 1 and -1 is 0
	-------------------------
	#FUNCTION: TENTH POWER 
	def tenth_power(num):
		return num ** 10
	print(tenth_power(2))			# 2 to the 10th power is 1024
	-------------------------
	#extra practise (did on my own)
	#FUNCTION: SQUARED (number)
	def square(num):
		return num ** 2
	print(square(2))				# 2^2 = 4
	print(square(3))				# 3^2 = 9
	print(square(4))				# 4^2 = 16
	
	#FUNCTION: CUBED (number)
	def cube(num):
		return num ** 3
	print(cube(2))				# 2^3 = 8
	print(cube(3))				# 3^3 = 27
	print(cube(4))				# 4^3 = 64
	
	#FUNCTION: POWER (number)(a number to any power)
	def power(num, power=2):
		return num ** power
	print(power(2, 3))			# 2^3 = 8
	print(power(3, 3))			# 3^3 = 27
	print(power(2, 6))			# 2^6 = 64
	print(power(9))				# 9^2 = 81 (defaults to SQUARE ^2)
	print(power(10))			# 10^2 = 100 
	-------------------------
	#FUNCTION: INTRO
	def introduction(fname, lname):
		return '{1}, {0} {1}'.format(fname, lname)
	print(introduction("James", "Bond"))			# should print Bond, James Bond
	print(introduction("Maya", "Angelou"))			# should print Angelou, Maya Angelou
	-------------------------
	#FUNCTION: SQUARE ROOT 
	def square_root(num):
		return num ** (1 / 2)
	print(square_root(16))			# should print 4
	print(square_root(100))			# should print 10
	-------------------------
	#extra practise 
	#FUNCTION: NTH ROOT 
	def nth_root(num, root=2):
		return num ** (1 / root)
	print(nth_root(25, 2))			# should print 5.0
	print(nth_root(2))				# should print 1.414...
	print(nth_root(2, 3))			# should print 1.2599...
	-------------------------
	#FUNCTION: TIP CALCULATOR
	def tip(total, percentage):
		return total * (percentage / 100) 
	print(tip(10, 25))				# should print 2.5
	print(tip(0, 100))				# should print 0.0
	
	#formatted for currency
	print('${:,.2f}'.format(tip(10, 25)))		#$2.50
	print('${:,.2f}'.format(tip(32.50, 10)))	#3.25
	-------------------------
	#FUNCTION: CURRENCY FORMAT 
	def currency(num):
		return '${:,.2f}'.format(num)
	#formatted with function
		print(currency(tip(77.00, 22)))
	-------------------------
	#FUNCTION: WIN PERCENTAGE 
	def win_percentage(wins, losses):
		return wins / (wins + losses) * 100

	print(win_percentage(5, 5))			# should print 50
	print(win_percentage(10, 0))		# should print 100
	-------------------------
	#FUNCTION: FIRST THREE MULTIPLES 
	def first_three_multiples(num):
		num1 = num * 1
		num2 = num * 2
		num3 = num * 3
		print('{0}, {1}, {2}'.format(num1, num2, num3))
		return num3

	first_three_multiples(10)			# should print 10, 20, 30, and return 30
	first_three_multiples(0)			# should print 0, 0, 0, and return 0
	print(str(first_three_multiples(7)))	#7, 14, 21
	-------------------------
	#FUNCTION: DOG YEARS 
	def dog_years(name, age):
		#one(1) year equals seven(7) dog years
		return "{0}, you are {1} years old in dog years".format(name, age * 7)

	print(dog_years("Lola", 16))			# should print "Lola, you are 112 years old in dog years"
	print(dog_years("Baby", 0))				# should print "Baby, you are 0 years old in dog years"
	-------------------------
	#FUNCTION: REMAINDER 
	#??? this is just an example (not practical)(use REMAINDER2 FUNCTION below)
	def remainder(num1, num2):
		return (num1 * 2) % (num2 / 2)

	print(remainder(15, 14))			# should print 2
	print(remainder(9, 6))				# should print 0
	-------------------------
	def remainder2(num1, num2):
		return num1 % num2

	print(remainder2(10, 3))			# should print 1
	-------------------------
	#FUNCTION: ALL OPERATIONS
	def lots_of_math(a, b, c, d):
		#calculations
		first = a + b
		second = d - c
		third = first * second
		fourth = third % a
		
		#print
		print(first)
		print(second)
		print(third)
		
		return fourth
	  
	print(lots_of_math(1, 2, 3, 4))			# should print 3, -1, -3, 0
	print(lots_of_math(1, 1, 1, 1))			# should print 2, 0, 0, 0
	-------------------------
	
	SOCKETS (youtube.com DrapsTV) 		https://www.youtube.com/watch?v=XiVVYfgDolU
		-CLIENT/SERVER model 			-website (server), client (user's browser)
										-server (is constantly available)
		-CLIENT/CLIENT					-PEER-TO-PEER					
										-game server, skype 
										-DON'T have to be constantly available
										-clients connect to clients (without a central server)
		-IP ADDRESS 					-eg. 127.0.0.1 (localhost)
		-PORT 							-port 80 ()
										-ports (1 to 1024) are reserved for CORE PROTOCOLS
										-ports (>1024 to 65535)
		-SOCKETS 						-are programming abstractions for CONNECTIONS 
										-are BI-DIRECTIONAL connections (once they are connected, or ready to transmit)
										-used to SEND and RECEIVE data
										-they implement TCP and UDP protocols 
		-TCP (Transmission Control Protocol)	https://support.holmsecurity.com/hc/en-us/articles/212963869-What-is-the-difference-between-TCP-and-UDP-
										-When you LOAD A WEB PAGE, your computer SENDS TCP PACKETS to the web server’s address, asking it to send the web page to you. 
										-The web server RESPONDS by sending a STREAM of TCP PACKETS, which your WEB BROWSER STITCHES TOGETHER to form the web page and display it to you.
										-TCP guarantees the recipient will receive the PACKETS in order by NUMBERING them.
										-If the sender does not get a correct response, IT WILL RESEND THE PACKETS to ensure the recipient received them. 
										-Packets are also CHECKED FOR ERRORS.
										-TCP is all about this reliability 
											—packets sent with TCP are TRACKED SO NO DATA IS LOST OR CORRUPTED IN TRANSIT.
		-UDP (User Datagram Protocol)	-a DATAGRAM is the same thing as a PACKET of information.
										-UDP protocol works similarly to TCP
											-but it THROWS ALL THE ERROR-CHECKING STUFF OUT. 
										-UDP is used when SPEED IS DESIRABLE
										-and ERROR CORRECTION is not necessary
										-When using UDP, packets are just sent to the recipient. 
											-The sender will not wait to make sure the recipient received the packet 
											— it will just continue sending the next packets. 
											-If you are the recipient and you miss some UDP packets, too bad 
											— you can not ask for those packets again. 
											-There is no guarantee you are getting all the packets 
											-and there is no way to ask for a packet again if you miss it, 
											-but losing all this overhead means the computers can communicate more quickly.
		-PACKETS 						https://computer.howstuffworks.com/question525.htm
										-everything you do on the Internet involves packets
										-every WEB PAGE that you receive comes as a series of packets
										-every E-MAIL you send leaves as a series of packets
										-the network BREAKS AN E-MAIL MESSAGE into PARTS of a certain size IN BYTES
											-*** THIS IS A PACKET ***
										-the sender's IP address, the intended receiver's IP address, 
											-something that tells the network HOW MANY PACKETS this E-MAIL MESSAGE has been 
											-BROKEN INTO AND THE NUMBER of this particular PACKET. 
										-The PACKETS carry the DATA in the PROTOCOLS that the Internet uses: 
											-Transmission Control Protocol/Internet Protocol (TCP/IP)
										-Each PACKET contains PART of the body OF YOUR MESSAGE. 
										-A TYPICAL PACKET contains perhaps 1,000 or 1,500 bytes.
										-PACKETS can be delivered across the NETWORK using the best ROUTE possible (don't all need to take the same route)
										-OTHER NAMES 
											-FRAME
											-BLOCK
											-CELL
											-SEGMENT
		-PACKETS (STRUCTURE)			https://computer.howstuffworks.com/question5251.htm
										-HEADER, PAYLOAD (body), TRAILER(footer)
										HEADER
											-LENGTH OF PACKET (some networks have fixed-length packets, while others rely on the header to contain this information)
											-PACKET NUMBER (which packet this is in a sequence of packets)
											-PROTOCOL (the PROTOCOL DEFINES what TYPE OF PACKET is being transmitted: E-MAIL, WEB PAGE, STREAMING VIDEO)
											-DESTINATION IP ADDRESS (where the packet is going)
											-ORIGINATING IP ADDRESS (where the packet came from)
											-ROUTERS in the network will look at the DESTINATION ADDRESS in the HEADER and compare it to their lookup table to find out where to send the packet
										PAYLOAD 
											-the ACTUAL DATA that the packet is delivering to the destination. 
											-If a packet is FIXED-LENGTH, then the PAYLOAD MAY BE PADDED with blank information to make it the right size.
										TRAILER(footer)
											-typically contains a COUPLE OF BITS that TELL THE RECEIVING DEVICE that it has reached the END OF THE PACKET.
											-It may also have some type of ERROR CHECKING.
		
	SOCKETS (SERVER SIDE)
		socket(family, type)
			family 		socket.AF_INET 
			type 		socket.SOCK_STREAM 		(TCP)
						socket.SOCK_DGRAM 		(UDP)
		bind((host_ip, port))
			-takes a TUPLE (host, port) as input *** THIS IS WHY THE DOUBLE-BRACKETS ***
		listen()
			-starts listening for TCP connections
		accept()
			-accepts a NEW CONNECTION (if found) 
			-RETURNS (a socket OBJECT)
	SOCKETS (CLIENT SIDE)
		connect((host_ip, port))
			-takes a TUPLE (host, port) as input *** THIS IS WHY THE DOUBLE-BRACKETS ***
		recv(buffer)
			-tries to GRAB DATA from a TCP CONNECTION (waits)
		send(bytes)
			-attempts to SEND the BYTES given to it
		close()
			-closes the SOCKET/CONNECTION and frees the PORT
			
	--------------------------------------------------------
	TCP CLIENT (drapstv_socket_TCP_client.py)
	--------------------------------------------------------
	#TCP CLIENT
	#go to folder (in terminal)(powershell) where (*.py) files are...
	#to run (python .\drapstv_socket_TCP_client.py)

	#IMPORTS
	import socket

	#FUNCTION:
	def main():
		host = '127.0.0.1'		#localhost (connecting to...)
		port = 5000

		s = socket.socket()		#creates a new socket object
		s.connect((host, port))		#connect to SERVER

		message = input("-> ")		#raw_input (rename to input())
		while message != 'q': 		#'q' for quit
			#s.send(message)	#send message (down socket) to server
			s.send(message.encode('utf-8'))	#TypeError (a bytes-like object is required, not 'str')
			data = s.recv(1024)
			print("Received from server: " + data.decode('utf-8'))
			message = input("-> ")
		s.close()			#close socket			

	if __name__ == '__main__':
		main()				#run MAIN function
	--------------------------------------------------------
	TCP SERVER (drapstv_socket_TCP_server.py)
	--------------------------------------------------------
	#TCP SERVER 
	#go to folder (in terminal)(powershell) where (*.py) files are...
	#to run (python .\drapstv_socket_TCP_server.py)
	#(note, it will sit and wait (listen) for a client to connect)

	#IMPORTS
	import socket

	#FUNCTION:
	def main():
		host = '127.0.0.1'		#localhost
		port = 5000

		s = socket.socket()		#creates a new socket object
		s.bind((host, port))		#bind the socket (to host)

		s.listen(1)			#only listen (1 connection at a time)

		#c - connection
		#addr - address 
		c, addr = s.accept()
		print("Connection from: " + str(addr))	#print connection (if accepted)
		while True:
			data = c.recv(1024)		#buffer (max 1024 bytes)
			if not data:
				break			#end connection
			print("from connected user: " + str(data))
			#data = str(data).upper()	#convert to UPPERCASE
			data = data.decode('utf-8').upper()	#convert BYTES (back to string)
			print("sending: " + str(data))
			#c.send(data)			#send data
			c.send(data.encode('utf-8'))	#TypeError (a bytes-like object is required, not 'str')
		c.close()				#close

	if __name__ == '__main__':
		main()					#run MAIN function
	--------------------------------------------------------
			
JUL.24, 2018 (CONTROL FLOW, LOOPS, ELSE, ELIF)
	BOOLE (BOOLEAN)
		True or False 
		eg.
			(5 * 2) - 1 == 8 + 1		#True 
			13 - 6 != (3 * 2) + 1		#False
			13 * (2 - 1) == 4 - 1		#True
	
	-check the TYPE 
		my_baby_bool = "true"
		print(type(my_baby_bool))		#<class 'str'>

		my_baby_bool_two = True
		print(type(my_baby_bool_two))	#<class 'bool'>
		
	-how to use a STATEMENT to build a BOOLEAN FUNCTION?
		"If it is raining then bring an umbrella"
		-the BOOLE is "it is raining"		(so you would TURN this into a VARIABLE)
		-it is easier to see this way...
			"IF [it is raining] THEN [bring an umbrella]"
		-statement 
			"it is raining" == True
		-statement 
			if is_raining:
				bring_umbrella()
	
	IF-ELSE (TERNARY FUNCTION)(???want to OPTIMIZE THIS, make a UNIVERSAL TERNARY FUNCTION???)
		#FUNCTION: GREATER_THAN
		def greater_than(x, y):
		  if x > y: return x
		  if x < y: return y
		  if x == y: return "These numbers are the same"
					
		#FUNCTION: CREDITS 
		def graduation_reqs(credits):
		  if credits >= 120: return "You have enough credits to graduate!"
		  
	BOOLEAN EXPRESSIONS (AND, OR, NOT)
		AND (BOTH expressions must be TRUE, to return TRUE)
			<expression1> and <expression2>
			---
			>>> (1 + 1 == 2) and (2 + 2 == 4)
			True
			>>> (1 + 1 == 2) and (2 < 1)
			False
			>>> (1 > 9) and (5 != 6)
			False
			>>> (0 == 10) and (1 + 1 == 1) 
			False							
			
		-----------
		statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

		statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

		def graduation_reqs(gpa, credits):
		  if (credits >= 120) and (gpa >= 2.0):
			return "You meet the requirements to graduate!"
		-----------
		
		OR (EITHER one or other IS TRUE, returns TRUE)
			"Oranges are a fruit or apples are a vegetable"
			[Oranges are a fruit] OR [apples are a vegetable]
			[True] OR [False]			#this will return TRUE (because at least one is true)
			----
			>>> True or (3 + 4 == 7)
			True
			>>> (1 - 1 == 0) or False
			True
			>>> (2 < 0) or True
			True
			>>> (3 == 8) or (3 > 4) 
			False
			----
			
		-----------
		statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

		statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

		#FUNCTION: GRADUATION MAIL (SENT)
		def graduation_mailer(gpa, credits):
		  return (gpa >= 2.0) or (credits >= 120)		
		-----------
							
		NOT (RETURNS THE OPPOSITE of True or False)
			"Oranges are not a fruit"						
			[Oranges are...] NOT [...a fruit]
			[False]					#this will return FALSE (because oranges are a fruit, this statement is incorrect)
			---
			>>> not 1 + 1 == 2
			False
			>>> not 7 < 0
			True
			---
			
		------------
		statement_one = False

		statement_two = True

		#SOLUTION:
		#def graduation_reqs(gpa, credits):
		#  if (gpa >= 2.0) and (credits >= 120):
		#    return "You meet the requirements to graduate!"
		#  if (gpa >= 2.0) and not (credits >= 120):
		#    return "You do not have enough credits to graduate."
		#  if not (gpa >= 2.0) and (credits >= 120):
		#    return "Your GPA is not high enough to graduate."

		def graduation_reqs(gpa, credits):
		  if (gpa >= 2.0) and (credits >= 120):
					return "You meet the requirements to graduate!"
		  elif (gpa >= 2.0) and not (credits >= 120):
					return "You do not have enough credits to graduate."
		  elif not (gpa >= 2.0) and (credits >= 120):
					return "Your GPA is not high enough to graduate."
		  else:
				return "None"
		------------
		
		ELSE (IF, ELIF, ELSE)
			if <condition>:
				#some code (if true)
			elif <condition>:
				#some code (or if this is true)
			else:
				#some code (else false)
			-----
			eg. 
				if weekday:
				  wake_up("6:30")
				else:
				  sleep_in()
			----------------------
			def graduation_reqs(gpa, credits):
				if (gpa >= 2.0) and (credits >= 120):
					return "You meet the requirements to graduate!"
				if (gpa >= 2.0) and not (credits >= 120):
					return "You do not have enough credits to graduate."
				if not (gpa >= 2.0) and (credits >= 120):
					return "Your GPA is not high enough to graduate."
				else:
					return "You do not meet the GPA or the credit requirement for graduation."
			----------------------
			#FUNCTION: CONVERT GPA TO (LETTER GRADE)
			def grade_converter(gpa):
			  if(gpa >= 4.0):
				return "A"
			  elif(gpa >= 3.0):
				return "B"
			  elif(gpa >= 2.0):
				return "C"
			  elif(gpa >= 1.0):
				return "D"
			  elif(gpa >= 0.0):
				return "F"
			  else:
				return "Something went wrong?"
			----------------------
			
		TRY-EXCEPT (ERROR HANDLING)
			try:
				#some code (to test)
			except ErrorName:
				#what to do if the error occurs
			-------------
			def divides(a, b):
				try:
					result = a / b
						print(result)
				except ZeroDivisionError:
					print("Can't divide by zero")

			>>> divides(2, 4)
			0.5
			>>> divides(5, 4)
			1.25
			>>> divides(5, 0)
			Can't divide by zero
			-------------
		
		RAISE (EXECUTES ERROR)
			-------------
			def raises_value_error():
			  raise ValueError
			  
			try:
				raises_value_error()
			except ValueError:
			  print("You raised a ValueError!")
			-------------
			
		REVIEW 
			-reviewed, boolean, if-elif-else, try-except 
			-------------
			def applicant_selector(gpa, ps_score, ec_count):
			  if(gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
				return "This applicant should be accepted."
			  elif(gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
				return "This applicant should be given an in-person interview."
			  else:
				return "This applicant should be rejected."
			-------------
			
		IF-ELSE (ONE function only, executes...)			
			---------
			if(<condition>):
				#func1 
			elif(<condition>):
				#func2 
			else:
				#func3
			---------
		IF-ELSE (ALL, function executes ALL the conditions)
			if(<condition>):
				#func1 
			if(<condition>):
				#func2 
			if(<condition>):
				#func3 
			
JUL.25, 2018 QUIZ (CONTROL FLOW)
	-on boolean, if-elif-else, try-except 
	-6/8 (75%)
	-8/8 (100%) RE-TAKE
				
		
	YOUTUBE 		What Does It Take To Be An Expert At Python?
					https://www.youtube.com/watch?v=7lmCu8wz8ro
					
		--------------------
		data-model.py 		(TO RUN: python -i data-model.py)	
		--------------------
		class Polynomial:
			#INIT
			def __init__(self, *coeffs):			#initialization method 
				self.coeffs = coeffs 				#coeffs (co-efficients)
			
			#FUNCTION: PRINT (repr (REPR esentation))
			def __repr__(self): 
				return 'Polynomial(*{!r})'.format(self.coeffs)
				
			#FUNCTION:	ADDS (individual terms together)
			def __add__(self, other):
				return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))
				
		p1 = Polynomial(1, 2, 3) 		#x² + 2x + 3
		p2 = Polynomial(3, 4, 3)		#3x² + 4X + 3
		--------------------
		python -i data-model.py 
		>>> p1 
		Polynomial(*(1, 2, 3))
		>>> p2 
		Polynomial(*(3, 4, 3))
		>>> p1 + p2
		Polynomial(*(4, 6, 6)
		--------------------
		
	REPR (REPRESENTATION)
		-looks like it's related to EVAL (shows the CODE, not the OUTPUT, as a STRING?)
		-------
		import datetime
		>>> datetime.datetime.now()
		datetime.datetime(2018, 7, 24, 13, 1, 23, 364086)
		>>> str(datetime.datetime.now())
		'2018-07-24 13:01:33.791161'
		>>> repr(datetime.datetime.now())
		'datetime.datetime(2018, 7, 24, 13, 1, 38, 987511)'
		-------	
		
	ASTERISK (IN PARAMETER, of a function)
		-changes HOW THE ARGUMENTS are supplied for say (A LIST, or AN OBJECT)
		https://stackoverflow.com/questions/31197586/difference-call-function-with-asterisk-parameter-and-without
		-------
		#LIST
		arg = [1,2,3]
		func(*arg) == func(1,2,3) variables come out of list(or ther sequence type) as parameters
		func(arg) == func([1,2,3]) a list goes in

		#KEY-VALUE
		kwargs = dict(a=1,b=2,c=3)
		func(kwargs ) == func({'a':1, 'b':2, 'c':3}) a dict goes in
		func(**kwargs ) == func(a=1,b=2,c=3) (key, value) come out of dict(or other mapping type) as named parameters
		-------
		
	JUL.24, 2018 (localhost:8888)
		-I just saw this after having a meltdown and feeling anxiety around looking for work
		-this is a lucky number ...
		-abundance x10, find my greatest sense of purpose (and follow that)
		-through your mindset of abundance the universe will reward you
		
	JUL.24 (YOUTUBE - CORY SCHAFER)		https://www.youtube.com/watch?v=ZDa-Z5JzLYM
		-PYTHON TUTORIAL 1 (CLASSES AND INHERITANCE)
			-METHOD, function associated with a CLASS
		CLASS 
			class Employee:
				pass 			#Python with skip this (like rough in...)
									
		-CLASS variable 
		-CREATE INSTANCES 

		-INSTANCE variable (this is inefficient, we'll use __init__ METHOD instead)
			#create instances
				emp1 = Employee()
				emp2 = Employee()
			#add properties
				emp1.first = 'Corey'
				emp1.lastname = 'Schafer'
				emp1.email = 'email.@company.com'
				print(emp1.email)
				
		-METHOD INIT 
			#initialize 
			class Employee:
				def __init__(self, fname, lname, pay):
					self.fname = fname 
					self.lname = lname 
					self.pay = pay 
					self.email = fname + '.' + lname + '@company.com'
			#this will INSTANTIATE the objects (with the VALUE in one line)
			emp1 = Employee('Corey', 'Schafer', 50000)
			emp2 = Employee('Test', 'User', 60000)
		
	JUL.25, 2018 PROJECT: SAL'S SHIPPING
		-done, see file...
			"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\03-Control Flow (logic)\
				proj2_sals_shipping.py"
		------------
		#SAL'S SHIPPING
		#PROJECT #2
		#CODE ACADEMY 
		#PROGRAMMING WITH PYTHON 
		#Dean Jones, Jul.25, 2018

		#----------------
		# Ground Shipping
		# Weight of Package	                                Price per Pound	    Flat Charge
		# 2 pounds or less  	                            $1.50               $20.00
		# Over 2 pounds but less than or equal to 6 pounds	$3.00	            $20.00
		# Over 6 pounds but less than or equal to 10 pounds	$4.00	            $20.00
		# Over 10 pounds	                                $4.75	            $20.00

		# Drone Shipping
		# Weight of Package	                                Price per Pound	    Flat Charge
		# 2 pounds or less	                                $4.50	            $00.00
		# Over 2 pounds but less than or equal to 6 pounds	$9.00	            $00.00
		# Over 6 pounds but less than or equal to 10 pounds	$12.00	            $00.00
		# Over 10 pounds	                                $14.25	            $00.00

		# Premium Ground Shipping
		# Flat charge: $125.00
		#----------------

		#FUNCTION: CURRENCY FORMAT
		def currency(num):
		  return '${:,.2f}'.format(num)

		#FUNCTION: CALC COST (helper function)
		def calc_cost(price_per_pound, weight, flat_fee):
		  return (price_per_pound * weight) + flat_fee

		#FUNCTION: COST (GROUND SHIPPING)
		#They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. 
		def cost_ground_shipping(weight):
		  if (weight <= 2.0):
			return calc_cost(1.50, weight, 20.00)
		  elif (weight <= 6.0):
			return calc_cost(3.00, weight, 20.00)
		  elif (weight <= 10.0):
			return calc_cost(4.00, weight, 20.00)
		  elif (weight > 10.0):
			return calc_cost(4.75, weight, 20.00)
		  else:
			return "Error: cost_ground_shipping() function"
		#TEST: cost_ground_shipping(8.4)
		#53.6  
		print("Ground Shipping: 8.4lbs should be $53.60")
		print(cost_ground_shipping(8.4))
		#formatted with function
		print(currency(cost_ground_shipping(8.4)))
		  
		  
		#VARIABLE: COST (PREMIUM SHIPPING)
		#Premium ground shipping, which is a much higher flat charge, but you aren't charged for weight.
		flat_fee_premium_shipping = 125.00

		#FUNCTION: COST (DRONE SHIPPING)
		#They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
		def cost_drone_shipping(weight):
		  if (weight <= 2.0):
			return calc_cost(1.50 * 3, weight, 0.00)
		  elif (weight <= 6.0):
			return calc_cost(3.00 * 3, weight, 0.00)
		  elif (weight <= 10.0):
			return calc_cost(4.00 * 3, weight, 0.00)
		  elif (weight > 10.0):
			return calc_cost(4.75 * 3, weight, 0.00)
		  else:
			return "Error: cost_drone_shipping() function"
		#TEST: cost_drone_shipping(1.5)
		#6.75  
		print("Drone Shipping: 1.5lbs should be $6.75")
		print(cost_drone_shipping(1.5))
		#formatted with function
		print(currency(cost_drone_shipping(1.5)))

		#ENUM (for shipping)
		#from enum import Enum
		#class ShippingType(Enum):
		#	GROUND = 1
		#  PREMIUM = 2
		#  DRONE = 3
		  
		#FUNCTION: FIND CHEAPEST (SHIPPING METHOD)
		def find_cheapest_shipping(weight):
		  result = ""
		  a = cost_ground_shipping(weight)
		  a_currency = currency(a)
		  a_message = "Grounding is the cheapest, costing: {}".format(a_currency)
		  b = flat_fee_premium_shipping
		  b_currency = currency(b)
		  b_message = "Premium is the cheapest, costing: {}".format(b_currency)
		  c = cost_drone_shipping(weight)
		  c_currency = currency(c)
		  c_message = "Drone is the cheapest, costing: {}".format(c_currency)
		  
		  #compare (a and b)
		  if(a < b):		#means (can't be b)
			#compare (a and c)
			if(a < c):
			  #print a
			  result = a_message
			else:
			  #print c
			  result = c_message
		  elif(a > b):	#means (can't be a)
			#compare (b and c)
			if(b < c):
			  #print b
			  result = b_message
			else:
			  #print c
			  result = c_message
		  return result
		#TEST: find_cheapest_shipping(1.5)
		print("Cheapest Shipping for: 1.5lbs")
		print(find_cheapest_shipping(1.5))
		#TEST: find_cheapest_shipping(4.8)
		print("Cheapest Shipping for: 4.8lbs")
		print(find_cheapest_shipping(4.8))
		#TEST: find_cheapest_shipping(41.5)
		print("Cheapest Shipping for: 41.5lbs")
		print(find_cheapest_shipping(41.5))		
		------------
	
	
		ENUM 		https://docs.python.org/3/library/enum.html
			-enum, are created from a class 
			---------
			from enum import Enum
			class Color(Enum):
				RED = 1
				GREEN = 2
				BLUE = 3
			---------
			#implementation 
			print(Color.RED)
			#Color.RED
			---------	
			>>> class ShippingType(Enum):
			...     GROUND = 1
			...     PREMIUM = 2
			...     DRONE = 3
			>>> print(ShippingType.GROUND)
			ShippingType.GROUND
			>>> print(ShippingType.GROUND.value)
			1			
										
	JUL.25, 2018
		BOOK - PYTHON THE HARD WAY (ex7.py) 
		-----------------
		print("Mary had a little lamb.")
		print("It\'s fleece was white as {}.".format('snow'))
		print("And everwhere that Mary went.")
		print("." * 10) #this repeats the period (x10)

		end1 = "C"
		end2 = "h"
		end3 = "e"
		end4 = "e"
		end5 = "s"
		end6 = "e"
		end7 = "B"
		end8 = "u"
		end9 = "r"
		end10 = "g"
		end11 = "e"
		end12 = "r"

		#watch end = ' ' at the end. try removing it and see what happens
		print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
		print(end7 + end8 + end9 + end10 + end11 + end12)	#end = ' ' (suppresses NEWLINE? interesting)

		print(end1 + end2 + end3 + end4 + end5 + end6)		#end = ' ' (removed)
		print(end7 + end8 + end9 + end10 + end11 + end12)	
		-----------------
		ex8.py 
		my_format = "{} {} {} {}"

		print(my_format.format(1, 2, 3, 4))
		print(my_format.format("one", "two", "three", "four"))
		print(my_format.format(True, False, False, True))
		print(my_format.format(my_format, my_format, my_format, my_format))
		print(my_format.format(
			"Roses are red", 
			"Violets are blue",
			"I am awesome", 
			"And you are too :)"
		))

		my_format = "{} + {} + {} + {}"					#'+' added
		#EVAL (turns '+' into CONCAT)
		print(eval(my_format.format(1, 2, 3, 4)))			#10
		#print(eval(my_format.format("one", "two", "three", "four")))	#doesn't EVAL
		print(eval(my_format.format("1", "2", "3", "4")))		#10
		-----------------
		
	JUL.25 CODE ACADEMY
		------------------
		#FUNCTION: IN RANGE (and equal to limits)
		def in_range(num, lower, upper):
		  return lower <= num <= upper

		#FUNCTION: IN RANGE (and NOT equal to limits)
		def in_range2(num, lower, upper):
		  return lower < num < upper

		#TEST
		print(in_range(10, 10, 10))		#True
		print(in_range(5, 10, 20))		#False
		------------------		
		#FUNCTION: MOVIE REVIEW
		def movie_review(rating):
		  if (rating <= 5):
			return "Avoid at all costs!"
		  elif (rating < 9):
			return "This one was fun."
		  elif (9 <= rating):
			return "Outstanding!"
		  else:
			return "movie_review() failed"

		#TEST
		print(movie_review(9))	# should print "Outstanding!"
		print(movie_review(4))	# should print "Avoid at all costs!"
		print(movie_review(6))	# should print "This one was fun."		
		------------------
		#FUNCTION: TWICE AS LARGE 
		def twice_as_large(num1, num2):
		  return num1 > (num2 * 2)

		#TEST
		print(twice_as_large(10, 5))		#False
		print(twice_as_large(11, 5))		#True
		------------------
		#FUNCTION: POWER (is greater than 5000)
		def large_power(base, exponent):
		  return (base ** exponent) > 5000

		#TEST
		print(large_power(2, 13))		#True (2^13 = 8192)
		print(large_power(2, 12))		#False (2^12 = 4096)
		------------------
		#FUNCTION: DIVISIBLE BY TEN
		def divisible_by_ten(num):
		  return num % 10 == 0		#mod will equal 0 if divisible

		#TEST
		print(divisible_by_ten(20))		#True
		print(divisible_by_ten(25))		#False
		------------------
		#FUNCTION: MAX NUMBER
		def max_num(a, b, c):
		  #need to test (for equals) first
		  if (a == b) or (a == c) or (b == c):
			return "It's a tie!"
		  elif (a <= b >= c):
			return b
		  elif (c <= a >= b):
			return a
		  elif (b <= c >= a):
			return c
		  else:
			return "max_num failed"
				
		#TEST
		print(max_num(-10, 0, 10))		#max is 10
		print(max_num(-10, 5, -30))		#max is 5
		print(max_num(-5, -10, -10))	#print "it's a tie"
		print(max_num(2, 3, 3))				#print "it's a tie"
		------------------
		#FUNCTION: OVER BUDGET 
		def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
		  return budget < (food_bill + electricity_bill + internet_bill + rent)

		#TEST
		print(over_budget(100, 20, 30, 10, 40))		#False
		print(over_budget(80, 20, 30, 10, 30))		#True
		------------------
		#FUNCTION: ALWAYS FALSE (CONTRADICTION)
		def always_false(num):
			return num < num > num		#*** watch the NAMES are the same ***

		#CONTRADICTION? (when an IF-STATEMENT always returns false)

		#TEST
		print(always_false(0))		#FALSE
		print(always_false(-1))		#FALSE
		print(always_false(1))		#FALSE
		------------------
		#FUNCTION: NOT EQUAL (to 10)
		def not_sum_to_ten(num1, num2):
		  return (num1 + num2) != 10
		  
		#TEST
		print(not_sum_to_ten(9, -1))		#True
		print(not_sum_to_ten(9, 1))			#False
		print(not_sum_to_ten(5,5))			#False
		------------------
		#FUNCTION: SAME NAME 
		def same_name(your_name, my_name):
		  return your_name == my_name

		#TEST
		print(same_name("Colby", "Colby"))		#True
		print(same_name("Tina", "Amber"))			#False
		------------------
		
	JUL.26, 2018 (UNIT 2)(WEEK 3, DAY 3) 
		INSTALLING PYTHON 
		JUPYTER (EDITOR)			(local web application, to create python files)
		ANACONDA ??? 
		MINICONDA ???
		DEBUGGING PYTHON ??? HOW TO ?
		PIP3 (???)(What is this?)(for installing Python additions?)
			(PIP3 VS CONDA)
			
		ANACONDA
			-is a large-scale data analytics distribution 
			-provided by CONTINUUM ANALYTICS INC
			-many tools for LARGE SETS OF DATA 
				-includes...
					-Python core language 
					-over 1000 data science packages 
					-package management (with CONDA)
					-IPython (??? what is this?)(IDE?)
					-and more...
		MINICONDA 
			-lite version (of ANACONDA) 
			-also includes Python language
			-a much smaller download 
			-basic requirements 
			-can INSTALL packages as needed 
			
JUL.29, 2018 (CUSTOMER SERVICE BOT: JUPITER PROJECT)
	-download ZIP
	-OPEN in JUPYTER NOTEBOOK (for instructions)
	
	DATE FUNCTION 
	
	import datetime
	#FUNCTION: HOME VISIT (GET DATE)
	def home_visit_get_date():
			year = int(input('\t\tPlease enter a year: '))
			#year: 2018
			month = int(input('\t\tPlease enter a month: '))
			#month: 07
			day = int(input('\t\tPlease enter a day: '))
			#day: 30

			print('')
			#validate date
			try:
				home_visit_date = datetime.date(year, month, day)
				return home_visit_date
			except ValueError:
				print('\t\tPROBLEM -------------------------------------------')
				print('\t\tThe date you entered was invalid, please try again.')
				home_visit_get_date()      #try again
	
	
	
	
JUL.30, 2018 (BOOK - PYTHON THE HARD WAY)(p.48)
	READING FILES 
	ARGV (used for command prompt)
		import sys 
		print("sys.argv: ", sys.argv)			#sys.argv:  ['.\\ex15.py']		#first argument is the SCRIPT FILENAME
		
	#------------------------------
	# EX15.PY
	#------------------------------
	#READING FILES 
	#JUL.30, 2018

	#**********************************************************************************
	# We want to ASK THE USER (the filename) rather than HARD CODING the filename here.
	#**********************************************************************************

	# TO RUN...
	# -make sure to EXECUTE (with parameter TO SAMPLE.TXT file)
	# python '.\ex15.py' .\ex15_sample.txt

	#SEE WHAT (sys.argv) IS?
	#import sys						
	#print("sys.argv: ", sys.argv)				#sys.argv:  ['.\\ex15.py', '.\\ex15_sample.txt']
						
	from sys import argv 					#import
	script, filename = argv 				#assign arguments (script needs 2 arguments)(python '.\ex15.py' .\ex15_sample.txt)

	txt = open(filename)

	#PRINT FILE
	print(f"Here's your file {filename}:")	#"Here is your file .\ex15_sample.txt
	print(txt.read())						#prints the file

	#-------------------
	#ASK FOR (USER INPUT)
	print("************************")
	print("Type the filename again:")
	file_again = input("> ")				#input (ex15_sample.txt)

	txt_again = open(file_again)			#opens the (file you typed in)

	print(txt_again.read())					#prints the file
	#------------------------------
	# EX15B.PY
	#------------------------------
	#READING FILES 
	#JUL.30, 2018

	#**********************************************************************************
	# We want to ASK THE USER (the filename) rather than HARD CODING the filename here.
	#**********************************************************************************

	# TO RUN...
	# -make sure to EXECUTE (with parameter TO SAMPLE.TXT file)
	# python '.\ex15.py' .\ex15_sample.txt
						
	import sys						
	print("sys.argv: ", sys.argv)				#sys.argv:  ['.\\ex15.py', '.\\ex15_sample.txt']
	print("---------------------")

	#PRINT FILE
	with open(sys.argv[1], 'r') as my_file:		#READS (2nd argument)('.\\ex15_sample.txt')
		print(my_file.read())

	print("---------------------")
	#------------------------------		

AUG.01, 2018 (WEEK 4)
	LISTS 
	----------------------
	heights = [61, 70, 67, 64]
	heights.append(65)				#appends to (end of list)

	broken_heights = [65, 71, 59, 62]

	#list constructor
	x = list((1,2,3))
	print(x)
	----------------------
	#MIXED LIST (different data types)
	ints_and_strings = [1, 2, 3, 'four', 'five', 'six', "seven"]
	print(ints_and_strings)

	sam_height = ['Sam', 67]
	print(sam_height)
	----------------------
	#LIST OF LISTS (lists as data type)(2d array)
	heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

	ages = [['Aaron', 15], ['Dhruti', 16]]
	----------------------
	#ZIP (create a LIST OF LISTS)
	names = ['Jenny', 'Alexus', 'Sam', 'Grace']
	dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

	names_and_dogs_names = zip(names, dogs_names)
	print(list(names_and_dogs_names))

	#[('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]	
	----------------------
	#EMPTY LIST 
	my_empty_list = []
	----------------------
	#APPEND
	orders = ['daisies', 'periwinkle']

	orders.append('tulips')
	orders.append('roses')
	print(orders)
	----------------------
	#CONCATENATION (+)
	orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

	# Create new orders here:
	new_orders = orders + ['lilac', 'iris']

	#broken_prices = [5, 3, 4, 5, 4] + 4
	broken_prices = [5, 3, 4, 5, 4] + [4]
	----------------------	
	#RANGE
	list1 = range(9)
	range1 = range(8)

	print(range1)
	print(list(range1))
	----------------------
	#RANGE (START, MAX, COUNT_BY)
	list1 = range(5, 15, 3)
	print(list(list1))		#[5, 8, 11, 14]

	list2 = range(0, 40, 5)
	print(list(list2))		#[0, 5, 10, 15, 20, 25, 30, 35]
	----------------------
	#REVIEW (LIST AND RANGE)

	first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
	print(first_names)				#['Ainsley', 'Ben', 'Chani', 'Depak']

	#empty list 
	age = []
	print(age)						#[]

	#append 
	age.append(42)
	print(age)						#[42]

	#concatenation (+)
	all_ages = age + [32, 41, 29]
	print(all_ages)					#[42, 32, 41, 29]

	#zip 
	name_and_age = zip(first_names, all_ages)
	print(name_and_age)				#<zip object at 0x7f77726c4488>
	print(list(name_and_age))		#[('Ainsley', 42), ('Ben', 32), ('Chani', 41), ('Depak', 29)]

	#range 
	ids = range(4)
	print(ids)						#range(0, 4)
	print(list(ids))				#[0, 1, 2, 3]	
	----------------------
	QUIZ#3 LISTS 
		9/9 (100%)
		
	AUG.01, 2018 (PROJECT - BUILD A GRADEBOOK)
	--------------------------------------------------
	# BUILD A GRADEBOOK (WEEK 4, DAY 3)
	#PROJECT #4
	#CODE ACADEMY 
	#PROGRAMMING WITH PYTHON 
	#Dean Jones, Aug.01, 2018

	# Build a Gradebook
	# In this project, you will act as a student and create a gradebook to keep track of some 
	# of the subjects you've taken and grades you have received in them. To complete the project, 
	# you will need to understand how to create and combine lists, and how to add elements. 
	# On the way, you'll refresh your knowledge of basic Python syntax. If you get stuck or confused, 
	# remember that your Slack community is there to help!

	# This project is not graded and you do not need to submit it anywhere. 
	# If you would like to check your results, the solution code can be found here.


	#FUNCTION: ADD SUBJECT 
	def add_subject(subject, grade):
	  subjects.append(subject)
	  grades.append(grade)
	  
	#FUNCTION: CREATE LISTS (COMBINE)(subjects and grades)
	def list_subjects_and_grades(list_subjects, list_grades):
	  #return zip(list_subjects, list_grades)		#***WARNING, causes empty list
	  return list(zip(list_subjects, list_grades))
	  
	#FUNCTION: PRINT GRADES
	def print_grades(message, list_grades):
	  #print(message, list(zip_grades))
		print(message, list_grades)
	  
	#--------------------

	#old grades
	last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

	#LISTS
	subjects = ['physics', 'calculus', 'poetry', 'history']
	grades = list((98, 97, 85, 88))		#alternate method
	#grades = [98, 97, 85, 88]

	#(see ADD SUBJECT)
	#APPEND (new subject and grade)
	#subjects.append("computer science")
	#grades.append(100)

	#add subject
	add_subject('computer science', 100)  #100% wow!
	add_subject('visual art', 93)

	#ZIP (subjects with grades)
	gradebook = list_subjects_and_grades(subjects, grades)


	#gradebook = zip(subjects, grades)
	print_grades("Gradebook: ", list(gradebook))
	#print("gradebook: ", list(gradebook))

	#FULL GRADES (this semester and last)
	full_gradebook = last_semester_gradebook + gradebook

	#print("full gradebook: ", list(full_gradebook))
	print_grades("Full Grades: ", full_gradebook)
	--------------------------------------------------
	
	AUG.02, 2018 
	PYTHON - LISTS II 
	-----------------------------
	#LENGTH (OF LIST)
	#list1 = range(2, 20, 2)
	list1 = range(2, 20, 3)
	list1_len = len(list1)

	print(list(list1))
	print("There are {} elements in this list".format(list1_len))		
	-----------------------------
	#INDEX (SELECT AN ELEMENT)
	employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

	index4 = employees[4]
	print(index4)
	print("There are {} elements in this list".format(len(employees)))

	#SELECT (FIRST IN LIST)
	print("First element:", employees[0])
	#SELECT (LAST IN LIST)
	#NOTE, the (-)(negative) sign indexes in reverse
	print("Last element:", employees[-1])
	#SELECT (SECOND LAST ELEMENT)
	print("2nd last element:", employees[-2])
	#ERROR (IndexError)(INDEX OUT OF RANGE) 
	print(employees[-4])		
	-----------------------------
	#LAST ELEMENT
	shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

	print("Length: ", len(shopping_list))
	#last element
	last_element = shopping_list[-1]
	print("Last element: ", last_element)
	#5th element (same as last)
	element5 = shopping_list[5]
	print("5th element: ", element5)
	-----------------------------
	#SLICING (breaking up list into PARTS)
	#COLON (:) (TO CREATE A RANGE)(SUBSET OF LIST)
	#SYNTAX (my_list[<start_index>:<one_less_end_index>])
	suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

	beginning = suitcase[0:4]
	print(beginning)

	#new list 
	middle = suitcase[2:-2]
	print("middle two elements: ", middle)

	test = suitcase[1:-1]
	print(test)
	-----------------------------
	#MORE SLICING
	suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

	start = suitcase[:3]	#first 3 elements
	print("start: ", start)

	end = suitcase[-2:]
	print("end: ", end)

	#play
	test = ["one", "two", "three", "four", "five", "six"]
	#when starting at (0 index)(you can OMIT the index)
	print(test[:3])		#first 3 elements
	print(test[2:])		#start at (2nd element)(to end of list)
	print(test[-3:])	#last 3 elements
	-----------------------------
	#COUNT (how many times ELEMENT appears IN LIST)
	votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

	jake_votes = votes.count('Jake')
	print("Jakes votes: ", jake_votes)
	-----------------------------
	#SORT LIST
	#NOTE, sort DOES NOT RETURN a value 

	### Exercise 1 & 2 ###
	addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

	# Sort addresses here:
	addresses.sort()
	print("addresses: ", addresses)

	### Exercise 3 ###
	names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
	#ERROR: NameError: name 'sort' is not defined
	#sort(names)
	names.sort()
	print("names: ", names)

	### Exercise 4 ###
	cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

	sorted_cities = cities.sort()						#None?
	print("sorted_cities: ", sorted_cities)	#sorted_cities:  None
	print("cities: ", cities)
	-----------------------------
	#SORTED (NOT the same as <list>.sort())
	#SYNTAX (sort(my_list))
	games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

	games_sorted = sorted(games)
	print("sorted games: ", games_sorted)
	-----------------------------
	-----------------------------
	#REVIEW
	inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

	#LENGTH
	inventory_len = len(inventory)
	print("Length of inventory list: ", inventory_len)

	#SELECT (FIRST ELEMENT)
	first = inventory[0]
	print("Inventory list (first element): ", first)

	#SELECT (LAST ELEMENT)
	last = inventory[-1]
	print("Inventory list (last element): ", last)

	#SLICE (GET A SUBSET) OF LIST
	inventory_2_6 = inventory[2:6]
	print("Subset(2 to 6): ", inventory_2_6)

	#SLICE (FIRST 3 ELEMENTS)
	first_3 = inventory[:3]
	print("First 3 elements: ", first_3)

	#COUNT (HOW MANY OF ELEMENT)
	twin_beds = inventory.count('twin bed')
	print("Count (twin beds): ", twin_beds)

	#SORT 
	inventory.sort()
	print("Sort: ", inventory)

	#--------------
	print("-" * 20)

	#MY SHORTER VERSION OF THE SAME CODE
	#FUNCTION: HELPER (FUNCTION, PRINT)
	def helper(message, func):
	  temp = func
	  print(message, temp)

	#LENGTH
	helper("Length of inventory list: ", len(inventory))
	#SELECT (FIRST ELEMENT)
	helper("Inventory list (first element): ", inventory[0])
	#SELECT (LAST ELEMENT)
	helper("Inventory list (last element): ", inventory[-1])
	#SLICE (GET A SUBSET) OF LIST
	helper("Subset(2 to 6): ", inventory[2:6])
	#SLICE (FIRST 3 ELEMENTS)
	helper("First 3 elements: ", inventory[:3])
	#COUNT (HOW MANY OF ELEMENT)
	helper("Count (twin beds): ", inventory.count('twin bed'))
	#SORT 
	helper("Sort: ", sorted(inventory))
	-----------------------------
	-----------------------------
	AUG.02, 2018 
	QUIZ#4 PYTHON LISTS II 
		7/8 (87%)
		8/8 (100%) RE-TAKE 
		
	-----------------------------
	AUG.03, 2018
	LISTS - CODE CHALLENGE (WEEK 5, DAY 2)
	-----------------------------
	#FUNCTION: DOUBLE INDEX 
	def double_index(lst, index):
	  if (index < len(lst)):
		return 2 * lst[index]
	  else:
		return lst
	  
	#FUNCTION: DOUBLE INDEX 
	def double_index2(lst, index):
		try:
			return 2 * lst[index]
		except IndexError:
			return "Except IndexError..."
		except:
			return "Except..."
	  
	#TEST
	print(double_index2([1,2], 2))
	print(double_index2([3, 8, -10, 12], 2))
	print("-" * 20)
	#TEST
	print(double_index([1,2], 2))
	print(double_index([3, 8, -10, 12], 2))

	#SOLUTION
	#Write your function here
	#def double_index(lst, index):
	#  if index < len(lst):
	#  	lst[index] = lst[index] * 2
	#  return lst

	#Uncomment the line below when your function is done
	#print(double_index([3, 8, -10, 12], 2))
	-----------------------------
	#FUNCTION: REMOVE MIDDLE 
	def remove_middle(lst, start, end):
	  return lst[:start] + lst[end + 1:]

	#TEST
	print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))	#[4, 23, 42]
	-----------------------------
	#FUNCTION: ELEMENT (appears MORE THAN)(n times)
	def more_than_n(lst, item, n):
	  return lst.count(item) > n

	#TEST
	print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) #True
	print(more_than_n(["a", "a", "a", "b", "b", "c"], "a", 2)) #True
	print(more_than_n(["a", "a", "a", "b", "b", "c"], "a", 3)) #False
	-----------------------------
	#FUNCTION: MORE FREQUENT ITEM
	def more_frequent_item(lst, item1, item2):
	  if lst.count(item2) > lst.count(item1):
		return item2
	  else:
		return item1

	#TEST
	print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
	-----------------------------
	#FUNCTION: MIDDLE TERM
	def middle_element(lst):
	  len_lst = len(lst)
	  if len_lst % 2 == 1: 	#odd (get middle element)
		#get middle item
		mid_item = len_lst // 2
		return lst[mid_item]
	  else:									
		#even elements (get average)
		mid2 = len_lst // 2
		mid1 = mid2 - 1
		avg = (lst[mid1] + lst[mid2]) / 2
		return avg

	#TEST
	print(middle_element([5, 2, -4, 4, 5]))				#-4
	print(middle_element([5, 2, -10, -4, 4, 5]))		#-7.0
	-----------------------------
	#FUNCTION: APPEND SUM (FIBONACCI)
	def append_sum(lst):
	  lst.append(lst[-1] + lst[-2])
	  lst.append(lst[-1] + lst[-2])
	  lst.append(lst[-1] + lst[-2])
	  return lst
	  
	#FUNCTION: SUM LAST TWO (FIBONACCI)
	def fib_sum(lst):
	  lst.append(lst[-1] + lst[-2])
	  return lst

	#TEST
	print(append_sum([1, 1, 2]))	#[1, 1, 2, 3, 5, 8]

	lst2 = [1, 1]
	#HOW CREATE REPEAT FUNCTION?
	fib_sum(lst2)
	fib_sum(lst2)
	fib_sum(lst2)
	fib_sum(lst2)
	print(lst2)			#[1, 1, 2, 3, 5, 8]
	-----------------------------
	#FUNCTION: LARGER LIST (LAST ELEMENT)
	def larger_list(lst1, lst2):
	  if len(lst1) < len(lst2):
		return lst2[-1]
	  else:
		return lst1[-1]

	#TEST
	print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
	print(larger_list([1, 3, 4], [0, -1, 3, 99]))
	print(larger_list(["ONE", "two", "three"], [-10, 2, 5]))
	-----------------------------
	#FUNCTION: COMBINE SORT 
	def combine_sort(lst1, lst2):
	  return sorted(lst1 + lst2)

	#TEST
	print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) 			#[-10, 2, 2, 4, 5, 5, 10, 10]
	-----------------------------
	#FUNCTION: APPEND SIZE 
	def append_size(lst):
	  #temp = 0
	  #for x in lst:
	  #  temp = temp + x
	  #temp = sum(range(0, len(lst) + 1))
	  temp = list(range(1, len(lst) + 1))
	  lst = lst + temp
	  return lst

	#TEST
	print(append_size([23, 42, 108]))
	-----------------------------
	#FUNCTION: EVERY THREE NUMS 
	def every_three_nums(start):
	  return list(range(start, 101, 3))

	#TEST
	print(every_three_nums(91))
	-----------------------------
	
	AUG.03, 2018 LOOPS 
	-----------------------------
	#LOOP (FOR LOOP)
	dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

	for breed in dog_breeds:
	  print(breed)
	-----------------------------
	#BOARD GAMES
	board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

	for game in board_games:
		print(game)
	  
	print("-" * 20)
	  
	#SPORT GAMES
	sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

	for game in sport_games:
	  print(game)
	-----------------------------
	#LOOP (RANGE)
	promise = "YOU ARE LOVED"

	for i in range(5):
	  print(promise)
	-----------------------------
	students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
	students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

	#CAREFUL (INFINITE LOOP)
	#lst = [1, 2, 3]
	#for x in lst:
	#  lst.append(1)		#*** WARNING, infinite loop ***


	#LOOP (ADD ONE LIST TO ANOTHER)
	#print(students_period_B + students_period_A)		#same as concat two lists
	for student in students_period_A:
	  students_period_B.append(student)
	  print(student)

	print("A: ", students_period_A)
	print("B: ", students_period_B)
	-----------------------------
	#LOOP (BREAK) (use this to LEAVE the loop)
	dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
	dog_breed_I_want = 'dalmation'

	#LOOP 
	for dog in dog_breeds_available_for_adoption:
	  print(dog)
	  if dog == dog_breed_I_want:
		print('They have the dog I want!')
		break			#STOPS (after finding this element)
	#french_bulldog
	#dalmation
	#They have the dog I want!
	-----------------------------
	#LOOP (CONTINUE) (continue after skipping something)
	ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

	for age in ages:
	  if age < 21:
		continue
	  print(age)
	-----------------------------
	#LOOP (WHILE)(use when you DON'T KNOW how many loops are required)
	all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
	students_in_poetry = []

	#WHILE
	num = 0							#need (counter)		
	while num != 6:			#test (counter)
	  students_in_poetry.append(all_students.pop())
	  num += 1					#increment (counter)
	  
	print("Poetry class: ", students_in_poetry)
	print(students_in_poetry)
	-----------------------------
	#NESTED LOOPS (LOOP inside a loop)
	sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

	scoops_sold = 0
	for location in sales_data:
	  print(location)
	  for i in location:
		scoops_sold += i
		
	print("How many scoops sold?: ", scoops_sold)
	-----------------------------
	#LIST COMPREHENSION
	#WEB SCRAPPING
	words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
	usernames = []
	usernames2 = []

	#LONG 
	for word in words:
	  if word[0] == '@':
		usernames.append(word)
		
	#SHORTHAND (LIST COMPREHENSION)
	usernames2 = [word for word in words if word[0] == '@']
	#SHORTHAND (syntax)
	#  <output> <for X in MY_LIST> <condition_to_test>
	#  http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
	  
	print(usernames)		#['@coolguy35', '@kewldawg54', '@matchamom']
	print(usernames2)

	#-----------
	#examples 
	lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	tmp = [x for x in lst if x % 2 == 0]
	print("tmp: ", tmp)		#tmp:  [2, 4, 6, 8, 10]
	tmp2 = [x * 2 for x in lst if x % 2 == 0]
	print("tmp2: ", tmp2)	#tmp2:  [4, 8, 12, 16, 20]

	#-----------------------------
	heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
	can_ride_coaster = [e for e in heights if e > 161]
	print("can ride: ", can_ride_coaster)
	-----------------------------
	#LIST COMPREHENSION
	celsius = [0, 10, 15, 32, -5, 27, 3]

	#CONVERT (CELSIUS TO FAHRENHEIT)
	fahrenheit = [temp * 9/5 + 32 for temp in celsius]
	print("degF: ", fahrenheit)
	#degF:  [32.0, 50.0, 59.0, 89.6, 23.0, 80.6, 37.4]
	-----------------------------
	#REVIEW LOOPS 
	single_digits = range(0, 10)
	for x in single_digits:
	  print(x)
	  
	#SQUARES
	squares = []
	for x in single_digits:
	  squares.append(x ** 2)
	print("squares: ", squares)  #squares:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

	#CUBES
	cubes = [x ** 3 for x in single_digits]
	print("cubes: ", cubes)  #cubes:  [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
	-----------------------------
	
	AUG.03, 2018 QUIZ (LOOPS)
		7/9 (77%), got CONTINUE and BREAK mixed up a bit 
			BREAK (doesn't UP TO)
			CONTINUE (SKIPS)
		9/9 (100%) RE-TAKE
		
	AUG.05, 2018 (BOOK: PYTHON THE HARD WAY)
		ex.10.py 
		
	AUG.06, 2018 PROJECT - CARLY'S CLIPPERS (WEEK 5, DAY 3)
		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\06-Project (Carlys Clippers)\
			proj6_carlys_clippers.py"
		
??? CHAIN METHODS?
	-can I do this with a FUNCTION, or do I need to make a CLASS?
	
	AUG.06 CODE CHALLENGE 
		-------------------------
		#FUNCTION: DIVISIBLY BY TEN (GET LENGTH OF LIST)
		def divisible_by_ten(nums):
		  return len([x for x in nums if x % 10 == 0])

		#TEST
		print(divisible_by_ten([20, 25, 30, 35, 40]))
			#returns 3
		-------------------------
		#FUNCTION: GREETINGS
		def add_greetings(names):
		  return ["Hello, " + x for x in names]

		#TEST
		print(add_greetings(["Owen", "Max", "Sophie"]))
			#['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
		-------------------------
	AUG.07 (CONTINUE...)
		#FUNCTION: DELETE STARTING (EVEN NUMBERS)
		def delete_starting_evens(lst):
		  #return [lst[lst.index(x):] for x in lst if x % 2 == 1]
		  while (len(lst) > 0 and lst[0] % 2 != 1):
			lst = lst[1:]
		  return lst

		#TEST
		print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
		print(delete_starting_evens([4, 8, 10]))

		#SOLUTION 
		#def delete_starting_evens(lst):
		#  while (len(lst) > 0 and lst[0] % 2 == 0):
		#    lst = lst[1:]
		#  return lst
		-------------------------
		#FUNCTION: ODD INDICES
		def odd_indices(lst):
		  return lst[1::2]	#start at ODD index, count by TWO

		#TEST
		print(odd_indices([4, 3, 7, 10, 11, -2]))
		#[3, 10, -2]
		-------------------------
		#FUNCTION: EXPONENTS 
		def exponents(bases, powers):
		  result = []
		  for b in bases:
			for p in powers:
			  result.append(b ** p)
		  return result

		#TEST
		print(exponents([2, 3, 4], [1, 2, 3]))
		#[2, 4, 8, 3, 9, 27, 4, 16, 64]
		-------------------------
		#FUNCTION: LARGER SUM 
		def larger_sum(lst1, lst2):
		  lst1_sum = sum(lst1)
		  lst2_sum = sum(lst2)
		  if lst1_sum >= lst2_sum:
			return lst1
		  else:
			return lst2
		   
		#TEST
		print(larger_sum([1, 9, 5], [2, 3, 7]))
		#[1, 9, 5]
		-------------------------
		#STATUS (CODE) in a class VARIABLE (TO RUN A FUNCTION)(AND SAVE THE CODE)
			>>> class Chess():
			...     status = {'setup_board': False}
			...     def __init__(self):
			...             self.setup = self.setup_board()
			...     def setup_board(self):
			...             print('setting up chess board')
			...             self.status['setup_board'] = True
			...             return self.status
			...
			>>> c = Chess()
			setting up chess board
			>>> c.__dict__
			{'setup': {'setup_board': True}}
			>>> dir(c)
			['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'setup', 'setup_board', 'status']
			>>> c.setup
			{'setup_board': True}
			>>> c.setup_board
			<bound method Chess.setup_board of <__main__.Chess object at 0x0000027E2A4ABCC0>>
			>>> c.status
			{'setup_board': True}
		-------------------------
		#INTERFACE (SEEING HOW THIS WORKS)
		# both CLASSES have a PLAY METHOD 
		# so we can make a FUNCTION that can take EITHER object

		class Chess:
		  def play(self):
			print("Playing chess!")

		class Checkers:
		  def play(self):
			print("Playing checkers!")

		chess1 = Chess()
		check1 = Checkers()

		def test(chess_or_checker_object):
			chess_or_checker_object.play()        #runs either PLAY METHOD (depending on the object)

		test(chess1)        #Playing chess!
		test(check1)        #Playing checkers!
		-------------------------
		#FUNCTION: OVER 9000
		def over_nine_thousand(lst):
		  result = 0
		  for x in lst:
			result += x
			if (result > 9000):
			  break
		  return result

		#TEST
		print(over_nine_thousand([8000, 900, 120, 5000]))
		#9020

		#SOLUTION
		#def over_nine_thousand(lst):
		#  sum = 0
		#  for number in lst:
		#    sum += number
		#    if (sum > 9000):
		#      break
		#  return sum
		-------------------------
		#FUNCTION: MAX NUM
		def max_num(nums):
		  return max(nums)

		#TEST
		print(max_num([50, -10, 0, 75, 20]))
		#75
		-------------------------
		-------------------------
		#FUNCTION: SAME VALUES
		def same_values(lst1, lst2):
		  return [i for i in range(0, len(lst1)) if lst1[i] == lst2[i]]

		#TEST
		print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
		#[0, 2, 3]
		print(same_values([5, 1, -10, 3, 3, 1], [5, 10, -10, 3, 5, 1]))				
		#[0, 2, 3, 5]
			---
			#SOLUTION
			#def same_values(lst1, lst2):
			#  new_lst = []
			#  for index in range(len(lst1)):
			#    if lst1[index] == lst2[index]:
			#      new_lst.append(index)
			#  return new_lst
			---
			#*** WARNING, there is PROBLEM WITH HOW THIS WORKS? I THINK IT'S RUNNING NESTED LIST? ***
			#*** KEEP IN MIND WHAT THE LIST LOOKS LIKE... ***
			#		[(5, 5), (1, 10), (-10, -10), (3, 3), (3, 5), (1, 1)]
			#def same_values(lst1, lst2):
			#  try:
			#	return [lst2.index(y) for x, y in zip(lst1, lst2) if x == y]
			#	#this doesn't work correctly? (lst1, x)
			#	#return [lst1.index(x) for x, y in zip(lst1, lst2) if x == y]
			#  except ValueError:		#don't think I need this...
			#	pass								#do nothing (SKIP)
		-------------------------
		-------------------------
		#FUNCTION: REVERSED LIST (*** my solution is much easier to understand and efficient ***)
		def reversed_list(lst1, lst2):
		  return lst1 == lst2[::-1]			#COUNT_BY (ONE) BACKWARDS (NEGATIVE)

		#TEST
		print(reversed_list([1, 2, 3], [3, 2, 1]))	#True
		print(reversed_list([1, 5, 3], [3, 2, 1]))	#False
		
		#SOLUTION
		#def reversed_list(lst1, lst2):
		#  for index in range(len(lst1)):
		#    if lst1[index] != lst2[len(lst2) - 1 - index]:
		#      return False
		#  return True
		-------------------------

	AUG.07 LIST COMPREHENSION (CODE CHALLENGE)
		*** DO THIS NEXT ***
			https://www.codecademy.com/courses/learn-python-list-comprehension/lessons/lists/exercises/introduction
		-------------------------
		#DOUBLE
		nums = [4, 8, 15, 16, 23, 42]
		double_nums = [x * 2 for x in nums]
		print(nums)					#[4, 8, 15, 16, 23, 42]
		print(double_nums)	#[8, 16, 30, 32, 46, 84]
		-------------------------
		#SQUARES
		nums = range(11)
		squares = [x ** 2 for x in nums]
		print(nums)			#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		print(squares)	#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
		-------------------------
		#ADD TEN
		nums = [4, 8, 15, 16, 23, 42]
		add_ten = [x + 10 for x in nums]
		print(nums)			#[4, 8, 15, 16, 23, 42]
		print(add_ten)	#[14, 18, 25, 26, 33, 52]
		-------------------------
		#DIVIDE BY 2
		nums = [4, 8, 15, 16, 23, 42]
		divide_by_two = [x / 2 for x in nums]
		print(nums)							#[4, 8, 15, 16, 23, 42]
		print(divide_by_two)		#[2, 4, 7, 8, 11, 21]
		-------------------------
		#PARITY 
		nums = [4, 8, 15, 16, 23, 42]
		parity = [num % 2 for num in nums]
		print(nums)
		print(parity)		#[0, 0, 1, 0, 1, 0]
		---
		#first pass (this is much more efficient above...)
		#PARITY (0 = even, 1 = odd)
		nums = [4, 8, 15, 16, 23, 42]

		#HELPER FUNCTION: to return parity
		def isOddorEven(num):
		  if x % 2 == 0:
			return 0
		  else:
			return 1
		  
		parity = [isOddorEven(x) for x in nums]
		print(nums)					#[4, 8, 15, 16, 23, 42]
		print(parity)				#[0, 0, 1, 0, 1, 0]
		-------------------------
		#ADD HELLO (GREETING)
		names = ["Elaine", "George", "Jerry", "Cosmo"]
		greetings = ["Hello, " + x for x in names]
		print(names)
		print(greetings)			#['Hello, Elaine', 'Hello, George', 'Hello, Jerry', 'Hello, Cosmo']
		-------------------------
		#FIRST CHARACTER
		names = ["Elaine", "George", "Jerry", "Cosmo"]
		first_character = [x[0] for x in names]
		print(names)				#['Elaine', 'George', 'Jerry', 'Cosmo']
		print(first_character)		#['E', 'G', 'J', 'C']
		-------------------------
		#SIZE (get length of chars in names)
		names = ["Elaine", "George", "Jerry", "Cosmo"]
		lengths = [len(x) for x in names]
		print(names)				#['Elaine', 'George', 'Jerry', 'Cosmo']
		print(lengths)				#[6, 6, 5, 5]
		-------------------------
		#OPPOSITE
		booleans = [True, False, True]
		opposite = [not x for x in booleans]
		print(booleans)				#[True, False, True]
		print(opposite)				#[False, True, False]
		-------------------------
		#SAME STRING
		names = ["Elaine", "George", "Jerry", "Cosmo"]
		is_Jerry = [x == "Jerry" for x in names]
		print(names)				#['Elaine', 'George', 'Jerry', 'Cosmo']
		print(is_Jerry) 			#[False, False, True, False]
		-------------------------
		#GREATER THAN TWO
		nums = [5, -10, 40, 20, 0]
		greater_than_two = [x > 2 for x in nums]
		print(nums)					#[True, False, True, True, False]
		print(greater_than_two)		#[True, False, True, True, False]
		-------------------------
		#PRODUCT
		nested_lists = [[4, 8], [15, 16], [23, 42]]
		product = [x * y for (x, y) in nested_lists]
		print(nested_lists)			#[[4, 8], [15, 16], [23, 42]]
		print(product)				#[32, 240, 966]
		-------------------------
		#GREATER THAN (if the first number (sub-list) is greater)
		nested_lists = [[4, 8], [16, 15], [23, 42]]
		greater_than = [x > y for (x, y) in nested_lists]
		print(nested_lists)			#[[4, 8], [16, 15], [23, 42]]
		print(greater_than) 		#[False, True, False]
		-------------------------
		#FIRST ONLY
		nested_lists = [[4, 8], [16, 15], [23, 42]]
		first_only = [x for (x, y) in nested_lists]
		print(nested_lists)			#[[4, 8], [16, 15], [23, 42]]
		print(first_only)			#[4, 16, 23]
		-------------------------
		#ADD WITH ZIP (ZIP LIST)
		# https://docs.python.org/3/library/functions.html#zip
		a = [1.0, 2.0, 3.0]
		b = [4.0, 5.0, 6.0]
		sums = [x + y for (x, y) in zip(a, b)]
		print(a)					#[1.0, 2.0, 3.0]
		print(b)					#[4.0, 5.0, 6.0]
		print(sums)					#[5.0, 7.0, 9.0]
		-------------------------
		#DIVIDE WITH ZIP
		a = [1.0, 2.0, 3.0]
		b = [4.0, 5.0, 6.0]
		quotients = [y / x for (x, y) in zip(a, b)]
		print(a)					#[4.0, 5.0, 6.0]
		print(b)					#[4.0, 5.0, 6.0]
		print(quotients)			#[4.0, 2.5, 2.0]
		-------------------------
		#CAPITALS
		capitals = ["Santiago", "Paris", "Copenhagen"]
		countries = ["Chile", "France", "Denmark"]
		locations = ['{}, {}'.format(cap, cou) for (cap, cou) in zip(capitals, countries)]
		print(capitals)				#['Santiago', 'Paris', 'Copenhagen']
		print(countries)			#['Chile', 'France', 'Denmark']
		print(locations)			#['Santiago, Chile', 'Paris, France', 'Copenhagen, Denmark']
		-------------------------
		#AGES
		names = ["Jon", "Arya", "Ned"]
		ages = [14, 9, 35]
		users = ['Name: {}, Age: {}'.format(x, y) for (x, y) in zip(names, ages)]
		print(names)				#['Jon', 'Arya', 'Ned']
		print(ages)					#[14, 9, 35]
		print(users)				#['Name: Jon, Age: 14', 'Name: Arya, Age: 9', 'Name: Ned, Age: 35']
		-------------------------
		#GREATER THAN WITH ZIP
		a = [30, 42, 10]
		b = [15, 16, 17]
		greater_than = [x > y for (x, y) in zip(a, b)]
		print(a) 					#[30, 42, 10]
		print(b) 					#[15, 16, 17]
		print(greater_than) 		#[True, True, False]
		-------------------------
		
	AUG.07 PROJECT - REGGIE'S LINEAR REGRESSION 
		-DOWNLOAD (*.ZIP)
		-OPEN PROJECT (IN JUPYTER NOTEBOOKS)
			-go to folder...
			PS C:\Users\Pythagoras\Documents\000-Code\code academy\python\07-Project (Reggies Linear Regression)\Reggie's+Linear+Regression> jupyter notebook
			-type (jupyter notebook)
			
	AUG.10 DEBUGGING (can you debug?)
		(found this about an IMPORT terminal debugger called PDB)
		-commands are in (lowercase)
		----------------------------------------------
		#TEST DEBUGGING IN PYTHON 
		#PDB		https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

		#HOW TO USE...
		#--------------------------			TERMINAL...
		#RUN CODE 					(python *.py)
		#it should pause with 				(pdb)
		#NEXT LINE (step)				(n)
		#PRINT (VARIABLE)				(p c) returns 'ccc'
								(p final) returns 'aaabbbccc'
		#REPEAT (last command)				(...press ENTER)
		#LIST CODE 					(l)

		#STEP INTO (nesting subroutine)			(s)
		#RETURN (end current subroutine)		(r)

		#TURN OFF (PDB PROMPT)(continue)		(c)
		#QUIT 						(q)
		#--------------------------

		import pdb
		a = "aaa"
		pdb.set_trace()
		b = "bbb"
		c = "ccc"
		final = a + b + c
		print(final)
		print('Text: ABC\b\b\bXYZ')	#Text: XYZ
		str = 'abcdefghi\b\b\b\b\b\b'
		print(str)			#abcdefghi (THIS DOESN'T WORK RIGHT?)
		----------------------------------------------
	
	AUG.12 INTRO TO STRINGS 
		--------------------
		#STRING
		favorite_word = 'Muppet'
		print(favorite_word)
		--------------------
		#STRING (AS A LIST)
			test = 'abcdef'
			test[-1]			#'f'			#LAST LETTER same as... (len(my_string)-1)
			test[-2]			#'e'			#GETS (ONE LETTER) 2ND LAST
			test[-2:]			#'ef'			#GETS (2nd LAST) TO END OF LIST
			test[-3]			#'d'
			test[0:2]			#'ab'
			test[0:3]			#'abc'
			test[0:3:2]			#'ac'
			test[0::2]			#'ace'
			test[-1::-2]		#'fdb'			#BACKWARDS
			test[::-2]			#'fdb'			#BACKWARDS
			test[::1]			#'abcdef'		#IN ORDER
			test[::2]			#'ace'			#EVERY 2ND LETTER
		--------------------
		my_name = 'Dean'
		first_initial = my_name[0]
		print(my_name)
		print(first_initial)
		--------------------
		#STRING (AS A LIST)
		#VARIABLES
		first_name = "Rodrigo"
		last_name = "Villanueva"

		#FUNCTION: CREATE NEW USERID
		def NewUserName(fname, lname):
		  return lname[:5:]

		new_account = NewUserName(first_name, last_name)
		print(new_account)			#Villa

		#FUNCTION: TEMP PASSWORD 
		def TempPassword(fname, lname):
		  return lname[3:7]

		temp_password = TempPassword(first_name, last_name)
		print(temp_password)		#lanu
		--------------------
		#STRING (CONCATENATION)
		first_name = "Julie"
		last_name = "Blevins"

		#FUNCTION: CREATE ACCOUNT 
		def account_generator(fname, lname):
				  return fname[:3] + lname[:3]
		  
		new_account = account_generator(first_name, last_name)
		print(new_account) 			#JulBle
		--------------------
		#STRING (SLICING)(originally using len(), but I found this more confusing)
		first_name = "Reiko"
		last_name = "Matsuki"

		#FUNCTION: PASSWORD GENERATOR 
		def password_generator(fname, lname):
		  return fname[-3:] + lname[-3:]

		temp_password = password_generator(first_name, last_name)
		print(temp_password)				#ikouki
		--------------------
		#STRING (NEGATIVE INDICES)
		company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

		second_to_last = company_motto[-2]
		print(second_to_last)				#'f'

		final_word = company_motto[-4:]
		print(final_word)					#'life'
		--------------------
		#STRING 
		# strings are IMMUTABLE (unchangeable)
		first_name = "Bob"
		last_name = "Daily"

		#CREATES ERROR (because STRING is unchangeable)
		#first_name[0] = "R"		#TypeError: 'str' object does not support item assignment
		print(first_name)					#'Bob'

		fixed_first_name = 'R' + first_name[1:]
		print(fixed_first_name)		#'Rob'
		--------------------
		#STRING (ESCAPE CHARACTERS)
		#password = "theycallme"crazy"91" 	#SyntaxError: invalid syntax

		#ESCAPE CHARACTER (USE DIFFERENT QUOTES)(single or double)
		test = 'He said, "Blueberries are my fav!"'
		print(test)			#'He said, "Blueberries are my fav!"'

		#ESCAPE CHARACTER (ADD BACKSLASH)
		test2 = "He said, \"Blueberries are my fav!\""
		print(test2)		#'He said, "Blueberries are my fav!"'

		#FIX PASSWORD
		password = "theycallme\"crazy\"91"
		password2 = 'theycallme"crazy"91'
		print(password)			#theycallme"crazy"91
		print(password2)		#theycallme"crazy"91
		--------------------
		#STRING (LOOPING THRU WORDS)

		#GET LENGTH OF STRING 
		len('abcdefghi')

		#FUNCTION: LENGTH STRING (without len())
		def get_length2(my_str):
		  return my_str.index(my_str[-1]) + 1

		get_length2('abcdefghi')			#returns 9

		#FUNCTION: LENGTH STRING (without len())
		def get_length(my_str):
		  result = 0
		  for x in my_str:
			result += 1
		  return result
		--------------------
		#STRING (CONDITIONAL)

		#FUNCTION: LETTER CHECK 
		def letter_check(word, letter):
		  count = 0
		  for x in word:
			if x == letter:
			  count += 1
		  return count > 0

		#TEST 
		print(letter_check('strawberry', 'w'))
		print(letter_check('strawberry', 'W'))		#uppercase?
		print(letter_check('strawberry', 'o'))

		#----------------------
		#FUNCTION: LETTER COUNT
		def letter_count(word, letter):
		  count = 0
		  for x in word:
			if x == letter:
			  count += 1
		  return count

		print(letter_count('aabbbcccc', 'b'))

		#FUNCTION (WITH DEFAULT**)
		def letter_check(word, letter, ignoreCase=False):
			pass
		
		#FUNCTION: LETTER CHECK
		# (note, doesn't check MORE-THAN-ONE letter)
		def letter_check(word, letter, ignoreCase=False):
		  if ignoreCase:
			word = word.lower()	#change both to lowercase
			letter = letter.lower()
		  count = 0
		  for x in word:
			if x == letter:
			  count += 1
		  return count > 0

		#IGNORE CASE
		letter_check('abc', 'a', True)		#True
		letter_check('abc', 'b', True)		#True
		letter_check('abc', 'A', True)		#True
		letter_check('abc', 'B', True)		#True
		#MUST BE EXACT
		letter_check('abc', 'a', False)		#True
		letter_check('abc', 'A', False)		#False
		letter_check('abc', 'b', False)		#True
		letter_check('abc', 'B', False)		#False
		#WITHOUT CASE 
		letter_check('aabbcc', 'b')				#True
		--------------------
		#STRING (CONDITIONAL)

		#FUNCTION: WORD IN WORD (TEST)
		def contains(big_string, little_string):
		  return little_string in big_string

		#TEST
		print(contains("watermelon", "melon")) 	#true
		print(contains("watermelon", "water"))	#true
		print(contains("watermelon", "WATER"))	#false
		print(contains("watermelon", "berry"))	#false

		#FUNCTION: COMPARE STRINGS (COMMON LETTERS)
		def common_letters(string_one, string_two):
		  result = []
		  for x in string_one:
			if (x in string_two) and not (x in result):
			  result.append(x)
		  return result

		#TEST 
		print(common_letters('banana', 'cream'))		#['a']
		print(common_letters('Dean Jones', 'Nadine Jones')) #['e', 'a', 'n', ' ', 'J', 'o', 's']

		#SOLUTION
		#def common_letters(string_one, string_two):
		#  common = []
		#  for letter in string_one:
		#    if (letter in string_two) and not (letter in common):
		#      common.append(letter)
		#  return common
		--------------------
		#STRINGS (REVIEW)

		#FUNCTION: USERNAME GENERATOR 
		def username_generator(fname, lname):
		  if len(fname) < 3:
			fname = fname
		  else:
			fname = fname[:3]
		  if len(lname) < 4:
			lname = lname
		  else:
			lname = lname[:4]
		  return fname + lname

		#TEST 
		f1 = 'Dean'
		l1 = 'Jones'
		username = username_generator(f1, l1)
		print(username_generator(f1, l1))				#DeaJone
		f2 = 'Al'
		print(username_generator(f2, l1))				#AlJone
		l2 = 'Kim'
		print(username_generator(f1, l2))				#DeaKim

		#FUNCTION: PASSWORD GENERATOR
		def password_generator(username):
		  return username[-1] + username[:-1]

		#TEST
		print(password_generator('AbeSimp'))		#pAbeSim
		--------------------
	AUG.12 QUIZ#5 STRINGS 
		6/6 	(100%)
		
	-------------------------------------------	
	-------------------------------------------
		#HOW TO SAVE A LIST TO A NUMBER
		#AUG.13, 2018

		# This is something I've been exploring for some time...
		# Based on the AUTOCAD OSNAP (how it saved SNAP SETTINGS)
		# This was brilliant at the time, (I want to expand on this idea... which I don't think many people really grasp)

		# [1, 4, 4]
		# Need to save this in (3^n) base (because there are at least TWO REPEATING VALUES)
		# (3^n --> 55 --> [1, 4, 4])
		# Need to store the BASE (3^n) and the VALUE (55), which can be converted to the LIST ([1, 4, 4])
		# Also need a KEY (in this case it's simply the DIGITS 0-9)
		# key (EXAMPLE BASE 3^n)
		#   0 : 0
		#   1 : 1
		#   3 : 2
		#   9 : 3
		#   27 : 4
		#   81 : 5
		#   243 : 6
		#   729 : 7
		#   2187: 8
		#   6561: 9
		#   19683: 10
		#   59049: 11
		#   177147: 12

		#-----------------
		#Let's see this in action... not theory
		key = [
			(0, 0),
			(1, 1),
			(3, 2),
			(9, 3),
			(27, 4),
			(81, 5)
		]
		#this would be better implemented using ZIP of (two lists)
		key2_key = [3 ** x for x in range(10)]                  #[1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]
		key2_value = list(range(10))                            #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		key2 = list(zip(key2_key, key2_value))                  #[(1, 0), (3, 1), (9, 2), (27, 3), (81, 4), (243, 5), (729, 6), (2187, 7), (6561, 8), (19683, 9)]
		#turn this into a FUNCTION

		#FUNCTION: CREATE KEY
		def create_key(range_limit, base):
			key = [base ** x for x in range(range_limit)]
			return list(zip(key, range(range_limit)))

		#TEST
		create_key(10, 3)
		#  [(1, 0), (3, 1), (9, 2), (27, 3), (81, 4), (243, 5), (729, 6), (2187, 7), (6561, 8), (19683, 9)]
		create_key(10, 2)
		#  [(1, 0), (2, 1), (4, 2), (8, 3), (16, 4), (32, 5), (64, 6), (128, 7), (256, 8), (512, 9)]
		create_key(10, 4)
		#  [(1, 0), (4, 1), (16, 2), (64, 3), (256, 4), (1024, 5), (4096, 6), (16384, 7), (65536, 8), (262144, 9)]
	-------------------------------------------
	-------------------------------------------	
	AUG.13 STRING METHODS (CODE ACADEMY)
	------------------
	#STRING (FORMATTING)(LOWER, UPPER, TITLE)
	poem_title = "spring storm"
	poem_author = "William Carlos Williams"

	#TITLE CASE (.title())
	poem_title_fixed = poem_title.title()
	print(poem_title_fixed)			#Spring Storm

	#UPPERCASE (.upper())
	poem_author_fixed = poem_author.upper()
	print(poem_author_fixed)		#WILLIAM CARLOS WILLIAMS
	------------------	
	#STRING (SPLITTING STRINGS)
	line_one = "The sky has given over"

	#SPLIT (.split(delimitter))(splits by DELIMITTER)
	#default delimitter is (a space ' ')
	line_one_words = line_one.split()
	print(line_one_words) 		#['The', 'sky', 'has', 'given', 'over']
	------------------
	#STRING (SPLITTING)
	authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

	author_names = authors.split(',')
	print(author_names)		
	#['Audre Lorde', ' William Carlos Williams', ' Gabriela Mistral', ' Jean Toomer', ' An Qi', ' Walt Whitman', ' Shel Silverstein', ' Carmen Boullosa', ' Kamala Suraiyya', ' Langston Hughes', ' Adrienne Rich', ' Nikki Giovanni']

	author_first_names = [x.split()[0] for x in author_names]
	#['Audre', 'William', 'Gabriela', 'Jean', 'An', 'Walt', 'Shel', 'Carmen', 'Kamala', 'Langston', 'Adrienne', 'Nikki']
	print(author_first_names)
	author_last_names = [x.split()[-1] for x in author_names]
	print(author_last_names)
	#['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']
	------------------
	#STRING (SPLITTING)(ESCAPE CHARACTERS)
	spring_storm_text = \
	"""The sky has given over 
	its bitterness. 
	Out of the dark change 
	all day long 
	rain falls and falls 
	as if it would never end. 
	Still the snow keeps 
	its hold on the ground. 
	But water, water 
	from a thousand runnels! 
	It collects swiftly, 
	dappled with black 
	cuts a way for itself 
	through green ice in the gutters. 
	Drop after drop it falls 
	from the withered grass-stems 
	of the overhanging embankment."""

	#SPLIT (\n NEWLINE)
	spring_storm_lines = spring_storm_text.split('\n')
	print(spring_storm_lines)
	#['The sky has given over ', 'its bitterness. ', 'Out of the dark change ', 'all day long ', 
	'rain falls and falls ', 'as if it would never end. ', 'Still the snow keeps ', 'its hold on the ground. 
	', 'But water, water ', 'from a thousand runnels! ', 'It collects swiftly, ', 'dappled with black ', 
	'cuts a way for itself ', 'through green ice in the gutters. ', 'Drop after drop it falls ', 'from the withered grass-stems ', 
	'of the overhanging embankment.']
	------------------
	#STRING (JOIN)
	# opposite of SPLIT
	reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

	#STRING (JOIN)(<delimiter>.join(<list_of_string>))
	reapers_line_one = ' '.join(reapers_line_one_words)
	print(reapers_line_one)
	#Black reapers with the sound of steel on stones
	------------------
	#STRING (JOIN)(CSV, comma separated files)
	winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

	winter_trees_full = '\n'.join(winter_trees_lines)
	print(winter_trees_full)
	# All the complicated details
	# of the attiring and
	# the disattiring are completed!
	# A liquid moon
	# moves gently among
	# the long branches.
	# Thus having prepared their buds
	# against a sure winter
	# the wise trees
	# stand sleeping in the cold.
	------------------
	#STRING (STRIP)(REMOVES WHITESPACE)
	love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

	#REMOVE WHITESPACE
	love_maybe_lines_stripped = [x.strip() for x in love_maybe_lines]
	print(love_maybe_lines_stripped)
	#['Always', 'in the middle of our bloodiest battles', 'you lay down your arms', 'like flowering mines', '', 'to conquer me home.']

	#JOIN
	love_maybe_full = '\n'.join(love_maybe_lines_stripped)
	print(love_maybe_full)
	------------------
	#STRING (REPLACE)
	toomer_bio = \
	"""
	Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
	"""
	#FIX HIS NAME ('Toomer')
	toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
	print(toomer_bio_fixed)
	------------------
	#STRING (FIND)(FINDS THE FIRST INDEX ONLY)
	god_wills_it_line_one = "The very earth will disown you"

	disown_placement = god_wills_it_line_one.find('disown')
	print('Index of "disown": ', disown_placement)
	#Index of "disown":  20
	------------------
	#STRING (FORMAT)
	def poem_title_card(poet, title):
	  return 'The poem "{}" is written by {}.'.format(title, poet)

	#TEST 
	print(poem_title_card("Walt Whitman", "I Hear America Singing"))
	#The poem "I Hear America Singing" is written by Walt Whitman.
	------------------
	#STRING (FORMAT)(using KEYWORDS)
	def poem_description(publishing_date, author, title, original_work):
	  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
	  return poem_desc

	my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
	print(my_beard_description)
	#The poem My Beard by Shel Silverstein was originally published in Where the Sidewalk Ends in 1974.
	------------------
	#STRING (REVIEW)
	highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

	#print poem
	#print(highlighted_poems)

	#convert to list
	highlighted_poems_list = highlighted_poems.split(',')
	#print(highlighted_poems_list)

	#clean up (whitespace)
	highlighted_poems_stripped = [x.strip() for x in highlighted_poems_list]
	print(highlighted_poems_stripped)

	#empty list 
	highlighted_poems_details = []
	
	#create a (list of lists)
	highlighted_poems_details = [x.split(':') for x in highlighted_poems_stripped]
	print(highlighted_poems_details)
	#[['Afterimages', 'Audre Lorde', '1997'], ['The Shadow', 'William Carlos Williams', '1915'], ['Ecstasy', 'Gabriela Mistral', '1925'], ['Georgia Dusk', 'Jean Toomer', '1923'], ['Parting Before Daybreak', 'An Qi', '2014'], ['The Untold Want', 'Walt Whitman', '1871'], ["Mr. Grumpledump's Song", 'Shel Silverstein', '2004'], ['Angel Sound Mexico City', 'Carmen Boullosa', '2013'], ['In Love', 'Kamala Suraiyya', '1965'], ['Dream Variations', 'Langston Hughes', '1994'], ['Dreamwood', 'Adrienne Rich', '1987']]
	print('------')
	
	#create separate lists (into titles, author & dates)
	#titles 
	titles = [x[0] for x in highlighted_poems_details]
	print("titles: ", titles)
	#titles:  ['Afterimages', 'The Shadow', 'Ecstasy', 'Georgia Dusk', 'Parting Before Daybreak', 'The Untold Want', "Mr. Grumpledump's Song", 'Angel Sound Mexico City', 'In Love', 'Dream Variations', 'Dreamwood']
	print('------')
	#poets
	poets = [x[1] for x in highlighted_poems_details]
	print("poets: ", poets)
	#poets:  ['Audre Lorde', 'William Carlos Williams', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich']
	print('------')
	#dates
	dates = [x[2] for x in highlighted_poems_details]
	print("dates: ", dates)
	#dates:  ['1997', '1915', '1925', '1923', '2014', '1871', '2004', '2013', '1965', '1994', '1987']
	------------------
	
	AUG.13, 2018 QUIZ#6 (STRING METHODS)
		5/7 (71%)
		6/7	(85%) 	RE-DO
		7/7 (100%)	RE-DO
		
	AUG.13, 2018 PROJECT (THREAD SHED)
		DID THIS IN 2 HOURS (NICE!)
		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\08-Project (Thread Shed)\
			proj8_thread_shed.py"
			
	-------------
	AUG.14, 2018 PYTHON SCRIPT (EXECUTED FROM SERVER)
		-when the BROWSER (CLIENT) request this page (it finds the script) and the SCRIPT writes the PAGE
		------------------------------
		HELLO.PY
		------------------------------
		#!/usr/bin/python

		print "Content-type:text/html\r\n\r\n"
		print '<html>'
		print '<head>'
		print '<title>Hello Word - First CGI Program</title>'
		print '</head>'
		print '<body>'
		print '<h2>Hello Word! This is my first CGI program</h2>'
		print '</body>'
		print '</html>'
		------------------------------
		import os 
		os.environ.keys()		#dumps a bunch of OS ENVIRONMENT VARIABLES
		-TO VIEW (KEY-VALUE) of object
			os.environ['APPDATA']				#%APPDATA%
				'C:\\Users\\Pythagoras\\AppData\\Roaming'
			os.environ['TEMP']					#%TEMP%
				'C:\\Users\\PYTHAG~1\\AppData\\Local\\Temp'
			os.environ['HOMEDRIVE']
				'C:'
			os.environ['HOMEPATH']				#*** can access any of these paths in EXPLORER (%HOMEPATH%) ***
				'\\Users\\Pythagoras'
		-LIST OF VALUES 
			os_values = [os.environ[x] for x in os.environ]
		-LIST OF KEYS 
			os_keys = [x for x in os.environ]
				#['ALLUSERSPROFILE', 'APPDATA','HOMEDRIVE', 'HOMEPATH', 'LOCALAPPDATA', 'LOGONSERVER', 'ONEDRIVE', 'OS', 'PATH', 'PATHEXT', 'PROGRAMDATA', 'PROGRAMFILES', 'PROGRAMFILES(X86)',
				'PROGRAMW6432', 'PUBLIC', 'SESSIONNAME', 'SYSTEMDRIVE', 'SYSTEMROOT', 'TEMP', 'TMP', 'USERDOMAIN', 'USERNAME', 'USERPROFILE', 'WINDIR', 'WORK']
		-PRINT (CLEANER)
			t1 = [print("key: {}, path: {}".format(x, os.environ[x])) for x in os.environ]		
		-------------------
		ADD CUSTOM (ENVIRONMENT VARIABLES)(SHORTCUTS)
			ENV VARIABLE 	SHORTCUT 		PATH
			HELP 			%HELP%			'E:\000-BACKUP\000-SAIT\000-HELP'	
			CODEACAD		%CODEACAD% 		'E:\000-BACKUP\0000-CODE ACADEMY'
			PYTHON 			%PYTHON%		'C:\Users\Pythagoras\Documents\000-Code\code academy\python'
		-------------------
		COMMON IMPORTS 
			import os 			(os - operating system) 
			import sys 
			import re 			(regular expressions)
			import math 		(math utilities)
		https://docs.python.org/3/tutorial/stdlib.html
		-------------------
		ACCESS GOOGLE...
			from urllib.request import urlopen
			#html = urlopen("http://www.google.com/")
			html = urlopen('https://www.google.ca/search?source==inspiration')
			----
			dump(html) 		#make sure to load (dump method above)
		--------------
		#https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
		#THIS WORKS!!!

		from urllib.request import urlopen
		#html = urlopen("http://www.google.com/")
		html = urlopen('https://www.google.ca/search?source==inspiration')

		print(html)			#<http.client.HTTPResponse object at 0x0000020A96750898>
		--------------
		import urllib.request

		req = urllib.request.Request('http://www.google.ca')
		with urllib.request.urlopen(req) as response:
		   the_page = response.read()
		   print(the_page)		#DUMPS A GIANT STRING (OF HTML!!!)	*** NOT THIS IS IN (BYTES, b'...' type string)
		   #the_page (bytes)
		   #CONVERT TO STRING 
		   page = the_page.decode('UTF-8')
		--------------	
	AUG.14, 2018 CODE ACADEMY
		CODE CHALLENGE : STRING METHODS
		------------------------------
		#STRING (HOW MANY DIFFERENT...)(TYPES OF LETTERS in string)
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		#FUNCTION: COUNT DIFFERENT LETTERS (IN STRING)
		def unique_english_letters(word):
		  t = word
		  count = 0
		  while t != '':					#while 't' temp word is not blank
			t = t.replace(t[0], '')			#replace off (all) the first letter
			#repeat until word (t) is blank
			#count the (iterations)
			count += 1
		  return count
		  
		  
		#TEST
		print(unique_english_letters("mississippi"))
		# should print 4
		print(unique_english_letters("Apple"))
		# should print 4
		------------------------------	
		#STRING (COUNT)(NUMBER OF TIMES)(WORD APPEARS)

		#FUNCTION: COUNT (NUMBER OF TIMES)(WORD APPEARS)
		def count_char_x(word, char):
		  return word.count(char)

		#TEST
		print(count_char_x("mississippi", "s"))
		# should print 4
		print(count_char_x("mississippi", "m"))
		# should print 1
		------------------------------	
		#... exact same function?
		#STRING (COUNT)(MULTIPLE CHARS)(IN STRING)
		#FUNCTION: MULTI-CHAR COUNT
		def count_multi_char_x(word, m_char):
		  return word.count(m_char)

		#TEST
		print(count_multi_char_x("mississippi", "iss"))
		# should print 2
		print(count_multi_char_x("apple", "pp"))
		# should print 1	
		------------------------------	
		#STRING (SUBSTRING BETWEEN)
		#FUNCTION: SUBSTRING (BETWEEN LETTERS)
		def substring_between_letters(word, start, end):
		  try:
			word_list = [x for x in word]
			return ''.join(word_list[word.index(start) + 1:word.index(end)])
		  except ValueError:
			return word

		#TEST
		print(substring_between_letters("apple", "p", "e"))
		# should print "pl"
		print(substring_between_letters("apple", "p", "c"))
		# should print "apple"
		------------------------------
		#STRING (X LENGTH)
		#FUNCTION: TEST IF (EVERY WORD) HAS GREATER LEN THAN (N)
		def x_length_words(sentence, n):
		  words_list = sentence.split(' ')	#['this', 'is', 'a', 'sentence']
		  test_list = [len(x) >= n for x in words_list]	#[True, False, False, True]
		  #test (if all elements are true)
		  #  sum (counts the trues, true = 1) and compares to length of list
		  test_all = sum(test_list) == len(test_list)
		  return test_all

		#TEST
		print(x_length_words("i like apples", 2))
		# should print False
		print(x_length_words("he likes apples", 2))
		# should print True
		
		#SOLUTION
		# Write your x_length_words function here:
		#def x_length_words(sentence, x):
		#  words = sentence.split(" ")
		#  for word in words:
		#    if len(word) < x:
		#      return False
		#  return True
		------------------------------
		WRAPPING CODE ???
			-what if I have LONG LINE OF CODE, how do I wrap it?
			https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python
			--------
			a = some_function(
				'1' + '2' + '3' - '4')
			--------
			-USE BACKSLASH(\)
			a = '1'   \
				+ '2' \
				+ '3' \
				- '4'
			--------
		------------------------------	
		#STRING (CHECK NAME)
		#FUNCTION: 
		def check_for_name(sentence, name):
		  if (sentence.find(name.lower()) != -1):
			return True
		  if (sentence.find(name.upper()) != -1): 
			 return True
		  if (sentence.find(name.title()) != -1):
			return True
		  else:
			return False

		#TEST
		print(check_for_name("My name is Jamie", "Jamie"))
		# should print True
		print(check_for_name("My name is jamie", "Jamie"))
		# should print True
		print(check_for_name("My name is Samantha", "Jamie"))
		# should print False
		------------------------------
		#STRING (EVERY OTHER LETTER)
		#FUNCTION: EVERY OTHER LETTER
		def every_other_letter(word):
		  return word[::2]

		#TEST
		print(every_other_letter("Codecademy"))
		# should print Cdcdm
		print(every_other_letter("Hello world!"))
		# should print Hlowrd
		print(every_other_letter(""))
		# should print 
		------------------------------
		#STRING (REVERSE)
		#FUNCTION: REVERSE THE STRING 
		def reverse_string(word):
		  return word[::-1]

		#TEST
		print(reverse_string("Codecademy"))
		# should print ymedacedoC
		print(reverse_string("Hello world!"))
		# should print !dlrow olleH
		print(reverse_string(""))
		# should print
		------------------------------
		#STRING (MAKE SPOONERISM)(ERROR IN SPEECH)(REVERSE SYLLABLES)
		#FUNCTION: (ERROR IN SPEECH)(REVERSE SYLLABLES)
		def make_spoonerism(word1, word2):
		  return word2[0] + word1[1:] + ' ' + word1[0] + word2[1:]

		#TEST
		print(make_spoonerism("Codecademy", "Learn"))
		# should print Lodecademy Cearn
		print(make_spoonerism("Hello", "world!"))
		# should print wello Horld!
		print(make_spoonerism("a", "b"))
		# should print b a
		------------------------------
		#STRING (ADD EXCLAMATION)
		#FUNCTION: ADD EXCLAMATION
		def add_exclamation(word):
		  space_left = 20 - len(word)
		  if len(word) < 20 and space_left > 0:
			return word + ('!' * space_left)
		  else:
			return word

		#TEST
		print(add_exclamation("Codecademy"))
		# should print Codecademy!!!!!!!!!!
		print(add_exclamation("Codecademy is the best place to learn"))
		# should print Codecademy is the best place to learn
		------------------------------
	AUG.15 CODE PLAY (RECURSION)
		(EVAL) use for expression
		(EXEC) use for statement 
		-not sure the difference yet?
		https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python
		-------------------
		-pass a STRING to RUN AS CODE
			>>> test = '''
			... for x in range(4):
			...     for y in range(3):
			...             for z in range(2):
			...                     print(x, y, z)
			... '''
			>>> exec(test)
			0 0 0
			0 0 1
			0 1 0
			0 1 1
			0 2 0
			0 2 1
			1 0 0
			1 0 1
			1 1 0
			1 1 1
			1 2 0
			1 2 1
			2 0 0
			2 0 1
			2 1 0
			2 1 1
			2 2 0
			2 2 1
			3 0 0
			3 0 1
			3 1 0
			3 1 1
			3 2 0
			3 2 1
		--------------------
		*** USE (LIST COMPREHENSION) INSTEAD ***
		[(x,y) for x in range(3) for y in range(3)]
			#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
		[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
			#[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), 
			(1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), 
			(2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]	
		--------------------
		# COMBINATIONS (OF A LIST)
		#   -this method just uses the BINARY ARRAY (value)(if it's equal to 1)(that INDEX will PRINT or create the lists)
		# use a BINARY ARRAY (this will work for 3 elements only)
		array = [(x, y, z) for x in [0,1] for y in [0,1] for z in [0,1]]
		array 
		# [
		# (0, 0, 0), 
		# (0, 0, 1), 
		# (0, 1, 0), 
		# (0, 1, 1), 
		# (1, 0, 0), 
		# (1, 0, 1), 
		# (1, 1, 0), 
		# (1, 1, 1)
		# ]
		my_list = [1, 2, 3]
		my_list.reverse()       #reverse order (fixes output)
		for row in array:
			[t for t,r in zip(my_list, row) if r == 1]
		# []
		# [1]
		# [2]
		# [2, 1]
		# [3]
		# [3, 1]
		# [3, 2]
		# [3, 2, 1]
		****************************************************************************************************
		****************************************************************************************************
		COMBINATIONS** (FUNCTIONS)
		# FUNCTION: ARRAY BUILDER
		# num_terms - is the number of columns (of array) also the same as (length of terms, for COMBINATIONS)
		def array_builder(num_terms):
			alpha = 'abcdefghijklmnopqrstuvwxyz'            #letters (to use as lambda variables)
			# build a string (end of list comprehension)(dynamically)
			s = ''
			for x in range(num_terms):
				s += ' for {0} in [0,1]'.format(alpha[x])   #' for a in [0,1] for b in [0,1] for c in [0,1]'
			# build a string (start of list comprehension)(dynamically)
			t = ''
			for x in range(num_terms):
				t += '{}, '.format(alpha[x])
			# cleanup
			t = t.strip(', ')                               #'a, b, c'
			# concatenate (to add bracket
			list_comprehension = '[(' + t + ')' + s + ']'
			# eval (evaluate to list comprehension)
			return eval(list_comprehension)
		# TEST 
		array_builder(3)
		#[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
		# ------
		# FUNCTION: GET COMBINATIONS
		def combinations(my_list):
			l = len(my_list)                #get length (to find out what SIZE of array is needed)
			array = array_builder(l)        #build array 
			lst = my_list                   #create list (from argument)(so we can reverse and use in combinations)
			result = []
			for row in array:
				result.append([t for t,r in zip(lst, row) if r == 1])
			return result
		# TEST 
		combinations([1, 2, 3])
		#[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
		# ------
		# FUNCTION: GET TERMS (NTH IN LENGTH)
		def get_lists_nth_long(my_list, num_terms):
			if 0 <= num_terms <= max(my_list)[0]:
				return [x for x in my_list if len(x) == num_terms]
			else:
				return 'The num_terms argument needs to be between (0-{})'.format(max(my_list)[0])
		# TEST
		get_lists_nth_long(combinations([1, 2, 3, 4]), 2)
		# [[3, 4], [2, 4], [2, 3], [1, 4], [1, 3], [1, 2]]
		get_lists_nth_long(combinations([1, 2, 3, 4]), 3)
		# [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
		get_lists_nth_long(combinations([1, 2, 3, 4]), 4)
		# [[1, 2, 3, 4]]
		get_lists_nth_long(combinations([1, 2, 3, 4]), 5)
		# 'The num_terms argument needs to be between (0-4)'
		get_lists_nth_long(combinations([1, 2, 3, 4]), 1)
		# [[4], [3], [2], [1]]
		get_lists_nth_long(combinations([1, 2, 3, 4]), 0)
		# [[]]
		get_lists_nth_long(combinations([1, 2, 3, 4]), -1)
		# 'The num_terms argument needs to be between (0-4)'
		****************************************************************************************************
		****************************************************************************************************
		ITERTOOLS (IMPORT) (ITERATIONS, COMBINATIONS)
		>>> import itertools
		>>> t = [1,2,3]
		>>> for i in itertools.product(t, t):
		...     print(i)
		...
		(1, 1)
		(1, 2)
		(1, 3)
		(2, 1)
		(2, 2)
		(2, 3)
		(3, 1)
		(3, 2)
		(3, 3)
		-----------
		>>> for i in itertools.product(t, t, t):
		...     print(i)
		...
		(1, 1, 1)
		(1, 1, 2)
		(1, 1, 3)
		(1, 2, 1)
		(1, 2, 2)
		(1, 2, 3)
		(1, 3, 1)
		(1, 3, 2)
		(1, 3, 3)
		(2, 1, 1)
		(2, 1, 2)
		(2, 1, 3)
		(2, 2, 1)
		(2, 2, 2)
		(2, 2, 3)
		(2, 3, 1)
		(2, 3, 2)
		(2, 3, 3)
		(3, 1, 1)
		(3, 1, 2)
		(3, 1, 3)
		(3, 2, 1)
		(3, 2, 2)
		(3, 2, 3)
		(3, 3, 1)
		(3, 3, 2)
		(3, 3, 3)
		-----------
		
	AUG.16, 2018 
	PROJECT: CODED COMMUNICATION 
		CRYPTOGRAPHY 
		INFO ON KHAN ACADEMY (CRYPTOGRAPHY)
			https://www.khanacademy.org/computing/computer-science/cryptography#crypt
		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\09-Project (Coded Correspondence)
			\coded_correspondence\proj9_coded_correspondence.py"	
		*** FINISHED ON AUG.21, this was tricky, there were lots of errors on JUPYTER and the website I referenced were ENCRYPTING DIFFERENTLY... ***
		
	AUG.21, 2018 
		DICTIONARIES** DICTIONARY** 
			https://www.tutorialspoint.com/python/python_dictionary.htm
			
			SYNTAX 
				my_dict = {<string_key>: <anytype_value>}
			CONSTRUCTOR 
				thisdict = dict(apple="green", banana="yellow", cherry="red")
				thisdict			#{'apple': 'green', 'banana': 'yellow', 'cherry': 'red'}
			EMPTY DICTIONARY 
				empty_dict = {}
			TO ACCESS 
				my_dict = {'a': 1, 'b': 2, 'c': 3}
				my_dict['a']		#returns 1 
				my_dict['b']		#returns 2
			(LIST)(KEYS OR VALUES)
				my_dict.keys() 		#my_dict_keys(['a', 'b', 'c'])
				my_dict.values()	#my_dict_values([1, 2, 3])
			METHODS  
				dir(my_dict) 		#[...'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
			DELETE 
				my_dict.pop('c')	#returns 3 (RETURNS VALUE)
				my_dict			#{'a': 1, 'b': 2}
			DELETE (POP)(WITH DEFAULT)
				#DICTIONARY: DELETE (A KEY)
				available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
				#health
				health_points = 20

				#get value, add to health, pop (deletes)
				health_points += available_items.pop("stamina grains", 0)
				print("health_points: ", health_points)		#health_points:  35
				health_points += available_items.pop("power stew", 0)
				print("health_points: ", health_points)		#health_points:  65
				health_points += available_items.pop("mystic bread", 0)
				print("health_points: ", health_points)		#health_points:  65
				print(available_items)
				#{'health potion': 10, 'strength sandwich': 25, 'green elixir': 20, 'cake of the cure': 5}
				
			DELETE(DEL)(DOESN'T RETURN ANYTHING)(use POP)
				del(thisdict['banana'])		
				thisdict			#{'apple': 'green', 'cherry': 'red'}
			DELETE (ALL)(.clear())
				my_dict.clear()
				my_dict				#returns {} (EMPTY DICTIONARY)
			GET (INDEX?)
				-dict.get(key, default=None)
				-For key key, returns value or default if key not in dictionary
				my_dict.get('a')	#returns 1
				my_dict.get('b')	#returns 2
					type(my_dict.get('b')) 		#<class 'int'>
				my_dict.get('c')	#returns NoneType... (was deleted)
					type(my_dict.get('c'))			#<class 'NoneType'>
				--------
				-this will produce an ERROR (use GET, it defaults to NoneType if NOT FOUND)
				 my_dict['d']		#ERROR: KeyError: 'd'
				 my_dict['a']		#returns 1 (IF FOUND)
			GET (WITH DEFAULT)
				#DICTIONARY: GET METHODS (SAFELY GET A KEY)
				user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

				#get (with default, if not found)
				tc_id = user_ids.get('teraCoder', 100000)
				print(tc_id)			#100019

				stack_id = user_ids.get('superStackSmash', 100000)
				print(stack_id)		#100000 (default value)
			ITEMS 
				my_dict_items([('a', 1), ('b', 2)])
			ADD 
				my_dict['c'] = 3
				my_dict				#{'a': 1, 'b': 2, 'c': 3}
			UPDATE (=)(ASSIGNMENT)
				my_dict['c'] = 99
				my_dict				#{'a': 1, 'b': 2, 'c': 99}
			UPDATE (.update())
				d2.update({'a':13})
				d2					#{'a': 13, 'b': 2, 'c': 3}
			UPDATE (ADDS MULTIPLE KEYS)(OR DICT)
				#DICTIONARY: ADD MULTIPLE KEYS (UPDATE)
				user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

				user_ids.update({'theLooper': 138475, 'stringQueen': 85739})
				print(user_ids)
				#{'teraCoder': 9018293, 'stringQueen': 85739, 'theLooper': 138475, 'proProgrammer': 119238}
			
			DICTIONARY (**dict DOUBLE ASTERISK)(CONCATENATE, ADD TWO DICTIONARIES TOGETHER)
				https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
				dict1 = {'a':1, 'b':2}
				dict2 = {'c':3, 'd':4}
				dict = {**dict1, **dict2}
				dict						#{'a': 1, 'b': 2, 'c': 3, 'd': 4}
				*** WARNING, (if there are DUPLICATE KEYS, the LAST DICTIONARY (KEY) will overwrite it) ***
					>>> dict1 = {'a':1, 'b':2}
					>>> dict2 = {'b':99,'c':3, 'd':4}
					>>> d = {**dict1, **dict2}
					>>> d
					{'a': 1, 'b': 99, 'c': 3, 'd': 4}
				--------------
				**FIX**
				#create (OVERLAP)(in this case ADDING THE TWO (same key VALUES) is what we want
				>>> {k:v+v2 for k,v in dict1.items() for k2,v2 in dict2.items() if k == k2}
					{'b': 101}
				>>> overlap = {k:v+v2 for k,v in dict1.items() for k2,v2 in dict2.items() if k == k2}
				>>> d = {**dict1, **dict2, **overlap}
				>>> d
				{'a': 1, 'b': 101, 'c': 3, 'd': 4}

			LENGTH OF DICTIONARY 
				len(my_dict)		#returns 3
			LOOP DICTIONARY 
				for x in my_dict:
					print(x)
				#a
				#b
				#c
			LOOP (KEYS)
				test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
				for x in test_scores.keys():		#can OMIT (.keys()) will DEFAULT to KEYS (for x in test_scores:)
					print(x)
				#Grace
				#Jeffrey
				#Sylvia
				#Pedro
				#Martin
				#Dina
			LOOP (VALUES)
				for x in test_scores.values():
					print(x)
				#[80, 72, 90]
				#[88, 68, 81]
				#[80, 82, 84]
				#[98, 96, 95]
				#[78, 80, 78]
				#[64, 60, 75]		
			LOOP (SUM)(AGGREGATE)
				#DICTIONARY: (VALUES) GET ALL 
				num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

				total_exercises = 0
				for num in num_exercises.values():
				  total_exercises += num
				  #print(num)
				print("total: ", total_exercises)		#total:  115
			
			LOOP (CREATE A DICTIONARY)(FROM TWO LISTS)
				#DICTIONARIES: CREATE A DICTIONARY
				english = ['mountain', 'bread', 'friend', 'horse']
				sindarin = ['orod', 'bass', 'mellon', 'roch']

				translations = {}
				for (x, y) in zip(english, sindarin):
				  translations[x] = y
				  
				print(translations)
				#{'bread': 'bass', 'friend': 'mellon', 'mountain': 'orod', 'horse': 'roch'}	
			DICTIONARY (ITEMS)(LOOP KEY-VALUE)
				for k, v in num_exercises.items():
					print("key: " + str(k) + ", value: " + str(v))
				key: functions, value: 10
				key: syntax, value: 13
				key: control flow, value: 15
				key: loops, value: 22
				key: lists, value: 19
				key: classes, value: 18
				key: dictionaries, value: 18
				
			DICTIONARY (ITERATE)(ITEMS)(CONVERT TO LIST)
				-.ITEMS() generates TUPLE LIST
				num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
				list(num_exercises.items())				#[('functions', 10), ('syntax', 13), ('control flow', 15), ('loops', 22), ('lists', 19), ('classes', 18), ('dictionaries', 18)]
				list(num_exercises.items())[0]			#('functions', 10)
				list(num_exercises.items())[1]			#('syntax', 13)
				list(num_exercises.items())[1][0]		#'syntax'
				list(num_exercises.items())[1][1]		#13
			DICTIONARY (LIST COMPREHENSION)
				-create a DICTIONARY (like a LIST COMPREHENSION)
					#create dict
					plays = {k:v for k,v in zip(songs, playcounts)}
				
			LIST COMPREHENSION 
				*** BIG DIFFERENCE, IS THE (CURLY BRACES {}) instead of ([] for a LIST)
				#DICTIONARIES: LIST COMPREHENSION (TO DICT)
				#SYNTAX: students = {key:value for key, value in zip(names, heights)}
				drinks = ["espresso", "chai", "decaf", "drip"]
				caffeine = [64, 40, 0, 120]

				#zip lists
				zipped_drinks = zip(drinks, caffeine)
				#print(list(zipped_drinks))	#careful, makes ZIP EMPTY
				#create dict (from LIST COMPREHENSION)
				drinks_to_caffeine = {key:value for (key, value) in zipped_drinks}
				print(drinks_to_caffeine)
				#{'drip': 120, 'chai': 40, 'espresso': 64, 'decaf': 0}
			LIST (GENERATE LIST)(FROM VALUES)
				num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
				list(num_exercises.values())
					#[10, 13, 15, 22, 19, 18, 18]
			TYPE 
				type(my_dict)		#<class 'dict'>
			COPY 
				*** DON'T USE ASSIGNMENT (=) IT WILL JUST (REFERENCE) THE SAME OBJECT ***
				d2 = my_dict
				d2					#{'a': 1, 'b': 2, 'c': 3}
				my_dict['a'] = 22	#change value
				#both DICTIONARIES change
				my_dict				#{'a': 22, 'b': 2, 'c': 3}
				d2					#{'a': 22, 'b': 2, 'c': 3}
			COPY (GOOD) 
				#copy
					d2 = my_dict.copy()
				#both appear same
					d2					#{'a': 1, 'b': 2, 'c': 3}
					my_dict				#{'a': 1, 'b': 2, 'c': 3}
				#update
					my_dict['a'] = 22
				#check dictionaries (now two different dictionaries)
					my_dict				#{'a': 22, 'b': 2, 'c': 3}
					d2					#{'a': 1, 'b': 2, 'c': 3}
			DICTIONARY (TEST KEY)
				zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], 
					"earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}
				'earth' in zodiac_elements		#True
			DICTIONARY (GET KEY)
				dict = {'a': 1, 'b': 2, 'c': 3}
				# to get the KEY (one only) and save it to a variable (this is great if the KEY is an OBJECT)
				#   go through the DICTIONARY (the [0] will grab the FIRST ELEMENT of LIST RETURNED)(this works because THERE CAN ONLY BE ONE KEY)
				b = [x for x in dict if x == 'a'][0]
				b           #'a'
				#ERROR (because DOESN'T FIND ANYTHING IN LIST)(wrap in IF STATEMENT if empty list)
				b = [x for x in dict if x == 'd'][0]
				#FUNCTION: get_key (from dictionary)
				def get_key(dict, key_to_save):
					result = [x for x in dict if x == key_to_save]
					if result == []:
						return 'None'
					else:
						return result[0]
				get_key(dict, 'a')              #'a'
				get_key(dict, 'd')              #'None'    ('d' doesn't exist!)
		
	*** MOUSE PROBLEM, LOGITECH G302, I think the LEFT MOUSE BUTTON is STICKING, OR WORN OUT??? ***
		-changed it to he RIGHT BUTTON, and works AS EXPECTED...
		-WIRELESS MOUSE, still has BAD SCROLL WHEEL?? WTF? 
		
	-----------------------
	#DICTIONARIES: INTRO
	sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
	num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

	#TEST 
	print(sensors)
	-----------------------
	#DICTIONARIES: CREATE A DICTIONARY
	english = ['mountain', 'bread', 'friend', 'horse']
	sindarin = ['orod', 'bass', 'mellon', 'roch']

	translations = {}
	for (x, y) in zip(english, sindarin):
	  translations[x] = y
	  
	print(translations)
	#{'bread': 'bass', 'friend': 'mellon', 'mountain': 'orod', 'horse': 'roch'}	
	-----------------------	
	#DICTIONARIES: INVALID KEYS
	#unhashable...
	#children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
	children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

	#eg. powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
	#TypeError: unhashable type: 'list'
	#The word "unhashable" in this context means that this #'list' is an object that can be changed. Dictionaries in 
	#Python rely on each key having a hash value, a specific #identifier for the key. If the key can change, that hash 
	#value would not be reliable. So the keys must always be #unchangeable, hashable data types, like numbers or #strings.
	-----------------------
	#DICTIONARY: EMPTY DICTIONARY 
	empty_dict = {}
	my_empty_dictionary = {}
	print(my_empty_dictionary)
	-----------------------
	#DICTIONARY: ADD KEY 
	#SYNTAX:   my_dict["new_key"] = "new_value"
	#empty dict 
	animals_in_zoo = {}
	#add
	animals_in_zoo['zebras'] = 8
	animals_in_zoo['monkeys'] = 12
	animals_in_zoo['dinosaurs'] = 0
	#print 
	print(animals_in_zoo)	#{'dinosaurs': 0, 'monkeys': 12, 'zebras': 8}
	-----------------------
	#DICTIONARY: ADD MULTIPLE KEYS (UPDATE)
	user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

	user_ids.update({'theLooper': 138475, 'stringQueen': 85739})
	print(user_ids)
	#{'teraCoder': 9018293, 'stringQueen': 85739, 'theLooper': 138475, 'proProgrammer': 119238}
	-----------------------
	#DICTIONARY: OVERWRITE VALUES
	oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
	#add key 
	oscar_winners['Supporting Actress'] = "Viola Davis"
	#overwrite 
	oscar_winners['Best Picture'] = "Moonlight"
	#print
	print(oscar_winners)
	#{'Animated Feature': 'Zootopia', 'Best Actor': 'Casey Affleck', 'Best Actress': 'Emma Stone', 'Best Picture': 'Moonlight', 'Supporting Actress': 'Viola Davis'}
	-----------------------
	#DICTIONARIES: LIST COMPREHENSION (TO DICT)
	#SYNTAX: students = {key:value for key, value in zip(names, heights)}
	drinks = ["espresso", "chai", "decaf", "drip"]
	caffeine = [64, 40, 0, 120]

	#zip lists
	zipped_drinks = zip(drinks, caffeine)
	#print(list(zipped_drinks))	#careful, makes ZIP EMPTY
	#create dict (from LIST COMPREHENSION)
	drinks_to_caffeine = {key:value for (key, value) in zipped_drinks}
	print(drinks_to_caffeine)
	#{'drip': 120, 'chai': 40, 'espresso': 64, 'decaf': 0}
	-----------------------
	#DICTIONARY: REVIEW
	songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
	playcounts = [78, 29, 44, 21, 89, 5]

	#create dict
	plays = {k:v for k,v in zip(songs, playcounts)}
	#print 
	print(plays)
	#{'Good Vibrations': 5, 'Satisfaction': 29, 'Like a Rolling Stone': 78, "What's Going On": 21, 'Respect': 89, 'Imagine': 44}
	#add 
	plays["Purple Haze"] = 1
	#update
	plays["Respect"] = plays["Respect"] + 5

	#create dict 
	library = {"The Best Songs": plays, "Sunday Feelings": {}}
	#print
	print(library)
	#{'Sunday Feelings': {}, 'The Best Songs': {'Good Vibrations': 5, 'Purple Haze': 1, 'Like a Rolling Stone': 78, 'Imagine': 44, 'Satisfaction': 29, 'Respect': 94, "What's Going On": 21}}
	-----------------------	
	AUG.21, QUIZ#7 DICTIONARIES
		4/5 80%	 ...missed [] vs {} on last answer :(
		5/5 100% REDO
		
	AUG.22 DICTIONARIES (USING THEM...)
	-----------------------
	#DICTIONARY: GET A KEY
	zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

	print(zodiac_elements['earth'])
	#['Taurus', 'Virgo', 'Capricorn']
	print(zodiac_elements['fire'])
	#['Aries', 'Leo', 'Sagittarius']
	-----------------------
	#DICTIONARY: GET AN INVALID KEY
	zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}

	print(zodiac_elements["energy"])

	#TEST KEY
	print('earth' in zodiac_elements)		#True
	-----------------------
	#DICTIONARY: TRY-EXCEPT (TO GET A KEY)
	caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}

	try:
	  print(caffeine_level['matcha'])
	except KeyError as e:
	  print('Unknown Caffeine Level')	#Unknown Caffeine Level
	  print "KeyError: {0}".format(e)	#KeyError: 'matcha'
	-----------------------
	#DICTIONARY: GET METHODS (SAFELY GET A KEY)
	user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

	#get (with default, if not found)
	tc_id = user_ids.get('teraCoder', 100000)
	print(tc_id)			#100019

	stack_id = user_ids.get('superStackSmash', 100000)
	print(stack_id)		#100000 (default value)
	-----------------------
	#DICTIONARY: DELETE (A KEY)
	available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
	#health
	health_points = 20

	#get value, add to health, pop (deletes)
	health_points += available_items.pop("stamina grains", 0)
	print("health_points: ", health_points)		#health_points:  35
	health_points += available_items.pop("power stew", 0)
	print("health_points: ", health_points)		#health_points:  65
	health_points += available_items.pop("mystic bread", 0)
	print("health_points: ", health_points)		#health_points:  65
	print(available_items)
	#{'health potion': 10, 'strength sandwich': 25, 'green elixir': 20, 'cake of the cure': 5}
	-----------------------
	#DICTIONARY: (KEYS) GET ALL
	user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
	num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

	#get keys
	users = user_ids.keys()
	print("keys: ", list(users))
	#keys:  ['samTheJavaMaam', 'teraCoder', 'keysmithKeith', 'lyleLoop', 'pythonGuy']

	#get keys (using list)
	#lessons = list(num_exercises)
	lessons = num_exercises.keys()
	print(lessons)
	#dict_keys(['loops', 'functions', 'classes', 'dictionaries', 'lists', 'control flow', 'syntax'])
	-----------------------
	#DICTIONARY: (VALUES) GET ALL 
	num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

	total_exercises = 0
	for num in num_exercises.values():
	  total_exercises += num
	  #print(num)
	print("total: ", total_exercises)		#total:  115
	-----------------------
	#DICTIONARY: (ITEMS) GET ALL
	#gets BOTH (keys and values)(as a TUPLE)(key, value)
	pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

	for k, v in pct_women_in_occupation.items():
		print('Women make up {1} percent of {0}s.'.format(k, v))
	#Women make up 9 percent of Aerospace Engineers.
	#Women make up 40 percent of Physicians.
	#Women make up 37 percent of Lawyers.
	#...
	-----------------------
	#DICTIONARY: REVIEW (TAROT)
	tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

	#empty spread 
	spread = {}
	#1st draw (card 13)(pop out card)
	spread['past'] = tarot.pop(13)		#this TAKES OUT this card from TAROT
	#2nd draw (card 22)
	spread['present'] = tarot.pop(22)
	#3rd draw (card 10)
	spread['future'] = tarot.pop(10)

	#review spread 
	for k, v in spread.items():
	  print('Your {0} is the {1} card.'.format(k, v))
	#Your past is the Death card.
	#Your future is the Wheel of Fortune card.
	#Your present is the The Fool card.
	-----------------------
	AUG.22 QUIZ#8 	DICTIONARY USAGE 
		9/9 100% (found a couple errors in questions)
	
	AUG.22 TAROT (MY VERSION) 
		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\10b-Personal (Tarot, expand example)\
			tarot.py"
	
	AUG.23 PLAY (WITH COMBINATIONS)(AND VIGENERE CIPHER)
		a1 = [0, 1, 2]
		#three NESTED LOOP (creates 3 COLUMNS only...)(of ALL COMBINATIONS)
		def comb3(_list):
			for x in _list:
				for y in _list:
					for z in _list:
						print('{}, {}, {}'.format(x, y, z))
		comb3(a1)
			0, 0, 0
			0, 0, 1
			0, 0, 2
			0, 1, 0
			0, 1, 1
			0, 1, 2
			0, 2, 0
			0, 2, 1
			0, 2, 2
			1, 0, 0
			1, 0, 1
			1, 0, 2
			1, 1, 0
			1, 1, 1
			1, 1, 2
			1, 2, 0
			1, 2, 1
			1, 2, 2
			2, 0, 0
			2, 0, 1
			2, 0, 2
			2, 1, 0
			2, 1, 1
			2, 1, 2
			2, 2, 0
			2, 2, 1
			2, 2, 2
		------------------------------
		#FUNCTION: GENERATE (3 COLUMN LIST 2D ARRAY)
		def comb3(_list):
			result = []			#need to define (outside loop)
			for x in _list:
				for y in _list:
					for z in _list:
						#print('{}, {}, {}'.format(x, y, z))
						result.append([x, y, z])
			return result
		#TEST
		comb3(a1)
			#[
			[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], 
			[1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], 
			[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]
			]

	AUG.27, 2018 DICTIONARIES - CODING CHALLENGE 
	--------------------------------
	#DICTIONARY: SUM VALUES 
	#FUNCTION: SUM VALUES
	def sum_values(my_dictionary):
	  return sum([v for k,v in my_dictionary.items()])

	#TEST
	print(sum_values({"milk":5, "eggs":2, "flour": 3}))
	#returns 10
	print(sum_values({10:1, 100:2, 1000:3}))
	#returns 6
	--------------------------------
	#DICTIONARY: EVEN KEYS 
	#FUNCTION: EVEN KEYS 
	#def sum_even_keys(my_dictionary):
	#  return sum([v for k,v in my_dictionary.items()][1::2])
	def sum_even_keys(my_dictionary):
	  return sum([v for k,v in my_dictionary.items() if k % 2 == 0])

	#TEST
	print(sum_even_keys({1:5, 2:2, 3:3}))
	#returns 2
	print(sum_even_keys({10:1, 100:2, 1000:3}))
	#returns 6
	--------------------------------
	#DICTIONARY: ADD TEN 
	#FUNCTION: ADD TEN 
	def add_ten(my_dictionary):
	  return {k:v + 10 for k,v in my_dictionary.items()}

	#TEST
	print(add_ten({1:5, 2:2, 3:3}))
	#returns {1:15, 2:12, 3:13}
	print(add_ten({10:1, 100:2, 1000:3}))
	#returns {10:11, 100:12, 1000:13}	
	--------------------------------
	#DICTIONARY: VALUES THAT ARE KEYS 
	#FUNCTION: VALUES THAT ARE KEYS
	# if any KEYS are EQUAL to any VALUES then make LIST
	def values_that_are_keys(my_dictionary):
	  result = []
	  for k in my_dictionary.keys():
		for v in my_dictionary.values():
		  if k == v:
			result.append(k)
	  return result

	#TEST
	print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
	#returns [1, 4]
	print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
	#returns ["a"]
	--------------------------------
	#DICTIONARY: LARGEST VALUE
	#FUNCTION: LARGEST VALUE
	# gets the KEY of the MAXIMUM VALUE
	def max_key(my_dictionary):
	  max_value = max([v for k,v in my_dictionary.items()])
	  return [k for k,v in my_dictionary.items() if v == max_value][0]
	------
	def max_key(my_dictionary):
	  max_value = max([v for k,v in my_dictionary.items()])
	  #return [k for k,v in my_dictionary.items() if v == max_value][0]		#will RETURN (first max value only)
	  return [k for k,v in my_dictionary.items() if v == max_value]			#will RETURN (a list of all KEYS with max value)

	#TEST
	print(max_key({1:100, 2:1, 3:4, 4:10}))
	#returns 1 (because 100 is max value)
	print(max_key({"a":100, "b":10, "c":1000}))
	#returns "c" (because 1000 is max value)
	--------------------------------
	#DICTIONARY: WORD LENGTH DICT 
	#FUNCTION: WORD LENGTH DICT 
	def word_length_dictionary(words):
	  return {k:v for k,v in zip(words, [len(x) for x in words])}
	  
	#TEST
	print(word_length_dictionary(["apple", "dog", "cat"]))
	#returns {"apple":5, "dog": 3, "cat":3}
	print(word_length_dictionary(["a", ""]))
	#returns {"a": 1, "": 0}
	--------------------------------
	#DICTIONARY: FREQUENCY COUNT 
	#FUNCTION: FREQUENCY COUNT 
	def frequency_dictionary(words):
	  return {x:words.count(x) for x in words}

	#TEST
	print(frequency_dictionary(["apple", "apple", "cat", 1]))
	#returns {"apple":2, "cat":1, 1:1}
	print(frequency_dictionary([0,0,0,0,0]))
	#returns {0:5}	
	--------------------------------	
	#DICTIONARY: UNIQUE VALUES 
	#FUNCTION: UNIQUE VALUES 
	# use SET to convert a LIST to SET (this makes UNIQUE VALUES only) the do whatever you want
	# *** NOTE, I THINK THIS SORTS IT ***
	# here it makes a list (then gets the LENGTH of list)
	def unique_values(my_dictionary):
	  return len(list(set([v for k,v in my_dictionary.items()])))

	#TEST
	print(unique_values({0:3, 1:1, 4:1, 5:3}))
	#returns 2
	print(unique_values({0:3, 1:3, 4:3, 5:3}))
	#returns 1
	--------------------------------	
	AUG.28, 2018 (*** DIFFICULT ***)
	#DICTIONARY: COUNT FIRST LETTER
	# wow! this was a bit of work figuring this out...
	# got er done, Good Job Dean!
	# SET function (changed the ORDER) but it still seemed to work on Code Academy, more difficult to PRESERVE ORDER with UNIQE VALUES
	#FUNCTION: COUNT FIRST LETTER
	def count_first_letter(names):
	  result = {}		#empty dictionary
	  letters = list(set([k[0] for k,v in names.items()]))	#['L', 'S']
	  keys = [k[0] for k,v in names.items()]  				#['S', 'S', 'L']
	  values = [len(v) for k,v in names.items()]			#[3, 1, 3]
	  for l in letters:
		#s, sums ALL THE KEYS (that start with 'S' or 'L')
		s = sum([v for k,v in zip(keys, values) if k == l])
		result[l] = s
	  return result

	#TEST
	print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
	#returns {"S": 4, "L": 3}
	print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
	# should print {"S": 7}
	--------------------------------	
	*** IMPROVED previous... (see above) ***
	#DICTIONARY: COUNT FIRST LETTER
	def count_first_letter(t):
		result = {}
		for l in list(set([k[0] for k,v in t.items()])):    					#['L', 'S'], get LETTERS to iterate through
			result[l] = sum([len(v) for k,v in t.items() if k[0] == l])			#[3, 1], get SUM of SUB-LISTS (add this in ONE-STEP to NEW DICT)
		return result
	
	#TEST
	print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
	#returns {"S": 4, "L": 3}
	print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
	# should print {"S": 7}
	--------------------------------	
	
	MODULE (PYTHON PATH)
		-looking for HOW MODULES are loaded...
		-HTML PARSER 
			"C:\Program Files\Anaconda3\Lib\html\
				parser.py"
			--------------	
			...shows how to use REGEX (REGULAR EXPRESSIONS) to (PARSE HTML) an html file WOW!
			--------------
		-THIS FILE (contains MAP of all HTML CHARACTERS and UNICODE NUMBERS) (as dictionary)
		"C:\Program Files\Anaconda3\Lib\html\
			entities.py"
			--------------	*** OPEN IN NOTEPAD++ ***
			"""HTML character entity references."""

			__all__ = ['html5', 'name2codepoint', 'codepoint2name', 'entitydefs']


			# maps the HTML entity name to the Unicode code point
			name2codepoint = {
				'AElig':    0x00c6, # latin capital letter AE = latin capital ligature AE, U+00C6 ISOlat1
				'Aacute':   0x00c1, # latin capital letter A with acute, U+00C1 ISOlat1
				'Acirc':    0x00c2, # latin capital letter A with circumflex, U+00C2 ISOlat1
				...
			--------------
	
	AUG.28, 2018 MODULES (IMPORTS)
	MODULE, is like a PACKAGE of code (files or sets)
	MODULES (COMMON)
		import math 			(for math operators)
		import datetime 		(date and time)
		import re				(regular expressions)
		import itertools
		import inspect 			(introspection, looking inside classes and functions)
		import io 				(io = input, output) 
		import sys 				(sys = system)
		import unittest			(unit testing)???			https://codingdose.info/2018/03/22/supress-print-output-in-python/
		
	MODULE (RESOURCE)
		https://docs.python.org/3/tutorial/modules.html
		https://docs.python.org/3/library/index.html			PYTHON STANDARD LIBRARY
		https://pypi.org/search/								INSTALL MORE MODULES using (pip3, pip, conda, ...)
		-----------------
	??	__init.py__ FILE		This looks important?
	
		
		PRINT (SUPPRESS OUTPUT)
			https://codingdose.info/2018/03/22/supress-print-output-in-python/
			# remember to import io and sys
			import io
			import sys

			def salute(name):
				"""Says hi to someone."""
				print('Hi, {}!'.format(name))

			# create a text trap and redirect stdout
			text_trap = io.StringIO()
			sys.stdout = text_trap

			# execute our now mute function
			salute('Anne')
			print('abcdefghi')
			
			# now restore stdout function
			sys.stdout = sys.__stdout__
			
			#GET VALUE (all print displays trapped...
			trap.getvalue()
				"''\nabcdefghi\n"
	
		MODULE STRUCTURE 
		---
		#to import...
		import sound.effects.echo			#uses (echo.py) file
		#to call function (need full path)
		sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
		---------------------
		NAMESPACES 
		import random as r 		#use this if it becomes (too long) 
		r.randint(1, 10)		#returns 4, rather than calling (random.randint(1, 10))
		
		OR... 
		-THE DEFAULT (NAMESPACE) is (math) normally used as (math.sqrt(16))
		#import (WITH NAME)(ddd is name)
		import math as ddd
		ddd.sqrt(16)		#4.0
		---------------------
		IMPORTING TO LOCAL NAMESPACE (MORE SPECIFIC, only gets one function or thing)
		(SYNTAX: from {module} import {thing})
		eg.
			# imports the "date" data type from the "datetime" module
			from datetime import date
			
			py_release = date(2008, 12, 3)
			today = date.today()
			today					#returns datetime.date(2018, 8, 28)
			py_release				#returns datetime.date(2008, 12, 3)
			days_since_release = today - py_release
			days_since_release		#returns datetime.timedelta(3555)
		
		OR...
		#import (SYNTAX: from package import item)
		from sound.effects import echo
		#call...
		echo.echofilter(input, output, delay=0.7, atten=4)
		---------------------
		*** DANGER, this in NOT GOOD to do ***
		from {module} import *			#THIS IMPORTS (ALL FUNCTIONS, VARIABLES, AND CLASSES)
		*** May run into a NAMING CONFLICT with unexpected results ***
			eg. 
			from math import * 
			#now lets define a method...
			def sqrt(num):
				return 33 
			math.sqrt(16)		#returns 4.0 
			sqrt(16)			#returns 33 
			#HOWEVER, depending WHAT WAS DEFINED LAST (if I import MATH AGAIN, it will *** OVERWRITE OUR FUNCTION!!!! ***
			from math import * 
			math.sqrt(16)		#returns 4.0 
			sqrt(16)			#returns 4.0 
		---------------------
			sound/                          Top-level package
		  __init__.py               Initialize the sound package
		  formats/                  Subpackage for file format conversions
				  __init__.py
				  wavread.py
				  wavwrite.py
				  aiffread.py
				  aiffwrite.py
				  auread.py
				  auwrite.py
				  ...
		  effects/                  Subpackage for sound effects
				  __init__.py
				  echo.py
				  surround.py
				  reverse.py
				  ...
		  filters/                  Subpackage for filters
				  __init__.py
				  equalizer.py
				  vocoder.py
				  karaoke.py
		-----------------
		-Book: Python the Hard Way (p.146)
			-MODULES, are just like a DICTIONARY 
			-file (mystuff.py) has a FUNCTION called (apple()) in it...
				-you can IMPORT it...
				-*** CREATES a (__pycache__) FOLDER when I used IMPORT ***
				-*** NOTE, if you EDIT FILE, you need to RESTART POWERSHELL (YOU DON'T NEED TO RENAME (__pycache__) FOLDER so it RECREATES IT...) ***
				------------------
				mystuff.py
				------------------
				#learn to load MODULES (FUNCTIONS) from files and use them... :)

				#FUNCTION:
				def apple():
					print('How do you like dem apples! Booooy!')

				#VARIABLE 
				tang = 'I am an orange, sorta...'		#tang = tangerine
				tang2 = 'I AM AN ORANGE!'
				------------------
				-go to DIRECTORY where FILE IS IN...
				-go to PYTHON prompt 
				import mystuff
				mystuff.apple()
					#How do you like dem apples!
				mystuff.tang2
					#'I AM AN ORANGE!'
				mystuff.tang
					#'I am an orange, sorta...'
		-----------------
		from decimal import Decimal
		gum = Decimal('0.10')
		gumdrop = Decimal('0.35')
		gum + gumdrop
			#returns Decimal('0.45')
			
		#rounding problem...
		0.10 + 0.35
			#0.44999999999999996
		#solution
		((0.10 * 100) + (0.35 * 100)) / 100
			#0.45
		-----------------
		import math
		sine = math.sin(10)
		sine		#-0.5440211108893698
		sine2 = math.sin(30)
		sine2		#-0.9880316240928618
		sine3 = math.sin(45)
		sine3		#0.8509035245341184
		-----------------
		MODULES (GET A LIST OF FUNCTIONS)
		import math 
		dir(math) 	#THIS SHOWS A BUNCH OF FUNCTION NAMES...
			['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
			'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 
			'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 
			'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 
			'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
		-to fine MORE INFO...
			-GOOGLE (python module math.sprt)
			https://docs.python.org/3/library/math.html
	---------------------------------------------------------------
	LIST COMPREHENSION vs GENERATOR FUNCTIONS 
		https://docs.python.org/3/howto/functional.html?highlight=list%20comprehension
		yield KEYWORD?
		next METHOD
		-----------
		def gen(n):
			for i in range(n):
				yield i
		gen(3)
			<generator object gen at 0x000001F045870518>
		d = gen(3)
		d
			<generator object gen at 0x000001F045870518>
		next(d)				#0
		next(d)				#1
		next(d)				#2
		next(d)				#3
		next(d)
							Traceback (most recent call last):
							  File "<stdin>", line 1, in <module>
							StopIteration
		-----------
	ENUMERATE FUNCTION (used with DICTIONARY)
		https://docs.python.org/3/howto/functional.html?highlight=list%20comprehension
		enumerate()
		-use to GET INDEX based on CONDITION 
		>>> t
		{'stark': 3, 'snow': 1, 'lannister': 3}
		>>> for i in enumerate(t):
		...     print(i)
		...
		(0, 'stark')
		(1, 'snow')
		(2, 'lannister')
	OTHER METHODS (look into...)
		https://docs.python.org/3/howto/functional.html?highlight=list%20comprehension
		enumerate()									https://docs.python.org/3/library/functions.html#enumerate
		sorted(iterable, key=None, reverse=False)	https://docs.python.org/3/library/functions.html#sorted
		itertools.count(start, step) 				https://docs.python.org/3/howto/functional.html?highlight=list%20comprehension
		itertools.cycle(iter)
		itertools.repeat(elem, [n])
		itertools.combinations([1, 2, 3, 4, 5], 2) =>
			  (1, 2), (1, 3), (1, 4), (1, 5),
			  (2, 3), (2, 4), (2, 5),
			  (3, 4), (3, 5),
			  (4, 5)
		itertools.permutations([1, 2, 3, 4, 5], 2) =>
			  (1, 2), (1, 3), (1, 4), (1, 5),
			  (2, 1), (2, 3), (2, 4), (2, 5),
			  (3, 1), (3, 2), (3, 4), (3, 5),
			  (4, 1), (4, 2), (4, 3), (4, 5),
			  (5, 1), (5, 2), (5, 3), (5, 4)
		any()										https://docs.python.org/3/library/functions.html#any
			-IF (ANY) of the ELEMENTS in the LIST (are TRUE)
			any([0, 1, 0])		#True
			any([0, 0, 0])		#False
			any([1, 1, 1])		#True
		all()										https://docs.python.org/3/library/functions.html#all
			-IF (ALL) of the ELEMENTS in the LIST (are TRUE)
			all([0, 1, 0])		#False
			all([0, 0, 0])		#False
			all([1, 1, 1])		#True
	-------------------
	AUG.28 PLAYING WITH PERMUATIONS 
	import itertools
	itertools.permutations('abc',3)
		<itertools.permutations object at 0x00000245C90BA7D8>
	list(itertools.permutations('abc',3))
		[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
	list(itertools.permutations('abc',2))
		[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
	----
	USING (LIST COMPREHENSION) WE CAN DO THE SAME THING 
		-beautiful thing here is I CAN CHANGE AND SEE HOW IT WORKS 
		-PERMUTATIONS (seem to have UNIQUE VALUES only)(NO REPEATS)
		------------
		[(x,y,z) for x in 'abc' for y in 'abc' for z in 'abc' if x != y and x != z and y != z]
			[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
		------------
		[(x,y) for x in range(2) for y in range(2)]
			[(0, 0), (0, 1), (1, 0), (1, 1)]
		------------
		[(x,y) for x in range(2) for y in range(2) if x != y]
			[(0, 1), (1, 0)]
		------------
		[(x,y) for x in range(2) for y in range(2) if x == y]
			[(0, 0), (1, 1)]
		------------
		[(x,y) for x in 'abc' for y in 'abc' if x == y]
			[('a', 'a'), ('b', 'b'), ('c', 'c')]
		------------
		[(x,y) for x in 'abc' for y in 'abc' if x != y]
			[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
		------------
		*** I CAN CONTROL THE (DEPTH) PERFECTLY HERE ***
		-NOTE, the TWO LISTS are different lengths ('ab', 'abc')
		[(x,y) for x in 'ab' for y in 'abc']
			[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c')]
		------------
		[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1]]
			[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
		------------
		*** TRUTH TABLE ***
		[(x,y,z,w) for x in [0,1] for y in [0,1] for z in [0,1] for w in [0,1]]
			[
			(0, 0, 0, 0), 
			(0, 0, 0, 1), 
			(0, 0, 1, 0), 
			(0, 0, 1, 1),
			
			(0, 1, 0, 0),
			(0, 1, 0, 1), 
			(0, 1, 1, 0), 
			(0, 1, 1, 1), 
			
			(1, 0, 0, 0), 
			(1, 0, 0, 1), 
			(1, 0, 1, 0), 
			(1, 0, 1, 1), 
			
			(1, 1, 0, 0), 
			(1, 1, 0, 1), 
			(1, 1, 1, 0), 
			(1, 1, 1, 1)
			]
		-------------------------
		FILTERING...
		-resembles PASCAL'S TRIANGLE (ROW 1331)(because there are THREE ELEMENTS in two inner results)
		[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1] if (x + y + z) == 0]
			[(0, 0, 0)]
		[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1] if (x + y + z) == 1]
			[(0, 0, 1), (0, 1, 0), (1, 0, 0)]
		[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1] if (x + y + z) == 2]
			[(0, 1, 1), (1, 0, 1), (1, 1, 0)]
		[(x,y,z) for x in [0,1] for y in [0,1] for z in [0,1] if (x + y + z) == 3]
			[(1, 1, 1)]
		------------------------
		FILTERING...
		-resembles PASCAL'S TRIANGLE (ROW 121)
		[(x,y) for x in [0,1] for y in [0,1] if (x + y) == 0]
			[(0, 0)]
		[(x,y) for x in [0,1] for y in [0,1] if (x + y) == 1]
			[(0, 1), (1, 0)]
		[(x,y) for x in [0,1] for y in [0,1] if (x + y) == 2]
			[(1, 1)]
		------------------------
		FILTERING... (TWO DIFFERENT LISTS [0,1] and [0,1,2])
		-resembles PASCAL'S TRIANGLE (11 x 111)(row 1221)
		[(x,y) for x in [0,1] for y in [0,1,2]]
			[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
		[(x,y) for x in [0,1] for y in [0,1,2] if (x + y) == 0]
			[(0, 0)]
		[(x,y) for x in [0,1] for y in [0,1,2] if (x + y) == 1]
			[(0, 1), (1, 0)]
		[(x,y) for x in [0,1] for y in [0,1,2] if (x + y) == 2]
			[(0, 2), (1, 1)]
		[(x,y) for x in [0,1] for y in [0,1,2] if (x + y) == 3]
			[(1, 2)]
		------------------------
		TRUTH TABLE (KEY)
		>>> t = [(x,y) for x in [0,1] for y in [0,1]]
		>>> t[0]
		(0, 0)
		>>> (0,1) == t[0]
		False
		>>> (0,1) == t[1]
		True
		>>> (0,1) == t[2]
		False
		>>> (0,1) == t[3]
		False
		>>> a = 0
		>>> b = 1
		>>> (a,b) == t[3]
		False
		>>> (a,b) == t[0]
		False
		>>> (a,b) == t[1]
		True
		>>> (a,b) == t[2]
		False
		>>> (a,b) == t[3]
		False
		------------------------	
		TRUTH TABLE (DUAL KEY)
		-the truth table is actually a (DUAL KEY) this is a BRAIN MOMENT WOW!!!
		-use a TUPLE for the KEY (DICTIONARY)
		d = {(0,0): 'a', (0,1): 'b', (1,0): 'c', (1,1): 'd'}
		d[(0,0)]		#'a'
		---
		>>> _AND = {(0,0): 0, (0,1): 0, (1,0): 0, (1,1): 1}
		>>> _AND[(1,1)]
		1
		>>> _AND[(1,0)]
		0
		>>> _AND[(0,0)]
		0
		>>> _AND[(1,0)]
		0
		------------------------
		HOW TO MAP (MY OWN VALUES)(TO A KEY)(AUTOMATICALLY)
		>>> k = [(x,y) for x in [0,1] for y in [0,1]]
		>>> v = ['Dean', 'Nadine', 'Vivian', 'Muppet']
		>>> d = {k:v for k,v in zip(k,v)}
		>>> d
		{(0, 0): 'Dean', (0, 1): 'Nadine', (1, 0): 'Vivian', (1, 1): 'Muppet'}
		------------------------	
		#ACCESS DICTIONARY, BASED ON VALUES...
		def test(a, b):
			return d[(a,b)]
		
		test(0,0)		#'Dean'
		test(0,1)		#'Nadine'
		test(1,0)		#'Vivian'
		test(1,1)		#'Muppet'
		------------------------
	------------------------	
	#FUNCTION: LIST OF POWERS (SUM NUMBER)
	# creates a LIST of POWERS OF TWO (that SUM to the NUMBER)
	def sum_powers2(num):
		temp = num      #temp number
		pick = 0
		result = []
		# powers of 2
		my_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
		#loop through list
		while (temp != 0):
			# max num without going over
			pick = max([x for x in my_list if x <= temp])
			result.append(pick)     #add to list
			temp = temp - pick      #counter (also LIST value)
		result.sort()               #doesn't return value
		return result
	#TEST
	sum_powers2(5)      #[1, 4]
	sum_powers2(7)      #[1, 2, 4]
	sum_powers2(16)     #[16]
	sum_powers2(127)    #[1, 2, 4, 8, 16, 32, 64]
	------------------------
	#FUNCTION: GET (LIST OF) DAYS
	# num = saves a ONE NUMBER (for a LIST of)(days of week, to index)
	# num = sum of list of indexes [1, 4] --> sums to 5
	def get_days(num):  
		# days of week (dictionary)
		days_of_week = {"Sunday": 1, "Monday": 2, "Tuesday": 4, "Wednesday": 8, "Thursday": 16, "Friday": 32, "Saturday": 64}
		return [k for k,v in days_of_week.items() for y in sum_powers2(num) if y == v]
	#TEST
	# num = 5 ([1,4] --> ['Sunday', 'Tuesday'])
	get_days(5)         #['Sunday', 'Tuesday']
	get_days(7)         #['Sunday', 'Monday', 'Tuesday']
	# weekend only [1, 64]
	get_days(65)        #['Sunday', 'Saturday']
	# weekdays only [2,4,8,16,32]
	get_days(62)        #['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

	# print all
	for x in range(128):
		print(get_days(x))
	# []
	# ['Sunday']
	# ['Monday']
	# ['Sunday', 'Monday']
	# ['Tuesday']
	# ['Sunday', 'Tuesday']
	# ['Monday', 'Tuesday']
	# ['Sunday', 'Monday', 'Tuesday']
	# ...
	# ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	------------------------
	
	AUG.30 CLASSES (OBJECTS)
	------------------------
	#TYPES
	print(type(5))				#<class 'int'>

	my_dict = {}
	print(type(my_dict))		#class 'dict'>

	my_list = []
	print(type(my_list))		#<class 'list'>
	------------------------
	#CLASS: CREATING A CLASS
	# create a class 
	class Facade:
	  pass
	------------------------
	#CLASS: INSTANTIATION
	# define class
	class Facade:
	  pass

	# instantiate object 
	facade_1 = Facade()
	------------------------
	#CLASS: TYPE OF CLASS (__main__)
	class Facade:
	  pass

	# instance (object)
	facade_1 = Facade()

	#TYPE (will return the CLASS DEFINITION)
	facade_1_type = type(facade_1)
	print(facade_1_type)			#<class '__main__.Facade'>

	#(__main__)(means the CURRENT FILE *.py we are running)
	------------------------
	#play with CLASS VARIABLES...
	class Musician:
		title = 'Rockstar'

	d = Musician()
	d					#<__main__.Musician object at 0x0000027E2A3D5128>
	d.title				#'Rockstar'
	------------------------
	#CLASS: VARIABLES
	#create class 
	class Grade:
	  minimum_passing = 65
	------------------------
	#CLASS: SELF (argument)
	>>> class Dog():
	...     dog_years = 7
	...     #
	...     def dog_hello(self):
	...             print('Dogs experience {} years for every 1 year for a human'.format(self.dog_years))
	...
	>>> d1 = Dog()
	>>> d1.dog_hello()
	Dogs experience 7 years for every 1 year for a human
	------------------------
	#CLASS: METHODS 
	# a METHOD is a FUNCTION that is in a CLASS
	# SELF is the (instance of the object)
	# the FIRST ARGUMENT (is always)(self) in a METHOD

	# create class 
	class Rules():
	  def washing_brushes(self):
		return "Point bristles towards the basin while washing your brushes."
	------------------------
	#CLASS: METHOD (WITH ARGUMENTS)

	# create a class 
	class Circle():
	  pi = 3.14
	  
	  def area(self, radius):
		return self.pi * radius ** 2
	  
	# create instance (object)
	circle = Circle()
	pizza_area = circle.area(12 / 2)					#113.04
	teaching_table_area = circle.area(36 / 2)	#1017.36
	round_room_area = circle.area(11460 / 2)	#103095306.0
	print(pizza_area)
	print(teaching_table_area)
	print(round_room_area)
	------------------------
	#CLASS: CONSTRUCTORS 
	# dunder methods (the double underscore methods)(eg. __main__)
	# (__init__)(is the CONSTRUCTOR method)
	# the CONSTRUCTOR initializes the OBJECT

	# create a class
	class Circle:
	  pi = 3.14
	  
	  # constructor
	  def __init__(self, diameter):
		print("New circle with diameter: {dia}".format(dia=diameter))
		
	teaching_table = Circle(36)		#New circle with diameter: 36
	------------------------
	#CLASS: INSTANCE VARIABLES
	# there are (class variables) and (instance variables), the instance variables are for (each object) the class variables are (global to all the objects)

	# create a class
	class Store:
	  pass

	# instantiate objects
	alternative_rocks = Store()
	isabelles_ices = Store()

	# instance variable 
	alternative_rocks.store_name = "Alternative Rocks"
	isabelles_ices.store_name = "Isabelle's Ices"

	# these are stored in the (dictionary)
	alternative_rocks.__dict__
	#{'store_name': 'Alternative Rocks'}
	------------------------
	#CLASS: VARIABLES (__dict__)
	-variables are stored in (__dict__)
	>>> class Store:t.
	...   pass
	>>> a = Store()
	>>> a.aaa = 123
	>>> a.bbb = 200
	>>> a.ccc = 300
	>>> a
	<__main__.Store object at 0x0000027E2A3D5358>
	>>> a.aaa
	123
	>>> a.bbb
	200
	>>> a.ccc
	300
	>>> a.ddd								#THIS DOESN'T EXIST (in __dict__ so it errors AttributeError)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Store' object has no attribute 'ddd'
	------------------------
	>>> a.__dict__
	{'aaa': 123, 'bbb': 200, 'ccc': 300}
	------------------------
	>>> class Test:
	...     my_global = 33
	...     def __init__(self, url):
	...             self.url = url
	...
	>>> t = Test('test')
	>>> t2 = Test('test2')
	---
	dir(t2)
	[... '__dict__', 'my_global', 'url']
	__dict__ 	(the dictionary)(stores OBJECT VARIABLES)
	(my_global, url) are variables stored in the object here...
	t.my_global			#33
	t.__dict__			#{'url': 'test'}
	------------------------
	#CLASS: GLOBAL vs INSTANCE (OBJECT) VARIABLES
	# create class
	class Circle:
	  # global variable
	  pi = 3.14
	  def __init__(self, diameter):
		# intance variable 
		self.radius = diameter / 2
		print("Creating circle with diameter {d}".format(d=diameter))
	  def circumference(self):
		return 2 * self.pi * self.radius
		
	  
	medium_pizza = Circle(12)
	teaching_table = Circle(36)
	round_room = Circle(11460)
	print('medium_pizza: ', medium_pizza.circumference())
	print('teaching_table: ', teaching_table.circumference())
	print('round_room: ', round_room.circumference())
	#medium_pizza:  37.68
	#teaching_table:  113.04
	#round_room:  35984.4
	------------------------
	#CLASS: DIR() FUNCTION (EVERYTHING IS AN OBJECT)
	# dir() FUNCTION (use to inspect an object)

	# inspect ATTRIBUTES for (an int)
	print(dir(5))

	#define function
	def this_function_is_an_object(arg1, arg2):
	  return arg1 + arg2

	print('-' * 20)
	print(dir(this_function_is_an_object))
	#['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', 
	'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', 
	'__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', 
	'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
	------------------------
	#CLASS: (__REPR__) STRING (REPR) REPRESENTATION
	# this is like the (ToString()) methods in C#
	# if you PRINT the object, rather than giving you an object, you can choose your format

	#create class
	class Circle:
	  pi = 3.14
	  
	  def __init__(self, diameter):
		self.radius = diameter / 2
	  
	  def area(self):
		return self.pi * self.radius ** 2
	  
	  def circumference(self):
		return self.pi * 2 * self.radius
	  
	  # string function
	  def __repr__(self):
		return 'Circle with radius {}'.format(self.radius)
	  
	  
	medium_pizza = Circle(12)
	teaching_table = Circle(36)
	round_room = Circle(11460)
	
	print(medium_pizza)
	print(teaching_table)
	print(round_room)
	#Circle with radius 6.0
	#Circle with radius 18.0
	#Circle with radius 5730.0
	------------------------
	#CLASS: REVIEW
	#create class 
	class Student():
	  #global variables
	  #constructor
	  def __init__(self, name, year):
		self.name = name
		self.year = year
		self.grades = [] 		#empty
	  #string (repr) representation
	  def __repr__(self):
		return 'name: {}, year: {}, grades: {}'.format(self.name, self.year, self.grades)
	  #methods
	  def add_grade(self, grade):
		if isinstance(grade, Grade):	#test (Grade object)
		  self.grades.append(grade)
		
	#create objects 
	roger = Student('Roger van der Weyden', 10)
	sandro = Student('Sandro Botticelli', 12)
	pieter = Student('Pieter Bruegel the Elder', 8)

	#-----
	#create class
	class Grade():
	  #global variables
	  minimum_passing = 65
	  #constructor
	  def __init__(self, score):
		self.score = score
	  #string (repr) representation
	  def __repr__(self):
		return 'score: {}'.format(self.score)
	  
		
	#create grade (then add to student object)
	pieter.add_grade(Grade(100))
		
	print(pieter)
	#name: Pieter Bruegel the Elder, year: 8, grades: [score: 100]
	------------------------
	
	SEP.01, 2018 INHERITANCE AND POLYMORPHISM
		https://www.programiz.com/python-programming/inheritance
	------------------------
	#INHERITANCE AND POLYMORPHISM: INHERITANCE
	# Inheritance: (basic --> more detail)
	# SYNTAX 
	# class Child(Parent):

	# eg. 
	# PARENT CLASS
	# class User:
	#   is_admin = False
	#   def __init__(self, username)
	#     self.username = username
	# 
	# CHILD CLASS
	# class Admin(User):
	#   is_admin = True

	# create class (PARENT)
	class Bin:
	  pass
	# create class (CHILD)
	class RecyclingBin(Bin):
	  pass
	------------------------
	#CUSTOM EXCEPTION EXAMPLE 
		#CUSTOM EXCEPTION
		class OutOfStock(Exception):
		  """
		  We ran out of candles...
		  """
		  
		#DEFINE CLASS 
		class CandleShop:
		  def __init__(self, stock):
			self.stock = stock
		  def buy(self, color):
			  if self.stock[color] == 0:							#TEST (TO RAISE EXCEPTION)
				raise OutOfStock(color)								#RAISE EXCEPTION (if someone tries to buy when ZERO)
			  else:
				self.stock[color] = self.stock[color] - 1
		  
		#TRY-EXCEPT
			try:
			  candle_shop.buy('green')
			except OutOfStock as err:
			  print('OutOfStock ERROR: {}'.format(err.args[0]))		#OutOfStock ERROR: green
	------------------------
	#CUSTOM EXCEPTION ii (GLOBAL VARIABLES)
		#create error (add any variables...)
		class MyError(Exception):
			message = 'My error occured, lets have a funeral'
			type = 'MYERROR'
			code = 666

		#test error...
		try:
			raise MyError
		except MyError as err:
			print('MyError: \n\tmessage: {}, \n\ttype: {}, code: {}'.format(err.message, err.type, err.code))

		#returns...
		MyError:
				message: My error occured, lets have a funeral,
				type: MYERROR, code: 666
	------------------------
	#CUSTOM EXCEPTION iii (WITH CONSTRUCTOR)
		#create exception (with constructor)
		class MyError(Exception):
			def __init__(self, message):
			  self.message = message
		  
		try:
			raise MyError('This error happened right here, in this OBJECT')
		except MyError as err:
			print('MyError: message: {}'.format(err.args[0]))
			
		#MyError: message: This error happened right here, in this OBJECT
	------------------------
	SEP.01 EXCEPTIONS 
		https://www.tutorialspoint.com/python/python_exceptions.htm
		https://docs.python.org/3/library/exceptions.html#exception-hierarchy
		BaseException
	 +-- SystemExit
	 +-- KeyboardInterrupt
	 +-- GeneratorExit
	 +-- Exception
		  +-- StopIteration
		  +-- StopAsyncIteration
		  +-- ArithmeticError
		  |    +-- FloatingPointError
		  |    +-- OverflowError
		  |    +-- ZeroDivisionError
		  +-- AssertionError
		  +-- AttributeError
		  +-- BufferError
		  +-- EOFError
		  +-- ImportError
		  |    +-- ModuleNotFoundError
		  +-- LookupError
		  |    +-- IndexError
		  |    +-- KeyError
		  +-- MemoryError
		  +-- NameError
		  |    +-- UnboundLocalError
		  +-- OSError
		  |    +-- BlockingIOError
		  |    +-- ChildProcessError
		  |    +-- ConnectionError
		  |    |    +-- BrokenPipeError
		  |    |    +-- ConnectionAbortedError
		  |    |    +-- ConnectionRefusedError
		  |    |    +-- ConnectionResetError
		  |    +-- FileExistsError
		  |    +-- FileNotFoundError
		  |    +-- InterruptedError
		  |    +-- IsADirectoryError
		  |    +-- NotADirectoryError
		  |    +-- PermissionError
		  |    +-- ProcessLookupError
		  |    +-- TimeoutError
		  +-- ReferenceError
		  +-- RuntimeError
		  |    +-- NotImplementedError
		  |    +-- RecursionError
		  +-- SyntaxError
		  |    +-- IndentationError
		  |         +-- TabError
		  +-- SystemError
		  +-- TypeError
		  +-- ValueError
		  |    +-- UnicodeError
		  |         +-- UnicodeDecodeError
		  |         +-- UnicodeEncodeError
		  |         +-- UnicodeTranslateError
		  +-- Warning
			   +-- DeprecationWarning
			   +-- PendingDeprecationWarning
			   +-- RuntimeWarning
			   +-- SyntaxWarning
			   +-- UserWarning
			   +-- FutureWarning
			   +-- ImportWarning
			   +-- UnicodeWarning
			   +-- BytesWarning
			   +-- ResourceWarning
	------------------------	
	#ISSUBCLASS METHOD
		-tests to see if a CLASS is a SUB-CLASS
		https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/
			class Base():
				pass

			class MySubClass(Base):
				pass
		
			issubclass(Base, MySubClass)		#False
			issubclass(MySubClass, Base)		#True
	------------------------
	#INHERITANCE AND POLYMORPHISM: EXCEPTIONS
		# EXCEPTION CLASS (exceptions come from this class)
		# issubclass() (tests for sub-class, inheritance)
		# issubclass(class1, class2) 
		#   (if class1 is sub-class of class2 then TRUE)
		#   (if class2 is sub-class of class1 then FALSE)
		#   (else TypeError if either are NOT classes)

		#---------------------------------
		# issubclass(ZeroDivisionError, Exception)        #True
		# issubclass(Exception, ZeroDivisionError)        #False
		# issubclass(Exception2, ZeroDivisionError)       #NameError (Exception2 doesn't exist)
		# Exception2 = 33
		# issubclass(Exception2, ZeroDivisionError)       #TypeError (because it's still not a class)
		#---------------------------------
		# ?? EXCEPTION INHERITANCE 
		# ?? raise RefrigeratorException (raise exception)
		# class KitchenException(Exception):
		#   """
		#   Exception that gets thrown when a kitchen appliance isn't working
		#   """
		# 
		# class MicrowaveException(KitchenException):
		#   """
		#   Exception for when the microwave stops working
		#   """
		# 
		# class RefrigeratorException(KitchenException):
		#   """
		#   Exception for when the refrigerator stops working
		#   """

		# def get_food_from_fridge():
		#   if refrigerator.cooling == False:
		#     raise RefrigeratorException
		#   else:
		#     return food
		#---------------------------------

		# custom exception
		class OutOfStock(Exception):
		  """
		  We ran out of candles...
		  """
		  
		# Update the class below to raise OutOfStock
		class CandleShop:
		  name = "Here's a Hot Tip: Buy Drip Candles"
		  def __init__(self, stock):
			self.stock = stock
		  def buy(self, color):
			  if self.stock[color] == 0:
				raise OutOfStock(color)					#RAISE EXCEPTION
			  else:
				self.stock[color] = self.stock[color] - 1

		#create candle shop
		candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
		#check what's in shop 
		candle_shop.__dict__			#{'stock': {'blue': 6, 'red': 2, 'green': 0}}
		#buy a (blue) candle
		candle_shop.buy('blue')

		#---------------------------------
		# BAD FORMAT (need to add TRY-EXCEPT)
		#candle_shop.buy('green')
		# Traceback (most recent call last):
		#   File "<stdin>", line 1, in <module>
		#   File "<stdin>", line 7, in buy
		# __main__.OutOfStock: green
		#---------------------------------
		# BETTER FORMAT 
		#buy a (green) candle (OUT OF STOCK)
		try:
		  candle_shop.buy('green')
		except OutOfStock as err:
		  print('OutOfStock ERROR: {}'.format(err.args[0]))	#OutOfStock ERROR: green
		#---------------------------------
	------------------------
	#INHERITANCE AND POLYMORPHISM: OVERRIDING METHODS

	class Message:
	  def __init__(self, sender, recipient, text):
		self.sender = sender
		self.recipient = recipient
		self.text = text

	class User:
	  def __init__(self, username):
		self.username = username
		
	  def edit_message(self, message, new_text):
		if message.sender == self.username:
		  message.text = new_text
		  
	#----------------------------
	#create subclass (of User class)
	class Admin(User):
	  #override method (from parent class)
	  def edit_message(self, message, new_text):
		#removed (conditional)(like in parent class)
		message.text = new_text
	------------------------
	SUPER() (GETS PARENT CLASS)
		super()									(implicit)(it's implied who is the PARENT CLASS)(benefit here is if the classes change, the super() method doesn't)
		Book.__init__(self, title, isbn)  		(explicit)(this references exactly as it's stated)(disadvantage if classes change, this has to change)
		https://www.pythonforbeginners.com/super/working-python-super-function
		SYNTAX
			super().methodName(args)						#Python 3 
			super(subClass, instance).method(args)			#Older Python
		REQUIREMENTS (TO USE)
			-The method being called upon by super() must exist
			-Both the caller and callee functions need to have a matching argument signature
			-Every occurrence of the method must include super() after you use it
		----------
		class MyParentClass(object):
			def __init__(self):
				print('MyParentClass_init')

		class SubClass(MyParentClass):
			def __init__(self):
				MyParentClass.__init__(self)
				print('SubClass_init')
		s = SubClass()
		MyParentClass_init
		SubClass_init
		----------------------
		class Grandpa(object):
			def __init__(self):
				print('Grandpa')
		class Dad(Grandpa):
			def __init__(self):
				Grandpa.__init__(self)
				print('Dad')
		class Child1(Dad):
			def __init__(self):
				Dad.__init__(self)
				print('Child')
		c1 = Child1()
		#Grandpa
		#Dad
		#Child
		class Child2(Dad):
			def __init__(self):
				Grandpa.__init__(self)
				print('Child')
		c2 = Child2()
		#Grandpa
		#Child
		----------------------
		class A():
			def __init__(self, x, y):
				print('Parent: ', x, y)

		class B(A):
			def __init__(self, x, y):
				super().__init__(x, y)
				print('Child: ', x, y)
		a = B(2, 3)
		# Parent:  2 3
		# Child:  2 3	


	#SUPER (METHOD) 
	https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
	https://www.artima.com/weblogs/viewpost.jsp?thread=236275
	https://docs.python.org/2/library/functions.html#super
	------------------------
	SEP.2, 2018 (CONTINUE CLASSES) SUPER 
	class Sink:
	  def __init__(self, basin, nozzle):
		self.basin = basin
		self.nozzle = nozzle

	class KitchenSink(Sink):
	  def __init__(self, basin, nozzle, trash_compactor=None):
		#super().__init__(self, basin, nozzle)						#THIS GETS AN ERROR 
		super().__init__(basin, nozzle)								#REMOVE (self argument)(because I was getting NUMBER of arguments ERROR)
		if trash_compactor:
		  self.trash_compactor = trash_compactor
		  
	k = KitchenSink('b','n')
	k.__dict__						
		#{'basin': 'b', 'nozzle': 'n'}
	k2 = KitchenSink('b','n', 'trash')
	k2.__dict__
		#{'basin': 'b', 'nozzle': 'n', 'trash_compactor': 'trash'}
	-------------------------
	#SUPER (WITH ARGUMENTS)
	class BaseX():
		def __init__(self, x):
			self.x = x

	class Sub(BaseX):
		def __init__(self, x, y):
			super(Sub, self).__init__(x)
			self.y = y

	s = Sub(2,3)
	s.__dict__          #{'x': 2, 'y': 3}
	-------------------------
	#INHERITANCE AND POLYMORPHISM: SUPER
	# super(): will reference (with a proxy object) the PARENT CLASS
	#don't need (SELF) when calling super()

	class PotatoSalad:
	  def __init__(self, potatoes, celery, onions):
		self.potatoes = potatoes
		self.celery = celery
		self.onions = onions

	# ------------------------------------
	# create sub-class 
	class SpecialPotatoSalad(PotatoSalad):
	  #constructor
	  def __init__(self, potatoes, celery, onions):
		#don't need (SELF) when calling super()
		super().__init__(potatoes, celery, onions)
		#add extra property (for special podado salad)
		self.raisins = 40
	-------------------------
	https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/
	#CLASS (GETTERS AND SETTERS) 
	class Person():										#class Person(object): (***LOOK INTO THIS LATER???***)
	 
		# CONSTRUCTOR
		def __init__(self, name):
			self.name = name
	 
		# GETTER
		def getName(self):
			return self.name
			
		# SETTER 
		def setName(self, new_name):
			self.name = new_name
			
		p = Person('Dean')
		p.getName()						#'Dean'
		p.setName('Nadine')
		p.getName()						#'Nadine'
	-------------------------
	#INHERITANCE AND POLYMORPHISM: INTERFACES
	# WOW, just had a BRAIN SPARK that you can actually have a PROPERTY in an object equal to a FUNCTION running (to do something)
	# Interface, is simply TWO CLASSES that can PERFORM THE SAME TASK (so have the same method name)(this way it doesn't matter which object it is...)
	# Interface, refers to (an object), the (name of methods) and the (arguments) it takes.

	class InsurancePolicy:
	  def __init__(self, price_of_item):
		self.price_of_insured_item = price_of_item
		
	# create sub-class 
	class VehicleInsurance(InsurancePolicy):
	  #get price (of a vehicle)
	  def get_rate(self):
		return 0.001 * self.price_of_insured_item

	# create sub-class 
	class HomeInsurance(InsurancePolicy):
	  #get price (of a home)
	  def get_rate(self):
		return 0.00005 * self.price_of_insured_item
	-------------------------
	#INHERITANCE AND POLYMORPHISM: POLYMORPHISM
	# ADDITION OPERATOR (+)
	# this does DIFFERENT OPERATIONS (depending on CONTEXT)
	# ---
	# addition
	# 4 + 5					returns 9
	# 2.2 + 3.3			returns 5.5
	#concatenation
	#'This' + 'is' + 'concatenation'	returns 'Thisisconcatenation'
	#appending two lists
	#[1, 2, 3] + [100, 101, 102]	#returns [1, 2, 3, 100, 101, 102]
	# ---
	# POLYMORPHISM (is like saying ONE OPERATOR does MANY THINGS in different contexts)

	a_list = [1, 18, 32, 12]
	a_dict = {'value': True}
	a_string = "Polymorphism is cool!"
	#test LEN() method on each...
	len(a_list)				#returns 4
	len(a_dict)				#return 1
	len(a_string)			#returns 21 (counts the letters)
	-------------------------
	# CUSTOM (ADD DUNDER METHOD)(+)(__add__)
	>>> class Point2:
	...     def __init__(self, x, y):
	...             self.x = x
	...             self.y = y
	...     def __add__(self, point):
	...             return (self.x + point.x, self.y + point.y)
	...
	>>> pt2 = Point2(5, 5)
	>>> pt3 = Point2(10, 10)
	>>> pt2 + pt3
	(15, 15)
	-------------------------
	# INHERITANCE AND POLYMORPHISM: DUNDER METHODS
	# __init__ (initialize an instance)(constructor)
	# __repr__ (string representation)
	# __dict__ (dictionary of instance variables)
	# __add__ (+ operator)

	class Atom:
	  def __init__(self, label):
		self.label = label
	  # __add__ (+ operator)
	  def __add__(self, other):
		return Molecule([self, other])
	  # __repr__ (string representation)
	  def __repr__(self):
		return self.label
		
	class Molecule:
	  def __init__(self, atoms):
		if type(atoms) is list:
		  self.atoms = atoms
	  # __repr__ (string representation)
	  def __repr__(self):
		return '{}{}'.format(self.atoms[0], self.atoms[1])
		  
	#ATOMS
	sodium = Atom("Na")
	chlorine = Atom("Cl")
	#print...
	print('sodium: ', sodium)				#sodium:  Na
	print('chlorine: ', chlorine)		#chlorine:  Cl

	#MOLECULE
	salt = Molecule([sodium, chlorine])
	#print...
	print('salt: ', salt)				#salt:  NaCl

	#COPY CAT...
	salt2 = sodium + chlorine	
	#print...
	print('salt2: ', salt2) 		#salt2:  NaCl
	-------------------------
	#DUNDER** METHODS
	http://www.diveintopython3.net/special-method-names.html
	YOU WANT...										SO YOU WRITE... 		AND PYTHON CALLS...			
	to initialize an instance						x = MyClass()			x.__init__()
	the “official” representation as a string		repr(x)					x.__repr__()
	
	MAKE AN OBJECT (INSTANCE) LIKE (A FUNCTION)
		you can make an instance of a class callable — exactly like a function is callable — by defining the __call__() method.
	YOU WANT...										SO YOU WRITE... 		AND PYTHON CALLS...			
	to “call” an instance like a function			my_instance()			my_instance.__call__()
	
	the number of items								len(s)					s.__len__()
	to know whether it contains a specific value	x in s					s.__contains__(x)
	
	DICTIONARY
	to get a value by its key						x[key]					x.__getitem__(key)
	to set a value by its key						x[key] = value			x.__setitem__(key, value)
	
	HASH  https://www.programiz.com/python-programming/methods/built-in/hash
	a custom hash value								hash(x)					x.__hash__()
	equality										x == y					x.__eq__(y)
	
	MATH OPERATORS 
	YOU WANT...										SO YOU WRITE... 		AND PYTHON CALLS...			
	addition										x + y					x.__add__(y)
	subtraction										x - y					x.__sub__(y)
	multiplication									x * y					x.__mul__(y)
	division										x / y					x.__truediv__(y)
	floor division									x // y					x.__floordiv__(y)
	modulo (remainder)								x % y					x.__mod__(y)
	raise to power									x ** y					x.__pow__(y)
	
	in-place addition								x += y					x.__iadd__(y)
	in-place subtraction							x -= y					x.__isub__(y)
	in-place multiplication							x *= y					x.__imul__(y)
	in-place division								x /= y					x.__itruediv__(y)
	in-place floor division							x //= y					x.__ifloordiv__(y)
	in-place modulo									x %= y					x.__imod__(y)
	in-place raise to power							x **= y					x.__ipow__(y)
	
	NEGATIVES, ABSOLUTE AND CASTING
	YOU WANT...										SO YOU WRITE... 		AND PYTHON CALLS...		
	negative number									-x						x.__neg__()
	positive number									+x						x.__pos__()
	absolute value									abs(x)					x.__abs__()
	integer											int(x)					x.__int__()
	floating point number							float(x)				x.__float__()
	
	BOOLEAN 
	equality										x == y					x.__eq__(y)
	inequality										x != y					x.__ne__(y)
	less than										x < y					x.__lt__(y)				#I think this is used in (SORT) (mylist.sort())(might need to tweak this for objects?)
	less than or equal to							x <= y					x.__le__(y)
	greater than									x >  y					x.__gt__(y)
	greater than or equal to						x >= y					x.__ge__(y)
	truth value in a boolean context				if x:					x.__bool__()
	
	CLASSES 
	YOU WANT...										SO YOU WRITE... 		AND PYTHON CALLS...		
	a class constructor								x = MyClass()			x.__new__()
	to get a property’s value						x.color					type(x).__dict__['color'].__get__(x, type(x))
	to set a property’s value						x.color = 'PapayaWhip'	type(x).__dict__['color'].__set__(x, 'PapayaWhip')
	test an object is an instance of your class		isinstance(x, MyClass)	MyClass.__instancecheck__(x)
	test a class is a subclass of your class		issubclass(C, MyClass)	MyClass.__subclasscheck__(C)
	a class destructor								del x					x.__del__()
		* Exactly when Python calls the __del__() special method is incredibly complicated. 
		To fully understand it, you need to know how Python keeps track of objects in memory. 
		http://www.diveintopython3.net/special-method-names.html
	
	p = Person('Dean')
	p.__module__				#'__main__'
	frank.__class__
		<class '__main__.User'>
	
	http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html
	FUNCTIONS
	a_function.__name__			The __name__ attribute (previously func_name) contains the function’s name.
	a_function.__doc__			The __doc__ attribute (previously func_doc) contains the docstring that you defined in the function’s source code.
	a_function.__defaults__		The __defaults__ attribute default argument values for those arguments that have default values.
	a_function.__dict__			The __dict__ attribute (previously func_dict) is the namespace supporting arbitrary function attributes.
	a_function.__code__			The __code__ attribute (previously func_code) is a code object representing the compiled function body.
	a_function.__globals__		The __globals__ attribute (previously func_globals) is a reference to the global namespace of the module in which the function was defined.
	a_function.__closure__		The __closure__ attribute (previously func_closure) is a tuple of cells that contain bindings for the function’s free variables.
	test.__name__
		'test'
	GLOBALS (FUNCTION)
	test.__globals__
		{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
		'__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'test': <function test at 0x0000026ECB612268>}
		
	------------------------------
	#DUNDER METHODS 2 (EXAMPLE)
	#create class
	class UserGroup:
	  def __init__(self, users, permissions):
		self.user_list = users
		self.permissions = permissions
	  def __iter__(self):
		return iter(self.user_list)
	  def __len__(self):
		return len(self.user_list)
	  def __contains__(self, user):
		return user in self.user_list
	#create class
	class User:
	  def __init__(self, username):
		self.username = username

	#create USERS
	diana = User('diana')
	frank = User('frank')
	jenn = User('jenn')

	#create USER GROUPS
	can_edit = UserGroup([diana, frank], {'can_edit_page': True})
	can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

	print(len(can_edit))
	# Prints 2

	for user in can_edit:
	  print(user.username)
	# Prints "diana" and "frank"

	frank in can_delete                     #False
	can_delete.__dict__
	#{'user_list': [<__main__.User object at 0x0000026ECB6485C0>, <__main__.User object at 0x0000026ECB648860>], 'permissions': {'can_delete_posts': True}}
	can_delete.user_list[0].username        #'diana'
	can_delete.user_list[1].username        #'jenn'
	#THEY USED THE WRONG (USER GROUP)
	#if frank in can_delete:
	 # print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
	if frank in can_edit:
		print('yes Frank can edit things')          #yes Frank can edit things
	------------------------------
	??? enumerable()
	------------------------------
	# __iter__ (ITERABLE)(ITERATOR)(ITER)
			iter()
			next()		__next__
			StopIteration
		-need to add a METHOD to a CLASS (to make it iterable)
		-to be iterable, you can simply use it in a FOR-LOOP (for x in my_object:)
			class MyObj:
				def __iter__(self):
					#...
			obj = MyObj()
			for x in obj:
				print(x)
		-------------------
		https://www.programiz.com/python-programming/iterator
			# define a list
			my_list = [4, 7, 0, 3]

			# get an iterator using iter()
			my_iter = iter(my_list)

			## iterate through it using next() 

			#prints 4
			print(next(my_iter))

			#prints 7
			print(next(my_iter))

			## next(obj) is same as obj.__next__()

			#prints 0
			print(my_iter.__next__())

			#prints 3
			print(my_iter.__next__())

			## This will raise error, no items left
			next(my_iter)
	------------------------------
	# INHERITANCE AND POLYMORPHISM: DUNDER METHODS II
	# __init__ (initialize object)(constructor)
	# __iter__ (iterator)(for x in my_list)
	# https://docs.python.org/3/library/stdtypes.html#typeiter
	# __len__ (length)(if len() is called...)
	# __contains__ (x in my_string)(x in my_list)(test if a list CONTAINS an element)

	class LawFirm:
	  def __init__(self, practice, lawyers):
		self.practice = practice
		self.lawyers = lawyers
	  #__len__ add len() (to tally the lawyers)
	  def __len__(self):
		return len(self.lawyers)
	  #__contains__ (returns True/False)
	  def __contains__(self, lawyer):
		return lawyer in self.lawyers
		
	d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
	#print to test
	print('len: ', len(d_and_p))							#len:  2
	print('contains: ', 'Donelli' in d_and_p)				#contains:  True
	------------------------------
	#INHERITANCE AND POLYMORPHISM: REVIEW
	# create a class 
	class SortedList(list):
	  # define a new append
	  def append(self, value):
		super().append(value)								#use SUPER to not confuse the two methods
		self.sort()											#sort the list
		
	#TEST IT OUT...
	l = SortedList()
	l.append(3)
	l.append(5)
	l.append(1)
	l															#[1, 3, 5]
	------------------------------
	#INSPECT (FIND OUT MORE ABOUT FUNCTIONS)
	import inspect 
	#test func 
	def test(a, b):
		return a + b 
	inspect.getargspec(test)
	---
	#INSPECT (MANUALLY)
	 dir(test.__code__)
		['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
		'__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
		'__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 
		'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
	#GET DUNDER METHODS 
	[x for x in l if x[0] == '_']
		['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
		'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
	#GET OTHER VARIABLES 
	[x for x in l if x[0] != '_']
		['co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 
		'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
	----------------
	#GET NAME 
	test.__code__.co_name 
		'test'
	#GET NUMBER OF ARGUMENTS 
	test.__code__.co_argcount
		2
	#GET ARGUMENTS 
	test.__code__.co_varnames
		('a', 'b')
	l = dir(test.__code__)			#SAVES THE ABOVE LIST 
	---
	-these both do the SAME THING
	-this is the COMPILED CODE...
	#EVAL (use to print each)(by referencing its name)
	eval('test.__code__.' + l[-13])
		b'|\x00|\x01\x17\x00S\x00'
	test.__code__.co_code
		b'|\x00|\x01\x17\x00S\x00'
	---
	#this will show the COMPILED CODE... 
		https://docs.python.org/2/library/dis.html
	>>> import dis
	>>> dis.dis(test)
	  2           0 LOAD_FAST                0 (a)
				  2 LOAD_FAST                1 (b)
				  4 BINARY_ADD
				  6 RETURN_VALUE
	
	TOS (top-of-stack)
	LOAD_FAST(var_num)				Pushes a reference to the local co_varnames[var_num] onto the stack.
	BINARY_ADD()					Implements TOS = TOS1 + TOS.
	RETURN_VALUE()					Returns with TOS to the caller of the function.
	---------------------------------------------
	#HOW TO DUMP (ALL OF THEM)(TO SEE WHAT YOU NEED)
	v = [eval('test.__code__.' + x) for x in t]
	>>> result = [print(x,y) for x,y in zip(t, v)]
	co_argcount 2
	co_cellvars ()
	co_code b'|\x00|\x01\x17\x00S\x00'
	co_consts (None,)
	co_filename <stdin>
	co_firstlineno 1
	co_flags 67
	co_freevars ()
	co_kwonlyargcount 0
	co_lnotab b'\x00\x01'
	co_name test
	co_names ()
	co_nlocals 2
	co_stacksize 2
	co_varnames ('a', 'b')
	>>> result = [print(x,': ',y) for x,y in zip(t, v)]
	co_argcount :  2
	co_cellvars :  ()
	co_code :  b'|\x00|\x01\x17\x00S\x00'
	co_consts :  (None,)
	co_filename :  <stdin>
	co_firstlineno :  1
	co_flags :  67
	co_freevars :  ()
	co_kwonlyargcount :  0
	co_lnotab :  b'\x00\x01'
	co_name :  test
	co_names :  ()
	co_nlocals :  2
	co_stacksize :  2
	co_varnames :  ('a', 'b')
	---------------------------------------------
	#FUNCTION: DUMP ALL METHODS...
	def my_dump(func):
		l = dir(func.__code__)
		v = [eval(func.__code__.co_name + '.__code__.' + x) for x in l]
		result = [print(x,': ',y) for x,y in zip(l, v)]
	-------------
	#DUMP (ANYTHING...)
	def dump(s_to_test):
		keys = dir(eval(s_to_test))
		values = [eval(s_to_test + '.' + x) for x in keys]
		result = [print(x,': ',y) for x,y in zip(keys, values)]
	dump('myfun.__code__')
		-------------
		def myfun(x,y,z='Zzzzzzz sleeping!'):
			return x + y + z
		-------------
		myfun.__code__.__str__.__text_signature__			#'($self, /)'
		myfun.__code__.co_varnames							#('x', 'y', 'z')
		myfun.__defaults__									#('Zzzzzzz sleeping!',)
	-------------
	#TEST 
	my_dump(test)
	# __class__ <class 'code'>
	# __delattr__ <method-wrapper '__delattr__' of code object at 0x0000026ECB605DB0>
	# __dir__ <built-in method __dir__ of code object at 0x0000026ECB605DB0>
	# __doc__ code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
	#       constants, names, varnames, filename, name, firstlineno,
	#       lnotab[, freevars[, cellvars]])
	# 
	# Create a code object.  Not for the faint of heart.
	# __eq__ <method-wrapper '__eq__' of code object at 0x0000026ECB605DB0>
	# __format__ <built-in method __format__ of code object at 0x0000026ECB605DB0>
	# __ge__ <method-wrapper '__ge__' of code object at 0x0000026ECB605DB0>
	# __getattribute__ <method-wrapper '__getattribute__' of code object at 0x0000026ECB605DB0>
	# __gt__ <method-wrapper '__gt__' of code object at 0x0000026ECB605DB0>
	# __hash__ <method-wrapper '__hash__' of code object at 0x0000026ECB605DB0>
	# __init__ <method-wrapper '__init__' of code object at 0x0000026ECB605DB0>
	# __init_subclass__ <built-in method __init_subclass__ of type object at 0x0000000055190050>
	# __le__ <method-wrapper '__le__' of code object at 0x0000026ECB605DB0>
	# __lt__ <method-wrapper '__lt__' of code object at 0x0000026ECB605DB0>
	# __ne__ <method-wrapper '__ne__' of code object at 0x0000026ECB605DB0>
	# __new__ <built-in method __new__ of type object at 0x0000000055190050>
	# __reduce__ <built-in method __reduce__ of code object at 0x0000026ECB605DB0>
	# __reduce_ex__ <built-in method __reduce_ex__ of code object at 0x0000026ECB605DB0>
	# __repr__ <method-wrapper '__repr__' of code object at 0x0000026ECB605DB0>
	# __setattr__ <method-wrapper '__setattr__' of code object at 0x0000026ECB605DB0>
	# __sizeof__ <built-in method __sizeof__ of code object at 0x0000026ECB605DB0>
	# __str__ <method-wrapper '__str__' of code object at 0x0000026ECB605DB0>
	# __subclasshook__ <built-in method __subclasshook__ of type object at 0x0000000055190050>
	# co_argcount 2
	# co_cellvars ()
	# co_code b'|\x00|\x01\x17\x00S\x00'
	# co_consts (None,)
	# co_filename <stdin>
	# co_firstlineno 1
	# co_flags 67
	# co_freevars ()
	# co_kwonlyargcount 0
	# co_lnotab b'\x00\x01'
	# co_name test
	# co_names ()
	# co_nlocals 2
	# co_stacksize 2
	# co_varnames ('a', 'b')
	---------------------------------------------
	
	TRANSPOSE (HOW MAKE A 2D ARRAY)(SWITCH ROWS TO COLUMNS)
		-flip the matrix 
		https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
			ZIP (TO TRANSPOSE)
			>>> matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
			>>> for x in matrix:
			...     print(x)
			...
			(1, 2, 3)
			(4, 5, 6)
			(7, 8, 9)
			(10, 11, 12)
			>>> t = zip(*matrix)			#THIS IS THE MAGIC (the asterisk * WITH ZIP) I think does the trick
			>>> for x in t:
			...     print(x)
			...
			(1, 4, 7, 10)
			(2, 5, 8, 11)
			(3, 6, 9, 12)
			-------------
			LIST COMPREHENSION (TO TRANSPOSE)
			>>> m = [[1, 2], [3, 4], [5, 6]]
			>>> for x in m:
.			..     print(x)
			...
			[1, 2]
			[3, 4]
			[5, 6]
			----
			>>> col = len(m[0])		#2
			>>> row = len(m)		#3
			>>> m2 = [[m[x][y] for x in range(row)] for y in range(col)] 		#LIST COMPREHENSION (TRANSPOSE)
			>>> for x in m2:
			...     print(x)
			...
			[1, 3, 5]
			[2, 4, 6]
			---------------
			>>> m = [[1, 2], [3, 4], [5, 6]]
			>>> [[x[0] for x in m], [x[1] for x in m]]		#LIST COMPREHENSION (MANUALLY SORTA WORKS)(could fix this in a LOOP with RANGE)(depending on size of 2d array)
			[[1, 3, 5], [2, 4, 6]]
			>>> m
			[[1, 2], [3, 4], [5, 6]]
	----------------------
	
	****************************************************************************************************************
	****************************************************************************************************************
		SEP.06, 2018 PROJECT12: BASTA FAZOOLIN 

		"E:\000-BACKUP\0000-CODE ACADEMY\001-Programming with Python (Jul.17-Oct.2,2018)\12-Project (Basta Fazoolin)\
			proj12_basta_fazoolin.py"

	# BASTA FAZOOLIN ()
	# PROJECT #12
	# CODE ACADEMY
	# PROGRAMMING WITH PYTHON
	# Dean Jones, Sep.03, 2018 (finished on Sep.6)(GOOD CHALLENGE!!!)
	#
	# You've started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin' with My Heart.
	# The restaurant has been doing fantastically and seen a lot of growth lately. You've been hired to keep things organized.

	# TODO:
	# HOW TO TAKE AN ORDER? (like with dropdown on menu)(so I don't have to type it constantly)
	# WHAT IF THERE ARE (TWO MENUS)(the times overlap)
	#   What if there are TWO items (AT DIFFERENT PRICES)(need something to resolve this conflict)
	# CAN I SET THIS UP (TIME BASED) IN A (GRID LIKE NUMBERS)(to resolve these issues?)
	# HOW CHECK FOR THE (TIME OF ORDER)


	# DATE
	# TIME
	# MENU
	# NAME
	# ADDRESS
	# PHONE
	# RESTAURANT
	# ITEM
	# ITEMS
	# BILL
	# FRANCHISE
	# BUSINESS


	#IMPORTS
	import datetime

	# CLASS: DATE
	class Date:
		#constructor
		def __init__(self, date):
			self.date = date
			self.year = self.date.year
			self.month =  self.date.month
			self.day =  self.date.day
			self.dayOfWeek =  self.date.strftime('%A')
		#string representation
		def __repr__(self):
			return self.date.strftime('%A, %b.%d, %Y')
	# d = datetime.date(year=2018, month=9, day=5)
	# d.strftime('%A, %b.%d, %Y')         #'Wednesday, Sep.05, 2018'
	# d.strftime('%A')                    #'Wednesday'
	#SET THE DATE
	d = Date(datetime.date(year=1976, month=6, day=7))
	# Monday, Jun.07, 1976
	#GET THE CURRENT DATE
	current = Date(datetime.datetime.now())
	# Wednesday, Sep.05, 2018

	# CLASS: TIME
	# dependencies: (datetime) import
	class Time:
		#constructor
		def __init__(self, my_time, descr):
			self.time = my_time.strftime('%I:%M %p')	#'11:00 AM'
			self.description = descr
			self.hour24 = my_time.hour
			self.minute = my_time.minute
			self.day_night = my_time.strftime('%p')
		#string representation
		def __repr__(self):
			return '{}: {}'.format(self.description, self.time)
		# iterable (for x in ...)
		def __iter__(self):
			return iter(self)
	#TEST
	# t = Time(datetime.time(hour=11, minute=00), 'Start Time')
	# t.time                  #'11:00 AM'
	# t.description           #'Start Time'
	# print(t)                #Start Time: 11:00 AM

	# CLASS: MENU
	class Menu:
		# constructor
		def __init__(self, name, items, start_time, end_time):
			self.name = name
			self.items = items
			self.start = start_time
			self.end = end_time
		# string representation
		def __repr__(self):
			return self.menu_long()
		# items (string repr)
		def items_tostring(self):
			i = ''
			for k,v in self.items.items():
				#i += '\n' + str(k) + ' ' + str(v)
				i += '\n\t{}: {}'.format(k.title(), self.currency(v))
				#print(k, v)
			return i
		# currency format
		def currency(self, num):
			return '${:,.2f}'.format(num)
		# print menu (short)
		def menu_short(self):
			return '{} is available from {} to {}'.format(self.name, self.start.time, self.end.time)
		# print menu (long)
		def menu_long(self):
			#return 'Name: {}\nItems: {}\nStart: {}\nEnd: {}'.format(self.name, self.items, self.start, self.end)
			return 'Name: {}\nItems: {}\nStart: {}\nEnd: {}'.format(self.name, self.items_tostring(), self.start, self.end)
		# iterable (for x in ...)
		def __iter__(self):
			return iter(self.items)

	#TEST
	# st = Time(datetime.time(hour=11, minute=00), 'Start Time')
	# et = Time(datetime.time(hour=16, minute=00), 'End Time')
	# m = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00}, st, et)
	# m.items                     #{'pancakes': 7.5, 'waffles': 9.0}
	# m.name                      #'Brunch'
	# m.start_time                #Time OBJECT, Start Time: 11:00 AM
	# m.end_time                  #Time OBJECT, End Time: 04:00 PM
	# m.end_time.time             #'04:00 PM'
	# m.start_time.time           #'11:00 AM'
	# m.start_time.description    #'Start Time'
	# print(m)
		# Name: Brunch
		# Items: {'pancakes': 7.5, 'waffles': 9.0}
		# Start: Start Time: 11:00 AM
		# End: End Time: 04:00 PM

	# create menu (Brunch)
	brunch = {
	  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
	}
	stBrunch = Time(datetime.time(hour=11, minute=00), 'Start Time')
	etBrunch = Time(datetime.time(hour=16, minute=00), 'End Time')
	mnuBrunch = Menu('Brunch Menu', brunch, stBrunch, etBrunch)

	# create menu (Early Bird Dinner)
	early_bird = {
	  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
	}
	stEarlyBird = Time(datetime.time(hour=15, minute=00), 'Start Time')
	etEarlyBird = Time(datetime.time(hour=18, minute=00), 'End Time')
	mnuEarlyBird = Menu('Early Bird Dinner Menu', early_bird, stEarlyBird, etEarlyBird)

	# create menu (Dinner)
	dinner = {
	  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
	}
	stDinner = Time(datetime.time(hour=17, minute=00), 'Start Time')
	etDinner = Time(datetime.time(hour=23, minute=00), 'End Time')
	mnuDinner = Menu('Dinner Menu', dinner, stDinner, etDinner)

	# create menu (Kids)
	kids = {
	  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
	}
	stKids = Time(datetime.time(hour=11, minute=00), 'Start Time')
	etKids = Time(datetime.time(hour=21, minute=00), 'End Time')
	mnuKids = Menu('Kids Menu', kids, stKids, etKids)

	# ------------------------------------
	# CLASS: NAME
	class Name():
		#constructor
		def __init__(self, fname, lname):
			self.first = fname
			self.last = lname
		#string representation
		def __repr__(self):
			return '{} {}'.format(self.first, self.last)
	#TEST
	p = Name('Dean', 'Jones')
	p           #Dean Jones

	# CLASS: ADDRESS INFO
	class Address():
		#constructor
		def __init__(self, name='None', streetNo='None', streetName='None', quadrant='None', city='None', prov='None', postal='None'):
			self.name = name
			self.streetNo = streetNo
			self.streetName = streetName
			self.quadrant = quadrant
			self.city = city
			self.prov = prov
			self.postal = postal
		#string representation
		def __repr__(self):
			return '\n{}\n{} {} {}\n{}, {}\n{}'.format(self.name, self.streetNo, self.streetName, self.quadrant, self.city, self.prov, self.postal)
	#TEST
	#addr = Address('DEAN JONES', 16, 'WOODSTOCK RD', 'SW', 'Calgary', 'AB', 'T2W 5V8')
	# addr = Address(Name('DEAN', 'JONES'), 16, 'WOODSTOCK RD', 'SW', 'Calgary', 'AB', 'T2W 5V8')
	# addr.name.first         #'DEAN'
	# addr.name.last          #'JONES'
	addr = Address('Basta Fazoolin', 111, 'MAIN STREET', 'SE', 'Calgary', 'AB', 'X0X 0X0')

	# CLASS: PHONE INFO
	class Phone():
		#constructor
		def __init__(self, areaCode, digit3, digit4):
			self.areaCode = areaCode
			self.phone = '{}-{}'.format(digit3, digit4)
		#string representation
		def __repr__(self):
			return '({}) {}'.format(self.areaCode, self.phone)
	#TEST
	# ph = Phone(403, 555, 1234)
	# ph              #(403) 555-1234

	# CLASS: RESTAURANT INFO
	class Restaurant():
		#constructor
		def __init__(self, address, phone, style):
			self.address = address
			self.phone = phone
			self.style = style
		#string representation
		def __repr__(self):
			return '\n{}\n{}\n\n{} Restaurant'.format(self.address, self.phone, self.style)
	#TEST
	r = Restaurant(Address('Basta Fazoolin', 111, 'MAIN STREET', 'SE', 'Calgary', 'AB', 'X0X 0X0'), Phone(403, 555, 1234), 'Family-Style Italian')
	# Basta Fazoolin
	# 111 MAIN STREET SE
	# Calgary, AB
	# X0X 0X0
	# (403) 555-1234
	#
	# Family-Style Italian Restaurant


	# CLASS: ITEM
	class Item():
		#constructor
		def __init__(self, qty, item, price):
			self.qty = qty
			self.item = item
			self.price = price
			self.dict = {'qty': self.qty, 'item': self.item, 'price': self.price}
		#string representation
		def __repr__(self):
			return '{}'.format(self.dict)

	#TEST
	# itm1 = Item(2, 'cola', 1.00)
	# itm2 = Item(1, 'fries', 2.00)
	# itm3 = Item(1, 'burger', 5.00)
	# itm1            #2, cola, 1.0
	#CODE ACADEMY TEST (USE A MENU, to find items with correct price)
	itm1 = Item(1, 'pancakes', mnuBrunch.items['pancakes'])
	itm2 = Item(1, 'home fries', mnuBrunch.items['home fries'])
	itm3 = Item(1, 'coffee', mnuBrunch.items['coffee'])
	#'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
	itm4 = Item(1, 'salumeria plate', mnuEarlyBird.items['salumeria plate'])
	itm5 = Item(1, 'mushroom ravioli (vegan)', mnuEarlyBird.items['mushroom ravioli (vegan)'])
	# 'salumeria plate': 8.00, 'pizza with quattro formaggi': 9.00, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,



	# FUNCTION: currency format
	def currency(num):
		return '${:,.2f}'.format(num)

	# CLASS: ITEMS
	class Items():
		#constructor
		def __init__(self, items_list):
			self.list = items_list
			#self.subtotal = self.subtotal()
			self.gst = 5.0                      #5.0% tax
			#self.tax = self.tax()
			#self.total = self.total()
		#string representation
		def __repr__(self):
			return '{}'.format(self.list)
		#print
		def print_items(self):
			print('Qty\t\tPrice\t\tDescription')
			for x in self.list:
				print('{}\t\t{}\t\t{}'.format(x['qty'], currency(x['price']), x['item'].title()))
		#string items
		def str_items(self):
			s = ''
			s += '\nQty\t\tPrice\t\tDescription'
			for x in self.list:
				s += '\n{}\t\t{}\t\t{}'.format(x['qty'], currency(x['price']), x['item'].title())
			return s
		#calculate subtotal (qty * price) for all items (sum)
		def subtotal(self):
			return sum([x['qty'] * x['price'] for x in self.list])
		#calculate tax
		def tax(self):
			return self.subtotal() * (5.0 / 100)
		#calculate TOTALS
		def total(self):
			return self.subtotal() + self.tax()

	#TEST (ORDER)
	i = Items([itm1.dict, itm2.dict, itm3.dict, itm4.dict, itm5.dict])
	# i.print_items()
	# qty     price   description
	# 2       1.0     cola
	# 1       2.0     fries
	# 1       5.0     burger

	# CLASS: BILL (RECEIPT)
	class Bill():
		#constructor
		def __init__(self, restaurant, mnu, billNo, dateOfPurchase, itemsPurchased):
			self.restaurant = restaurant
			self.menu = mnu.name
			self.billNo = billNo
			self.date = dateOfPurchase
			self.itemsPurchased = itemsPurchased
		#string representation
		def __repr__(self):
			s = ''
			s += '\n-------------------------------------------------------'
			s += '\n{}'.format(self.menu)
			s += '\n{}{}\nBill#: {}\n\n{}'.format(self.date, self.restaurant, self.billNo, self.itemsPurchased.str_items())
			s += '\n'
			s += '\nSubTotal: {}'.format(currency(self.itemsPurchased.subtotal()))
			s += '\nTax @ {}%: {}'.format(self.itemsPurchased.gst, currency(self.itemsPurchased.tax()))
			s += '\nTotal: {}'.format(currency(self.itemsPurchased.total()))
			s += '\n-------------------------------------------------------'
			return s

	#TEST
	b = Bill(r, mnuBrunch, 101, Date(datetime.datetime.now()), i)
	# -------------------------------------------------------
	# Brunch Menu
	# Thursday, Sep.06, 2018
	#
	# Basta Fazoolin
	# 111 MAIN STREET SE
	# Calgary, AB
	# X0X 0X0
	# (403) 555-1234
	#
	# Family-Style Italian Restaurant
	# Bill#: 101
	#
	#
	# Qty             Price           Description
	# 1               $7.50           Pancakes
	# 1               $4.50           Home Fries
	# 1               $1.50           Coffee
	#
	# SubTotal: $13.50
	# Tax @ 5.0%: $0.68
	# Total: $14.18
	# -------------------------------------------------------

	# CLASS: FRANCHISE
	class Franchise():
		#constructor
		def __init__(self, address, menus):
			self.address = address
			self.menus = menus
		#string representation
		def __repr__(self):
			return '\n{}'.format(self.address)
		#string dump
		def str_dump(self):
			return '\naddress: {}\nmenu: {}'.format(self.address, self.menus)
		#list of available menus
		def available_menus(self, time):
			hr = time.hour24
			result = []
			for b in range(self.menus[0].start.hour24, self.menus[0].end.hour24):   #Brunch
				if b == hr:                                                         #if the (hour) is in (menu range)
					#result.append('b')                                              #add menu
					result.append(self.menus[0].name)
			for e in range(self.menus[1].start.hour24, self.menus[1].end.hour24):   #Early Bird (get range from start time to end time)
				if e == hr:                                                         #if the (hour) is in (menu range)
					#result.append('e')
					result.append(self.menus[1].name)   #add menu
			for d in range(self.menus[2].start.hour24, self.menus[2].end.hour24):   #Dinner
				if d == hr:                                                         #if the (hour) is in (menu range)
					#result.append('d')
					result.append(self.menus[2].name)                              #add menu
			for k in range(self.menus[3].start.hour24, self.menus[3].end.hour24):   #Kids
				if k == hr:                                                         #if the (hour) is in (menu range)
					#result.append('k')
					result.append(self.menus[3].name)                              #add menu
			return result


	#TEST
	#"12 East Mulberry Street"
	addrFlag = Address('Basta Fazoolin', 12, 'East Mulberry Street', 'E', 'Calgary', 'AB', 'X0X 0X0')
	mnuList = [mnuBrunch, mnuEarlyBird, mnuDinner, mnuKids]
	flagship_store = Franchise(addrFlag, mnuList)
	#"1232 West End Road"
	new_installment = Franchise(Address('Basta Fazoolin', 1232, 'West End Road', 'W', 'Calgary', 'AB', 'X0X 0X0'), [mnuBrunch, mnuEarlyBird, mnuDinner, mnuKids])

	#TEST (MENUS AVAILABLE)
	t = Time(datetime.time(hour=13, minute=00), 'Menus available')
	t1 = Time(datetime.time(hour=16, minute=00), 'Menus available')
	t2 = Time(datetime.time(hour=18, minute=00), 'Menus available')
	f = Franchise(addrFlag, mnuList)
	f.available_menus(t)        #['b', 'k']
	f.available_menus(t1)       #['e', 'k']
	f.available_menus(t2)       #['d', 'k']
	f.available_menus(t)        #['Brunch Menu', 'Kids Menu']
	f.available_menus(t1)       #['Early Bird Dinner Menu', 'Kids Menu']
	f.available_menus(t2)       #['Dinner Menu', 'Kids Menu']
	#TEST (CODE ACADEMY)
	test = Time(datetime.time(hour=12, minute=00), 'Menus available')
	f.available_menus(test)     #['Brunch Menu', 'Kids Menu']
	test2 = Time(datetime.time(hour=17, minute=00), 'Menus available')
	f.available_menus(test2)    #['Early Bird Dinner Menu', 'Dinner Menu', 'Kids Menu']

	# ----------------------
	# CREATE A BUSINESS (Business --> Franchise --> Menu)
	class Business():
		def __init__(self, name, franchises):
			self.name = name
			self.franchises = franchises
	#TEST
	bus = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
	#NEW MENU
	arepas = {
	  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
	}
	stArepas = Time(datetime.time(hour=10, minute=00), 'Start Time')
	etArepas = Time(datetime.time(hour=20, minute=00), 'End Time')
	mnuArepas = Menu('Arepas Menu', arepas, stArepas, etArepas)
	#MAKE FRANCHISE
	#"189 Fitzgerald Avenue"
	addrFlag2 = Address('Arepas Place', 189, 'Fitzgerald Avenue', 'None', 'Phoenix', 'AZ', '67760')
	mnuList2 = [mnuArepas]
	arepas_place = Franchise(addrFlag2, mnuList2)
	# type(arepas_place)            #<class '__main__.Franchise'>
	#MAKE A BUSINESS
	bus2 = Business("Take a' Arepa", [arepas_place])
	# type(bus2)                    #<class '__main__.Business'>
	
	****************************************************************************************************************
	****************************************************************************************************************
	#CLASS (VALIDATE PROPERTIES)
	class TestValidateProperties:
		def __init__(self, a, b):
			assert isinstance(a, int), 'Please enter an (int) for argument (a)'
			self.a = a
			assert isinstance(b, str), 'Please enter a (str) for argument (b)'
			self.b = b
	#TEST 
	t = TestValidateProperties(33, 'string')
	t.a         #33
	t.b         #'string'
	t = TestValidateProperties(2, 3)
	AssertionError: Please enter a (str) for argument (b)
	t = TestValidateProperties('str1', 'str2')
	AssertionError: Please enter an (int) for argument (a)
	
	# PRIVATE PROPERTIES (GETTER SETTER)
	# https://stackoverflow.com/questions/4555932/public-or-private-attribute-in-python-what-is-the-best-way
	# The (double underscore) in front of the PROPERTY (makes it INACCESSIBLE)
	class Foo():
		def __init__(self):
			self.__attr = 0
		@property
		def attr(self):  
			return self.__attr
		@attr.setter
		def attr(self, value):
			self.__attr = value
	# TEST 
	f = Foo()
	f.__attr        #AttributeError: 'Foo' object has no attribute '__attr'
	f.attr          #returns 0
	f.attr = 23     
	f.attr          #returns 23
	---------------------------
	#GETTER (PRIVATE PROPERTY)
	>>> class Test:
	...     def __init__(self, __name):
	...             self.__name = __name
	...     def get_name(self):
	...             return self.__name
	...
	>>> t = Test('Sam')
	>>> t
	<__main__.Test object at 0x000001C63100BD68>
	>>> t.get_name()
	'Sam'
	
	# FUNCTION: COUNT DIGITS (INTEGER)
	def digit_count(num):
		return len(str(num))
	
	DATA SCIENCE
	DATA SCIENCE: PANDAS 
		RESOURCES (PANDAS)
		https://pandas.pydata.org/pandas-docs/stable/tutorials.html
		
		>>> import pandas as pd
		>>> df = pd.read_csv("C:\_FTP\Book1.csv")
		>>> print(df.head())
			   colA  colB  colC  test$4
			0     1     2     3       4
			1     2     4     6       8
			2     3     6     9      12
			3     4     8    12      16
		----------
		PRINT (DIFFERENT ROWS)
		>>> df[::3]
			   colA  colB  colC  test$4
			0     1     2     3       4
			3     4     8    12      16
		>>> df[::2]
			   colA  colB  colC  test$4
			0     1     2     3       4
			2     3     6     9      12
		----------
		PRINT (COLUMN)
		>>> df['colA']
			0    1
			1    2
			2    3
			3    4
			Name: colA, dtype: int64
		dir(df)
			#SEE PROPERTIES... 
		df.values
			array([[ 1,  2,  3,  4],
				   [ 2,  4,  6,  8],
				   [ 3,  6,  9, 12],
				   [ 4,  8, 12, 16]], dtype=int64)
				   
	DATA SCIENCE: MATPLOTLIB 
		RESOURCES (MATPLOTLIB)
		https://matplotlib.org/gallery.html#showcase

		import matplotlib.pyplot as plt
		df['colA'].plot()
			#CREATES A (MATPLOTLIB object)
			#<matplotlib.axes._subplots.AxesSubplot object at 0x0000013BBD776208>
			??? HOW TO DISPLAY? (TO LOOK NICE?)
		------
		>>> import matplotlib.pyplot as plt
		>>> plt.plot(df)
		plt.show() 				#OPENS DIALOG (to display)
	MATPLOTLIB (EXPORT PDF)
		plt.show() 
		-after the DIALOG is displaying (CLICK SAVE BUTTON, change to PDF, JPG, PNG, etc.)
		
	MATPLOTLIB (GRAPH)
	----------------------
	import codecademylib3_seaborn
	from matplotlib import pyplot as plt
	import numpy as np
	import pandas as pd

	# x-axis (hour)
	hour = range(24)
	# y-axis (viewers data)
	viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
	# title (top)
	plt.title("Codecademy Learners Time Series")
	# x-y-axis labels
	plt.xlabel("Hour")
	plt.ylabel("Viewers")
	# plot
	plt.plot(hour, viewers_hour)
	# add (legend)
	plt.legend(['2015-01-01'])
	# -----------
	# add subplot (another layer)
	ax = plt.subplot()
	# set color
	ax.set_facecolor('seashell')
	# set x-axis (data)(same hours)
	ax.set_xticks(hour)
	# set y-axis (data)
	ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
	# ???
	y_upper = [i + (i*0.15) for i in viewers_hour]
	y_lower = [i - (i*0.15) for i in viewers_hour]

	plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

	#display 
	plt.show()
	----------------------
	
	MACHINE LEARNING (DEFINITION)
		Machine Learning is the science of getting computers to learn and act like humans do, 
		and improve their learning over time in autonomous fashion, by feeding them data and information 
		in the form of observations and real-world interactions. 
	MACHINE LEARNING (CATEGORIES)
		Supervised Learning
		Unsupervised Learning
		
	SUPERVISED LEARNING 
		is when the data is labeled and the program learns to predict the output from the input data. 
		For instance, a supervised learning algorithm for credit card fraud detection would take as input a set of recorded transactions. 
		It would learn what makes a transaction likely to be fraudulent. Then, for each new transaction, the program would predict if it is fraudulent or not.
	UNSUPERVISED LEARNING 
		is where the data is unlabeled and the program learns to recognize the inherent structure of the input data. For the same fraud example, 
		the model would take in a bunch of transactions with no indication of if they are fraudulent or not, and it would group them based on patterns it sees. 
		It might discover two groups, fraudulent and legitimate.
		
	------------------------
	#MACHINE LEARNING (EXAMPLE)
	import codecademylib3_seaborn
	import matplotlib.pyplot as plt
	import numpy as np
	import pandas as pd
	from sklearn.cluster import KMeans

	mu = 1
	std = 0.5
	mu2 = 4.188

	np.random.seed(100)

	xs = np.append(np.append(np.append(np.random.normal(0.25,std,100), np.random.normal(0.75,std,100)), np.random.normal(0.25,std,100)), np.random.normal(0.75,std,100))

	ys = np.append(np.append(np.append(np.random.normal(0.25,std,100), np.random.normal(0.25,std,100)), np.random.normal(0.75,std,100)), np.random.normal(0.75,std,100))

	values = list(zip(xs, ys))

	model = KMeans(init='random', n_clusters=2)

	results = model.fit_predict(values)

	plt.scatter(xs, ys, c=results, alpha=0.6)

	colors = ['#6400e4', '#ffc740']

	for i in range(2):
	  points = np.array([values[j] for j in range(len(values)) if results[j] == i])
	  plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.6)
	  
	plt.title('Codecademy Mobile Feedback - Data Science')

	plt.xlabel('Learn Python')
	plt.ylabel('Learn SQL')
	  
	plt.show()
	------------------------
	DATA SCIENCE PATH 
		-Explored CHURN DATA using SQL
		-ANALYZED data using PANDAS (Python library)
		-VISUALIZED DATA using Matplotlib (Python library)
		-Built a MACHINE LEARNING model using (scikit-learn)(Python library)
