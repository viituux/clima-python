# 🌦️ Dashboard de Clima em Tempo Real

> Primeiro projeto da jornada Full Stack Python. Uma aplicação web para consultar condições meteorológicas atuais e manter um histórico de pesquisas.

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## 💻 Sobre o Projeto

Este projeto é um Dashboard de Clima desenvolvido durante meus estudos de Análise e Desenvolvimento de Sistemas. O objetivo foi aplicar conceitos fundamentais de desenvolvimento web com Python, integrando **Frontend**, **Backend**, **Banco de Dados** e **APIs Externas**.

A aplicação permite:
- Buscar o clima de qualquer cidade do mundo em tempo real.
- Visualizar temperatura, velocidade do vento e condições climáticas.
- Salvar automaticamente o histórico de buscas em um banco de dados local.

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Backend:** Python 3.12, Flask
- **Banco de Dados:** SQLite, SQLAlchemy (ORM)
- **Frontend:** HTML5, CSS3 (Bootstrap 5), Jinja2
- **API Externa:** Open-Meteo (Geocoding e Weather Forecast)
- **Controle de Versão:** Git e GitHub

## ⚙️ Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)** simplificado:
1. **Model:** Definição da tabela `Historico` usando SQLAlchemy.
2. **View:** Templates HTML renderizados pelo Jinja2.
3. **Controller:** Rotas do Flask (`app.py`) e lógica de negócios (`previcao.py`).

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/). Além disso, é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

### Passo a passo

```bash
# Clone este repositório
$ git clone [https://github.com/SEU_USUARIO/portfolio-clima-python.git](https://github.com/SEU_USUARIO/portfolio-clima-python.git)

# Acesse a pasta do projeto no terminal/cmd
$ cd portfolio-clima-python

# Instale as dependências
$ pip install -r requirements.txt

# Execute a aplicação
$ python app.py
