from itensMenu import itensVendedor, itensProduto

while True:
    print()
    print("--##### MENU DAORA ######--")
    print("--## 1 - CRUD Vendedor ##--")
    print("--## 2 - CRUD Produto  ##--")
    print("--#######################--\n")
    
    menuKey = input("Digite a opção desejada (para sair, digite 'eu não quero mais'): ")

    if menuKey == '1':
        itensVendedor()
    elif menuKey == '2':
        itensProduto()
    elif menuKey == 'eu não quero mais':
        break
    else:
        print()
        print("--### Opção inválida! ###--")
