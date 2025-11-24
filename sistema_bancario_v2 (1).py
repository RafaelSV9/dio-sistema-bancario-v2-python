# sistema_bancario_v2.py
# Versão 2 do Sistema Bancário da DIO
# - Operações refatoradas em funções
# - Cadastro de usuários
# - Criação de contas correntes
# - Armazenamento em listas (sem persistência em arquivo/banco)

MENU = """\
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.0
AGENCIA_PADRAO = "0001"


def depositar(saldo, valor, extrato, /):
    """Função de depósito (argumentos apenas posicionais).

    Parâmetros:
        saldo (float): saldo atual da conta
        valor (float): valor a ser depositado (deve ser positivo)
        extrato (str): texto contendo o histórico de movimentações

    Retorno:
        tuple[float, str]: novo saldo e extrato atualizado
    """
    if valor <= 0:
        print("Operação falhou! O valor do depósito deve ser positivo.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função de saque (argumentos apenas nomeados / keyword-only).

    Parâmetros (apenas por nome):
        saldo (float): saldo atual da conta
        valor (float): valor solicitado para saque
        extrato (str): histórico de movimentações
        limite (float): limite máximo por saque
        numero_saques (int): quantidade de saques já realizados no dia
        limite_saques (int): quantidade máxima de saques permitida

    Retorno:
        tuple[float, str, int]: novo saldo, extrato atualizado
            e número de saques (incrementado em caso de sucesso).
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if valor <= 0:
        print("Operação falhou! O valor do saque deve ser positivo.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(
            f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}."
        )
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato (saldo posicional, extrato nomeado)."""
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato, end="")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================\n")


def filtrar_usuario(cpf, usuarios, /):
    """Retorna o usuário com o CPF informado ou None, caso não exista."""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    """Cria um novo usuário (cliente do banco).

    Usuário é composto por:
        - nome
        - data de nascimento
        - cpf (apenas números, sem ponto/traço)
        - endereço (logradouro, nro - bairro - cidade/UF)
    """
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/UF): "
    ).strip()

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    """Cria uma nova conta corrente vinculada a um usuário.

    Conta é composta por:
        - agência
        - número da conta (sequencial, iniciando em 1)
        - usuário (dict)
    """
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Fluxo de criação de conta encerrado.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
    }

    print("Conta criada com sucesso!")
    return conta


def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        linha = f"""Agência:	{conta["agencia"]}
C/C:		{conta["numero_conta"]}
Titular:	{conta["usuario"]["nome"]}
CPF:		{conta["usuario"]["cpf"]}
"""
        print("=" * 40)
        print(linha, end="")
    print("=" * 40)


def main():
    saldo = 0.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    proximo_numero_conta = 1

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
            except ValueError:
                print("Valor inválido.")
                continue

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
            except ValueError:
                print("Valor inválido.")
                continue

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA_PADRAO, proximo_numero_conta, usuarios)
            if conta:
                contas.append(conta)
                proximo_numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário! Até logo.")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")


if __name__ == "__main__":
    main()
