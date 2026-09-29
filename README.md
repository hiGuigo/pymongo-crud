## *Projeto desenvolvido e testado no VS Code (Linux)*

### Especificações
- python 3.12
- mongoDB

### Manual do usuário
1. Criar uma conta gratuita em https://www.mongodb.com
2. Criar um **cluster** e uma **base de dados**
3. Adicionar as collections: `compradores`, `compras`, `produtos` e `vendedores`
4. Obter a sua **connection string**
5. Declarar as variáveis de ambiente no arquivo *".env_template"*
6. Criar o ambiente virtual: `python3 -m venv .venv`
7. Ativar o ambiente virtual (pesquise: "ativar ambiente virtual <*seu sistema operacional*>")
8. Instalar as bibliotecas necessárias: `pip install -r requirements.txt`
9. Executar o arquivo *menu.py*: `cd src` -> `python3 menu.py`