import sys
import os

init_words = ["init", "initialised", "first"]
feat_words = ["added", "new", "created", "add", "feat", "feature"]
fix_words = ["fix", "fixed"]
style_words = ["style", "norme"]

aliases = {
    "init": "[INIT] Initialised repository.",
    "cs": "[STYLE] Improved coding style."
}

commit_type = "[OTHER]"
message = ' '.join(sys.argv[1:])
if len(message) == 0:
    message = "[OTHER] No message for this commit."
elif message in aliases:
    message = aliases[message]
else:
    words_of_message = message.split(' ')
    for i in range(len(words_of_message)):
        if words_of_message[i].lower() in init_words:
            commit_type = "[INIT]"
            break
        if words_of_message[i].lower() in feat_words:
            commit_type = "[FEAT]"
            break
        if words_of_message[i].lower() in fix_words:
            commit_type = "[FIX]"
            break
        if words_of_message[i].lower() in style_words:
            commit_type = "[STYLE]"
            break
    message = commit_type + " " + message.capitalize()+"."

os.system("make fclean; git add --all; git commit -m \""+message+"\"; git push --force")