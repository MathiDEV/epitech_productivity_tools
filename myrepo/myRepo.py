import os
gitignore = "*.o\n*.out\n*.lib\n*.a\n*.gcno\n*.gcda\n.vscode\n"
lib_makefile_content = "##\n## EPITECH PROJECT, 2021\n## $1\n## File description:\n## Makefile for lib $2.\n##\n\nSRC=	$(wildcard *.c)\n\nNAME=	lib$2.a\n\nLIB_DEST=	../\n\nOBJ=	$(SRC:.c=.o)\n\nall:	$(NAME)\n\n$(NAME):	$(OBJ)\n	ar rc $(NAME) $(OBJ)\n	cp $(NAME) $(LIB_DEST)\n\nclean:\n	rm -f $(OBJ)\n\nfclean: clean\n	rm -f $(NAME)\n	rm -f ../$(NAME)\n\nre: fclean all\n"
github_ci = "name: CI\n\non: push\njobs:\n  run-tests:\n    runs-on: ubuntu-latest\n    # needed for criterion\n    container:\n        image: epitechcontent/epitest-docker:latest\n\n    steps:\n    - uses: actions/checkout@v2\n    - name: compile binary\n      run: |\n          make\n          make re\n\n  code-quality:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v2\n    - name: install thingz\n      run: sudo apt install -y clang-tidy clang-format\n    - name: clang-format lint\n      run: make CI"
ascii_logo = ''' ____________________________________________
/                   _____                    \\
|                  |  __ \                   |
|   _ __ ___  _   _| |__) |___ _ __   ___    |
|  | '_ ` _ \| | | |  _  // _ \ '_ \ / _ \   |
|  | | | | | | |_| | | \ \  __/ |_) | (_) |  |
|  |_| |_| |_|\__, |_|  \_\___| .__/ \___/   |
|              __/ |          | |            |
|             |___/           |_|            |
\____________________________________________/
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

affirmative = ["o", "y", "oui", "yes"]
print(bcolors.OKBLUE + ascii_logo + bcolors.BOLD + "\nThe easiest way to init your {EPITECH.} repository.\n"+ bcolors.ENDC)
try:
    if "epitech" not in open(".git/config", "r").read().lower():
        raise Exception('Not Epitech repo')
except:
    rep = input(bcolors.WARNING +"WARNING: It seems that this repository is not affiliated with Epitech, do you want to initiate it anyway ?\n"+ bcolors.ENDC)
    if rep.lower() not in affirmative:
        exit(0)

infos = {
    "name" : ["Binary name", "*", ""],
    "libs" : ["Libs (comma separated)", "*", ""],
    "tests" : ["Unit tests", "o/n", False],
    "ci" : ["GitHub Actions", "o/n", False],
}


phony = ".PHONY: all clean fclean re"

for i in infos:
    rep = input(bcolors.HEADER + infos[i][0]+": ")
    if infos[i][1] == "*":
        infos[i][2] = rep
    elif infos[i][1] == "o/n":
        if rep.lower() in affirmative:
            infos[i][2] = True
infos["name"][2] = infos["name"][2].lower().replace(" ", "_")
infos["libs"][2] = list(filter(None,infos["libs"][2].replace(" ", "").split(",")))

makefile = '''##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Project's main makefile
##

