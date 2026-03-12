#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
MELHORIAS
- Adicionar a funcionalidade de colocar várias despesas até um critério de parada
- Adaptar leitura das variáveis do DRE (adicionar for para a entrada)
- Adaptar impressão na tela dos resultados com várias despesas
- Deixar a interface mais amigável
*/

typedef struct{
    char etapa_do_DRE[50];
    char tipo_da_despesa[10][50];
    float valor_da_despesa;
    float total_da_etapa_do_DRE;
} Despesa;

int main(){
    float receita_operacional_bruta, receita_operacional_liquida, lucro_bruto;
    float lucro_operacional, lucro_liquido_antes_IR, total;
    Despesa despesas_DRE[6];
    strcpy(despesas_DRE[0].etapa_do_DRE, "Receita Operacional Bruta");
    strcpy(despesas_DRE[1].etapa_do_DRE, "Receita Operacional Líquida");
    strcpy(despesas_DRE[2].etapa_do_DRE, "Lucro Bruto");
    strcpy(despesas_DRE[3].etapa_do_DRE, "Lucro Operacional");
    strcpy(despesas_DRE[4].etapa_do_DRE, "Lucro Líquido antes do IR");
    strcpy(despesas_DRE[5].etapa_do_DRE, "TOTAL");

    printf("=============== CÁLCULO DE DRE ===============\n");
    printf("> Insira a receita operacional bruta: R$");
    scanf("%f", &despesas_DRE[0].total_da_etapa_do_DRE);
    fflush(stdin);
    printf("\n> Escreva o que deve ser descontado: ");
    scanf("%[^\n]s", &despesas_DRE[0].tipo_da_despesa[0]);
    fflush(stdin);
    printf("\n> Insira o valor: R$");
    scanf("%f", &despesas_DRE[0].valor_da_despesa);
    fflush(stdin);

    // Receita Operacional Líquida = Receita Operacional Bruta - Despesas da Receita Operacional Bruta
    despesas_DRE[1].total_da_etapa_do_DRE = despesas_DRE[0].total_da_etapa_do_DRE - despesas_DRE[0].valor_da_despesa;

    printf("\n| Receita Operacional Líquida: R$%.2f",  despesas_DRE[1].total_da_etapa_do_DRE);
    printf("\n> Escreva o que deve ser descontado: ");
    scanf("%[^\n]s", &despesas_DRE[1].tipo_da_despesa[0]);
    fflush(stdin);
    printf("\n> Insira o valor: R$");
    scanf("%f", &despesas_DRE[1].valor_da_despesa);
    fflush(stdin);

    // Lucro Bruto = Receita Operacional Liquida - Despesas da Receita O. Liquida;
    despesas_DRE[2].total_da_etapa_do_DRE = despesas_DRE[1].total_da_etapa_do_DRE - despesas_DRE[1].valor_da_despesa;

    printf("\n| Lucro Bruto: R$%.2f", despesas_DRE[2].total_da_etapa_do_DRE);
    printf("\n> Escreva o que deve ser descontado: ");
    scanf("%[^\n]s", &despesas_DRE[2].tipo_da_despesa[0]);
    fflush(stdin);
    printf("\n> Insira o valor: R$");
    scanf("%f", &despesas_DRE[2].valor_da_despesa);
    fflush(stdin);

    // Lucro Operacional = Lucro Bruto - Despesas do Lucro Bruto;
    despesas_DRE[3].total_da_etapa_do_DRE = despesas_DRE[2].total_da_etapa_do_DRE - despesas_DRE[2].valor_da_despesa;

    printf("\n| Lucro Operacional: R$%.2f", despesas_DRE[3].total_da_etapa_do_DRE);
    printf("\n> Escreva o que deve ser descontado: ");
    scanf("%[^\n]s", &despesas_DRE[3].tipo_da_despesa[0]);
    fflush(stdin);
    printf("\n> Insira o valor: R$");
    scanf("%f", &despesas_DRE[3].valor_da_despesa);
    fflush(stdin);

    // Lucro Liquido antes do IR = Lucro Operacional - Despesas do Lucro Operacional
    despesas_DRE[4].total_da_etapa_do_DRE = despesas_DRE[3].total_da_etapa_do_DRE - despesas_DRE[3].valor_da_despesa;

    printf("\n| Lucro Líquido antes do IR: R$%.2f", despesas_DRE[4].total_da_etapa_do_DRE);
    printf("\n> Escreva o que deve ser descontado: ");
    scanf("%[^\n]s", &despesas_DRE[4].tipo_da_despesa[0]);
    fflush(stdin);
    printf("\n> Insira o valor: R$");
    scanf("%f", &despesas_DRE[4].valor_da_despesa);
    fflush(stdin);

    // TOTAL = Lucro Liquido antes do IR - Despesas do IR;
    despesas_DRE[5].total_da_etapa_do_DRE = despesas_DRE[4].total_da_etapa_do_DRE - despesas_DRE[4].valor_da_despesa;
    
    system("cls");
    
    for(int i = 0; i<6; i++){
        printf("(=)%s %.2f\n", despesas_DRE[i].etapa_do_DRE, despesas_DRE[i].total_da_etapa_do_DRE);
        if (i == 5) break;
        printf("\t(-)%s %.2f\n", despesas_DRE[i].tipo_da_despesa[0], despesas_DRE[i].valor_da_despesa);
    }

    return 0;
}