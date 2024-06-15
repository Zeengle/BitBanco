# Bibliotecas
import sys
import time
from datetime import datetime
import os
import json
import random
#-----------------------------FUNÇÕES-----------------------------------#

#função para o Botao de voltar
def botaoV():
    if opc == str() or opc.isdigit:
        for i in range(len(menu)):
            print(f"{menu[i]}")
            time.sleep(0.3)
        print("━"*34)
        return(resp)


#função do print do menu
def menuV():
    print("━━━━━━━━━━━━━━ Menu ━━━━━━━━━━━━━━")

#Função de verificação de senha
def senhaV():
    while True:
        senhaver = int(input("Digite sua senha: "))
        if senhaver == datas[cpf]['senha']:
            os.system("cls")
            print("━"*34)
            print("Acesso concedido")
            print("━"*34)
            break
        else:
            print("Senha incorreta, digite novamente")


#função para mostrar o saldo do usuario
def saldo():
    print(f"\nNome: {datas[cpf]['Nome']}\nCPF: {cpfformat}\n\nReais: {(datas[cpf]['reais']):.2f}\nBitcoin: {(datas[cpf]['bitcoin']):.2f}\nEthereum: {(datas[cpf]['ethereum']):.2f}\nRipple: {(datas[cpf]['ripple']):.2f}\n")

