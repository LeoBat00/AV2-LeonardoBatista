#/ Trabalho AV2 - Programação Funcional - Questão 2
#/ Nome: Leonardo Mendonça Teixeira Batista 
#/ Matrícula: 2210392
#/ Professor: Samuel Lincoln 

#/ Deixei no testar() as opções de inserir, remover e consultarTodas com algumas informações preenchidas para testar o banco de dados
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="videogamedb"
)
cursor = mydb.cursor()

executar_comando_SQL = lambda comandoSQL, cursor: cursor.execute(comandoSQL)
inserir = lambda tabela, atributos, valores, cursor: (executar_comando_SQL(f"INSERT INTO {tabela} ({atributos}) VALUES ({valores})", cursor), mydb.commit())
remover = lambda tabela, condicao, cursor: (executar_comando_SQL(f"DELETE FROM {tabela} WHERE {condicao}", cursor), mydb.commit())
consultar = lambda tabela, condicao, cursor: executar_comando_SQL(f"SELECT * FROM {tabela} WHERE {condicao}", cursor)

def test_inserir():
    print("\nInserção")
    
    inserir("USERS", "id, name, country, id_console", "1, 'Leo', 'Brasil', 1", cursor)
    print("Inserido-Users")
    
    inserir("VIDEOGAMES", "id_console, name, id_company, release_date", "1, 'XBOX360', 1, '2024-04-20'", cursor)
    print("Inserido-Videogames")
    
    inserir("GAMES", "id_game, title, genre, release_date, id_console", "1, 'NinjaGaiden', 'Ação', '2024-04-20', 1", cursor)
    print("Inserido-Games")
    
    inserir("COMPANY", "id_company, name, country", "1, 'NaoSei', 'Estados_Unidos'", cursor)
    print("Inserido-Company\n")

def test_remover():
    print("\nRemoção")
    
    remover("GAMES", "id_console = 1", cursor)
    print("Removido-Games")
    
    remover("USERS", "id = 1", cursor)
    print("Removido-Users")
    
    remover("VIDEOGAMES", "id_console = 1", cursor)
    print("Removido-Videogames")
    
    remover("COMPANY", "id_company = 1", cursor)
    print("Removido-Company\n")


def test_consultar_tabela():
    print("\nConsulta")
    consultar("USERS", "id = 1", cursor)
    res = cursor.fetchall()
    print_result(res)

def test_consultar_todas_tabelas():
    print("\nConsulta em Todas as Tabelas")
    consultar("USERS", "1", cursor)
    print("tabela USERS:")
    print_result(cursor.fetchall())
    
    consultar("VIDEOGAMES", "1", cursor)
    print("tabela VIDEOGAMES:")
    print_result(cursor.fetchall())
    
    consultar("GAMES", "1", cursor)
    print("tabela GAMES:")
    print_result(cursor.fetchall())
    
    consultar("COMPANY", "1", cursor)
    print("tabela COMPANY:")
    print_result(cursor.fetchall())
    print ("\n")

print_result = lambda res: {print(x) for x in res}

def testar():
    print("Escolha o teste: ")
    print("1 - Inserir registro")
    print("2 - Remover registro")
    print("3 - Consultar tabela")
    print("4 - Consultar todas as tabelas")
    
    opcao = input("Digite o teste desejado (1-4): ")
    
    if opcao == "1":
        test_inserir()
    elif opcao == "2":
        test_remover()
    elif opcao == "3":
        test_consultar_tabela()
    elif opcao == "4":
        test_consultar_todas_tabelas()
    else:
        print("???")
        
testar()
