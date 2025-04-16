
# ⛽ Análise de Vendas de Combustíveis no Brasil (2012–2025)

Este projeto é um **dashboard interativo em Streamlit** que analisa os dados públicos da ANP (Agência Nacional do Petróleo) sobre o volume de vendas de combustíveis no Brasil entre os anos de 2012 a 2025.

![streamlit-app](https://img.shields.io/badge/streamlit-app-red?logo=streamlit)
![pandas](https://img.shields.io/badge/pandas-dataframe-blue?logo=pandas)
![status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 📊 Funcionalidades

✅ Visualização interativa do volume de vendas por tipo de combustível  
✅ Seleção por produto diretamente na sidebar  
✅ Gráfico temporal das vendas (m³) no Brasil  
✅ Processamento automático de datas e valores  
✅ Fácil de rodar localmente com Streamlit

---

## 📁 Estrutura do Projeto

```
analise-vendas-combustivel/
│
├── data/
│   └── vendas-combustivel.csv          # Dados brutos da ANP
│
├── app.py                              # Aplicação Streamlit principal
├── requirements.txt                    # Dependências do projeto
└── README.md                           # Este arquivo lindo aqui 💅
```

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gblzera/data_project.git
cd data_project
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o app Streamlit 🎉

```bash
streamlit run app.py
```

---

## 📷 Preview

<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" alt="Streamlit Preview" width="250px">

> Interface intuitiva, com seleção de produto e visualização rápida de tendências ao longo do tempo.

---

## 📌 Fonte dos Dados

- [ANP - Agência Nacional do Petróleo, Gás Natural e Biocombustíveis](https://www.gov.br/anp/)

---

## 🧑‍💻 Autor

Feito com carinho por [gblzera](https://github.com/gblzera) 💙  
Colaborações e sugestões são muito bem-vindas!

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
