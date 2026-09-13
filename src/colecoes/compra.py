from mongoConnection import connect

from colecoes.comprador import encontrarCompradorUnico
from colecoes.produto import listarProdutos

database = connect()

collection = database["compras"]

# FUNÇÃO AUXILIAR
def encontrarComprasComprador(email):
    return list(collection.find({"email_comprador": email}))

#CREATE
def insertCompra(email):
    comprador = encontrarCompradorUnico(email)

    if comprador:
        itens = []

        print()
        adicionarItem = input("Deseja adicionar um novo item? (S/N): ")

        while adicionarItem != 'N':
            if adicionarItem not in ['N', 'S']:
                print()
                print("--### Opção inválida! ###--")

                print()
                adicionarItem = input("Deseja adicionar um novo item? (S/N): ")
            else:
                print()
                produtos = listarProdutos()

                print()
                escolha = input("Escolha o nº do produto para adicioná-lo ao seu carrinho: ")

                if not escolha:
                    print()
                    print("Nenhum produto foi selecionado.")
                    return

                if not escolha.isdigit():
                    print()
                    print("Digite um número válido.")
                    continue

                produtoEscolhido = int(escolha)

                if 0 <= produtoEscolhido < len(produtos):
                    if produtos[produtoEscolhido] in itens:
                        print()
                        print("Esse produto já está em seu carrinho.")
                    else:
                        itens.append(produtos[produtoEscolhido])
                        print()
                        print("Produto adicionado ao carrinho.")
                else:
                    print()
                    print("Número de produto inválido.")

            print()
            adicionarItem = input("Deseja adicionar um novo favorito? (S/N): ")

        try:
            if itens:
                while True:
                    print()
                    pagamento = input("Qual a forma de pagamento (PIX/CARTÃO)?")

                    if pagamento in ['PIX', "CARTÃO"]:
                        break
                    else:
                        print()
                        print("--## Opção inválida! ##--")

                compra = {
                    "id_comprador": comprador["_id"],
                    "nome_comprador": comprador["nome"],
                    "email_comprador": comprador["email"],
                    "pagamento": pagamento,
                    "itens": itens
                }
                collection.insert_one(compra)
                print()
                print("Compra registrada com sucesso.")
            else:
                print()
                print("Nenhuma produto selecionado para compra.")
        except Exception as erro:
            print()
            print("Não foi possível registrar a compra.")
            print(erro)      
    else:
        print()
        print("Este e-mail não está vinculado a nenhum comprador.")

#READ
def selectCompra(email):
    comprador = encontrarCompradorUnico(email)
    
    if comprador:
        comprasComprador = list(collection.find({"email_comprador": comprador["email"]}))
    else:
        print()
        print("Este e-mail não está vinculado a nenhum comprador.")

    if comprasComprador:
        print()
        print(f"{len(comprasComprador)} resultado(s) encontrado(s).")

        for c in comprasComprador:
            print()
            print(f"Compra {comprasComprador.index(c)}: ")
            print("-----")
            print(f"Forma de pagamento: {c["pagamento"]}")
            for i in c["itens"]:
                print("####################")
                print(f"# Produto: {i["nome"]}")
                print(f"# Preço: {i["preco"]}")
                print("####################")
    else:
        print()
        print("Esse comprador não possui uma compra registrada.")

#UPDATE
def updateCompra(email):
    comprasComprador = encontrarComprasComprador(email)
    
    if comprasComprador:
        print()
        print(f"{len(comprasComprador)} resultado(s) encontrado(s).")

        for c in comprasComprador:
            print()
            print(f"Compra nº{comprasComprador.index(c)}: ")
            print("-----")
            print(f"Forma de pagamento: {c["pagamento"]}")
            for i in c["itens"]:
                print("####################")
                print(f"# Produto: {i["nome"]}")
                print(f"# Preço: {i["preco"]}")
                print("####################")

        print()
        compraEscolhida = input("Digite o nº da compra que deseja alterar: ")

        if not compraEscolhida:
            print()
            print("Nenhuma compra foi selecionada.")
            return

        try:
            compraEscolhida = int(compraEscolhida)
            if 0 <= compraEscolhida < len(comprasComprador):
                compraAlterada = comprasComprador[compraEscolhida]

                print()
                print("-Alteração da forma de pagamento-")
                
                alteracoes = {}

                while True:
                    print()
                    pagamentoAlt = input("Mudar pagamento (PIX/CARTÃO): ")

                    if pagamentoAlt in ['PIX', "CARTÃO"]:
                        break
                    else:
                        print()
                        print("--## Opção inválida! ##--")
                
                if len(pagamentoAlt) and pagamentoAlt != compraAlterada["pagamento"]:
                    alteracoes["pagamento"] = pagamentoAlt

                try:
                    if alteracoes:
                        collection.update_one(
                            {"_id": compraAlterada["_id"]},
                            {"$set": alteracoes}
                        )
                        print()
                        print("Compra alterada com sucesso.")
                    else:
                        print()
                        print("Nenhuma alteração realizada.")
                except Exception as erro:
                    print()
                    print("Não foi possível alterar a compra.")
                    print(erro)
            else:
                print()
                print("Não existe uma compra com esse número.")
        except ValueError:
            print()
            print("Digite um número válido.")
    else:
        print()
        print("Esse comprador não possui uma compra registrada.")

#DELETE
def deleteCompra(email):
    comprasComprador = encontrarComprasComprador(email)

    if comprasComprador:
        print()
        print(f"{len(comprasComprador)} resultado(s) encontrado(s).")

        for c in comprasComprador:
            print()
            print(f"Compra {comprasComprador.index(c)}: ")
            for i in c["itens"]:
                print("####################")
                print(f"# Produto: {i["nome"]}")
                print(f"# Preço: {i["preco"]}")
                print("####################")

        print()
        compraEscolhida = input("Digite o nº da compra que deseja deletar: ")

        if not compraEscolhida:
            print()
            print("Nenhuma compra foi selecionada.")
            return

        try:
            compraEscolhida = int(compraEscolhida)
            if 0 <= compraEscolhida < len(comprasComprador):
                compraDeletada = comprasComprador[compraEscolhida]

                try:
                    collection.delete_one({"_id": compraDeletada["_id"]})
                    print()
                    print("Compra deletada com sucesso.")
                except Exception as erro:
                    print()
                    print("Não foi possível deletar a cmopra.")
                    print(erro)
            else:
                print()
                print("Não existe uma compra com esse número.")
        except ValueError:
            print()
            print("Digite um número válido.")
    else:
        print()
        print("Esse comprador não possui uma compra registrada.")