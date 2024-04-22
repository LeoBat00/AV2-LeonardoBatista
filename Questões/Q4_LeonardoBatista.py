#/ Trabalho AV2 - Programação Funcional - Questão 2
#/ Nome: Leonardo Mendonça Teixeira Batista 
#/ Matrícula: 2210392
#/ Professor: Samuel Lincoln 

#/ Nesse exemplo, para adicionar o Inner Join entre as 3 tabelas tive que fazer alterações em cada tabela, adicionando o id_company em GAMES e VIDEOGAMES, 
# e o id_console em COMPANY. Então não será possivel utilizar no banco de dados anterior pois não tem esses campos.

def gen_inner_join(t1, t2, t3):
    commonattrs_t1_t2 = [e for e in t1[1].keys() if e in t2[1].keys()]
    commonattrs_t1_t3 = [e for e in t1[1].keys() if e in t3[1].keys()]
    commonattrs_t2_t3 = [e for e in t2[1].keys() if e in t3[1].keys()]
    
    code = t1[0] + " " + t1[2] + " INNER JOIN " + t2[0] + " " + t2[2] + " ON "
    for i in range(len(commonattrs_t1_t2)):
        code += " AND " if i > 0 else ""
        code += t1[2] + "." + commonattrs_t1_t2[i] + " = " + t2[2] + "." + commonattrs_t1_t2[i]
        
    code += " INNER JOIN " + t3[0] + " " + t3[2] + " ON "
    for i in range(len(commonattrs_t1_t3)):
        code += " AND " if i > 0 else ""
        code += t1[2] + "." + commonattrs_t1_t3[i] + " = " + t3[2] + "." + commonattrs_t1_t3[i]
        
    for i in range(len(commonattrs_t2_t3)):
        code += " AND "
        code += t2[2] + "." + commonattrs_t2_t3[i] + " = " + t3[2] + "." + commonattrs_t2_t3[i]
    
    return code

gen_select_query = lambda t1, t2, t3: f"SELECT {t1[2]}.id_game, {t1[2]}.title, {t1[2]}.genre, {t1[2]}.release_date, {t3[2]}.name AS company_name, {t3[2]}.country FROM {gen_inner_join(t1, t2, t3)}"


GAMES = lambda: ("GAMES", {"id_game": "int", "id_console": "int", "title": "varchar(100)", "genre": "varchar(100)", "release_date": "date", "id_company": "int"}, "games")
VIDEOGAMES = lambda: ("VIDEOGAMES", {"id_console": "int", "name": "varchar(100)", "id_company": "int", "release_date": "date"}, "videogames")
COMPANY = lambda: ("COMPANY", {"id_company": "int", "name": "varchar(100)", "country": "varchar(100)"}, "company")

print_lambda = lambda lambda_func: print("\n" + lambda_func() + "\n")
print_lambda(lambda: gen_select_query(GAMES(), VIDEOGAMES(), COMPANY()))
