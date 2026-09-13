from colecoes.vendedor import insertVendedor, selectVendedor, updateVendedor, deleteVendedor
from colecoes.produto import insertProduto, selectProduto, updateProduto, deleteProduto
from colecoes.comprador import insertComprador, selectComprador, updateComprador, deleteComprador
from colecoes.compra import insertCompra, selectCompra, updateCompra, deleteCompra

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
        
        if key == '1':
            print()
            nome = input("Digite o nome do vendedor: ")
            email = input("Digite o e-mail do vendedor: ")
            insertVendedor(nome, email)
        elif key == '2':
            print()
            nome = input("Digite o nome do vendedor ('vazio' retornará todos): ")
            selectVendedor(nome)
        elif key == '3':
            print()
            email = input("Digite o e-mail do vendedor que você deseja alterar: ")
            updateVendedor(email)
        elif key == '4':
            print()
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
        
        if key == '1':
            print()
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço do produto: ")
            email = input("Digite o e-mail do vendedor: ")
            insertProduto(nome, preco, email)
        elif key == '2':
            print()
            nome = input("Digite o nome do produto ('vazio' retornará todos): ")
            selectProduto(nome)
        elif key == '3':
            print()
            email = input("Digite o e-mail do vendedor para listar seus produtos: ")
            updateProduto(email)
        elif key == '4':
            print()
            email = input("Digite o e-mail do vendedor para listar seus produtos: ")
            deleteProduto(email)
        elif key == 'voltar':
            break
        else:
            print()
            print("--### Opção inválida! ###--")

def itensComprador():
    while True:
            print()
            print("--####### MENU COMPRADOR ######--")
            print("--## 1 - Cadastrar Comprador ##--")
            print("--## 2 - Pesquisar Comprador ##--")
            print("--## 3 - Atualizar Comprador ##--")
            print("--## 4 - Deletar Comprador   ##--")
            print("--#############################--\n")

            key = input("Digite a opção desejada (para voltar, digite 'voltar'): ")
            
            if key == '1':
                print()
                nome = input("Digite o nome do comprador: ")
                email = input("Digite o e-mail do comprador: ")
                insertComprador(nome, email)
            elif key == '2':
                print()
                nome = input("Digite o nome do comprador ('vazio' retornará todos): ")
                selectComprador(nome)
            elif key == '3':
                print()
                email = input("Digite o e-mail do comprador que você deseja alterar: ")
                updateComprador(email)
            elif key == '4':
                print()
                email = input("Digite o e-mail do comprador que você deseja deletar: ")
                deleteComprador(email)
            elif key == "voltar":
                break
            else:
                print()
                print("--### Opção inválida! ###--")

def itensCompras():
    while True:
        print()
        print("--###### MENU COMPRAS ######--")
        print("--## 1 - Cadastrar Compra ##--")
        print("--## 2 - Pesquisar Compra ##--")
        print("--## 3 - Atualizar Compra ##--")
        print("--## 4 - Deletar Compra   ##--")
        print("--###########################--\n")

        key = input("Digite a opção desejada (para voltar, digite 'voltar'): ")

        if key == '1':
            print()
            email = input("Digite o e-mail do comprador: ")
            insertCompra(email)
        elif key == '2':
            print()
            email = input("Digite o e-mail do comprador: ")
            selectCompra(email)
        elif key == '3':
            print()
            email = input("Digite o e-mail do comprador: ")
            updateCompra(email)
        elif key == '4':
            print()
            email = input("Digite o e-mail do comprador: ")
            deleteCompra(email)
        elif key == "voltar":
            break
        else:
            print()
            print("--### Opção inválida! ###--")
