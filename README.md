## *Projeto desenvolvido e testado no VS Code (Linux)*

### Especificações
- python 3.12
- mongoDB

### Manual do usuário
1. Criar uma conta gratuita em https://www.mongodb.com/
2. Criar um cluster para a base de dados
3. Adicionar as collections: "compradores", "compras", "produtos" e "vendedores"
4. Obter a string connection
5. Criar um arquivo a partir do modelo de conexão com: `cp mongoConnectionModel.py mongoConnection.py`
5. Substituir "**string connection**" e "**nome da sua collection**" no arquivo *mongoConnection.py* pelas suas credenciais
6. Criar um ambiente virtual `python3 -m venv .venv`
7. Ativar o ambiente virtual (pesquise: "ativar ambiente virtual <*seu sistema operacional*>")
8. Instalar a biblioteca *pymongo* `python3 install pymongo`
9. Executar o arquivo *menu.py* `cd src`, `python3 menu.py`