# myRepo
The easiest way to init your {EPITECH.} repository.

We all agree that the structure of our Epitech repos is always the same ?

So why not automate it creation a bit ?

By answering 4 questions, this script will create YOUR repo (exactly as you imagine it) !

This tool was designed for C projects at Epitech but can correspond to other needs, do not hesitate to try it.

## Installation
- Download the python file.
- Add alias to your Run Command file :
```alias repo="python3 /path/to/myRepo.py"```

That's it !

## How does it work ?
To init your repo, open a command prompt at it root and run
```repo```

![Command Prompt Screenshot](https://github.com/MathiDEV/myrepo/blob/main/myRepo.jpg?raw=true)


This will ask you a few questions and at the end you will have your repo.

Your repo will include:
- Makefile (adapted to your settings)
- Header files
- Lib folders with Makefiles
- .gitignore
- Sources folder
- First C file
- (Optional) Unit tests (with make rule)
- (Optional) GitHub actions


![Output files](https://github.com/MathiDEV/myrepo/blob/main/files.jpg?raw=true)
## It is not custom enough for me...
I am sorry ! For reasons of simplicity and visibility, this code is not the easiest to read ... However, it is not very complicated to modify. For example, if you want to add a new rule to .gitignore, just edit the variable "gitignore"

If this is still too boring, I simply advise you to make your alterations once the repo has been initiated.
