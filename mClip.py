#! python3
# mClip.py - A multi-clipboard program.

import sys, pyperclip
from sys import argv
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Usage: python mClip.py [keyphrase] - copy phrase text')
    sys.exit()



# python mClip.py add key
keyphrase = sys.argv[1]    # first command line arg is the keyphrase
if keyphrase == "add":
    key = str(input("Enter the Key: "))
    

    if key not in TEXT:
        phrase = str(input("Enter the text for this phrase: "))
        newSlang = {key: phrase}
        TEXT.update(newSlang)
        print( keyphrase,":",phrase,"✅")
        sys.exit()
    else:
        print(keyphrase, "already added!")


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for', keyphrase , 'copied to clipboard.')
else:
    print("No text found for", keyphrase)