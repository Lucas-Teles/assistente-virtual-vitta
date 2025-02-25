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
 if imc < 18.5:
         classificação = "Abaixo do peso" 
         dicas = [
        " Alimentação: Aumente o consumo de proteínas (carnes magras, ovos, leguminosas) e carboidratos saudáveis (batata-doce, arroz integral, aveia).",
        " Frequência alimentar: Faça refeições frequentes, incluindo lanches nutritivos entre as principais refeições.",
        " Exercícios: Foque em musculação e atividades de fortalecimento para ganhar massa muscular de forma saudável.",
         " Hidratação e descanso: Beba bastante água e tenha boas noites de sono para otimizar a recuperação e o ganho de peso."
         " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."
    ]

 elif 18.5 <= imc < 24.9:
         classificaçãp = "Peso nomal"
          dicas = [
        "Alimentação: Mantenha uma dieta equilibrada, incluindo proteínas magras, carboidratos integrais e gorduras boas.",
        "Moderação: Evite excessos e mantenha uma alimentação variada e rica em fibras, frutas e vegetais.",
        "Exercícios: Pratique atividades físicas regularmente, como musculação, corrida ou esportes, para manter a composição corporal saudável.",
        "Sono e bem-estar: Priorize boas noites de sono e controle o estresse para manter o metabolismo equilibrado."
         " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."
    ]

elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
    dicas = [
        " Alimentação: Reduza o consumo de açúcares e ultraprocessados. Priorize alimentos naturais e ricos em fibras.",
        " Planejamento alimentar: Prefira refeições balanceadas e evite pular refeições para manter o metabolismo ativo.",
        " Exercícios: Comece com caminhadas diárias e exercícios de resistência para ajudar na perda de gordura e ganho de massa magra.",
        " Estilo de vida: Controle o estresse e pratique técnicas de relaxamento, pois o cortisol alto pode dificultar a perda de peso."
         " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."
    ]

elif 30 <= imc < 34.9:
    classificacao = "Obesidade Grau 1"
    dicas = [
        "Alimentação: Reduza carboidratos refinados e alimentos ricos em gorduras ruins. Inclua proteínas magras e vegetais no prato.",
        "Estratégias alimentares: Experimente técnicas como a reeducação alimentar ou um plano alimentar orientado por um nutricionista.",
        "Exercícios: Pratique atividades de baixo impacto, como natação ou caminhada, para proteger as articulações e melhorar a saúde cardiovascular.",
        "Acompanhamento: Considere buscar orientação médica e nutricional para um plano de emagrecimento saudável e sustentável."
             " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."
    ]

elif 35 <= imc < 39.9:
    classificacao = "Obesidade Grau 2"
    dicas = [
        " Alimentação: Evite frituras e açúcares adicionados. Prefira refeições ricas em fibras, proteínas magras e gorduras saudáveis.",
        "Reeducação alimentar: Um nutricionista pode ajudar a adaptar sua dieta às suas necessidades e objetivos.",
        " Exercícios: Prefira atividades de baixo impacto (como hidroginástica e pilates) para evitar sobrecarga nas articulações.",
        " Saúde mental: O suporte psicológico pode ser essencial para mudanças de hábitos e controle da compulsão alimentar."
         " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."
    ]

else:
    classificacao = "Obesidade Grau 3"
    dicas = [
        " Alimentação: Evite dietas restritivas sem orientação profissional. Priorize alimentos naturais e balanceados.",
        "Monitoramento nutricional: Um plano alimentar específico pode ajudar a alcançar metas realistas e sustentáveis.",
        "Exercícios: Atividades supervisionadas, como musculação adaptada e fisioterapia, podem ajudar na mobilidade e na perda de peso.",
        "Acompanhamento multidisciplinar: O suporte de profissionais da saúde (nutricionista, médico e educador físico) pode ser essencial para o processo de emagrecimento saudável."
        " Importante: Essas dicas servem para você ter um norte de que ações deve tomar para o cuidado com a sua saúde "
        " É indispensával consultar os profissionais de cada área para um acompanhamento como Profissionais de Nutrição, Educação Física, Médicos e Psicólogos."

    ]

# código para exeibir sugestões
print("\nDicas de Saúde:")
for dica in dicas:
    print(dica)
         
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
