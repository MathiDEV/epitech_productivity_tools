import subprocess
import sys
from pynput.keyboard import Key, Controller

keys = []
codes = {
    "up": Key.up,
    "right": Key.right,
    "left": Key.left,
    "down": Key.down
}
test_folder = sys.argv[1]
instructions = open("%s/test.txt" % test_folder).read().splitlines()
return_expected = int(instructions[0])
for inst in instructions[1:]:
    if inst.lower() in codes:
        keys.append(codes[inst.lower()])

keys += ["A"]

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    exit(0 if return_expected == return_code else 1)

key_index = 0
print("[?1h")
for path in execute(['./my_sokoban', "%s/map.txt" % test_folder]):
    if "[2J" in path:
        if key_index == len(keys):
            exit(1)
        keyboard = Controller()
        keyboard.press(keys[key_index])
        keyboard.release(keys[key_index])
        key_index += 1
