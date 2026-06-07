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

### Página 1 - Indicadores Gerais

* Faturamento Total
* Total de Pedidos
* Clientes Únicos
* Ticket Médio por Pedido
* Ticket Médio
* Maior Venda

### Página 2 - Análise Temporal

* Faturamento ao Longo do Tempo
* Vendas por Mês
* Faturamento por Região
* Clientes ao Longo do Tempo
* Quantidade de Pedidos por Modo de Envio
* Faturamento por Modo de Envio

### Página 3 - Produtos, Categorias e Clientes

* Faturamento por Categoria
* Faturamento por Subcategoria
* Top 10 Clientes
* Clientes por Região
* Top 10 Produtos

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

<img width="364" height="284" alt="Captura de tela 2026-06-06 222341" src="https://github.com/user-attachments/assets/3d37b30a-3cc4-4145-b348-c052709cd0b5" />

### Dashboard Power BI - Página 2

<img width="565" height="317" alt="Captura de tela 2026-06-06 222730" src="https://github.com/user-attachments/assets/928b0c62-7a36-4390-8e5e-a42c3f882e7e" />

### Dashboard Power BI - Página 3

<img width="566" height="316" alt="Captura de tela 2026-06-06 225411" src="https://github.com/user-attachments/assets/968a3328-6d9e-41c4-9be1-3aa1997d059b" />

---

## 📊 Relatório Excel

Além do dashboard em Power BI, o projeto gera automaticamente um relatório em Excel contendo:


<img width="378" height="238" alt="Captura de tela 2026-06-06 222142" src="https://github.com/user-attachments/assets/1811a1b5-b426-47ca-b390-2d7811d8b398" />


## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para estudos de Python, análise de dados e Business Intelligence.
