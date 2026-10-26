💰 FIN.AI | Assistente Virtual Financeiro com Inteligência Artificial


📌 Sobre o Projeto

O FIN.AI é um assistente virtual financeiro desenvolvido como parte do desafio "Construa Seu Assistente Virtual Com Inteligência Artificial".

O objetivo do projeto é demonstrar, de forma prática, como a Inteligência Artificial Generativa pode utilizar uma base de conhecimento estruturada para fornecer respostas contextualizadas, claras e seguras.

O FIN.AI apoia o usuário na compreensão de suas finanças pessoais, considerando informações como perfil financeiro, transações, objetivos, histórico de atendimento e produtos financeiros disponíveis.

🎯 Objetivo

Criar um protótipo funcional de um assistente financeiro capaz de:

Responder dúvidas sobre a situação financeira do usuário;
Consultar informações disponíveis em uma base de conhecimento;
Considerar o perfil financeiro do cliente;
Apoiar a interpretação de receitas, despesas e objetivos;
Apresentar produtos financeiros disponíveis na base quando aplicável;
Evitar respostas inventadas;
Reconhecer quando não possui informações suficientes;
Manter as respostas dentro do escopo de finanças pessoais.

🤖 Como o FIN.AI Funciona

O usuário interage com o FIN.AI através de uma interface desenvolvida em Streamlit.

A pergunta é combinada com:

System Prompt do agente;
Perfil financeiro do cliente;
Histórico de transações;
Histórico de atendimento;
Produtos financeiros disponíveis.
Essas informações são enviadas para um modelo de linguagem executado localmente através do Ollama.

Fluxo simplificado:

Usuário
↓
Interface Streamlit
↓
Pergunta
↓
System Prompt + Contexto
↓
Base de Conhecimento
↓
Modelo de IA via Ollama
↓
Resposta do FIN.AI

🧠 Base de Conhecimento

O FIN.AI utiliza quatro fontes principais de informação:

perfil_investidor.json
Contém informações sobre o cliente, como perfil financeiro, renda, patrimônio, objetivos e reserva de emergência.

transacoes.csv
Contém as transações utilizadas pelo agente para interpretar receitas, despesas e categorias de gastos.

historico_atendimento.csv
Fornece contexto sobre interações anteriores disponíveis para o agente.

produtos_financeiros.json
Contém os produtos financeiros que podem ser considerados pelo FIN.AI durante as respostas.

🛡️ Segurança e Confiabilidade

Uma das principais preocupações do projeto é reduzir respostas inventadas ou sem fundamento nos dados disponíveis.

Por isso, o FIN.AI foi orientado a:

Não inventar valores, transações ou produtos;
Utilizar as informações presentes na base de conhecimento;
Informar quando não possui contexto suficiente;
Não garantir resultados ou rentabilidade de produtos financeiros;
Respeitar o escopo de finanças pessoais;
Não fornecer informações confidenciais de outros clientes;
Considerar o perfil financeiro disponível antes de contextualizar respostas.

💬 Exemplo de Uso
Pergunta:

Quanto gastei com alimentação?

O FIN.AI consulta os dados disponíveis em transacoes.csv e utiliza essas informações para elaborar a resposta.

Outro exemplo:

Qual investimento você recomenda para mim?

Nesse cenário, o agente considera o perfil financeiro disponível e os produtos cadastrados na base de conhecimento antes de elaborar a resposta.

🧪 Testes Realizados

O agente foi avaliado em diferentes cenários.

Teste 1 - Consulta de gastos
Pergunta:
"Quanto gastei com alimentação?"

Objetivo:
Validar se o agente utiliza corretamente os dados disponíveis em transacoes.csv.

Teste 2 - Produto financeiro
Pergunta:
"Qual investimento você recomenda para mim?"

Objetivo:
Verificar se a resposta considera o perfil financeiro do cliente e os produtos disponíveis na base.

Teste 3 - Pergunta fora do escopo
Pergunta:
"Qual a previsão do tempo?"

Objetivo:
Verificar se o FIN.AI reconhece que a solicitação está fora do seu escopo.

Teste 4 - Informação inexistente
Pergunta:
"Quanto rende o produto XYZ?"

Objetivo:
Avaliar se o agente reconhece a ausência da informação em vez de criar uma resposta inexistente.

✅ O que Funcionou Bem

O agente respondeu de forma clara e contextualizada utilizando as informações das bases de conhecimento;
O FIN.AI respeitou o perfil financeiro do cliente e as regras definidas no System Prompt;
Perguntas fora do escopo e informações inexistentes foram tratadas adequadamente durante os testes;
A integração das bases de dados com o modelo de IA e a interface permitiu criar um protótipo funcional do assistente.

🔧 Tecnologias Utilizadas

Python
Streamlit
Pandas
Requests
JSON
CSV
Ollama
Modelo de linguagem local

📁 Estrutura do Projeto

fin-ai/
│
├── data/
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
│
├── docs/
│   ├── documentação do agente
│   ├── prompts
│   ├── testes
│   └── pitch
│
├── src/
│   └── app.py
│
├── requirements.txt
└── README.md
