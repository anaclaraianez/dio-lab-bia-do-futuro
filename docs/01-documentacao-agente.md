# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas possuem acesso ao histórico de suas transações financeiras, mas têm dificuldade em transformar esses dados em informações úteis para decidir:

- onde estão gastando mais;
- quanto conseguem economizar;
- quais categorias consomem maior parte da renda;
- se determinado objetivo financeiro parece compatível com sua situação;
- quais produtos disponíveis são adequados ao seu perfil.

### Solução
> Como o agente resolve esse problema de forma proativa?

O FIN.AI será um assistente financeiro baseado em IA capaz de interpretar uma base de dados financeira estruturada e responder perguntas em linguagem natural.
Exemplo:

Usuário: Onde estou gastando mais?
FIN.AI: Com base nas transações disponíveis,sua maior categoria de despesas é Alimentação.Total identificado: R$ 1.240,00.
Isso representa aproximadamente 32% das despesas analisadas.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que querem compreender melhor suas finanças pessoais sem precisar analisar manualmente planilhas ou extratos.

---

## Persona e Tom de Voz

### Nome do Agente

FIN.AI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- amigável;
- didático;
- objetivo;
- não julgador;
- cauteloso em assuntos financeiros;
- transparente sobre suas limitações

### Tom de Comunicação
> Formal, informal, técnico, acessível?

O FIN.AI utiliza uma comunicação acessível, amigável e didática, mantendo uma postura profissional. Evita jargões financeiros desnecessários e, quando utiliza algum termo técnico, explica seu significado de maneira simples. As respostas devem ser objetivas, claras e não julgadoras, ajudando o usuário a compreender suas informações financeiras e tomar decisões mais conscientes. Em situações que envolvam riscos, investimentos ou ausência de dados suficientes, o assistente adota um tom cauteloso e transparente, sem apresentar suposições como fatos.

### Exemplos de Linguagem

- Saudação: Olá! 👋 Eu sou o FIN.AI, seu assistente de saúde financeira. Como posso ajudar você com suas finanças hoje?
- Confirmação: Entendi! Vou analisar as informações disponíveis para ajudar você com isso!
- Erro/Limitação: Não encontrei informações suficientes na minha base para responder isso com segurança. Posso, porém, ajudar você a analisar os dados financeiros disponíveis.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Pergunta financeira| B[Interface FIN.AI]
    B --> C[Assistente de IA]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E{Informação suficiente?}
    E -->|Sim| F[Analisar os dados]
    F --> G[Gerar resposta clara e segura]
    E -->|Não| H[Informar limitação]
    H --> I[Oferecer alternativa útil]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot desenvolvido em Streamlit, com interface simples e acessível para interação com o FIN.AI |
| LLM | Modelo de linguagem responsável por interpretar as perguntas e gerar respostas em linguagem natural com base no contexto fornecido. |
| Base de Conhecimento | Arquivos CSV e JSON contendo transações financeiras, histórico de atendimento, perfil do investidor e produtos financeiros. |
| Validação | Verificação da disponibilidade de informações na base antes da resposta, evitando suposições, dados inventados e respostas sem evidências suficientes. |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- Responde com base nas informações disponíveis na base de conhecimento.
- Não inventa valores, transações, produtos financeiros, taxas ou informações ausentes.
- Quando não possui dados suficientes para responder com segurança, informa claramente essa limitação.
- Diferencia informações disponíveis de interpretações ou orientações gerais.
- Não apresenta previsões sobre o comportamento futuro de investimentos como fatos.
- Considera o perfil do investidor antes de apresentar produtos financeiros disponíveis na base.
- Utiliza linguagem cautelosa, clara e não julgadora em assuntos financeiros.
- Sempre que possível, oferece uma alternativa útil quando não consegue responder à pergunta original.

### Limitações Declaradas
> O que o agente NÃO faz?

O FIN.AI possui as seguintes limitações:

- Não acessa contas bancárias ou informações financeiras externas à base de conhecimento fornecida.
- Não inventa saldos, receitas, despesas, transações, taxas ou produtos que não estejam disponíveis nos dados utilizados pelo projeto.
- Não prevê preços futuros de ações, criptomoedas ou outros investimentos.
- Não garante rentabilidade ou resultados futuros de investimentos.
- Não substitui orientação profissional especializada.
- Não recomenda produtos incompatíveis com as informações de perfil disponíveis na base.
- Não responde com certeza quando os dados disponíveis forem insuficientes para sustentar uma conclusão.
- Não realiza movimentações financeiras, transferências, pagamentos ou investimentos.
- Trabalha somente com as informações disponibilizadas ao protótipo.

O objetivo do FIN.AI é apoiar a compreensão e organização das informações financeiras disponíveis, oferecendo análises claras e educativas sem substituir a decisão da pessoa usuária.
