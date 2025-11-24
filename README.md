# Sistema Bancário em Python – Versão 2 (DIO)

Este repositório contém a solução da **Versão 2 do Sistema Bancário** proposta na DIO.  
Nesta etapa, o sistema foi totalmente **refatorado com funções** e agora inclui:

- Cadastro de **usuários (clientes)**  
- Criação de **contas correntes** vinculadas aos usuários  
- Operações de **depósito, saque e extrato** seguindo regras específicas de parâmetros

---

## 🏗 Estrutura do Projeto

```text
.
├── sistema_bancario_v2.py   # Código principal do sistema bancário (Versão 2)
└── README.md                # Este arquivo de documentação
```

---

## 🧠 Requisitos do Desafio

### 1. Separar as operações em funções

- `depositar` → recebe argumentos **apenas por posição** (*positional only*).  
  - Sugestão de parâmetros: `saldo, valor, extrato`  
  - Retorno: `saldo, extrato`

- `sacar` → recebe argumentos **apenas por nome** (*keyword only*).  
  - Sugestão de parâmetros: `saldo, valor, extrato, limite, numero_saques, limite_saques`  
  - Retorno: `saldo, extrato, numero_saques`

- `exibir_extrato` → recebe argumentos por **posição e nome** (*positional only + keyword only*).  
  - Parâmetros posicionais: `saldo`  
  - Parâmetros nomeados: `extrato`

### 2. Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista.  
Cada usuário é composto por:

- `nome`
- `data_nascimento`
- `cpf` (somente números)
- `endereco` (string no formato: `logradouro, nro - bairro - cidade/UF`)

Regra importante:

- **Não pode haver dois usuários com o mesmo CPF.**

### 3. Criar conta corrente

O programa deve armazenar as contas em uma lista.  
Cada conta é composta por:

- `agencia` (fixa: `"0001"`)
- `numero_conta` (sequencial, iniciando em 1)
- `usuario` (referência ao dicionário do usuário)

Regras:

- Um usuário pode ter **mais de uma conta**
- Uma conta pertence **somente a um usuário**

---

## ⚙️ Como o código funciona

### Variáveis principais

Dentro da função `main()`:

- `usuarios` → lista de dicionários representando os clientes
- `contas` → lista de dicionários representando as contas correntes
- `saldo` → saldo atual da conta (simples, sem múltiplas contas)
- `extrato` → string com o histórico das movimentações
- `numero_saques` → contador de saques realizados
- `proximo_numero_conta` → inteiro que controla o número da próxima conta criada

Constantes:

```python
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.0
AGENCIA_PADRAO = "0001"
```

---

## 📋 Menu de Operações

Ao executar o programa, o seguinte menu é exibido:

```text
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> 
```

### Opções

- **`d` – Depositar**  
  Solicita um valor e chama a função `depositar`.

- **`s` – Sacar**  
  Solicita um valor e chama a função `sacar`.

- **`e` – Extrato**  
  Chama a função `exibir_extrato`.

- **`nu` – Novo usuário**  
  Chama a função `criar_usuario`, que:
  - pede os dados do cliente,
  - verifica se o CPF já existe,
  - adiciona o usuário à lista `usuarios`.

- **`nc` – Nova conta**  
  Chama a função `criar_conta`, que:
  - solicita o CPF do usuário,
  - valida se o usuário existe,
  - cria a conta com agência fixa `"0001"` e número sequencial,
  - adiciona à lista `contas`.

- **`lc` – Listar contas**  
  Chama a função `listar_contas`, exibindo todas as contas cadastradas.

- **`q` – Sair**  
  Encerra o programa.

---

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3.8+** instalado:

```bash
python --version
# ou
python3 --version
```

2. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

3. Execute o sistema:

```bash
python sistema_bancario_v2.py
# ou
python3 sistema_bancario_v2.py
```

---

## 🧾 Exemplo de Fluxo

1. Criar usuário (`nu`)  
2. Criar conta (`nc`)  
3. Realizar depósitos (`d`)  
4. Realizar saques (`s`)  
5. Visualizar extrato (`e`)  
6. Listar contas (`lc`)

---

## 🚀 Possíveis Melhorias Futuras

- Suporte a múltiplas contas ativas por sessão (escolher qual conta operar)
- Persistência de dados em arquivo (`JSON`, `CSV`) ou banco de dados
- Validações mais robustas de CPF e datas
- Interface gráfica (Tkinter) ou API REST (Flask / FastAPI)

---

Projeto desenvolvido para fins de estudo no bootcamp da **Digital Innovation One (DIO)**.
