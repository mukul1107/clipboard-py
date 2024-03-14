#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.


newText = text.split("\n")
for i in range(len(newText)):
    newText[i] = '* ' + newText[i]


text = "\n".join(newText)
print(text)
pyperclip.copy(text)

