from chatterbot.trainers import ListTrainer
from chatterbot import  ChatBot
from corpus import student, introdution, lingPython

bot = ChatBot('Teste')
bot.set_trainer(ListTrainer)
bot.train(introdution.trainIntrodution)
bot.train(student.trainStudent)
bot.train(lingPython.trainStudent)
cont = 0
while True:

    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence)>0.5:
        print ('Bot: ', response)
    else:
        cont = cont + 1
        if cont==1:
            print('Bot: Não entendi')
        elif cont==2:
            print('Bot: Desculpe, não estou entendo.')
        elif cont>2:
            print('Bot: Caramba, não entendo.')




