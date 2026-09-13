from mongoConnection import connect

database = connect()

collection = database["vendedores"]

#FUNÇÃO AUXILIARES
def encontrarVendedorUnico(email):
    return collection.find_one({"email": email})

#CREATE
def insertVendedor(nome, email):
    vendedor = encontrarVendedorUnico(email)

    if not vendedor:
        vendedor = { "nome": nome, "email":email}
        collection.insert_one(vendedor)
        print()
        print(f"Vendedor '{vendedor["nome"]}' registrado com sucesso.")
    else:
        print()
        print(f"O e-mail '{email}' já está em uso.")

#READ
def selectVendedor(nome):
    if not len(nome):
        vendedores = list(collection.find().sort("nome"))
    else:
        vendedores = list(collection.find({"nome": nome}))

    print()
    print(f"{len(vendedores)} resultado(s) encontrado(s).")

    for v in vendedores:
                print()
                print("####################")
                print(f"# Nome: {v["nome"]}")
                print(f"# E-mail: {v["email"]}")
                print("####################")

#UPDATE
def updateVendedor(email):
    vendedor = encontrarVendedorUnico(email)

    if vendedor:
        print()
        print("Dados do vendedor:")
        print("------")
        print(f"Nome: {vendedor["nome"]}")
        print(f"E-mail: {vendedor["email"]}")
        print("------")

        print()
        print("-Alteração dos dados do vendedor-")

        alteracoes = {}

        print()
        nomeAlt = input("Mudar nome: ")
        if len(nomeAlt) and nomeAlt != vendedor["nome"]:
            alteracoes["nome"] = nomeAlt

        emailAlt = input("Mudar e-mail: ")
        if len(emailAlt) and emailAlt != vendedor["email"]:
            emailExiste = encontrarVendedorUnico(emailAlt)

            if not emailExiste:
                alteracoes["email"] = emailAlt
            else:
                print()
                print(f"O e-mail '{emailAlt}' já está em uso.")

        try:
            if alteracoes:
                collection.update_one(
                    {"_id": vendedor["_id"]},
                    {"$set": alteracoes}
                )
                print()
                print("Vendedor alterado com sucesso.")
            else:
                print()
                print("Nenhuma alteração realizada.")
        except Exception as erro:
            print()
            print("Não foi possível alterar o vendedor.")
            print(erro)
    else:
        print()
        print("Este e-mail não está vinculado a nenhum vendedor.")

#DELETE
def deleteVendedor(email):
    vendedor = encontrarVendedorUnico(email)

    if vendedor:
        try:
            collection.delete_one({"_id": vendedor["_id"]})
            print()
            print("Vendedor deletado com sucesso.")
        except Exception as erro:
            print()
            print("Não foi possível deletar o vendedor.")
            print(erro)
    else:
        print()
        print("Este e-mail não está vinculado a nenhum vendedor.")