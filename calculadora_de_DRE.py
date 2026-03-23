import os
import subprocess

def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    
    subprocess.run(comando, shell=True)

dre = []
balanco = []
totais = {}
resultado_do_balanço = 0.0
indices = {}

def calcularDRE():
    limpar_tela()

    etapas_do_DRE = [
        "Receita Operacional Bruta",
        "Receita Operacional Líquida",
        "Lucro Bruto",
        "Lucro Operacional",
        "Lucro Líquido antes do IR",
        "Lucro Líquido do Exercício (TOTAL)"
    ]

    for etapa in etapas_do_DRE:
        if etapa == "Receita Operacional Líquida":
            dre.append({
                "etapa": etapa,
                "despesas": [{"nome": "CMV / CSV", "valor": None}],  
                "total": 0.0
            })
        else:
            dre.append({
                "etapa": etapa,
                "despesas": [],  
                "total": 0.0
            })

    print("=" * 50)
    print(f"{'CÁLCULO DE DRE':^50}")
    print("=" * 50)

    while True:
        try:
            dre[0]["total"] = float(input("\n> Insira a Receita Operacional Bruta: R$ "))
            break
        except ValueError:
            print("[Erro] Por favor, insira um valor numérico válido.")

    for i in range(len(dre) - 1):
        limpar_tela()
        print(f"\n{'-' * 50}")
        print(f"| Etapa Atual: {dre[i]['etapa']}")
        print(f"| Valor Base : R$ {dre[i]['total']:.2f}")
        print(f"{'-' * 50}")
        
        print("Insira as deduções para esta etapa.")
        print("(Deixe o nome da despesa em branco e aperte ENTER para ir para a próxima etapa)")
        
        total_descontos_etapa = 0.0

        if (i == 1):
            while True:
                try:
                    valor_despesa = float(input(f"\n> Valor de CMV / CSV: R$ "))
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            dre[1]["despesas"][0] = {"nome": "CMV / CSV", "valor": valor_despesa}
            total_descontos_etapa += valor_despesa

        while True:
            nome_despesa = input("\n> Nome da despesa (ou ENTER para parar): ").strip()
            
            if not nome_despesa:
                break
            
            while True:
                try:
                    valor_despesa = float(input(f"> Valor de '{nome_despesa}': R$ "))
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            dre[i]["despesas"].append({"nome": nome_despesa, "valor": valor_despesa})
            total_descontos_etapa += valor_despesa

        dre[i+1]["total"] = dre[i]["total"] - total_descontos_etapa

    limpar_tela()

    gerarRelatorioDRE()    

