from datetime import datetime
from copy import deepcopy

# SISTEMA ESPECIALISTA ESCOLAR 3.0 - Python / Google Colab
# Dados demonstrativos. Estoque e historico persistem somente durante a sessao.
PRODUTOS_INICIAIS = {
    1: {"nome": "Lápis Faber-Castell HB", "tipo": "lapis_hb", "preco": 4.50, "estoque": 0},
    2: {"nome": "Lápis BIC HB", "tipo": "lapis_hb", "preco": 2.50, "estoque": 20},
    3: {"nome": "Lápis Genérico HB", "tipo": "lapis_hb", "preco": 1.50, "estoque": 30},
    4: {"nome": "Borracha Branca Premium", "tipo": "borracha", "preco": 3.00, "estoque": 10},
    5: {"nome": "Borracha Branca Econômica", "tipo": "borracha", "preco": 1.50, "estoque": 20},
    6: {"nome": "Caderno 10 Matérias Premium", "tipo": "caderno_10", "preco": 25.00, "estoque": 5},
    7: {"nome": "Caderno 10 Matérias Econômico", "tipo": "caderno_10", "preco": 18.00, "estoque": 10},
    8: {"nome": "Lápis de Cor 24 Cores Premium", "tipo": "cor_24", "preco": 32.00, "estoque": 5},
    9: {"nome": "Lápis de Cor 24 Cores Econômico", "tipo": "cor_24", "preco": 22.00, "estoque": 10},
    10: {"nome": "Caneta Azul BIC", "tipo": "caneta_azul", "preco": 3.50, "estoque": 10},
    11: {"nome": "Caneta Azul Econômica", "tipo": "caneta_azul", "preco": 1.50, "estoque": 20},
}

produtos = deepcopy(PRODUTOS_INICIAIS)
historico = []
regras = {"limite_por_produto": 10}  # Parametro de uma regra de negocio
compra = None  # Memoria de trabalho da compra corrente


def moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def catalogo():
    print("\n=== CATÁLOGO ===")
    for codigo, p in produtos.items():
        print(f"{codigo:2} - {p['nome']} | {moeda(p['preco'])} | Estoque: {p['estoque']}")


def ler_inteiro(mensagem, minimo=None):
    try:
        valor = int(input(mensagem))
        if minimo is not None and valor < minimo:
            raise ValueError
        return valor
    except ValueError:
        print("Digite um número inteiro válido.")
        return None


def iniciar_compra():
    global compra
    try:
        orcamento = float(input("Orçamento (R$): ").replace(",", "."))
        if not 0 <= orcamento < float("inf"):
            raise ValueError
    except ValueError:
        print("Orçamento inválido.")
        return
    compra = {"orcamento": orcamento, "itens": {}, "analise": None, "estado": "CARRINHO_ABERTO"}
    print("Compra iniciada. Carrinho vazio.")


def invalidar_analise():
    if compra is not None:
        compra["analise"] = None
        compra["estado"] = "CARRINHO_ABERTO"


def adicionar_produto():
    if compra is None:
        print("Inicie uma compra primeiro.")
        return
    catalogo()
    codigo = ler_inteiro("Código do produto: ", 1)
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    qtd = ler_inteiro("Quantidade a adicionar: ", 1)
    if qtd is None:
        return
    compra["itens"][codigo] = compra["itens"].get(codigo, 0) + qtd
    invalidar_analise()
    print("Produto adicionado. A análise anterior, se houver, foi invalidada.")


def remover_produto():
    if compra is None:
        print("Inicie uma compra primeiro.")
        return
    codigo = ler_inteiro("Código a remover: ", 1)
    if codigo in compra["itens"]:
        del compra["itens"][codigo]
        invalidar_analise()
        print("Produto removido.")
    else:
        print("Produto não está no carrinho.")


def alterar_quantidade():
    if compra is None:
        print("Inicie uma compra primeiro.")
        return
    codigo = ler_inteiro("Código do produto: ", 1)
    if codigo not in compra["itens"]:
        print("Produto não está no carrinho.")
        return
    qtd = ler_inteiro("Nova quantidade (0 remove): ", 0)
    if qtd is None:
        return
    if qtd == 0:
        del compra["itens"][codigo]
    else:
        compra["itens"][codigo] = qtd
    invalidar_analise()
    print("Carrinho alterado. Será necessária nova análise.")


def visualizar_carrinho():
    if compra is None:
        print("Nenhuma compra iniciada.")
        return
    print(f"\n=== CARRINHO | Estado: {compra['estado']} ===")
    total = 0
    for codigo, qtd in compra["itens"].items():
        p = produtos[codigo]
        subtotal = p["preco"] * qtd
        total += subtotal
        print(f"{qtd}x {p['nome']} - {moeda(subtotal)}")
    print(f"Total solicitado (sem substituições): {moeda(total)}")
    print(f"Orçamento: {moeda(compra['orcamento'])}")


