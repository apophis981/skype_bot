import sys
import os
import time
import Skype4Py
import random
import cleverbot
import markovify

# Read text file, replace new lines with spaces, and save to variable
with open ("padula.txt", "r") as myfile:
      padula_text=myfile.read().replace('\n', ' ')

# Build the model.
text_model = markovify.Text(padula_text)

#Create cleverbot instance
cb1 = cleverbot.Cleverbot()

# Fired on attachment status change. Here used to re-attach this script to Skype in case attachment is lost. Just in
#case.
def OnAttach(status):
    print 'API attachment status: ' + skype.Convert.AttachmentStatusToText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

    if status == Skype4Py.apiAttachSuccess:
       print('***************************************')
       print('Type "markov" to generate sentences')
       print('Type "exit" to quit')
       print('Type "help" for help')


# Fired on chat message status change.
# Statuses can be: 'UNKNOWN' 'SENDING' 'SENT' 'RECEIVED' 'READ'

def OnMessageStatus(Message, Status):
    if Status == 'RECEIVED':
        print(Message.FromHandle + ': ' + Message.Body)
        response = cb1.ask(Message.Body)
        print('sending to: ' + Message.FromHandle + ' message: ' + response)
        if response != "Developers, start your chat engines! Cleverscript.com." or "Create chatty bots for fun and games, or even for business - Cleverscript.com." or "*kicks you* Hey you! Chat to the free ANGRY DUDE iOS app!":
            skype.SendMessage(Message.FromHandle, response)
        else:
            skype.SendMessage(Message.FromHandle, "No Comment")

    if Status == 'READ':
        print(Message.FromDisplayName + ': ' + Message.Body)

    if Status == 'SENT':
        print('Myself: ' + Message.Body)


# Creating instance of Skype object, assigning handler functions and attaching to Skype.
skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnMessageStatus = OnMessageStatus

print('***************************************')
print 'Connecting to Skype..'
skype.Attach()

# Looping until user types 'exit'
Cmd = ''
while not Cmd == 'exit' and not Cmd == 'quit':
    Cmd = raw_input('User/: ')
    if Cmd == 'markov':
        for i in range(50):
            print(text_model.make_sentence())
            next
    if Cmd == 'help':
       print('Type "markov" to generate sentences')
       print('Type "exit" to quit')
       print('Type "help" for help')
       next
