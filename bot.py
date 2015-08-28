import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Variable to check if the script has attached to skype sucessfully (skype.attach())
status = Skype4Py.apiAttachSuccess

# Checks if the Skype Object is already connected to the Skype Client Sucessfully then
# Connects the Skype object to the Skype client if its not Sucessfull, otherwise
# Does nothing.
if status == 0:
    pass
    print 'passed'
else:
    skype.Attach()
    print 'attached'

# Asks for a Username and Message, then sends the message.
while 0==0:
    Usr = raw_input('Who would you like to Send a message to (Skype Username): ')
    Msg = raw_input('What would you like to Send: ')
    skype.SendMessage(Usr, Msg)