#Função da compra de criptomoedas
def comprarC():
    print(f"Cotação das Criptomoedas:\nBitcoin [1 real vale: {(datas[cpf]['moedas']["cotB"]):.2f} BTC]\nEthereum [1 real vale: {(datas[cpf]['moedas']["cotE"]):.2f} ETH]\nRipple [1 real vale: {(datas[cpf]['moedas']["cotR"]):.2f} XRP]")
    moeda = str(input("Que moeda deseja comprar?\n[B] - Bitcoin\n[E] - Ethereum\n[R] - Ripple\n")).upper()
    if moeda == "B":
        os.system("cls")
        while True:
            print(f"Você possui R${(datas[cpf]['reais']):.2f}")
            print(f"Cotação do Bitcoin [1 real equivale a {(datas[cpf]['moedas']["cotB"]):.2f} BTC]")
            compra = float(input(f"Você possui {(datas[cpf]['bitcoin']):.2f}BTC\nQuantos bitcoins deseja comprar?(Em R$): "))
            os.system("cls")
            if compra ==0:
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} BTC CT: {(datas[cpf]['moedas']["cotB"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            preco = (datas[cpf]['reais'] - compra)*0.02 + compra
            if datas[cpf]['reais'] - preco >= 0:
                datas[cpf]['bitcoin'] = (compra*datas[cpf]['moedas']["cotB"]) + datas[cpf]['bitcoin']
                datas[cpf]['reais'] -= preco
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} BTC CT: {(datas[cpf]['moedas']["cotB"]):.2f}  TX:0.02 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Você não possui reais necessários para comprar esta quantidade de Bitcoins")
        

    if moeda == "E":
        os.system("cls")
        while True:
            print(f"Você possui R${(datas[cpf]['reais']):.2f}")
            print(f"Cotação do Ethereum [1 real equivale a {(datas[cpf]['moedas']["cotE"]):.2f} ETH]")
            compra= float(input(f"Você possui {(datas[cpf]['ethereum']):.2f}ETH\nQuantos Ethereum deseja comprar?(Em R$): "))
            os.system("cls")
            if compra ==0:
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} ETH CT: {(datas[cpf]['moedas']["cotE"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            preco  = ((datas[cpf]["reais"] - compra)*0.01) + compra
            if datas[cpf]['reais'] - preco >=0:
                datas[cpf]['ethereum'] = (compra*datas[cpf]['moedas']["cotE"]) + datas[cpf]['ethereum']
                datas[cpf]["reais"] -= preco
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} ETH CT: {(datas[cpf]['moedas']["cotE"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Você não possui reais necessários para comprar esta quantidade de Ethereum")
                

    if moeda == "R":
        os.system("cls")
        while True:
            print(f"Você possui R${(datas[cpf]['reais']):.2f}")
            print(f"Cotação do Ripple [1 real equivale a {(datas[cpf]['moedas']["cotR"]):.2f} XRP]")
            compra = float(input(f"Você possui {(datas[cpf]['ripple']):.2f}XRP\nquantos Ripple deseja comprar?(Em R$): "))
            os.system("cls")
            if compra ==0:
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} XRP CT: {(datas[cpf]['moedas']["cotR"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            preco = (datas[cpf]['reais'] - compra)*0.01 + compra
            if datas[cpf]['reais'] - preco >=0:
                datas[cpf]["ripple"] = (compra*datas[cpf]['moedas']["cotR"]) + datas[cpf]['ripple']
                datas[cpf]["reais"] -= preco
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {compra:.2f} XRP CT: {(datas[cpf]['moedas']["cotR"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Você não possui reais necessários para comprar esta quantidade de Ripple")

#Função de vender as criptomoedas
def venderC():
    print(f"Cotação das Criptomoedas:\nBitcoin [1 real vale: {(datas[cpf]['moedas']["cotB"]):.2f} BTC]\nEthereum [1 real vale: {(datas[cpf]['moedas']["cotE"]):.2f} ETH]\nRipple [1 real vale: {(datas[cpf]['moedas']["cotR"]):.2f} XRP]")
    moeda = str(input("Que moeda deseja vender?\n[B] - Bitcoin\n[E] - Ethereum\n[R] - Ripple\n")).upper()
    if moeda == "B":
        os.system("cls")
        while True:
            print(f"Cotação do Bitcoin [1 real equivale a {(datas[cpf]['moedas']["cotB"]):.2f} BTC]")
            venda = float(input(f"Você possui {(datas[cpf]['bitcoin']):.2f}BTC\nQuantos bitcoins deseja vender?: "))
            os.system("cls")
            if venda <= datas[cpf]['bitcoin']:
                juros = (-venda)+(datas[cpf]['bitcoin']-venda)*0.03
                datas[cpf]['bitcoin']-= venda
                datas[cpf]['reais'] += (-juros*datas[cpf]['moedas']["cotB"])
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {venda:.2f} BTC CT: {(datas[cpf]['moedas']["cotB"]):.2f}  TX:0.03 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Saldo de Bitcoins indisponível")

    if moeda == "E":
        os.system("cls")
        while True:
            print(f"Cotação do Ethereum [1 real equivale a {(datas[cpf]['moedas']["cotE"]):.2f} ETH]")
            venda = float(input(f"Você possui {(datas[cpf]['ethereum']):.2f}ETH\nQuantos Ethereum deseja vender?: "))
            os.system("cls")
            if venda <= datas[cpf]['ethereum']:
                juros = (-venda)+(datas[cpf]['ethereum']-venda)*0.02
                datas[cpf]["ethereum"]-= venda
                datas[cpf]["reais"] += (-juros/datas[cpf]['moedas']["cotE"])
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {venda:.2f} ETH CT: {(datas[cpf]['moedas']["cotE"]):.2f}  TX:0.02 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Saldo de Ethereum indisponível")

    if moeda == "R":
        os.system("cls")
        while True:
            print(f"Cotação do Ripple [1 real equivale a {(datas[cpf]['moedas']["cotR"]):.2f} XRP]")
            venda = float(input(f"Você possui {(datas[cpf]['ripple']):.2f}XRP\nQuantos Ripple deseja vender?: "))
            os.system("cls")
            if venda <= datas[cpf]['ripple']:
                juros = (-venda)+(datas[cpf]['ripple']-venda)*0.01
                datas[cpf]["ripple"] -= venda
                datas[cpf]['reais'] += (-juros*datas[cpf]['moedas']["cotR"])
                saldo()
                extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {venda:.2f} XRP CT: {(datas[cpf]['moedas']["cotR"]):.2f}  TX:0.01 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
                datas[cpf]['EXT'].append(extrato)
                break
            else:
                print("Saldo de Ripple indisponível")

#Função para sacar reais
def sacar():
    while True:
        reais = float(input(f"Você possui R${(datas[cpf]['reais']):.2f}\nDigite o valor que deseja retirar (em R$): "))
        if reais <= datas[cpf]["reais"]:
            datas[cpf]["reais"] -= reais
            saldo()
            extrato = (f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {reais:.2f} REAL CT: 0.0  TX:0.00 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
            datas[cpf]['EXT'].append(extrato)
            break
        else:
            print("Impossível sacar este valor")

#Função para depositar reais
def depositar():
    reais = float(input(f"Você possui R${(datas[cpf]['reais']):.2f}\nDigite o valor que deseja depositar (em R$): "))
    datas[cpf]["reais"]+= reais
    datas[cpf]['reais'] = datas[cpf]['reais']
    saldo()
    extrato =(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} + {reais:.2f} REAL CT: 0.0  TX:0.00 REAL: {(datas[cpf]['reais']):.2f} BTC: {(datas[cpf]['bitcoin']):.2f} ETH: {(datas[cpf]['ethereum']):.2f} XRP: {(datas[cpf]['ripple']):.2f}")
    datas[cpf]['EXT'].append(extrato)

#Função que mostra o extrato
def ler_extrato():
    for i in datas[cpf]['EXT']:
        print(i)

#Função que atualiza a cotação das moedas
def atualizar_cot():
    os.system("cls")
    datas[cpf]['moedas']["cotB"] = (random.uniform(-0.05, 0.05)*datas[cpf]['moedas']["cotB"]+datas[cpf]['moedas']["cotB"])
    print(f"Cotação do Bitcoin em relação ao real: {(datas[cpf]['moedas']["cotB"]):.2f}")
    datas[cpf]['moedas']["cotE"] =(random.uniform(-0.05, 0.05)*datas[cpf]['moedas']["cotE"]+datas[cpf]['moedas']["cotE"])
    print(f"Cotação do Ethereum em relação ao real: {(datas[cpf]['moedas']["cotE"]):.2f}")
    datas[cpf]['moedas']["cotR"] = (random.uniform(-0.05, 0.05)*datas[cpf]['moedas']["cotR"]+datas[cpf]['moedas']["cotR"])
    print(f"Cotação do Ripple em relação ao real: {(datas[cpf]['moedas']["cotR"]):.2f}")

#Função que atualiza as informações no json pro codigo
def atualizar_usuarios_json(datas):
    with open("data.json", "w") as file:
        json.dump(datas, file, indent=4)

#Função que atualiza as infos no codigo pro json
def atualizar_usuarios_codigo():
    with open("data.json", "r") as file:
        datas = json.load(file)
    return datas

#Função de verificar se o cpf esta ou nao no banco de dados
def verificarcpf():
    with open("data.json", "r") as file:
        cpfs = json.load(file)
    if cpf in cpfs:
        atualizar_usuarios_codigo()
        return
    else:
        atualizar_usuarios_json(datas)
        datas[cpf]={"Nome": nome, "senha": senha, "reais":0, "bitcoin": 0, "ethereum": 0, "ripple": 0, "EXT": [], "moedas": {"cotB": 1, "cotE": 2, "cotR": 0.5}}

#-------------------------------------------------------------------------------------------------#

#introdução do terminmal
os.system("cls")
print("━"*34)
print("Bem vindo ao BitBanco!")
print("━"*34)
print("Por favor, insira seus dados: ")

#criação de uma lista dos elementos do menu
menu = ["1 .Consultar saldo ", "2 .Consultar extrato", "3 .Depositar", "4 .Sacar ", "5 .Comprar criptomoedas", "6 .Vender criptomoedas", "7 .Atualizar cotação", "8 .Sair"]

#atualizar as infos pro json
datas = atualizar_usuarios_codigo()

# looping para toda a funcionalidade do projeto
while True:
    # criação de variaveis bases para o login do usuario
    cpf = str(input("Digite seu CPF: "))
    nome = str(input("Nome: "))
    senha = int(input("Senha (deve conter até 6 dígitos numéricos): "))
    #limpar o terminal
    os.system("cls")
    #Formatação do CPF
    cpfformat = (f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    
    # Condição para saber se a senha o cpf ou o nome foram digitados corretamente
    if len(str(senha)) == 6 and len(str(cpf)) == 11 and len(str(nome)) >=2:
        
        #Verificar se o cpf esta no banco de dados
        verificarcpf()

        #Atualizar as infos no json
        atualizar_usuarios_json(datas)

        # caso esteja tudo certo, o programa começa mostrando o menu
        print("━"*34)
        print(f"Bem vindo {datas[cpf]['Nome']}!")
        menuV()
        
        #looping de for para mostrar todas as abas disponiveis do menu pela lista criada acima 
        for i in range(len(menu)):
            print(f"{menu[i]}")
            time.sleep(0.3) 
        print("━"*34)

        while True:    
            # variavel para o usuario digitar o respectivo numero da aba que queira 
            resp = int(input("Digite o número correspondente a aba que queira acessar: "))
            os.system("cls")

            #condições, que dependendo do numero digitado pelo usuario, o levarao para diferentes abas 
            if resp == 1:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━ Consultar Saldo ━━━━━━━━━")
                senhaV()
                saldo()
                opc = input("Deseja voltar? [Digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()         
                
            if resp == 2:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━ Consultar Extrato ━━━━━━━━━")
                senhaV()
                ler_extrato()
                opc = input("Deseja voltar? [digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()

            if resp == 3:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━━━━ Depositar ━━━━━━━━━━━━")
                depositar()
                opc = input("Deseja voltar? [Digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()

            if resp == 4:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━━━━ Sacar ━━━━━━━━━━━━")
                sacar()
                opc = input("Deseja voltar? [Digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()

            if resp == 5:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━━━━ Comprar Criptomoedas ━━━━━━━━━━━━")
                senhaV()
                saldo()
                comprarC()      
                opc = input("Deseja voltar? [Digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()

            if resp == 6:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━━━━ Vender Criptomoedas ━━━━━━━━━━━━")
                senhaV()
                saldo()
                venderC()
                opc = input("Deseja voltar? [Digite qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()

            if resp == 7:
                atualizar_usuarios_codigo()
                print("━━━━━━━━━━━━ Atualizar Cotação ━━━━━━━━━━━━")
                atualizar_cot()
                opc = input("Deseja voltar? [Ditie qualquer tecla]: ")
                atualizar_usuarios_json(datas)
                os.system("cls")
                menuV()
                botaoV()
            if resp == 8:
                    atualizar_usuarios_codigo()
                    atualizar_usuarios_json(datas)
                    # caso o numero digitado seja a aba (saida), o programa fecha.
                    sys.exit()
                    
    # caso a senha ou o cpf sejam digitados de forma errada
    else:
        print("CPF ou Senha incorreta, tente novamente")