def motor_inferencia(itens, orcamento):
    """Encadeamento para frente: fatos -> regras -> conclusao.

    Retorna uma recomendacao SEM alterar o estoque real.
    R1: disponibilidade; R2: equivalencia; R3: menor preco;
    R4: sem alternativa; R5: reducao de custo; R6: aprovacao.
    Regra adicional configuravel: limite por produto.
    """
    disponivel = {codigo: p["estoque"] for codigo, p in produtos.items()}
    recomendados, pendentes, trilha = [], [], []
    limite = regras["limite_por_produto"]

    for codigo, quantidade in itens.items():
        solicitado = produtos[codigo]
        fatos = f"produto={solicitado['nome']}; quantidade={quantidade}; estoque={disponivel[codigo]}"
        if quantidade > limite:
            trilha.append(f"LIMITE: SE quantidade {quantidade} > limite {limite}, ENTÃO solicitar ajuste. Fatos: {fatos}")
            pendentes.append((codigo, quantidade, "Limite por produto excedido"))
            continue

        if disponivel[codigo] >= quantidade:
            escolhido = codigo
            trilha.append(f"R1: SE estoque >= quantidade, ENTÃO manter produto. Fatos: {fatos}")
        else:
            trilha.append(f"R1: estoque insuficiente. Fatos: {fatos}")
            equivalentes = [
                (alternativo, p) for alternativo, p in produtos.items()
                if alternativo != codigo and p["tipo"] == solicitado["tipo"]
                and disponivel[alternativo] >= quantidade
            ]
            if not equivalentes:
                trilha.append(f"R4: SE não existe equivalente disponível, ENTÃO marcar {solicitado['nome']} como pendente.")
                pendentes.append((codigo, quantidade, "Sem equivalente em estoque"))
                continue
            escolhido = min(equivalentes, key=lambda item: (item[1]["preco"], item[0]))[0]
            trilha.append(f"R2/R3: SE há equivalentes, ENTÃO escolher o mais barato disponível: {produtos[escolhido]['nome']}.")

        disponivel[escolhido] -= quantidade
        recomendados.append({"original": codigo, "escolhido": escolhido, "quantidade": quantidade})

    def total_atual():
        return sum(produtos[item["escolhido"]]["preco"] * item["quantidade"] for item in recomendados)

    total = total_atual()
    if total > orcamento:
        trilha.append(f"R5: SE total {moeda(total)} > orçamento {moeda(orcamento)}, ENTÃO buscar alternativas mais econômicas.")
        indices = sorted(range(len(recomendados)), key=lambda i: produtos[recomendados[i]["escolhido"]]["preco"] * recomendados[i]["quantidade"], reverse=True)
        for i in indices:
            if total <= orcamento:
                break
            item = recomendados[i]
            atual_id, qtd = item["escolhido"], item["quantidade"]
            atual = produtos[atual_id]
            alternativas = [
                (codigo, p) for codigo, p in produtos.items()
                if p["tipo"] == atual["tipo"] and p["preco"] < atual["preco"]
                and disponivel[codigo] >= qtd
            ]
            if alternativas:
                novo_id = min(alternativas, key=lambda x: (x[1]["preco"], x[0]))[0]
                disponivel[atual_id] += qtd
                disponivel[novo_id] -= qtd
                item["escolhido"] = novo_id
                trilha.append(f"R5: substituir {atual['nome']} por {produtos[novo_id]['nome']} para reduzir o custo.")
                total = total_atual()

    # Uma recomendacao nunca deve usar mais unidades do que o estoque existente.
    # A copia 'disponivel' controla a reserva simulada entre os itens.
    aprovado = bool(recomendados) and not pendentes and total <= orcamento
    if pendentes:
        trilha.append("R6: SE existem itens pendentes, ENTÃO não aprovar compra completa.")
    elif total > orcamento:
        trilha.append("R6: SE total excede orçamento, ENTÃO não aprovar.")
    elif not recomendados:
        trilha.append("R6: SE carrinho vazio, ENTÃO não aprovar.")
    else:
        trilha.append("R6: SE todos os itens estão atendidos e total <= orçamento, ENTÃO aprovar recomendação.")
    return {"carrinho": recomendados, "pendentes": pendentes, "total": total, "aprovado": aprovado, "trilha": trilha}


