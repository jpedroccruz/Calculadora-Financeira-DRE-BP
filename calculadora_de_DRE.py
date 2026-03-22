import os
import subprocess

def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    
    subprocess.run(comando, shell=True)

dre = []

def calcaular_dre():
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

    print("=" * 55)
    print(f"{'DEMONSTRAÇÃO DO RESULTADO DO DRE':^55}")
    print("=" * 55)

    for i in range(len(dre)):
        print(f"(=) {dre[i]['etapa']:<32} R$ {dre[i]['total']:10.2f}")
        
        if i < len(dre) - 1:
            if dre[i]["despesas"]:
                for desp in dre[i]["despesas"]:
                    print(f"    (-) {desp['nome']:<28} R$ {desp['valor']:10.2f}")
            else:
                print("    ( Nenhuma dedução informada )")
        print("-" * 55)

def balancoPatrimonial():
    limpar_tela()

    secoes_do_balanco = [
        "Ativo Circulante",
        "Ativo Não Circulante",
        "Passivo Circulante",
        "Passivo Não Circulante",
        "Patrimônio Líquido"
    ]

    balanco = []
    for secao in secoes_do_balanco:
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

        while True:
            nome_item = input("\n> Nome do item (ou ENTER para parar): ").strip()

            if not nome_item:
                break

            while True:
                try:
                    valor_item = float(input(f"> Valor de '{nome_item}': R$ "))
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")

            balanco[i]["itens"].append({"nome": nome_item, "valor": valor_item})
            total_itens_secao += valor_item

        balanco[i]["total"] = total_itens_secao

    total_ativo = balanco[0]["total"] + balanco[1]["total"]
    total_passivo = balanco[2]["total"] + balanco[3]["total"]
    total_pl = balanco[4]["total"]
    total_passivo_pl = total_passivo + total_pl

    limpar_tela()

    print("=" * 55)
    print(f"{'DEMONSTRAÇÃO DO RESULTADO DO BALANÇO':^55}")
    print("=" * 55)
    
    for secao in balanco:
        print(f"{secao['secao']:<36} R$ {secao['total']:10.2f}")
        if secao["itens"]:
            for item in secao["itens"]:
                print(f"    {item['nome']:<32} R$ {item['valor']:10.2f}")
        else:
            print("    ( Nenhum item informado )")
        print("-" * 55)

    print(f"{'SUBTOTAL DO ATIVO':<36} R$ {total_ativo:10.2f}")
    print(f"{'SUBTOTAL DO PASSIVO':<36} R$ {total_passivo:10.2f}")
    print(f"{'SUBTOTAL DO P.L.':<36} R$ {total_pl:10.2f}")
    print(f"{'TOTAL DO ATIVO':<36} R$ {total_ativo:10.2f}")
    print(f"{'TOTAL PASSIVO + PL':<36} R$ {total_passivo_pl:10.2f}")
    print("=" * 55)

def main():
    option = 1

    while option != 0:
        limpar_tela()

        print("=" * 50)
        print(f"{'CÁLCULADORA DE DE BALANÇO PATRIMONIAL E DRE':^50}")
        print("=" * 50)
        print(f"{'[ 0 ] SAIR':<50}")
        print(f"{'[ 1 ] DRE':<50}")
        print(f"{'[ 2 ] BALANÇO PATRIMONIAL':<50}")
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
                calcaular_dre()
            case 2: 
                balancoPatrimonial()
            case _:
                print("[Erro] Por favor, insira um valor válido.")
        
        input("Pressione uma tecla para continuar...")

if __name__ == "__main__":
    main()  