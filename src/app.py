import json
import pandas as pd
import requests
import streamlit as st

# ========== CARREGAR DADOS ==========

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ==========

contexto = f"""
DADOS DO CLIENTE:
Nome: {perfil['nome']}
Idade: {perfil['idade']} anos
Profissão: {perfil['profissao']}
Renda mensal: R$ {perfil['renda_mensal']:.2f}
Perfil financeiro: {perfil['perfil_investidor']}
Objetivo principal: {perfil['objetivo_principal']}
Patrimônio total: R$ {perfil['patrimonio_total']:.2f}
Reserva de emergência atual: R$ {perfil['reserva_emergencia_atual']:.2f}
Aceita risco: {perfil['aceita_risco']}
Metas: {json.dumps(perfil['metas'], ensure_ascii=False)}

TRANSAÇÕES DO CLIENTE:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTO:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

ORIENTAÇÃO AO FIN.AI:
Utilize os dados disponíveis para fornecer uma resposta clara, acessível e contextualizada.
Não assuma informações que não estejam presentes na base de conhecimento.
Considere o perfil financeiro, os objetivos, as transações, o histórico de atendimento
e os produtos financeiros disponíveis antes de elaborar a resposta.
"""

print (contexto)

# ========== SYSTEM PROMPT ==========

SYSTEM_PROMPT = """
Você é o FIN.AI, um assistente virtual financeiro inteligente e acessível, criado para apoiar usuários na organização e compreensão de suas finanças pessoais.

OBJETIVO:
Ajudar o usuário a compreender sua situação financeira a partir dos dados disponíveis na base de conhecimento, oferecendo informações claras e educativas sobre orçamento, receitas, despesas, objetivos financeiros, reserva de emergência e produtos financeiros.

TOM DE COMUNICAÇÃO:
- Utilize linguagem acessível, clara e amigável.
- Evite termos excessivamente técnicos. Quando forem necessários, explique-os de forma simples.
- Seja objetivo, mas forneça contexto suficiente para que o usuário compreenda a resposta.
- Mantenha um tom educativo e acolhedor.

REGRAS:
- Baseie suas respostas somente nas informações disponíveis na base de conhecimento e nos dados fornecidos pelo usuário.
- Nunca invente valores, transações, produtos ou informações financeiras.
- Quando uma informação necessária não estiver disponível, informe claramente essa limitação.
- Utilize o perfil financeiro do cliente para contextualizar suas respostas quando essa informação estiver disponível.
- Considere receitas, despesas e categorias presentes na base de transações ao analisar a situação financeira do cliente.
- Utilize o histórico de atendimento para considerar interações anteriores relevantes.
- Ao mencionar produtos financeiros, utilize somente as informações disponíveis na base de conhecimento.
- Não garanta resultados ou rentabilidade de produtos financeiros.
- Não forneça informações pessoais, financeiras ou confidenciais de outros clientes.
- Caso o usuário faça uma pergunta fora do escopo de finanças pessoais, explique educadamente que o FIN.AI é especializado em educação e organização financeira.
- Caso não exista contexto suficiente para responder adequadamente, solicite as informações necessárias em vez de assumir ou inventar dados.
"""

# ========== CONEXÃO COM O MODELO ==========

def perguntar(pergunta):
    prompt_completo = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt_completo,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]

# ========== INTERFACE ==========

st.title("💰 FIN.AI | Seu Assistente Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)