def analisar_compra():
    if compra is None:
        print("Inicie uma compra primeiro.")
        return
    compra["estado"] = "EM_ANALISE"
    resultado = motor_inferencia(compra["itens"], compra["orcamento"])
    compra["analise"] = resultado
    compra["estado"] = "AGUARDANDO_CONFIRMACAO" if resultado["aprovado"] else "AJUSTE_NECESSARIO"
    print("\n=== REGRAS ACIONADAS / EXPLICAÇÕES ===")
    for passo in resultado["trilha"]:
        print("-", passo)
    print("\n=== RECOMENDAÇÃO DO AGENTE ===")
    for item in resultado["carrinho"]:
        p = produtos[item["escolhido"]]
        original = produtos[item["original"]]
        aviso = f" (substitui {original['nome']})" if item["original"] != item["escolhido"] else ""
        print(f"{item['quantidade']}x {p['nome']}{aviso} - {moeda(p['preco'] * item['quantidade'])}")
    for codigo, qtd, motivo in resultado["pendentes"]:
        print(f"PENDENTE: {qtd}x {produtos[codigo]['nome']} - {motivo}")
    print(f"Total recomendado: {moeda(resultado['total'])} | Orçamento: {moeda(compra['orcamento'])}")
    print("Resultado:", "APROVADO (aguardando cliente)" if resultado["aprovado"] else "AJUSTE NECESSÁRIO")


def finalizar_compra():
    global compra
    if compra is None or compra["analise"] is None or compra["estado"] != "AGUARDANDO_CONFIRMACAO":
        print("É necessário obter uma análise aprovada antes de finalizar.")
        return
    # Reavalia fatos e regras atuais: impede finalizar uma analise desatualizada.
    anterior = compra["analise"]
    atualizado = motor_inferencia(compra["itens"], compra["orcamento"])
    if not atualizado["aprovado"] or atualizado["carrinho"] != anterior["carrinho"] or atualizado["total"] != anterior["total"]:
        compra["analise"] = atualizado
        compra["estado"] = "AJUSTE_NECESSARIO" if not atualizado["aprovado"] else "CARRINHO_ABERTO"
        print("Os fatos ou as recomendações mudaram. Faça uma nova análise antes de confirmar.")
        return
    if input("Confirmar compra e substituições recomendadas? (s/n): ").strip().lower() != "s":
        print("Compra não finalizada. Carrinho preservado.")
        return
    for item in atualizado["carrinho"]:
        produtos[item["escolhido"]]["estoque"] -= item["quantidade"]
    registro = {"data": datetime.now().strftime("%d/%m/%Y %H:%M"), "total": atualizado["total"],
                "itens": deepcopy(atualizado["carrinho"]), "regras": atualizado["trilha"][:]}
    historico.append(registro)
    with open("ultimo_relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"RELATÓRIO DO SISTEMA ESPECIALISTA\nData: {registro['data']}\n")
        for item in registro["itens"]:
            arquivo.write(f"{item['quantidade']}x {produtos[item['escolhido']]['nome']}\n")
        arquivo.write(f"Total: {moeda(registro['total'])}\n\nREGRAS ACIONADAS:\n")
        arquivo.write("\n".join(registro["regras"]) + "\n")
    compra["estado"] = "COMPRA_FINALIZADA"
    compra = None
    print("Compra concluída. Estoque atualizado e ultimo_relatorio.txt gerado.")


def repor_estoque():
    catalogo()
    codigo = ler_inteiro("Código do produto: ", 1)
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    quantidade = ler_inteiro("Quantidade a repor: ", 1)
    if quantidade is None:
        return
    produtos[codigo]["estoque"] += quantidade
    invalidar_analise()
    print("Estoque atualizado. Análise anterior invalidada, se existia.")


def alterar_regra():
    print(f"Limite atual por produto: {regras['limite_por_produto']} unidades")
    novo_limite = ler_inteiro("Novo limite por produto: ", 1)
    if novo_limite is None:
        return
    regras["limite_por_produto"] = novo_limite
    invalidar_analise()
    print("Regra alterada manualmente. Compras abertas precisam de nova análise.")


def mostrar_historico():
    print("\n=== HISTÓRICO ===")
    if not historico:
        print("Nenhuma compra registrada.")
    for indice, registro in enumerate(historico, 1):
        print(f"{indice} - {registro['data']} - {moeda(registro['total'])}")


def menu():
    opcoes = {"1": catalogo, "2": iniciar_compra, "3": adicionar_produto,
              "4": remover_produto, "5": alterar_quantidade, "6": visualizar_carrinho,
              "7": analisar_compra, "8": finalizar_compra, "9": repor_estoque,
              "10": mostrar_historico, "11": alterar_regra}
    while True:
        print("\n=== SISTEMA ESPECIALISTA ESCOLAR 3.0 ===")
        print("1 - Consultar catálogo\n2 - Iniciar compra\n3 - Adicionar produto ao carrinho")
        print("4 - Remover produto do carrinho\n5 - Alterar quantidade\n6 - Visualizar carrinho")
        print("7 - Analisar compra (SE–ENTÃO)\n8 - Finalizar compra\n9 - Repor estoque")
        print("10 - Histórico de compras\n11 - Alterar regra (demonstração)\n0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            print("Sistema encerrado.")
            break
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()