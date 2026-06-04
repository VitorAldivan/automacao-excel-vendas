import os
import pandas as pd

from config import (
    ARQUIVO_ENTRADA,
    ARQUIVO_SAIDA,
    ARQUIVO_POWERBI
)


def carregar_dados():
    return pd.read_csv(ARQUIVO_ENTRADA)


def limpar_dados(df):

    df = df.dropna(how="all")
    df = df.drop_duplicates()

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

    receita_por_cliente = df["Sales"].sum() / df["Customer ID"].nunique()

    top_cliente = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    ticket_medio_por_pedido = df["Sales"].sum() / df["Order ID"].nunique()

    qtd_media_pedido = df.groupby("Order ID")["Sales"].sum().mean()

    kpis = pd.DataFrame({

        "Indicador": [
            "Faturamento Total",
            "Total de Pedidos",
            "Clientes Únicos",
            "Total de Produtos Diferentes",
            "Produto com Maior Faturamento",
            "Categoria Líder",
            "Região com Mais Vendas",
            "Top Cliente",
            "Receita por Cliente",
            "Ticket Médio por Pedido",
            "Ticket Médio",
            "Maior Venda",
            "Qtd Média por Pedido"
        ],

        "Valor": [
            faturamento_total,
            total_pedidos,
            clientes_unicos,
            total_produtos,
            produto_top,
            categoria_top,
            regiao_top,
            top_cliente,
            f"R$ {receita_por_cliente:,.2f}",
            f"R$ {ticket_medio_por_pedido:,.2f}",
            ticket_medio,
            maior_venda,
            round(qtd_media_pedido, 2)
        ]
    })

    return kpis


# =========================
# POWER BI EXPORT (NOVO)
# =========================

def exportar_powerbi(df):

    os.makedirs("data/saida", exist_ok=True)

    df_powerbi = df.copy()

    # garante formato limpo pro BI
    df_powerbi.to_csv(
        ARQUIVO_POWERBI,
        index=False,
        encoding="utf-8"
    )


def salvar_relatorio(df, categoria, regiao, produtos, kpis):

    os.makedirs("data/saida", exist_ok=True)

    with pd.ExcelWriter(ARQUIVO_SAIDA, engine="openpyxl") as writer:

        df.to_excel(writer, sheet_name="Dados Limpos", index=False)
        categoria.to_excel(writer, sheet_name="Categorias", index=False)
        regiao.to_excel(writer, sheet_name="Regioes", index=False)
        produtos.to_excel(writer, sheet_name="Top Produtos", index=False)
        kpis.to_excel(writer, sheet_name="KPIs", index=False)