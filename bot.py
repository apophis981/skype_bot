import Skype4Py
import codecs
import hashlib
import logging

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Variable to check if the script has attached to skype Successfully (skype.attach())
status = Skype4Py.apiAttachSuccess

# Checks if the Skype Object is already connected to the Skype Client Sucessfully then
# Connects the Skype object to the Skype client if its not Successfull, otherwise
# Does nothing.
if status == 1:
    skype.Attach()
    print 'attached'
else:
    pass
    print 'passed'

print skype.Conferences[0]

# Pulls conversations and outputs them to a file.
#LogFile = 'TeamUR.log'
#iteratedObject = skype.Messages(Target =
#for x in skype.ActiveChats:
#    if len(x.Members) > 3:)

def get_chat_id(chat):
    """
    Get unique internal persistent id of the chat object.

    All ids are URL safe.

    This is the same id as in the web interface.

    :param chat: Skype4Py.chat.Chat instance
    """
    m = hashlib.md5()
    m.update(chat.Name)
    return m.hexdigest()

def FindGroupTarget():
    for x in skype.ActiveChats:
        if len(x.Members) > 20:
            return x
        else:
            pass

# Asks for a Username and Message, then sends the message.
while 0==0:
    Usr = raw_input('Who would you like to Send a message to (Skype Username): ')
    Msg = raw_input('What would you like to Send: ')
    skype.SendMessage(Usr, Msg)
