produtos = {}

def adicionar_produtos(produtos):
    # Pedir nome
    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("Nome do produto não pode ser vazio.")
        return
    if nome in produtos:
        print("Esse produto já existe.")
        return
    # Pedir quantidade
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("A quantidade deve ser positiva.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro para quantidade.")
    # Pedir preço
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("O preço deve ser positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um valor válido para o preço.")
    produtos[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de produtos:")
        for nome, status in sorted(produtos.items(), key=lambda item: item[0]):
            print(f"- {nome}: {status}")

def remover_produto(produtos):
    nome = input("Digite o nome do produto que queira remover: ").strip()
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Erro: Produto '{nome}' não encontrado.")

def atualizar_quantidade_de_produto(produtos):
    nome = input("Digite o nome do produto que queira atualizar a quantidade: ").strip()
    if nome in produtos:
        try:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            produtos[nome] = nova_quantidade
            print(f"Quantidade de '{nome}' foi alterada para {nova_quantidade}!")
        except ValueError:
            print("Erro: Digite um valor numérico válido para a quantidade.")
    else:
        print("Erro: Produto não encontrado.")

def exibir_menu():
    return (
        "\nMenu:\n"
        "1 - Adicionar produto\n"
        "2 - Lista produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade de produto\n"
        "5 - Sair\n"
    )

def menu():
    produtos = {}
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ").strip()
            adicionar_produtos(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            nome = input("Digite o nome do produto que deseja remover: ").strip()
            remover_produto(produtos)
        elif opcao == "4":
            nome = input("Digite o nome do produto que : ").strip()
            atualizar_quantidade_de_produto(produtos)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()