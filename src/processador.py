import os
import pandas as pd

from config import (
    ARQUIVO_ENTRADA,
    ARQUIVO_SAIDA
)


def carregar_dados():

    return pd.read_csv(
        ARQUIVO_ENTRADA
    )


def limpar_dados(df):

    df = df.dropna(
        how="all"
    )

    df = df.drop_duplicates()

    df["Order Date"] = (
        pd.to_datetime(
            df["Order Date"],
            dayfirst=True,
            errors="coerce"
        )
    )

    df["Ship Date"] = (
        pd.to_datetime(
            df["Ship Date"],
            dayfirst=True,
            errors="coerce"
        )
    )

    df["Order Date"] = df["Order Date"].dt.strftime("%d/%m/%Y")
    df["Ship Date"] = df["Ship Date"].dt.strftime("%d/%m/%Y")

    return df


def gerar_resumos(df):

    vendas_categoria = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    vendas_regiao = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    top_produtos = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    return vendas_categoria, vendas_regiao, top_produtos


def gerar_kpis(df):

    faturamento_total = f"R$ {df['Sales'].sum():,.2f}"

    total_pedidos = df["Order ID"].nunique()

    clientes_unicos = df["Customer ID"].nunique()

    total_produtos = df["Product Name"].nunique()

    produto_top = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    categoria_top = (
        df.groupby("Category")["Sales"]
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

    ticket_medio = f"R$ {df['Sales'].mean():,.2f}"

    maior_venda = f"R$ {df['Sales'].max():,.2f}"

    kpis = pd.DataFrame({

        "Indicador": [

            "Faturamento Total",
            "Total de Pedidos",
            "Clientes Únicos",
            "Total de Produtos Diferentes",
            "Produto com Maior Faturamento",
            "Categoria Líder",
            "Região com Mais Vendas",
            "Ticket Médio",
            "Maior Venda"

        ],

        "Valor": [

            faturamento_total,
            total_pedidos,
            clientes_unicos,
            total_produtos,
            produto_top,
            categoria_top,
            regiao_top,
            ticket_medio,
            maior_venda

        ]

    })

    return kpis


def salvar_relatorio(
    df,
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

        df.to_excel(
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