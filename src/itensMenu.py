from vendedor import insertVendedor, selectVendedor, updateVendedor, deleteVendedor
from produto import insertProduto, selectProduto, updateProduto

def itensVendedor():
    while True:
        print()
        print("--###### MENU VENDEDOR #######--")
        print("--## 1 - Cadastrar Vendedor ##--")
        print("--## 2 - Pesquisar Vendedor ##--")
        print("--## 3 - Atualizar Vendedor ##--")
        print("--## 4 - Deletar Vendedor   ##--")
        print("--############################--\n")

        key = input("Digite a opção desejada (para voltar, digite 'voltar'): ")
        print()
        
        if key == '1':
            nome = input("Digite o nome do vendedor: ")
            email = input("Digite o e-mail do vendedor: ")
            insertVendedor(nome, email)
        elif key == '2':
            nome = input("Digite o nome do vendedor ('vazio' retornará todos): ")
            selectVendedor(nome)
        elif key == '3':
            email = input("Digite o e-mail do vendedor que você deseja alterar: ")
            updateVendedor(email)
        elif key == '4':
            email = input("Digite o e-mail do vendedor que você deseja deletar: ")
            deleteVendedor(email)
        elif key == "voltar":
            break
        else:
            print()
            print("--### Opção inválida! ###--")

def itensProduto():
    while True:
        print()
        print("--####### MENU PRODUTO #######--")
        print("--## 1 - Cadastrar Produto  ##--")
        print("--## 2 - Pesquisar Produto  ##--")
        print("--## 3 - Atualizar Produto  ##--")
        print("--## 4 - Deletar Produto    ##--")
        print("--############################--\n")

        key = input("Digite a opção desejada (para voltar, digite 'voltar'): ")
        print()
        
        if key == '1':
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço do produto: ")
            email = input("Digite o e-mail do vendedor: ")
            insertProduto(nome, preco, email)
        elif key == '2':
            nome = input("Digite o nome do produto ('vazio' retornará todos): ")
            selectProduto(nome)
        elif key == '3':
            email = input("Digite o e-mail do vendedor para listar seus produtos: ")
            updateProduto(email)
        elif key == 'voltar':
            break