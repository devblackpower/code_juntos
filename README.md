Processamento de Dados de Vendas com SQLite

Este script Python demonstra como carregar dados de um arquivo CSV em um banco de dados SQLite e realizar consultas básicas.


Funcionalidade:

    Carrega dados CSV: Lê dados de um arquivo CSV chamado sales.csv.
    Cria banco de dados SQLite: Cria um banco de dados SQLite em memória.
    Insere dados na tabela: Escreve os dados CSV em uma tabela chamada sales.
    Consulta dados: Executa uma consulta SELECT * FROM sales para verificar a inserção de dados.
    Exibe resultados: Imprime os dados recuperados.

Pré-requisitos:

    Python 3.x
    Biblioteca Pandas (pip install pandas)


Uso:

    Certifique-se de que o arquivo sales.csv exista no mesmo diretório que o script.
    Execute o script usando python script.py.
    Os dados recuperados serão impressos no console.

Observação:

    Este script cria um banco de dados em memória, portanto, os dados não são persistidos após a finalização do script.
    Para armazenar os dados permanentemente, modifique a string de conexão na função sqlite3.connect() para especificar um caminho de arquivo.