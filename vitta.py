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
    nome = input("| Qual o seu nome? ")
    idade = int(input("| Qual a sua idade? "))
    peso = float(input("| Qual o seu peso? "))
    altura = float(input("| Qual a sua altura? (ex: 1.70) "))
    print("+" + "-" * 60 + "+")

    print("\n+" + "-" * 60 + "+")
    print("|{:^60}|".format(f" Olá, {nome}! "))
    print("|{:^60}|".format(" Analisando seus dados... "))
    print("+" + "-" * 60 + "+")
    time.sleep(1.5)

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    print("|{:^60}|".format(f" Seu IMC é: {imc:.2f} "))

    if imc < 18.5:
        status = " No momento seu IMC está informando -> abaixo do peso. "
    elif imc < 24.9:
        status = " No momento seu IMC está informando -> peso normal. "
    elif imc < 29.9:
        status = " No momento seu IMC está informando -> sobrepeso. "
    elif imc < 34.9:
        status = " No momento seu IMC está informando -> obesidade grau 1. "
    elif imc < 39.9:
        status = " No momento seu IMC está informando -> obesidade grau 2. "
    else:
        status = " No momento seu IMC está informando -> obesidade grau 3. "

    print("|{:^60}|".format(status))
    print("+" + "-" * 60 + "+")

    # Dicas de saúde
    dicas = {
        "Abaixo do peso": [
            "Alimentação: Aumente o consumo de proteínas e carboidratos saudáveis.",
            "Frequência alimentar: Faça refeições frequentes e nutritivas.",
            "Exercícios: Foque em musculação para ganho de massa muscular.",
            "Hidratação e descanso: Beba bastante água e tenha boas noites de sono.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ],
        "Peso normal": [
            "Alimentação: Mantenha uma dieta equilibrada.",
            "Moderação: Evite excessos e consuma fibras, frutas e vegetais.",
            "Exercícios: Pratique atividades físicas regularmente.",
            "Sono e bem-estar: Priorize boas noites de sono e controle o estresse.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ],
        "Sobrepeso": [
            "Alimentação: Reduza açúcares e ultraprocessados.",
            "Planejamento alimentar: Evite pular refeições.",
            "Exercícios: Caminhadas diárias ajudam na perda de gordura.",
            "Estilo de vida: Controle o estresse e pratique relaxamento.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ],
        "Obesidade Grau 1": [
            "Alimentação: Evite carboidratos refinados e gorduras ruins.",
            "Estratégias alimentares: Busque reeducação alimentar.",
            "Exercícios: Opte por atividades de baixo impacto.",
            "Acompanhamento: Busque orientação médica e nutricional.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ],
        "Obesidade Grau 2": [
            "Alimentação: Evite frituras e açúcares adicionados.",
            "Reeducação alimentar: Nutricionista pode ajudar.",
            "Exercícios: Prefira atividades de baixo impacto.",
            "Saúde mental: Suporte psicológico pode ser essencial.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ],
        "Obesidade Grau 3": [
            "Alimentação: Evite dietas restritivas sem orientação.",
            "Monitoramento nutricional: Um plano alimentar pode ajudar.",
            "Exercícios: Musculação adaptada pode auxiliar na mobilidade.",
            "Acompanhamento multidisciplinar: Suporte de especialistas é essencial.",
            "Consulte profissionais: Nutricionista, médico e educador físico."
        ]
    }

    classificacao = "Peso normal"
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade Grau 2"
    elif imc >= 40:
        classificacao = "Obesidade Grau 3"

    print("\n+" + "-" * 60 + "+")
    print("|{:^60}|".format(" Dicas de Saúde "))
    print("+" + "-" * 60 + "+")
    for dica in dicas[classificacao]:
        print("| {:<58} |".format(dica))
    print("+" + "-" * 60 + "+")

    # Opção de continuar ou sair
    print("\nDeseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "2":
        break
