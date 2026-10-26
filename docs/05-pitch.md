Pitch - FIN.AI



**O problema**
Organizar e interpretar informações financeiras pode ser uma tarefa complexa. Muitas vezes, uma pessoa possui dados sobre renda, gastos, objetivos e investimentos, mas encontra dificuldade para transformar essas informações em uma visão clara da própria situação financeira.

**A solução**
O FIN.AI é um assistente virtual financeiro criado para apoiar usuários na compreensão e organização de suas finanças pessoais.

O agente utiliza informações disponíveis em uma base de conhecimento para fornecer respostas claras, acessíveis e contextualizadas, considerando dados como perfil financeiro, transações, objetivos, histórico de atendimento e produtos financeiros disponíveis.

**Como funciona**
A pessoa interage com o FIN.AI por meio de uma interface desenvolvida em Streamlit.

A pergunta é combinada com o System Prompt e com o contexto proveniente das bases de conhecimento.

O modelo de inteligência artificial é executado localmente através do Ollama e gera uma resposta seguindo as regras definidas para o agente.

**Fluxo simplificado:**

Usuário 
  ↓ 
Interface Streamlit 
  ↓ 
Pergunta 
  ↓ 
System Prompt + Base de Conhecimento 
  ↓ 
Modelo de IA via Ollama 
  ↓ 
Resposta contextualizada do FIN.AI

**Segurança e confiabilidade**
Um dos principais objetivos do FIN.AI é reduzir respostas inventadas.

**O agente foi orientado a:**

utilizar somente as informações disponíveis na base de conhecimento;
não inventar valores, transações ou produtos financeiros;
reconhecer quando não possui informações suficientes;
respeitar o escopo de finanças pessoais;
não garantir rentabilidade de produtos financeiros;
considerar o perfil financeiro do cliente antes de contextualizar uma resposta.
Validação
O agente foi testado em quatro cenários principais:

**Consulta de gastos;**
Recomendação contextualizada de produto financeiro;
Pergunta fora do escopo;
Solicitação de informação inexistente.
Os testes buscaram avaliar a utilização correta da base de conhecimento, coerência com o perfil do cliente, controle de escopo e prevenção de respostas inventadas.

**Pontos de melhoria**
O principal ponto identificado para evolução é o tempo de resposta.

Atualmente, o FIN.AI utiliza um modelo de IA executado localmente através do Ollama. Dessa forma, o processamento depende dos recursos computacionais disponíveis na máquina e pode apresentar maior tempo de resposta.

Como evolução futura, poderia ser avaliada a integração com um modelo disponibilizado através de API em nuvem, buscando maior desempenho e escalabilidade.

**Conclusão**
O FIN.AI demonstra, por meio de um protótipo funcional, como Inteligência Artificial Generativa pode ser combinada com dados estruturados, engenharia de prompts e regras de segurança para apoiar usuários na compreensão de informações financeiras.

Além da construção do agente, o projeto possibilitou explorar conceitos como bases de conhecimento, prompts, integração com modelos locais, desenvolvimento de interfaces com Streamlit e avaliação de respostas de sistemas de IA.
