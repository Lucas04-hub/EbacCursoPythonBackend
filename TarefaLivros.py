def adicionar_livro(biblioteca, titulo, autor, quantidade):
    if not autor:
        return "Nome do(a) autor(a) do livro não pode ser vazio."
    if not titulo:
        return "Título do livro não pode ser vazio."
    if titulo in biblioteca:
        return "Livro já existe."
    biblioteca[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro '{titulo}' do(a) autor(a) '{autor}' adicionado com sucesso!"

def listar_livros(biblioteca):
    if not biblioteca:
        return "Nenhum livro cadastrado."
    resultado = ["Quantidade de livros:"]
    for titulo, info in sorted(biblioteca.items()):
        autor = info.get("autor", "Autor desconhecido")
        quantidade = info.get("quantidade", 0)
        resultado.append(f"- {titulo}, autor: {autor}, quantidade: {quantidade}")
    return "\n".join(resultado)

def remover_livro(biblioteca, titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        return "Livro removido com sucesso."
    else:
        return "Livro não encontrado."

def atualizar_quantidade(biblioteca, titulo, nova_quantidade):
    if titulo in biblioteca:
        biblioteca[titulo]["quantidade"] = nova_quantidade
        return "Quantidade atualizada com sucesso."
    else:
        return "Livro não encontrado."

def registrar_emprestimo(biblioteca, titulo, quantidade, historico):
    if titulo not in biblioteca:
        return "Livro não encontrado."
    if biblioteca[titulo].get("quantidade", 0) < quantidade:
        return "Quantidade indisponível para empréstimo."
    biblioteca[titulo]["quantidade"] -= quantidade
    historico.append((titulo, quantidade))
    return f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!"

def exibir_historico_emprestimos(historico):
    if not historico:
        return "Nenhum empréstimo registrado."
    return "\n".join([f"{titulo} - {quantidade}" for titulo, quantidade in historico])

def exibir_menu():
    return (
        "\nMenu:\n"
        "1 - Adicionar Livro\n"
        "2 - Listar Livros\n"
        "3 - Remover Livros\n"
        "4 - Atualizar Quantidade\n"
        "5 - Registrar Empréstimo\n"
        "6 - Exibir Historico de Empréstimos\n"
        "7 - Sair\n"
    )

def menu():
    biblioteca = {}
    historico = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o nome do(a) autor(a): ").strip()
            try:
                quantidade = int(input("Digite a quantidade de exemplares: ").strip())
            except ValueError:
                print("Quantidade inválida.")
                continue
            resultado = adicionar_livro(biblioteca, titulo, autor, quantidade)
            print(resultado)

        elif opcao == "2":
            print(listar_livros(biblioteca))

        elif opcao == "3":
            titulo = input("Digite o título do livro a remover: ").strip()
            resultado = remover_livro(biblioteca, titulo)
            print(resultado)

        elif opcao == "4":
            titulo = input("Digite o título do livro: ").strip()
            try:
                nova_quantidade = int(input("Digite a nova quantidade: ").strip())
            except ValueError:
                print("Quantidade inválida.")
                continue
            resultado = atualizar_quantidade(biblioteca, titulo, nova_quantidade)
            print(resultado)

        elif opcao == "5":
            titulo = input("Digite o título do livro: ").strip()
            try:
                quantidade = int(input("Digite a quantidade a emprestar: ").strip())
            except ValueError:
                print("Quantidade inválida.")
                continue
            resultado = registrar_emprestimo(biblioteca, titulo, quantidade, historico)
            print(resultado)

        elif opcao == "6":
            print(exibir_historico_emprestimos(historico))

        elif opcao == "7":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()