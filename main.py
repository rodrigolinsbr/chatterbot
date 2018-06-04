from  chatterbot.trainers import ListTrainer
from chatterbot import  ChatBot

bot = ChatBot('Teste')
convI = ['oi', 'olá','olá, bom dia!', 'Bom dia como vai?','Estou bem']
convF = ['Qual seu nome?','Meu nome é Sabidão', 'Você é aluno?','Já conhece nossos curso?','Não?','Acesse: www.sabertecnologias.com' ]
convE = ['Estou com problemas','Você tem problemas com Elabore?','O que achou do sistema?', 'Eu gostei bastante!', 'Você conhece Isabela?', 'Qual o browser que você usa?']

bot.set_trainer(ListTrainer)
bot.train(convI)
bot.train(convF)
bot.train(convE)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence)>0.5:
        print ('Bot: ', response)
    else:
        print('Bot: Não entendi')
