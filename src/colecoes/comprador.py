from mongoConnection import connect
from colecoes.produto import listarProdutos

database = connect()

collection = database["compradores"]

#FUNÇÃO AUXILIARES
def encontrarCompradorUnico(email):
    return collection.find_one({"email": email})

#CREATE
def insertComprador(nome, email):
    comprador = encontrarCompradorUnico(email)
    
    if not comprador:
        comprador = { "nome": nome, "email": email, "favoritos": []}
        collection.insert_one(comprador)
        print()
        print(f"Comprador '{comprador["nome"]}' registrado com sucesso.")
    else:
        print()
        print(f"O e-mail '{email}' já está em uso.")

#READ
def selectComprador(nome):
    if not len(nome):
        compradores = list(collection.find().sort("nome"))
    else:
        compradores = list(collection.find({"nome": nome}))

    print()
    print(f"{len(compradores)} resultado(s) encontrado(s).")

    for c in compradores:
                print()
                print("####################")
                print(f"# Nome: {c["nome"]}")
                print(f"# E-mail: {c["email"]}")
                print("# Favoritos:")
                for f in c["favoritos"]:
                    print("# -----")
                    print(f"# Produto nº{c["favoritos"].index(f)}")
                    print(f"# Nome produto: {f["nome"]}")
                    print(f"# Preço produto: {f["preco"]}")
                print("####################")

#UPDATE
def updateComprador(email):
    comprador = encontrarCompradorUnico(email)

    if comprador:
        print()
        print("Dados do comprador:")
        print("------")
        print(f"Nome: {comprador["nome"]}")
        print(f"E-mail: {comprador["email"]}")
        print("Favoritos:")
        for f in comprador["favoritos"]:
            print("-----")
            print(f"Produto nº{comprador["favoritos"].index(f)}")
            print(f"Nome produto: {f["nome"]}")
            print(f"Preço produto: {f["preco"]}")
        print("------")

        print()
        print("-Alteração dos dados do comprador-")

        alteracoes = {}

        print()
        nomeAlt = input("Mudar nome: ")
        if len(nomeAlt) and nomeAlt != comprador["nome"]:
            alteracoes["nome"] = nomeAlt

        emailAlt = input("Mudar e-mail: ")
        if len(emailAlt) and emailAlt != comprador["email"]:
            emailExiste = encontrarCompradorUnico(emailAlt)

            if not emailExiste:
                alteracoes["email"] = emailAlt
            else:
                print()
                print(f"O e-mail '{emailAlt}' já está em uso.")

        favoritosAlt = []
        favoritosAlt = comprador["favoritos"].copy()
        adicionarFavorito = input("Deseja adicionar um novo favorito? (S/N): ")

        while adicionarFavorito != 'N':
            if adicionarFavorito not in ['N', 'S']:
                print()
                print("--### Opção inválida! ###--")

                print()
                adicionarFavorito = input("Deseja adicionar um novo favorito? (S/N): ")
            else:
                print()
                produtos = listarProdutos()

                print()
                escolha = input("Escolha o nº do produto para adicioná-lo a seus favoritos: ")

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
                    if produtos[produtoEscolhido] in comprador["favoritos"]:
                        print()
                        print("Esse produto já está em seus favoritos.")
                    elif produtos[produtoEscolhido] in favoritosAlt:
                        print()
                        print("Esse produto já está em seus favoritos.")
                    else:
                        favoritosAlt.append(produtos[produtoEscolhido])
                        print()
                        print("Produto adicionado aos favoritos.")
                else:
                    print()
                    print("Número de produto inválido.")

            print()
            adicionarFavorito = input("Deseja adicionar um novo favorito? (S/N): ")

        if favoritosAlt != comprador["favoritos"]:
            alteracoes["favoritos"] = favoritosAlt

        try:
            if alteracoes:
                collection.update_one(
                    {"_id": comprador["_id"]},
                    {"$set": alteracoes}
                )
                print()
                print("Comprador alterado com sucesso.")
            else:
                print()
                print("Nenhuma alteração realizada.")
        except Exception as erro:
            print()
            print("Não foi possível alterar o comprador.")
            print(erro)      
    else:
        print()
        print("Este e-mail não está vinculado a nenhum vendedor.")

#DELETE
def deleteComprador(email):
    comprador = encontrarCompradorUnico(email)

    if comprador:
        try:
            collection.delete_one({"_id": comprador["_id"]})
            print()
            print("Comprador deletado com sucesso.")
        except Exception as erro:
            print()
            print("Não foi possível deletar o comprador.")
            print(erro)
    else:
        print()
        print("Este e-mail não está vinculado a nenhum comprador.")