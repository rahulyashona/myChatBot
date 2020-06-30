from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

convo = [
    "Hello",
    "Hi there!",
    "what is your name?",
    "My name is Bot, created by Rahul.",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "In which city do you live ?",
    "I live in Bhopal"
    "Thank you.",
    "You're welcome."
]


trainer = ListTrainer(bot)


trainer.train(convo)
print("Enter  'exit' whenever you want to stop.")
print("Talk to Rahul's bot:")
while True:
    ask =input()
    if ask =='exit':
        break
    response=bot.get_response(ask)
    print("bot: ",response)