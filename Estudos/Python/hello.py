destinos = ["Gramado", "São Jorge", "São Paulo", "Rio de Janeiro"]
idade = 18
temPassagem = False
temAcompanhante = False
question = None
red_text = "\033[91m"
green_text = "\033[92m"
reset_text = "\033[0m"

if idade >= 18 or temAcompanhante == True:
    while question not in destinos:
        question = input(
            f"Parece que você pode viajar, para onde vai?\n{destinos}:\n"
        ).capitalize()

        if question in destinos:
            print(f"\nVocê selecionou {question}.")
            destinos.remove(question)
            temPassagem = True
            break
        else:
            print(red_text + "\nEsse destino não existe, escolha outro!" + reset_text)

    if temPassagem == True or idade >= 18:
        print(green_text + "\nBoa Viagem" + reset_text)
        print(f"\nDestinos ainda disponíveis: \n{destinos}")
