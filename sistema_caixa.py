import getpass

# Lista de produtos fictícios com preços
produtos = {
    "12345": {"nome": "Leite", "preco": 5.00},
    "23456": {"nome": "Pão de Sanduíche", "preco": 7.00},
    "34567": {"nome": "Dúzia de Ovos", "preco": 10.00},
    "45678": {"nome": "Arroz 5kg", "preco": 20.00},
    "56789": {"nome": "Feijão 1kg", "preco": 8.00},
    "67890": {"nome": "Macarrão", "preco": 4.50},
    "78901": {"nome": "Café 500g", "preco": 12.00},
    "89012": {"nome": "Açúcar 1kg", "preco": 3.50},
    "90123": {"nome": "Sal 1kg", "preco": 2.00},
    "01234": {"nome": "Detergente", "preco": 1.50}
}

def exibir_tabela_produtos():
    print(f"{'Código':<10}{'Produto':<20}{'Preço (R$)':<10}")
    print("-" * 40)
    for codigo, info in produtos.items():
        print(f"{codigo:<10}{info['nome']:<20}{info['preco']:<10.2f}")

def sistema_caixa():
    print("=== Bem-vindo ao Sistema de Caixa ===")
    
    # Perguntar CPF na nota
    cpf = input("Gostaria de colocar o CPF na nota fiscal? (s/n): ").strip().lower()
    if cpf == 's':
        cpf_numero = input("Digite seu CPF: ")
        print(f"CPF {cpf_numero} registrado na nota fiscal.\n")
    else:
        cpf_numero = "Não informado"
    
    print("Produtos disponíveis:")
    exibir_tabela_produtos()
    
    print("\nComece a passar os produtos. Use o menu abaixo para operações:")
    print(f"{'Tecla':<10}{'Função':<30}")
    print("-" * 40)
    print(f"{'X':<10}{'Multiplicar quantidade'}")
    print(f"{'D':<10}{'Deletar item (requer senha)'}")
    print(f"{'F':<10}{'Finalizar compra'}")
    print("-" * 40)

    total = 0
    itens = []

    while True:
        operacao = input("Digite uma tecla do menu ou um código de barras: ").strip().upper()
        
        if operacao == 'X':
            try:
                quantidade = int(input("Digite a quantidade: "))
                codigo = input("Digite o código de barras do produto: ").strip()
                if codigo in produtos:
                    produto = produtos[codigo]
                    total += produto["preco"] * quantidade
                    itens.extend([produto] * quantidade)
                    print(f"{quantidade} x {produto['nome']} - R$ {produto['preco'] * quantidade:.2f} adicionado ao carrinho.")
                else:
                    print("Código de barras inválido.")
            except ValueError:
                print("Quantidade inválida. Tente novamente.")
        
        elif operacao == 'D':
            senha = getpass.getpass("Digite a senha do sistema: ")
            if senha == getpass.getuser():  # Valida com o nome do usuário logado no sistema
                codigo = input("Digite o código de barras do produto para deletar: ").strip()
                if codigo in produtos:
                    produto = produtos[codigo]
                    if produto in itens:
                        itens.remove(produto)
                        total -= produto["preco"]
                        print(f"{produto['nome']} removido do carrinho.")
                    else:
                        print("Produto não encontrado no carrinho.")
                else:
                    print("Código de barras inválido.")
            else:
                print("Senha incorreta.")
        
        elif operacao == 'F':
            confirmar = input("Deseja encerrar a compra? (s/n): ").strip().lower()
            if confirmar == 's':
                break
            else:
                print("Continue adicionando produtos.")

        elif operacao in produtos:
            produto = produtos[operacao]
            total += produto["preco"]
            itens.append(produto)
            print(f"{produto['nome']} - R$ {produto['preco']:.2f} adicionado ao carrinho.")
        else:
            print("Comando inválido. Tente novamente.")

    # Nota fiscal
    print("\n=== Nota Fiscal ===")
    print(f"{'Produto':<20}{'Preço (R$)':<10}")
    print("-" * 30)
    for item in itens:
        print(f"{item['nome']:<20}{item['preco']:<10.2f}")
    print("-" * 30)
    print(f"Total: R$ {total:.2f}")
    print(f"CPF: {cpf_numero}")
    print("Obrigado por comprar conosco!")

if __name__ == "__main__":
    sistema_caixa()
