# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
1. Instale as dependências

```pip install -r requirements.txt```

2. Certifique-se de que o Ollama esteja disponível

Verifique os modelos instalados:

```ollama list```

3. Inicie o serviço do Ollama, se necessário

```ollama serve```

4. Execute o FIN.AI

Em outro terminal:

```python -m streamlit run ./src/app.py```

O Streamlit exibirá no terminal o endereço local para acessar a interface do agente.

📦 Dependências

Exemplo do arquivo requirements.txt:

Plain Text
streamlit
pandas
requests
```
