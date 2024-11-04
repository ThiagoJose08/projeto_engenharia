class ListaCompras:
    def __init__(self):
        # Inicializa a lista de produtos vazia.
        self.produtos = []

    def adicionar_produto(self, produto):
        # Adiciona um produto à lista de compras.
        self.produtos.append(produto)
        return f"O produto {produto} foi adicionado à lista."

    def remover_produto(self, produto):
        # Remove um produto da lista se ele existir, caso contrário, informa que o produto não está na lista.
        if produto in self.produtos:
            self.produtos.remove(produto)
            return f"O produto {produto} foi removido da lista."
        else:
            return "Este produto não está na lista de compras!"

    def ver_lista(self):
        # Retorna a lista de produtos se houver itens, senão informa que a lista está vazia.
        return self.produtos if self.produtos else "A lista de compras está vazia."

def menu():
    # Exibe o menu de opções para o usuário escolher.
    print("\nMENU:")
    print("1. Adicionar produto à lista")
    print("2. Remover produto da lista")
    print("3. Visualizar lista de compras")
    print("4. Sair")
    return input("Digite o número da opção desejada: ")

if __name__ == "__main__":
    # Instancia a classe ListaCompras.
    lista_compras = ListaCompras()

    # Loop principal que mantém o programa em execução até que a opção de sair seja escolhida.
    while True:
        opcao = menu()
        if opcao == "1":
            # Solicita ao usuário o produto a ser adicionado e chama o método correspondente.
            produto = input("Qual produto você deseja adicionar à lista de compras? ")
            print(lista_compras.adicionar_produto(produto))
        elif opcao == "2":
            # Solicita ao usuário o produto a ser removido e chama o método correspondente.
            produto = input("Qual produto você deseja remover da lista de compras? ")
            print(lista_compras.remover_produto(produto))
        elif opcao == "3":
            # Chama o método para visualizar a lista de compras e exibe os produtos.
            produtos = lista_compras.ver_lista()
            if isinstance(produtos, list):
                print("Produtos na lista de compras:")
                for p in produtos:
                    print(f"- {p}")
            else:
                print(produtos)
        elif opcao == "4":
            # Encerra o programa.
            print("Saindo do programa...")
            break
        else:
            # Exibe uma mensagem de erro se a opção for inválida.
            print("Opção inválida! Tente novamente.")
