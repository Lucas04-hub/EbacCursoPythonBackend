def adicionar_pokemon(pokedex, nome, tipo, nivel):
    if nome in pokedex:
        return "Pokémon já cadastrado!"
    pokedex[nome] = {"tipo": tipo, "nivel": nivel}
    return "Pokémon adicionado com sucesso!"

def listar_pokemon(pokedex):
    if not pokedex:
        return "Nenhum Pokémon cadastrado!"
    resultado = []
    for nome, info in sorted(pokedex.items()):
        resultado.append(f"{nome} {info['tipo']} {info['nivel']}")
    return "\n".join(resultado)

def remover_pokemon(pokedex, nome):
    validacao = nome in pokedex
    if not validacao:
        return "Pokémon não encontrado!"
    del pokedex[nome]
    return "Pokémon removido com sucesso!"

def atualizar_nivel_pokemon(pokedex, nome, nivel):
    validacao = nome in pokedex
    if not validacao:
        return "Pokémon não encontrado!"
    pokedex[nome]["nivel"] = nivel
    return "Nível do Pokémon atualizado com sucesso!"

def registrar_captura(historico, nome, tipo, nivel):
    historico.append(f"{nome} {tipo} {nivel}")
    return "Captura registrada com sucesso!"

def exibir_historico_capturas(historico):
    if not historico:
        return "Nenhuma captura registrada!"
    return "\n".join([entrada for entrada in historico])

def exibir_menu():
    return (
        "\nMenu:\n"
        "1 - Adicionar Pokemon\n"
        "2 - Listar Pokémon\n"
        "3 - Remover Pokemon\n"
        "4 - Atualizar Nivel do Pokemon\n"
        "5 - Registrar Captura\n"
        "6 - Exibir Historico de Capturas\n"
        "7 - Sair\n"
    )

def menu():
    pokedex = {}
    historico = []
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Nome do Pokemon: ")
            tipo = input("Tipo do Pokemon: ")
            nivel = input("Nível do Pokemon: ")
            try:
                nivel_convertido = int(nivel)
                print(adicionar_pokemon(pokedex, nome, tipo, nivel_convertido))
            except ValueError:
                print("Nível inválido!")
        elif opcao == '2':
            print(listar_pokemon(pokedex))
        elif opcao == '3':
            nome = input("Nome do Pokemon a remover: ")
            print(remover_pokemon(pokedex, nome))
        elif opcao == '4':
            nome = input("Nome do Pokemon: ")
            nivel = input("Novo nível: ")
            try:
                nivel_convertido = int(nivel)
                print(atualizar_nivel_pokemon(pokedex, nome, nivel_convertido))
            except ValueError:
                print("Nível inválido!")
        elif opcao == '5':
            nome = input("Nome do Pokemon: ")
            tipo = input("Tipo do Pokemon: ")
            nivel = input("Nível do Pokemon: ")
            try:
                nivel_convertido = int(nivel)
                adicionar_msg = adicionar_pokemon(pokedex, nome, tipo, nivel_convertido)
                print(registrar_captura(historico, nome, tipo, nivel_convertido))
                if adicionar_msg == "Pokémon adicionado com sucesso!":
                    print(adicionar_msg)
            except ValueError:
                print("Nível inválido!")
        elif opcao == '6':
            print(exibir_historico_capturas(historico))
        elif opcao == '7':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()