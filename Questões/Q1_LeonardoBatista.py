#/ Trabalho AV2 - Programação Funcional - Questão 1 
#/ Nome: Leonardo Mendonça Teixeira Batista 
#/ Matrícula: 2210392
#/ Professor: Samuel Lincoln 

#/ Observação: A função testar_código() está habilitada por padrão, quando for testado a questão 2 e a questão 5
# comente o testar_codigo()


# "Login" de usuário 
usuarios = {
    "leo": {"nome": "Leo", "limite_credito": 2000, "saldo_conta_corrente": 1000},
    "samuel": {"nome": "Samuel", "limite_credito": 1500, "saldo_conta_corrente": 1000}
}

banco = {
    "usuario1": usuarios["leo"],
    "usuario2": usuarios["samuel"]
}

def logar_usuario(nome_usuario):
    usuario = login_usuario(nome_usuario)
    return usuario if usuario is not None else print("Usuário não encontrado")

# Funções gerais 
print_lambda = lambda *args: print(*args)
login_usuario = lambda nome_usuario: usuarios.get(nome_usuario.lower(), None)
receive_cash = lambda usuario, valor: usuario.update({"saldo_conta_corrente": usuario["saldo_conta_corrente"] - valor})
receive_credit = lambda usuario, valor: usuario.update({"limite_credito": usuario["limite_credito"] - valor})
requestCreditAccount = lambda usuario: print_creditDetails(usuario)
requestPaymentBank = lambda: "Pagamento aprovado pelo Banco"
transacao = lambda tipo: ["Transação completa.", "Transação encerrada.", "Transação cancelada."][tipo]
receive_fund = lambda usuario, conta_destino, valor: (receive_cash(usuario, valor), conta_destino.update({"saldo_conta_corrente": conta_destino["saldo_conta_corrente"] + valor}))
print_depositDetails = lambda usuario, conta_destino: (
    print_lambda(
        "\n== Detalhes da conta que está transferindo ==\nNome: {}\nCredito Atual: ${}\n=============\n".format(
            usuario["nome"], usuario["saldo_conta_corrente"]
        )
    ),
    print_lambda(
        "\n== Detalhes da conta que está recebendo ==\nNome: {}\nCredito Atual: ${}\n=============\n".format(
            conta_destino["nome"], conta_destino["saldo_conta_corrente"]
        )
    )
)
print_receipt = lambda usuario, valorSacado: (
    print_lambda(
        "\n== Recibo ==\nNome: {}\nValor sacado: ${}\nValor atual: ${}\n=============\n".format(
            usuario["nome"], valorSacado, usuario["saldo_conta_corrente"]
        )
    )
)
print_creditDetails = lambda usuario: (
     print_lambda(
        "\n== Detalhes de Credito ==\nNome: {}\nCredito Atual: ${}\n=============\n".format(
            usuario["nome"], usuario["limite_credito"]
        )
    )
)

# Fluxo de transações - Interações com o usuario ===========================================

# Escolha de transação -> Cash
def cash(usuario,valorSacado):    
    if valorSacado > usuario["saldo_conta_corrente"]:
        print_lambda("Saldo insuficiente.")
        return 
    else:
        receive_cash(usuario, valorSacado)
        print_receipt(usuario, valorSacado)
        return print_lambda(transacao(0))


# Escolha de transação -> Credit
def credit(usuario, credit):
    if credit > usuario["limite_credito"]:
        print_lambda("Limite insuficiente.")
        return
    else: 
        requestCreditAccount(usuario)
        print_lambda(requestPaymentBank())
        receive_credit(usuario, credit)
        requestCreditAccount(usuario)
        return print_lambda(transacao(0))


# Escolha de transação -> Fund 
def fund(usuario, conta_destino, valor_transferencia):
    if valor_transferencia > usuario["saldo_conta_corrente"]:
        print_lambda("Saldo insuficiente.")
        return 
    else:
        conta_destino = logar_usuario(conta_destino)
        if conta_destino is None:
            print_lambda("Conta de destino não encontrada.")
            return
        print_depositDetails(usuario, conta_destino)
        receive_fund(usuario, conta_destino, valor_transferencia)
        requestPaymentBank()
        print_depositDetails(usuario, conta_destino)
        return print_lambda(transacao(0))


# Testar codigo 
def testar_codigo():
    nome_usuario = input("Digite seu nome de usuário: ")
    usuario = logar_usuario(nome_usuario)
    
    tipo_transacao = input("Digite o tipo de transação (cash, credit ou fund): ").lower()
    if tipo_transacao not in ['cash', 'credit','fund']:
        print("Tipo de transação inválido. Por favor, digite 'cash', 'credit' ou 'fund'")
        return
    
    valor = float(input("Digite o valor da transação: "))
    
    if tipo_transacao == 'cash':
        print("\nRealizando transação de saque:")
        cash(usuario, valor)
    elif tipo_transacao == 'credit':
        print("\nRealizando transação de crédito:")
        credit(usuario, valor)
    else:
        conta_destino = input("Digite o nome do usuário destino: ")
        print("\nRealizando transação de transferência:")
        fund(usuario, conta_destino, valor)
        
#testar_codigo() # Desabilitar para a questão 02 e 05
