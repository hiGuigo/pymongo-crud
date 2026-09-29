from itensMenu import itensVendedor, itensProduto, itensComprador, itensCompras
import signal

def handler(signum, frame):
    print(" - Comando inválido")
    return

signal.signal(signal.SIGINT, handler)

while True:
    print()
    print("--###### MENU CRUD ########--")
    print("--## 1 - CRUD Vendedor   ##--")
    print("--## 2 - CRUD Produto    ##--")
    print("--## 3 - CRUD Comprador  ##--")
    print("--## 4 - CRUD Compras    ##--")
    print("--#########################--\n")
    
    menuKey = input("Digite a opção desejada (para sair, digite 'sair'): ").strip()

    if menuKey == '1':
        itensVendedor()
    elif menuKey == '2':
        itensProduto()
    elif menuKey == '3':
        itensComprador()
    elif menuKey == '4':
        itensCompras()
    elif menuKey == 'sair':
        break
    else:
        print()
        print("--### Opção inválida! ###--")
