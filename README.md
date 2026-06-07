# 📊 Automação de Relatório de Vendas com Python e Power BI

## 📌 Sobre o Projeto

Este projeto realiza a automação do processamento de dados de vendas utilizando Python. A aplicação lê um arquivo CSV, realiza a limpeza dos dados, gera indicadores de desempenho (KPIs), cria relatórios em Excel e disponibiliza uma base preparada para análises no Power BI.

O objetivo é demonstrar conhecimentos em manipulação de dados, automação de relatórios e criação de dashboards para apoio à tomada de decisão.

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* OpenPyXL
* Microsoft Excel
* Matplotlib
* Power BI


---

## 📂 Estrutura do Projeto

```text
automacao_excel_pedidos/
│
├── data/
│   └── saida/
│       ├── base_powerbi.csv
│       └── relatorio_vendas.xlsx
│
├── logs/
│   └── execucao.log
│
├── PowerBI/
│   └── DashBoard.pbix
│
├── src/
│   ├── config.py
│   ├── dashboard.py
│   ├── formatador.py
│   ├── logger.py
│   ├── main.py
│   ├── processador.py
│   └── vendas.csv
│
└── .gitignore
```

---

## ⚙️ Funcionalidades

* Leitura de dados de vendas em CSV
* Limpeza e tratamento dos dados
* Remoção de registros duplicados
* Conversão e padronização de datas
* Geração automática de KPIs
* Criação de relatório Excel formatado
* Exportação de base para Power BI
* Geração de gráficos e dashboards

---

## 📈 Indicadores Gerados

* Faturamento Total
* Total de Pedidos
* Clientes Únicos
* Total de Produtos Diferentes
* Produto com Maior Faturamento
* Categoria Líder
* Região com Mais Vendas
* Top Cliente
* Receita por Cliente
* Ticket Médio por Pedido
* Ticket Médio
* Maior Venda

---

## 📊 Dashboard Power BI

O dashboard foi dividido em três páginas:

### Página 1 - Visão Geral

* Faturamento por Categoria
* Faturamento por Subcategoria
* Top 10 Produtos
* Top 10 Clientes
* Indicadores principais

### Página 2 - Análise Temporal

* Faturamento ao longo do tempo
* Vendas por mês
* Clientes ao longo do tempo
* Faturamento por modo de envio

### Página 3 - Clientes e Logística

* Clientes por Região
* Quantidade de Pedidos por Modo de Envio
* Distribuição de clientes
* Indicadores complementares

---

## ▶️ Como Executar

Instale as dependências:

```bash
pip install pandas openpyxl matplotlib
```

Execute o projeto:

```bash
python src/main.py
```

Os arquivos gerados ficarão na pasta:

```text
data/saida/
```

---

## 📷 Screenshots

### Dashboard Python



### Dashboard Power BI - Página 1

<img width="565" height="317" alt="Captura de tela 2026-06-06 222730" src="https://github.com/user-attachments/assets/3078f041-1c1e-46fe-8fc2-f5a942790fbf" />


### Dashboard Power BI - Página 2

<img width="565" height="317" alt="Captura de tela 2026-06-06 222826" src="https://github.com/user-attachments/assets/8812d42d-23cd-48bb-b8e7-c9ab3f4fdd10" />


### Dashboard Power BI - Página 3

<img width="175" height="294" alt="Captura de tela 2026-06-06 223339" src="https://github.com/user-attachments/assets/a5c0a7f3-e2fe-408e-94c6-a1386b41a1f8" />


---

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para estudos de Python, análise de dados e Business Intelligence.
