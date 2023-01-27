import random

grinlist = [] #fill the list with discord emotes

def get_response(message: str) -> str:

    p_message = message.lower()

    if p_message == '-grin':
        index=random.randint(0,37)
        return grinlist[index]

    if p_message == '-help grin':
        return 'Just type `-grin` .'

    return