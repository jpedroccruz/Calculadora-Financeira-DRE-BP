import os
import subprocess

def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    
    subprocess.run(comando, shell=True)

def main():
    # 1. Estrutura de dados para o DRE
    # Usamos uma lista de dicionários no lugar da 'struct' do C.
    etapas_do_DRE = [
        "Receita Operacional Bruta",
        "Receita Operacional Líquida",
        "Lucro Bruto",
        "Lucro Operacional",
        "Lucro Líquido antes do IR",
        "Lucro Líquido do Exercício (TOTAL)"
    ]

    dre = []
    for etapa in etapas_do_DRE:
        dre.append(
            {
                "etapa": etapa,
                "despesas": [],  # Lista para armazenar múltiplas despesas
                "total": 0.0
            }
        )

    print("=" * 50)
    print(f"{'CÁLCULO DE DRE':^50}")
    print("=" * 50)

    # 2. Leitura da Receita Inicial com validação
    while True:
        try:
            dre[0]["total"] = float(input("\n> Insira a Receita Operacional Bruta: R$ "))
            break
        except ValueError:
            print("[Erro] Por favor, insira um valor numérico válido.")

    # 3. Laço principal pelas etapas do DRE (exceto a última que é o total final)
    for i in range(len(dre) - 1):
        limpar_tela()
        print(f"\n{'-' * 50}")
        print(f"| Etapa Atual: {dre[i]['etapa']}")
        print(f"| Valor Base : R$ {dre[i]['total']:.2f}")
        print(f"{'-' * 50}")
        
        print("Insira as deduções para esta etapa.")
        print("(Deixe o nome da despesa em branco e aperte ENTER para ir para a próxima etapa)")
        
        total_descontos_etapa = 0.0

        # 4. Funcionalidade de colocar várias despesas até o critério de parada
        while True:
            nome_despesa = input("\n> Nome da despesa (ou ENTER para parar): ").strip()
            
            # Critério de parada: se o usuário não digitar nada e der ENTER
            if not nome_despesa:
                break
            
            while True:
                try:
                    valor_despesa = float(input(f"> Valor de '{nome_despesa}': R$ "))
                    break
                except ValueError:
                    print("[Erro] Por favor, insira um valor numérico válido.")
            
            # Armazena a despesa e soma ao total de descontos da etapa atual
            dre[i]["despesas"].append({"nome": nome_despesa, "valor": valor_despesa})
            total_descontos_etapa += valor_despesa

        # Calcula o valor total da PRÓXIMA etapa do DRE
        dre[i+1]["total"] = dre[i]["total"] - total_descontos_etapa

    limpar_tela()

    # 5. Adaptação da impressão na tela (Interface mais amigável e detalhada)
    print("=" * 55)
    print(f"{'DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO (DRE)':^55}")
    print("=" * 55)

    for i in range(len(dre)):
        # Imprime o total da etapa em negrito (visual)
        print(f"(=) {dre[i]['etapa']:<32} R$ {dre[i]['total']:10.2f}")
        
        # Se não for a última etapa, imprime a lista de despesas que foram deduzidas
        if i < len(dre) - 1:
            if dre[i]["despesas"]:
                for desp in dre[i]["despesas"]:
                    print(f"    (-) {desp['nome']:<28} R$ {desp['valor']:10.2f}")
            else:
                print("    ( Nenhuma dedução informada )")
        print("-" * 55)

if __name__ == "__main__":
    main()  