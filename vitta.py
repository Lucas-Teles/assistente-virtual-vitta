import time

print("+" + "-" * 60 + "+")
print("|{:^60}|".format(" Olá, boas-vindas! "))
print("|{:^60}|".format(" Sou a Vitta "))
print("|{:^60}|".format(" Sua assistente virtual de saúde e bem-estar. "))
print("+" + "-" * 60 + "+")
print("\nPara iniciar, vou precisar de algumas informações sobre você.\n")
print("+" + "-" * 60 + "+")

while True:
        # Entrada de dados
        nome = input("Qual o seu nome? ")
        idade = int(input("Qual a sua idade? "))
        peso = float(input("Qual o seu peso? "))
        altura = float(input("Qual a sua altura? (ex: 1.70) "))
        print("+" + "-" * 60 + "+")


        print("\n+" + "-" * 60 + "+")
        print("|{:^60}|".format(f" Olá, {nome}! "))
        print("|{:^60}|".format(" Analisando seus dados... "))
        print("+" + "-" * 60 + "+")
        time.sleep(1.5)

        # Calculo do IMC ... 
        imc = peso / (altura ** 2)

        print("|{:<60}|".format(f" Seu IMC é: {imc:.2f} "))

        if imc < 18.5:
            status = " No momento seu imc está informando -> abaixo do peso. "
        elif imc < 24.9:
            status = " No momento seu imc está informando -> peso normal. "
        elif imc < 29.9:
            status = " No momento seu imc está informando -> sobrepeso. "
        elif imc < 34.9:
            status = " No momento seu imc está informando -> obesidade grau 1. "
        elif imc < 39.9:
            status = " No momento seu imc está informando -> obesidade grau 2. "
        else:
            status = " No momento seu imc está informando -> obesidade grau 3. "

        print("|{:<60}|".format(status))
        print("+" + "-" * 60 + "+")
        # Fim do calculo do IMC

        # Conforme o IMC, a Vitta vai sugerir dicas de alimentação e exercícios, para melhorar saúde e bem estar.


        # ESPAÇO PARA LÓGICA DE SUGESTÃO DE ALIMENTAÇÃO E EXERCÍCIOS



        # Fim da lógica de sugestão de alimentação e exercícios

        #Finalizador do programa, vai ser editado em breve
        print("Deseja continuar? ") 
        print("1 - Sim")
        print("2 - Não")
        opcao = int(input("Digite a opção desejada: ")) 
        if opcao == 2:
            break
        else:
            continue         