SRC	=	$(wildcard *.c) $(wildcard src/*.c)

OBJ	=	$(SRC:.c=.o)

NAME	=	''' + infos["name"][2] + '''

TESTS	=	-lcriterion --coverage

LIB	=	'''

lib_actions = ""

repo_name = os.getcwd().split("/")[-1]
if not os.path.exists("src"):
    os.mkdir("src")
if not os.path.exists("include"):
    os.mkdir("include")
includes = ""
main_file = open(infos["name"][2]+'.c', 'w+')
main_file.write("/*\n** EPITECH PROJECT, 2021\n** " + repo_name + "\n** File description:\n** Main file of " + infos["name"][2] + " project.\n*/\n\nint main(int argc, char **argv)\n{\n    return (0);\n}\n")
main_file.close()
if len(infos["libs"][2]) > 0:
    makefile += "	-L./lib -l" + " -l".join(infos["libs"][2])
    lib_actions = "			make$ -C./lib/" + "\n			make$ -C./lib/".join(infos["libs"][2])+ "\n"
    if not os.path.exists("lib"):
        os.mkdir("lib")
    for i in range(len(infos["libs"][2])):
        lib_name = infos["libs"][2][i]
        if not os.path.exists("lib/"+lib_name):
            os.mkdir("lib/"+lib_name)
            lib_makefile = open('lib/'+lib_name+'/Makefile', 'w+')
            lib_makefile.write(lib_makefile_content.replace("$1", repo_name).replace("$2", lib_name))
            lib_makefile.close()
        if (lib_name != infos["name"][2]):
            lib_header = open('include/'+lib_name+'.h', 'w+')
            lib_header.write("/*\n** EPITECH PROJECT, 2021\n** " + repo_name + "\n** File description:\n** Header file for lib " + lib_name + ".\n*/\n\n#ifndef "+lib_name.upper()+"_H_\n    #define "+lib_name.upper()+"_H_\n\n#endif")
            includes += ("\n#include \"" + lib_name + ".h\"")
            lib_header.close()
    if len(includes) > 0:
        includes += '\n'
lib_header = open('include/'+infos["name"][2]+'.h', 'w+')
lib_header.write("/*\n** EPITECH PROJECT, 2021\n** " + repo_name + "\n** File description:\n** Header file for project " + infos["name"][2] + ".\n*/\n"+includes+"\n#ifndef "+infos["name"][2].upper()+"_H_\n    #define "+infos["name"][2].upper()+"_H_\n\n#endif")
lib_header.close()
makefile += "\n\n"

makefile += "${NAME}:	${OBJ}\n" + lib_actions.replace("make$", "make") + "			gcc -o ${NAME} ${OBJ} $(LIB)\n\nall :		${NAME}\n\n"
makefile += "clean:\n			rm -f ${OBJ}\n" + lib_actions.replace("make$", "make clean") + "\n\n"
makefile += "fclean:	clean\n			rm -f ${NAME}\n" + lib_actions.replace("make$", "make fclean") + "\n"
if infos["tests"][2]:
    makefile += "			rm -f *.gcno *.gcda unit_tests\n"
makefile += "\nre:		fclean all\n\n"

if infos["tests"][2]:
    makefile += "unit_tests:		re\n		gcc -o unit_tests $(SRC) tests/tests_" + infos["name"][2] + ".c $(LIB) $(TESTS)\n\n"
    makefile += "tests_run:		unit_tests\n		./unit_tests\n\n"
    phony += " unit_tests tests_run"
    if not os.path.exists("tests"):
        os.mkdir("tests")
        tests = open('tests/tests_'+infos["name"][2]+'.c', 'w+')
        tests.write("/*\n** EPITECH PROJECT, 2021\n** " + repo_name + "\n** File description:\n** Unit tests for " + infos["name"][2] + " project.\n*/\n\n#include <criterion/criterion.h>\n#include <criterion/redirect.h>\n#include \"../include/"+infos["name"][2]+".h\"\n\n")
        tests.close()
makefile += phony + "\n"

mfile = open('Makefile', 'w+')
mfile.write(makefile)
mfile.close()

gitign = open('.gitignore', 'w+')
gitign.write(gitignore)
gitign.close()

if infos["ci"][2]:
    if not os.path.exists(".github"):
        os.mkdir(".github")
    if not os.path.exists(".github/workflows"):
        os.mkdir(".github/workflows")
    git_ci = open('.github/workflows/CI.yml', 'w+')
    git_ci.write(github_ci)
    git_ci.close()
