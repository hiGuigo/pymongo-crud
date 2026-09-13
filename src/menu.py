from itensMenu import itensVendedor, itensProduto, itensComprador, itensCompras

while True:
    print()
    print("--###### MENU DAORA #######--")
    print("--## 1 - CRUD Vendedor   ##--")
    print("--## 2 - CRUD Produto    ##--")
    print("--## 3 - CRUD Comprador  ##--")
    print("--## 4 - CRUD Compras    ##--")
    print("--#########################--\n")
    
    menuKey = input("Digite a opção desejada (para sair, digite 'eu não quero mais'): ")

    if menuKey == '1':
        itensVendedor()
    elif menuKey == '2':
        itensProduto()
    elif menuKey == '3':
        itensComprador()
    elif menuKey == '4':
        itensCompras()
    elif menuKey == 'eu não quero mais':
        break
    else:
        print()
        print("--### Opção inválida! ###--")
