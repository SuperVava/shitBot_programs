"""
I whant to grow. I ned an automatic answerig machine for my shitbot.
"""

import random
import log
from colorama import Fore, init
init()

Users = []
#open a save file for the users than the bot responded
fichier = open("Users.txt", "r")
lines = fichier.readlines()
for line in lines:
     Users.append(line.strip())
print(Users)
fichier.close

api = log.setApi()

def autoRep(message, sender):
    api.mark_direct_message_read(last_read_event_id = message.id, recipient_id = sender)
    api.indicate_direct_message_typing(sender)
    #take a randome quote from me
    lastTweetId = api.user_timeline(user_id = 1572219374647361536, count = 1, include_rts = False)[0].id
    randomStart = random.randint(1572221111244554241, lastTweetId)
    randomTweetId = api.user_timeline(user_id = 1572219374647361536, max_id = randomStart, count = 2, include_rts = False)[0].id
    randomCitation = api.get_status(randomTweetId).text
    api.send_direct_message(sender, "Bonjour! Vous savez que je suis un robot, n'est-ce pas? Je ne vais pas pouvoir vous répondre... En revanche, comme le dirait @PoubelleMentale, mon créateur:\n\"" + randomCitation + "\"\nInspirant, non?")


def update():
    print(Fore.YELLOW + "Checking..." + Fore.WHITE)
    try:
        messages = api.get_direct_messages()
        for message in messages:
            senderId = message.message_create.get("sender_id")
            print(message.message_create.get("message_data").get("text"))
            if(senderId not in Users):
                autoRep(message = message, sender = senderId)
                print("Add user: " + str(senderId))
                writer = open("Users.txt", "a")
                writer.write(senderId + "\n")
                writer.close 
                Users.append(senderId)
            else:
                print(Fore.YELLOW + "already answered..." + Fore.WHITE)  
    except Exception as e:
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)
    print(Fore.GREEN + "Done!" + Fore.WHITE)
