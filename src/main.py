from processador import (
    carregar_dados,
    limpar_dados,
    gerar_resumos,
    gerar_kpis,
    salvar_relatorio,
    exportar_powerbi
)

from formatador import formatar_excel
from dashboard import criar_dashboard
from logger import registrar_log

from config import ARQUIVO_SAIDA


def main():

    registrar_log("Iniciando processamento")

    df = carregar_dados()
    df = limpar_dados(df)

    categoria, regiao, produtos = gerar_resumos(df)
    kpis = gerar_kpis(df)

    salvar_relatorio(df, categoria, regiao, produtos, kpis)
    formatar_excel(ARQUIVO_SAIDA)

    criar_dashboard(ARQUIVO_SAIDA, kpis)

    # 🔥 POWER BI
    exportar_powerbi(df)

    registrar_log(f"Relatório gerado com {len(df)} registros")

    print("\nRelatório criado com sucesso!")


if __name__ == "__main__":
    main()