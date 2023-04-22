import openai
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Defina sua chave API da OpenAI
openai.api_key = "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"

# Crie uma função para enviar uma pergunta para o ChatGPT e receber a resposta
def ask_chatbot(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Inicialize o navegador e abra uma página de bate-papo
driver = webdriver.Chrome()
driver.get("https://www.exemplo.com/chat")

# Aguarde a página carregar
time.sleep(5)

# Envie uma pergunta para o ChatGPT
question = "Qual é a previsão do tempo para amanhã?"
response = ask_chatbot(question)

# Insira a resposta na caixa de texto do bate-papo e envie
textbox = driver.find_element_by_id("chat-input")
textbox.send_keys(response)
textbox.send_keys(Keys.RETURN)

# Aguarde a resposta ser exibida no bate-papo
time.sleep(5)

# Repita os passos anteriores para enviar mais perguntas e receber respostas do ChatGPT

# Feche o navegador
driver.quit()
