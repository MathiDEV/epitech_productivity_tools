from distutils.sysconfig import get_python_inc
import json
import time
from datetime import datetime
import os
import sys
timeline = json.loads(open("timeline.json", 'r').read())
def get_ts(text, pattern):
    return(int(time.mktime(datetime.strptime(text, pattern).timetuple())))
def print_line(now, size):
    for i in range(size):
        if i - 2 == now:
            print("|", end="")
        else:
            print(" ", end="")
    print("")
rows, columns = os.popen('stty size', 'r').read().split()
begin = get_ts("01/10/"+ str(datetime.now().year - (datetime.now().month < 9)), "%d/%m/%Y")
end = get_ts("20/06/"+ str(datetime.now().year + (datetime.now().month >= 9)), "%d/%m/%Y")
now = get_ts(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
width = int(columns) - 10
step = int((end - begin) / width)
modules = {}
now_pos = 0
i = 0
for curr in range(begin, end, step):
    if (curr - step < now and curr + step > now):
        now_pos = i
    i += 1
for proj in timeline:
    m_code = proj["module_code"]
    if m_code in modules:
        modules[m_code].append(proj)
    else:
        modules[m_code] = [proj]

selected = False
if len(sys.argv) == 3:
    if sys.argv[1] not in modules:
        print(sys.argv[1] + " is not a module.")
        exit(84)
    if int(sys.argv[2], 16) not in range(1, len(modules[sys.argv[1]]) + 1):
        print(sys.argv[2] + " out of range for module " + sys.argv[1] + ".")
        exit(84)
    project = sorted(modules[sys.argv[1]], key=lambda d: get_ts(d["start"], "%d/%m/%Y"))[int(sys.argv[2], 16) - 1]
    selected = [sys.argv[1], int(sys.argv[2], 16), get_ts(project["start"], "%d/%m/%Y"), get_ts(project["end"], "%d/%m/%Y")]
    print("Selected project: \033[1m"+ project["project"])
    print("\033[0;2;3mModule "+ project["module"][5:] + " ("+ project["module_code"] + ")")
    print("From "+ project["start"] + " to " + project["end"] + "\033[0m")

print((6 + width) * '-')

for mod in modules:
    modules[mod] = sorted(modules[mod], key=lambda d: get_ts(d["start"], "%d/%m/%Y"))
    print(mod + " | ", end="")
    i = -1
    last_proj = -1
    for curr in range(begin, end, step):
        found_proj = False
        print_count = 0
        if selected and selected[0] == mod and selected[2] <= curr and selected[3] >= curr:
            if selected[1] != last_proj:
                print("\033[41;30m"+hex(selected[1]).lstrip("0x").rstrip("L"), end="")
            else:
                print("\033[41m ", end="")
            last_proj = selected[1]
            i += 1
            continue
        for proj_index in range(len(modules[mod])):
            proj = modules[mod][proj_index]
            proj_index += 1
            if not found_proj and get_ts(proj["start"], "%d/%m/%Y") <= curr and get_ts(proj["end"], "%d/%m/%Y") >= curr:
                if proj_index != last_proj:
                    print("\033[47;30m"+hex(proj_index).lstrip("0x").rstrip("L"), end="")
                else:
                    print("\033[47m ", end="")
                last_proj = proj_index
                found_proj = True
        if not found_proj:
            now = get_ts(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
            if i == now_pos:
                print("\033[0m|", end="")
                print_count += 1
            else:
                print("\033[0m ", end="")
                print_count += 1
        i += 1
    print("\n-----", end="")
    if mod == list(modules)[-1]:
        print((1 + width) * '-')
    else:
        print_line(now_pos, width)