def calcularBP():
    limpar_tela()
    
    secoes_do_balanco = [
        "Ativo Circulante",
        "Ativo Não Circulante",
        "Passivo Circulante",
        "Passivo Não Circulante",
        "Patrimônio Líquido"
    ]

    for secao in secoes_do_balanco:
        if (secao == "Ativo Circulante"):
            balanco.append({
            "secao": secao,
            "itens": [{"nome": "Estoques", "valor": None}, {"nome": "Contas a receber", "valor": None}],
            "total": 0.0
        })
        elif (secao == "Passivo Circulante"):
            balanco.append({
            "secao": secao,
            "itens": [{"nome": "Fornecedores", "valor": None}],
            "total": 0.0
        })
        elif (secao == "Patrimônio Líquido"):
            balanco.append({
                "secao": secao,
                "itens": [{"nome": f"{"Lucros Acumulados" if dre[5]['total'] >= 0 else "Prejuízos acumulados"}", "valor": dre[5]['total']}],
                "total": 0.0
            })
        else:
            balanco.append({
                "secao": secao,
                "itens": [],
                "total": 0.0
            })

    print("=" * 50)
    print(f"{'CÁLCULO DE BALANÇO PATRIMONIAL':^50}")
    print("=" * 50)

    for i in range(len(balanco)):
        limpar_tela()
        print(f"\n{'-' * 50}")
        print(f"| Seção Atual: {balanco[i]['secao']}")
        print(f"{'-' * 50}")

        print("Insira os itens desta seção.")
        print("(Deixe o nome do item em branco e aperte ENTER para ir para a próxima seção)")

        total_itens_secao = 0.0

        if (i == 0):
            while True:
                try:
                    valor_despesa = float(input(f"\n> Valor de Estoques: R$ "))
                    if (valor_despesa <= 0):
                        print("[Erro] Por favor, insira um valor numérico maior que ZERO.")
                        continue
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            balanco[0]["itens"][0] = {"nome": "Estoques", "valor": valor_despesa}
            total_itens_secao += valor_despesa

            while True:
                try:
                    valor_despesa = float(input(f"\n> Valor de Contas a receber: R$ "))
                    if (valor_despesa <= 0):
                        print("[Erro] Por favor, insira um valor numérico maior que ZERO.")
                        continue
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            balanco[0]["itens"][1] = {"nome": "Contas a receber", "valor": valor_despesa}
            total_itens_secao += valor_despesa

        if (i == 2):
            while True:
                try:
                    valor_despesa = float(input(f"\n> Valor de Fornecedores: R$ "))
                    if (valor_despesa <= 0):
                        print("[Erro] Por favor, insira um valor numérico maior que ZERO.")
                        continue
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            balanco[2]["itens"][0] = {"nome": "Fornecedores", "valor": valor_despesa}
            total_itens_secao += valor_despesa

        if (i == 4):
            total_itens_secao += dre[5]['total']

        while True:
            nome_item = input("\n> Nome do item (ou ENTER para parar): ").strip()

            if not nome_item:
                itens_validos = [item for item in balanco[i]["itens"] if item.get("valor") is not None]
                if len(itens_validos) == 0:
                    print("[Erro] Você precisa informar pelo menos um item antes de avançar para a próxima seção.")
                    continue
                break

            while True:
                try:
                    valor_item = float(input(f"> Valor de '{nome_item}': R$ "))
                    if (valor_item <= 0):
                        print("[Erro] Por favor, insira um valor numérico maior que ZERO.")
                        continue
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")

            balanco[i]["itens"].append({"nome": nome_item, "valor": valor_item})
            total_itens_secao += valor_item

        balanco[i]["total"] = total_itens_secao

    totais["Ativo Circulante"] = balanco[0]["total"]
    totais["Ativo Não Circulante"] = balanco[1]["total"]
    totais["Passivo Circulante"] = balanco[2]["total"]
    totais["Passivo Não Circulante"] = balanco[3]["total"]
    totais["Patrimônio Líquido"] = balanco[4]["total"]

    limpar_tela()

    resultado_do_balanço = (totais["Ativo Circulante"] - totais["Ativo Não Circulante"]) - ((totais["Passivo Circulante"] + totais["Passivo Não Circulante"]) + totais["Patrimônio Líquido"])

    gerarRelatorioBP()

def calcularIndices():
    indices['Liquidez Corrente'] = totais["Ativo Circulante"] / totais['Passivo Circulante']
    indices['Liquidez Seca'] = (totais["Ativo Circulante"] - balanco[0]['itens'][0]['valor']) / totais['Passivo Circulante']
    indices['Giro de Estoque'] = dre[1]['despesas'][0]['valor'] / balanco[0]['itens'][0]['valor']
    indices['Prazo Médio de Recebimento'] = balanco[0]['itens'][1]['valor'] / (dre[0]['total'] / 365)
    indices['Prazo Médio de Pagamento'] = balanco[2]['itens'][0]['valor'] / ((0.7 * dre[1]['despesas'][0]['valor']) / 365)
    indices['Giro do Ativo Total'] = dre[0]['total'] / (totais["Ativo Circulante"] + totais["Ativo Não Circulante"])
    indices['Endividamento Geral'] = (totais["Passivo Circulante"] + totais["Passivo Não Circulante"]) / (totais["Ativo Circulante"] + totais["Ativo Não Circulante"])
    indices['Margem de Lucro Bruto'] = dre[2]['total'] / dre[0]['total']
    indices['Margem de Lucro Operacional'] = dre[3]['total'] / dre[0]['total']
    indices['Margem de Lucro Líquido'] = dre[5]['total'] / dre[0]['total']

def gerarRelatorioDRE():
    print("=" * 55)
    print(f"{'DRE':^55}")
    print("=" * 55)
    
    if (dre): 
        for i in range(len(dre)):
            print(f"(=) {dre[i]['etapa']:<32} R$ {dre[i]['total']:10.2f}")
            
            if i < len(dre) - 1:
                if dre[i]["despesas"]:
                    for desp in dre[i]["despesas"]:
                        print(f"    (-) {desp['nome']:<28} R$ {desp['valor']:10.2f}")
                else:
                    print("    ( Nenhuma dedução informada )")
            print("-" * 55)
    else:
        print("Você não calculou o DRE.")

    print('\n')

