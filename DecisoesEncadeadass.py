de_nome = input("Digite o nome: ")
idade = int(input("Digite a idade "))
doenca_infectocontagiosa = input("Suspeita de doenca infectocontagiosa? ").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Paciente deve aguardar na sala Amarela ")
    elif doenca_infectocontagiosa == "NAO":
        print("Paciente deve aguardar na sala Branca")
    else:
        print("Responda se há suspeita de doenca infectocontagiosa ")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Paciente deve aguardar na sala Amarela")
    elif doenca_infectocontagiosa == "NAO":
        print("Paciente deve aguardar na sala Branca ")
    else:
        print("Responda se há suspeita de doenca infectocontagiosa ")
