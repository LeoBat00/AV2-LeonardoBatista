#/ Trabalho AV2 - Programação Funcional - Questão 2
#/ Nome: Leonardo Mendonça Teixeira Batista 
#/ Matrícula: 2210392
#/ Professor: Samuel Lincoln 

#/ Observação: A função testar código está habilitada por padrão, quando for testado a questão 2 comente o testar_codigo()
import threading
from Q1_LeonardoBatista import *

# Testes Unitarios
def test_cash():
    print("\n TESTE DE CASH================================================\n")
    usuario = usuarios["leo"]
    initial_balance = usuario["saldo_conta_corrente"]
    cash(usuario, 500)
    assert usuario["saldo_conta_corrente"] == initial_balance - 500

def test_credit():
    print("\n TESTE DE CREDITO================================================ \n")
    usuario = usuarios["samuel"]
    initial_credit = usuario["limite_credito"]
    credit(usuario, 1000)
    assert usuario["limite_credito"] == initial_credit - 1000

def test_fund():
    print("\n TESTE DE TRANSFERENCIA================================================\n")
    usuario_origem = usuarios["leo"]
    usuario_destino = usuarios["samuel"]
    initial_balance_origem = usuario_origem["saldo_conta_corrente"]
    initial_balance_destino = usuario_destino["saldo_conta_corrente"]
    fund(usuario_origem, "samuel", 300)
    assert usuario_origem["saldo_conta_corrente"] == initial_balance_origem - 300
    assert usuario_destino["saldo_conta_corrente"] == initial_balance_destino + 300


#Teste de stress
def test_stress_cash():
    def executar_cash():
        usuario = usuarios["leo"]  
        for _ in range(1000):
            cash(usuario, 10)

    threads = []
    for _ in range(10): 
        thread = threading.Thread(target=executar_cash)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        
test_cash()
test_credit()
test_fund()
test_stress_cash()
print("Testes finalizados")
