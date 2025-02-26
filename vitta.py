import time

VERDE = "\033[32m"
AMARELO = "\033[33m"
VERMELHO = "\033[31m"
RESETAR = "\033[0m"

print("+" + "-" * 80 + "+")
print("|{:^80}|".format(" Olá, boas-vindas! "))
print("|{:^80}|".format(" Sou a Vitta "))
print("|{:^80}|".format(" Sua assistente virtual de saúde e bem-estar. "))
print("+" + "-" * 80 + "+")
print("\nPara iniciar, vou precisar de algumas informações sobre você.\n")
print("+" + "-" * 80 + "+")

while True:
    nome = input("| Qual o seu nome? ")
    idade = int(input("| Qual a sua idade? "))
    peso = float(input("| Qual o seu peso? "))
    altura = float(input("| Qual a sua altura? (ex: 1.70) "))
    print("+" + "-" * 80 + "+")

    print("\n+" + "-" * 80 + "+")
    print("|{:^80}|".format(f" Olá, {nome}! "))
    print("|{:^80}|".format(" Analisando seus dados... "))
    print("+" + "-" * 80 + "+")
    time.sleep(2)

    imc = peso / (altura ** 2)

    print("{:^80}".format(f" Seu IMC é: {imc:.2f} "))

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        cor = AMARELO
    elif imc < 24.9:
        classificacao = "Peso normal"
        cor = VERDE
    elif imc < 29.9:
        classificacao = "Sobrepeso"
        cor = AMARELO
    elif imc < 34.9:
        classificacao = "Obesidade Grau 1"
        cor = AMARELO
    elif imc < 39.9:
        classificacao = "Obesidade Grau 2"
        cor = AMARELO
    else:
        classificacao = "Obesidade Grau 3"
        cor = VERMELHO

    print("{:<80}".format(f"Classificação: {cor}{classificacao}{RESETAR} "))
    print("{:<80}".format("Vamos ver algumas boas praticas saudaveis para a sua classificação de IMC."))
    print("+" + "-" * 80 + "+")
    time.sleep(2)

    dicas = {
        "Abaixo do peso": [
            "Alimentação: Aumente o consumo de proteínas e carboidratos saudáveis.",
            "Frequência alimentar: Faça refeições frequentes e nutritivas.",
            "Exercícios: Foque em musculação para ganho de massa muscular.",
            "Hidratação e descanso: Beba bastante água e tenha boas noites de sono.",
        ],
        "Peso normal": [
            "Alimentação: Mantenha uma dieta equilibrada.",
            "Moderação: Evite excessos e consuma fibras, frutas e vegetais.",
            "Exercícios: Pratique atividades físicas regularmente.",
            "Sono e bem-estar: Priorize boas noites de sono e controle o estresse.",
        ],
        "Sobrepeso": [
            "Alimentação: Reduza açúcares e ultraprocessados.",
            "Planejamento alimentar: Evite pular refeições.",
            "Exercícios: Caminhadas diárias ajudam na perda de gordura.",
            "Estilo de vida: Controle o estresse e pratique relaxamento.",
        ],
        "Obesidade Grau 1": [
            "Alimentação: Evite carboidratos refinados e gorduras ruins.",
            "Estratégias alimentares: Busque reeducação alimentar.",
            "Exercícios: Opte por atividades de baixo impacto.",
            "Acompanhamento: Busque orientação médica e nutricional.",
        ],
        "Obesidade Grau 2": [
            "Alimentação: Evite frituras e açúcares adicionados.",
            "Reeducação alimentar: Nutricionista pode ajudar.",
            "Exercícios: Prefira atividades de baixo impacto.",
            "Saúde mental: Suporte psicológico pode ser essencial.",
        ],
        "Obesidade Grau 3": [
            "Alimentação: Evite dietas restritivas sem orientação.",
            "Monitoramento nutricional: Um plano alimentar pode ajudar.",
            "Exercícios: Musculação adaptada pode auxiliar na mobilidade.",
            "Acompanhamento multidisciplinar: Suporte de especialistas é essencial.",
        ]
    }

    print("\n+" + "-" * 80 + "+")
    print("|{:^80}|".format(" Dicas de Saúde "))
    print("+" + "-" * 80 + "+")
    for dica in dicas[classificacao]:
        print("| {:<78} |".format(dica))
    print("+" + "-" * 80 + "+")

    print(f"\n{AMARELO}+" + "-" * 80 + "+")
    print(f"|{' ATENÇÃO! ':^80}|")
    print("+" + "-" * 80 + "+")
    print("|{:^80}|".format(" Lembre-se: Eu sou uma assistente de boas práticas "))
    print("|{:^80}|".format(" de saúde e bem-estar, não substituo a necessidade de uma consulta com "))
    print("|{:^80}|".format(" profissionais qualificados. Sempre procure um médico, nutricionista "))
    print("|{:^80}|".format(" ou especialista adequado para um diagnóstico preciso e um "))
    print("|{:^80}|".format(" acompanhamento personalizado e ideal para você. "))
    print("+" + "-" * 80 + f"+{RESETAR}")

    print("\nDeseja consultar o nome de outra pessoa?")
    print("1 - Sim")
    print("2 - Não")
    opcao = input("Digite a opção desejada: ")

    if opcao == "2":
        print("|{:^80}|".format(" A Vitta agradece sua visita, até mais \o "))
        break
