import os
import pandas as pd
from formatador import formatar_excel

ARQUIVO_ENTRADA = "src/vendas.csv"
ARQUIVO_SAIDA = "data/saida/relatorio_vendas.xlsx"


def carregar_dados():
    return pd.read_csv(ARQUIVO_ENTRADA)


def limpar_dados(df):

    # Remove linhas totalmente vazias
    df = df.dropna(how="all")

    # Remove registros duplicados
    df = df.drop_duplicates()

    # Converte datas
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True,
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Formata datas para exibição
    df["Order Date"] = (
        df["Order Date"]
        .dt.strftime("%d/%m/%Y")
    )

    df["Ship Date"] = (
        df["Ship Date"]
        .dt.strftime("%d/%m/%Y")
    )

    return df


def gerar_resumos(df):

    vendas_categoria = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    vendas_regiao = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    top_produtos = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
        .head(10)
    )

    return (
        vendas_categoria,
        vendas_regiao,
        top_produtos
    )


def gerar_kpis(df):

    faturamento_total = (
        f"R$ {df['Sales'].sum():,.2f}"
    )

    total_pedidos = (
        df["Order ID"]
        .nunique()
    )

    clientes_unicos = (
        df["Customer ID"]
        .nunique()
    )

    produto_top = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    regiao_top = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    kpis = pd.DataFrame({
        "Indicador": [
            "Faturamento Total",
            "Total de Pedidos",
            "Clientes Únicos",
            "Produto Mais Vendido",
            "Região com Mais Vendas"
        ],
        "Valor": [
            faturamento_total,
            total_pedidos,
            clientes_unicos,
            produto_top,
            regiao_top
        ]
    })

    return kpis


def salvar_relatorio(
    dados,
    categoria,
    regiao,
    produtos,
    kpis
):

    os.makedirs(
        "data/saida",
        exist_ok=True
    )

    with pd.ExcelWriter(
        ARQUIVO_SAIDA,
        engine="openpyxl"
    ) as writer:

        dados.to_excel(
            writer,
            sheet_name="Dados Limpos",
            index=False
        )

        categoria.to_excel(
            writer,
            sheet_name="Categorias",
            index=False
        )

        regiao.to_excel(
            writer,
            sheet_name="Regioes",
            index=False
        )

        produtos.to_excel(
            writer,
            sheet_name="Top Produtos",
            index=False
        )

        kpis.to_excel(
            writer,
            sheet_name="KPIs",
            index=False
        )


def main():

    print("Lendo arquivo CSV...")

    df = carregar_dados()

    print("Limpando dados...")

    df = limpar_dados(df)

    print("Gerando resumos...")

    categoria, regiao, produtos = (
        gerar_resumos(df)
    )

    print("Gerando KPIs...")

    kpis = gerar_kpis(df)

    print("Salvando relatório Excel...")

    salvar_relatorio(
        df,
        categoria,
        regiao,
        produtos,
        kpis
    )

    print("Aplicando formatação...")

    formatar_excel(
        ARQUIVO_SAIDA
    )

    print("\nRelatório criado com sucesso!")
    print(
        f"Arquivo salvo em: {ARQUIVO_SAIDA}"
    )


if __name__ == "__main__":
    main()