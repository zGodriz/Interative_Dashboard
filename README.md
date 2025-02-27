# 📊 Dashboard de Faturamento

Este é um projeto de **Dashboard Interativo** desenvolvido com **Streamlit** e **Plotly**, que permite visualizar o faturamento de uma empresa com base em dados extraídos de um arquivo CSV. O painel apresenta métricas e gráficos que auxiliam na análise financeira.

## 🚀 Tecnologias Utilizadas

- **Python 3** - Linguagem principal do projeto.
- **Streamlit** - Framework para criação de dashboards interativos.
- **Pandas** - Manipulação e tratamento de dados.
- **Plotly** - Visualização de dados com gráficos dinâmicos.

## 📂 Estrutura do Projeto

```
📁 Dashboard
│-- 📄 dashboard.py  # Código principal
│-- 📄 empresa_invoicesnew.csv  # Base de dados
│-- 📄 README.md  # Documentação do projeto
```

## 📊 Funcionalidades

✔️ Filtro de faturamento por mês via sidebar.<br>
✔️ Gráfico de barras para visualizar faturamento diário.<br>
✔️ Gráfico de barras para faturamento por categoria de produto.<br>
✔️ Gráfico de pizza para distribuição de faturamento por tipo de pagamento.<br>
✔️ Gráfico de dispersão para análise da tendência de faturamento.<br>
✔️ Indicador de faturamento total no mês selecionado.<br>

## 🛠 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd Dashboard
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o dashboard:
   ```bash
   streamlit run dashboard.py
   ```

6. Acesse no navegador o endereço exibido, geralmente `http://localhost:8501/`.

---