def gerarRelatorioBP():
    print("=" * 55)
    print(f"{'BALANÇO PATRIMONIAL':^55}")
    print("=" * 55)
    
    if (balanco): 
        for secao in balanco:
            print(f"{secao['secao']:<36} R$ {secao['total']:10.2f}")
            if secao["itens"]:
                for item in secao["itens"]:
                    print(f"    {item['nome']:<32} R$ {item['valor']:10.2f}")
            else:
                print("    ( Nenhum item informado )")
            print("-" * 55)

        print(f"{'TOTAL DO ATIVO':<36} R$ {totais['Ativo Circulante'] + totais['Ativo Não Circulante']:10.2f}")
        print(f"{'TOTAL DO PASSIVO':<36} R$ {totais['Passivo Circulante'] + totais['Passivo Não Circulante']:10.2f}")
        print(f"{'TOTAL PL':<36} R$ {totais['Patrimônio Líquido']:10.2f}")
        print("=" * 55)
        
        if (resultado_do_balanço == 0): print("BALANÇO CONSISTENTE: A EQUAÇÃO FUNDAMENTAL FOI RESPEITADA.")
        elif (resultado_do_balanço > 0): print(f"BALANÇO INCONSISTENTE: ESTÁ SOBRANDO R$ {resultado_do_balanço:.2f}.")
        else: print(f"BALANÇO INCONSISTENTE: ESTÁ FALTANDO R$ {resultado_do_balanço:.2f}.")
    else:
        print("Você não calculou o Balanço Patrimonial.")

    print('\n')

def gerarRelatorioIndices():
    print("=" * 55)
    print(f"{'ÍNDICES FINANCEIROS':^55}")
    print("=" * 55)

    if (resultado_do_balanço == 0 and balanco): 
        calcularIndices()

        print(f"Liquidez Corrente: {indices['Liquidez Corrente']:.1f}")
        print(f"Liquidez Seca: {indices['Liquidez Seca']:.1f}")
        print(f"Giro de Estoque: {indices['Giro de Estoque']:.1f} vezes ao ano")
        print(f"Prazo Médio de Recebimento: {indices['Prazo Médio de Recebimento']:.1f} dias")
        print(f"Prazo Médio de Pagamento: {indices['Prazo Médio de Pagamento']:.1f} dias")
        print(f"Giro do Ativo Total: {indices['Giro do Ativo Total']:.2f}")
        print(f"Endividamento Geral: {(100 * indices['Endividamento Geral']):.0f}%")
        print(f"Margem de Lucro Bruto: {(100 * indices['Margem de Lucro Bruto']):.0f}%")
        print(f"Margem de Lucro Operacional: {(100 * indices['Margem de Lucro Operacional']):.0f}%")
        print(f"Margem de Lucro Líquido: {(100 * indices['Margem de Lucro Líquido']):.0f}%")
    else:
        print("Você não calculou, ou o resultado do Balanço\nPatrimonial está INCONSISTENTE.")
    
    print('\n')

def gerarRelatorioGeral():
    limpar_tela()
    gerarRelatorioDRE()
    gerarRelatorioBP()
    gerarRelatorioIndices()

def main():
    option = 1

    while option != 0:
        limpar_tela()

        print("=" * 50)
        print(f"{'CÁLCULADORA DE FINANCEIRA':^50}")
        print("=" * 50)
        print(f"{'[ 0 ] SAIR':<50}")
        print(f"{'[ 1 ] CALCULAR DRE':<50}")
        print(f"{'[ 2 ] CALCULAR BALANÇO':<50}")
        print(f"{'[ 3 ] EXIBIR RELATÓRIO FINAL':<50}")
        print("=" * 50)

        while True:
            try:
                option = int(input("Insira uma opção: "))
                break
            except ValueError:
                print("[Erro] Por favor, insira um valor numérico válido.")

        match option:
            case 0:
                return
            case  1:
                calcularDRE()
            case  2:
                if (len(dre)):
                    calcularBP()
                else:
                    print("\n[Erro] Você precisa calcular a DRE primeiro.")
            case 3:
                gerarRelatorioGeral()
            case _:
                print("[Erro] Por favor, insira um valor válido.")
        
        input("Pressione uma tecla para continuar...")
        
if __name__ == "__main__":
    main()  