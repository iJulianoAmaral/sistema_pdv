# Sistema de PDV

Bem-vindo ao **Sistema PDV**, um programa em Python que simula as funcionalidades básicas de um caixa operador. Este sistema foi projetado para facilitar o controle de vendas, registrar compras, e emitir uma nota fiscal detalhada.

## Funcionalidades Principais

1. **Registro de CPF na Nota:**
   - O cliente pode optar por inserir o CPF para registro na nota fiscal.

2. **Leitura de Produtos:**
   - O sistema lê códigos de barras fictícios de produtos e calcula o valor total da compra.

3. **Operações Especiais:**
   - Multiplicação de itens (ex.: registrar 12 unidades de leite de uma vez).
   - Exclusão de itens (necessário autenticar-se com a senha do sistema).

4. **Finalização da Compra:**
   - Antes de finalizar, o sistema valida se o cliente deseja encerrar a compra ou adicionar mais itens.

5. **Nota Fiscal Detalhada:**
   - Exibe uma tabela com os produtos comprados, seus valores individuais, e o total da compra.

## Tabela de Operações

| Letra | Função                                  |
|-------|-----------------------------------------|
| X     | Multiplica a quantidade de um produto   |
| D     | Deleta um item (requer senha do sistema)|
| F     | Finaliza a compra                       |

## Exemplo de Execução

### Passo 1: Inicialização
O programa inicia perguntando se o cliente deseja inserir o CPF na nota fiscal:

```
Deseja adicionar o CPF na nota fiscal? (S/N): S
Digite o CPF (apenas números): 12345678901
CPF adicionado com sucesso!
```

### Passo 2: Registro de Produtos
A seguir, o sistema solicita que você insira os códigos de barras dos produtos ou utilize os comandos disponíveis:

```
Comece a passar os produtos ou use os comandos abaixo:

| Letra | Função                                  |
|-------|-----------------------------------------|
| X     | Multiplica a quantidade de um produto   |
| D     | Deleta um item (requer senha do sistema)|
| F     | Finaliza a compra                       |

Digite o comando ou código de barras: 101
Produto adicionado: Leite - R$ 5.0

Digite o comando ou código de barras: X
Digite a quantidade: 12
Digite o código de barras do produto: 101
Produto adicionado: Leite - R$ 5.0 (x12)

Digite o comando ou código de barras: 103
Produto adicionado: Dúzia de Ovos - R$ 10.0
```

### Passo 3: Exclusão de Itens
Se necessário, você pode excluir um item digitando o comando `D` e a senha do sistema:

```
Digite o comando ou código de barras: D
Digite a senha do sistema: ********
Senha correta! Digite o código de barras do produto a ser removido: 103
Produto removido: Dúzia de Ovos
```

### Passo 4: Finalização
Ao finalizar a compra, o sistema pergunta se deseja encerrar ou adicionar mais itens:

```
Digite o comando ou código de barras: F
Deseja realmente finalizar a compra? (S/N): S
Compra finalizada com sucesso!
```

### Passo 5: Nota Fiscal
A nota fiscal é exibida com os itens comprados e o total:

```
Nota Fiscal
---------------------------------------
Produto             Quantidade    Valor
Leite               12            R$ 60.0
---------------------------------------
Total da compra: R$ 60.0
CPF na nota: 12345678901
```

## Como Executar o Sistema

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Torne o script executável (se necessário):
   ```bash
   chmod +x executar_caixa.sh
   ```

3. Execute o script:
   ```bash
   ./executar_caixa.sh
   ```

## Requisitos
- **Python 3** instalado na máquina.

## Contribuições
Contribuições são bem-vindas! Fique à vontade para abrir issues ou enviar pull requests com melhorias ou correções.

## Licença
Este projeto está sob a licença MIT. Para mais informações, consulte o arquivo `LICENSE`.

