# Configuration

epitech_year = 1

################################################################
################################################################
################################################################

import json
import sys
import webbrowser

if epitech_year < 1 or epitech_year > 3:
    print("ERROR: No projects for year \"%d\"" % epitech_year)
    exit(84)

projects = json.loads(open("%s/data/tek%d.json"%("/".join(sys.argv[0].split("/")[:-1]), epitech_year)).read())
matches = []
if len(sys.argv) != 2:
    print("USAGE: project <project name>")
    exit(84)
project_name = ''.join(x for x in sys.argv[1] if x.isalnum()).lower()
for module in projects:
    for project in module["projects"]:
        if project_name in ''.join(x for x in project["name"] if x.isalnum()).lower():
            matches.append(project)

try:
    if len(matches) == 0:
        print("ERROR: No project matches \"%s\"" % sys.argv[1])
        exit(84)
    if len(matches) == 1:
        selected = 0
    else:
        for i, v in enumerate(matches):
            if i == len(matches) - 1:
                char = "└"
            else:
                char = "├"
            print("%c─%d─ %s" % (char, i + 1, v["name"]))
        selected = -1
        while selected < 0 or selected >= len(matches):
            select = input("> ")
            if not select.isnumeric():
                continue
            selected = int(select) - 1
    if len(matches[selected]["files"]) == 1:
        fileid = 0
    else:
        print("========")
        for i, v in enumerate(matches[selected]["files"]):
            if i == len(matches[selected]["files"]) - 1:
                char = "└"
            else:
                char = "├"
            print("%c─%d─ %s" % (char, i + 1, v["name"]))
        fileid = -1
        while fileid < 0 or fileid >= len(matches[selected]["files"]):
            select = input("> ")
            if not select.isnumeric():
                continue
            fileid = int(select) - 1

    webbrowser.open(matches[selected]["files"][fileid]["url"])
except:
    print("exit")