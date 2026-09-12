from mongoConnection import connect

from vendedor import encontrarVendedorUnico

database = connect()

collection = database["produtos"]

#FUNÇÃO AUXILIAR
def encontrarProdutosVendedor(email):
    vendedor = {"vendedor.email_vendedor": email}
    produtosVendedor = list(collection.find(vendedor))

    if not produtosVendedor:
        print()
        print("Este vendedor não possui produtos.")
        return

    return produtosVendedor

#CREATE
def insertProduto(nome, preco, email):
    vendedor = encontrarVendedorUnico(email)

    if vendedor:
        produto = {
            "nome": nome,
            "preco": preco,
            "vendedor": {
                "vendedor_id": vendedor["_id"],
                "nome_vendedor": vendedor["nome"],
                "email_vendedor": vendedor["email"]
            }
        }
        collection.insert_one(produto)
        print()
        print(f"Produto '{nome}' registrado com sucesso.")
    else:
        print()
        print("Este e-mail não está vinculado a nenhum vendedor.")

#READ
def selectProduto(nome):
    if not len(nome):
        produtos = list(collection.find().sort("nome"))
    else:
        produtos = list(collection.find({"nome": nome}))

    print()
    print(f"{len(produtos)} resultado(s) encontrado(s).")

    for p in produtos:
                print("-----")
                print(f"Nome: {p["nome"]}")
                print(f"Preço: {p["preco"]}")
                print(f"Nome do vendedor: {p["vendedor"]["nome_vendedor"]}")
                print(f"E-mail do vendedor: {p["vendedor"]["email_vendedor"]}")
    print("-----")

#UPDATE
def updateProduto(email):
    produtosVendedor = encontrarProdutosVendedor(email)

    print()
    print(f"{len(produtosVendedor)} resultado(s) encontrado(s).")

    for i, p in enumerate(produtosVendedor):
        print("-----")
        print(f"Produto nº{i}")
        print(f"Nome: {p["nome"]}")
        print(f"Preço: {p["preco"]}")
    print("-----")

    print()
    produtoEscolhido = input("Digite o nº do produto que deseja alterar: ")

    if not produtoEscolhido:
        print()
        print("Nenhum produto foi selecionado.")
        return

    try:
        produtoEscolhido = int(produtoEscolhido)
        if 0 <= produtoEscolhido < len(produtosVendedor):
            produtoAlterado = produtosVendedor[produtoEscolhido]

            print()
            print("-Alteração dos dados do produto-")
            
            alteracoes = {}

            nomeAlt = input("Mudar nome: ")
            if len(nomeAlt) and nomeAlt != produtoAlterado["nome"]:
                alteracoes["nome"] = nomeAlt

            precoAlt = input("Mudar preço: ")
            if len(precoAlt) and precoAlt != produtoAlterado["preco"]:
                alteracoes["preco"] = precoAlt

            try:
                if alteracoes:
                    collection.update_one(
                        {"_id": produtoAlterado["_id"]},
                        {"$set": alteracoes}
                    )
                    print()
                    print("Produto alterado com sucesso.")
                else:
                    print()
                    print("Nenhuma alteração realizada.")
            except Exception as erro:
                print()
                print("Não foi possível alterar o produto.")
                print(erro)
        else:
            print()
            print("Não existe um produto com esse número.")
    except ValueError:
        print()
        print("Digite um número válido.")

#DELETE
def deleteProduto(email):
    produtosVendedor = encontrarProdutosVendedor(email)
    
    print()
    print(f"{len(produtosVendedor)} resultado(s) encontrado(s).")

    for i, p in enumerate(produtosVendedor):
        print("-----")
        print(f"Produto nº{i}")
        print(f"Nome: {p["nome"]}")
        print(f"Preço: {p["preco"]}")
    print("-----")

    print()
    produtoEscolhido = input("Digite o nº do produto que deseja alterar: ")

    if not produtoEscolhido:
        print()
        print("Nenhum produto foi selecionado.")
        return

    try:
        produtoEscolhido = int(produtoEscolhido)
        if 0 <= produtoEscolhido < len(produtosVendedor):
            produtoDeletado = produtosVendedor[produtoEscolhido]

            try:
                collection.delete_one({"_id": produtoDeletado["_id"]})
                print()
                print("Produto deletado com sucesso.")
            except Exception as erro:
                print()
                print("Não foi possível deletar o produto.")
                print(erro)
        else:
            print()
            print("Não existe um produto com esse número.")
    except ValueError:
        print()
        print("Digite um número válido.")
