# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json, re
from . import models

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def convey(self, message, bot):
        self.send(text_data=json.dumps({
            'userMessage': message,
            'bot': bot, # message from bot
        }))

    def receive(self, text_data):
        user = models.User.objects.latest('id') # getting latest user in the database by primary key
        ind = user.answerIndex
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if ind == 1:
            user.answerIndex += 1 #getting to next answer
            user.name = message
            self.convey(message, 'Are you male or female?')
        elif ind == 2 and message.strip().lower() in ("male", "female"):
            user.answerIndex += 1
            user.sex = message
            self.convey(message, 'When were you born? Please answer in (YYYY-MM-DD) format')
        elif ind == 3:
            date = re.search("^(19[0-9][0-9]|20[0-1][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", message)
            # if user input is valid datefield, we continue processing
            if date:
                user.birth = date.group()
                user.answerIndex += 1
                self.convey(message, ' Are you a smoker? (Yes or No)')
        elif ind == 4 and message.strip().lower() in ("yes", "no"):
            user.answerIndex += 1
            user.smoker = message.strip().lower() == "yes"
            self.convey(message, 'Please type "Done" for results')
        elif ind == 5 and message.strip().lower() == "done":
            message = "{} was born in {} and is a {} {}.".format(user.name, user.birth, user.sex, user.smoker == True and "smoker" or "non-smoker")
            self.convey(message, 'Thank you!')
        user.save()