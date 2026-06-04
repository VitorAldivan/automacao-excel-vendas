from processador import (
    carregar_dados,
    limpar_dados,
    gerar_resumos,
    gerar_kpis,
    salvar_relatorio
)

from formatador import (
    formatar_excel
)

from dashboard import (
    criar_dashboard
)

from logger import (
    registrar_log
)

from config import (
    ARQUIVO_SAIDA
)


def main():

    registrar_log(
        "Iniciando processamento"
    )

    print(
        "Lendo arquivo CSV..."
    )

    df = carregar_dados()

    print(
        "Limpando dados..."
    )

    df = limpar_dados(df)

    print(
        "Gerando resumos..."
    )

    categoria, regiao, produtos = (
        gerar_resumos(df)
    )

    print(
        "Gerando KPIs..."
    )

    kpis = gerar_kpis(df)

    print(
        "Salvando relatório..."
    )

    salvar_relatorio(
        df,
        categoria,
        regiao,
        produtos,
        kpis
    )

    print(
        "Formatando relatório..."
    )

    formatar_excel(
        ARQUIVO_SAIDA
    )

    print(
        "Criando dashboard..."
    )

    criar_dashboard(
        ARQUIVO_SAIDA,
        kpis
    )

    registrar_log(
        f"Relatório gerado com {len(df)} registros"
    )

    print(
        "\nRelatório criado com sucesso!"
    )


if __name__ == "__main__":
    main()