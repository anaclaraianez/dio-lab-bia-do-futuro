
## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$570 - O agente deve consultar transacoes.csv, identificar as transações da categoria alimentação e informar o valor com base exclusivamente nos dados disponíveis.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** O agente deve considerar o perfil financeiro e os objetivos do cliente e apresentar somente um produto compatível disponível em produtos_financeiros.json, sem garantir rentabilidade.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** O agente deve informar educadamente que o FIN.AI é especializado em educação e organização financeira e que previsão do tempo está fora do seu escopo.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** O agente deve informar que não possui informações suficientes sobre o produto XYZ na base de conhecimento e não deve inventar rendimento ou características.
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O FIN.AI conseguiu utilizar as bases de conhecimento para responder perguntas financeiras de forma contextualizada e coerente com o perfil do cliente.
-O agente respeitou as regras definidas no System Prompt, mantendo uma comunicação clara e acessível.
-As respostas permaneceram dentro do escopo de finanças pessoais.
-O agente reconheceu quando uma informação não estava disponível, evitando criar dados inexistentes.
-A integração entre os arquivos de dados, o modelo local via Ollama e a interface em Streamlit funcionou conforme a proposta do projeto.

**O que pode melhorar:**
- Otimizar o tempo de resposta. Como o FIN.AI utiliza um modelo executado localmente via Ollama, o processamento depende dos recursos da máquina e pode ser mais lento. Futuramente, a integração com uma API de IA em nuvem pode melhorar a velocidade e a escalabilidade.

---

