from senha import API_KEY
import requests
import json
import os


headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo-1106"

x = input()
question_text = x + '.txt'

caminho_arquivo = os.path.join('..', 'Questões/CodeForces', question_text)

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    mensagem_a_ser_enviada = arquivo.read()

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": 
                mensagem_a_ser_enviada
                }],
}

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data = body_mensagem)

resposta = requisicao.json()

conteudo_resposta = resposta.get("choices")[0].get("message").get("content")

arquivo_resposta = x + '-gpt.py'

with open(arquivo_resposta, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo_resposta)