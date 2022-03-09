# Clean Commit
From `fixed RAnDom CRashes` to `[FIX] Fixed random crashes.`

Clean commit helps you by auto-formating your commits to make your repos better !

## Installation
- Download the python file.
- Add alias to your Run Command file :
```alias gp="python3 /path/to/clean_commit.py"```

That's it !

## How does it work ?
Simply write
```gp <your commit message>```

The script will fclean your repo, add all new files to a commit and push it to your GitHub repo.

It will automatically detect the type of your commit (INIT / FEAT / FIX / STYLE) and format the message as it should.

It will also fix misplaced capital letters.

## Commit aliases
By default, the script has two commit aliases :
```C
gp init //[INIT] Initialised repository.
gp cs //[STYLE] Improved coding style.
```
