import openai
import json
import re


class GeradorMonstro:
    def __init__(self, api_key):
        openai.api_key = api_key

    def montar_prompt(self, genero_input, nome_input, raca_input, tamanho_input, alinhamento_input):
        self.prompt = f"""Gere em pt-br a descrição longa e detalhada de um monstro de RPG de mesa com as seguintes informações:
                    Name: {nome_input}
                    Race: {raca_input}
                    Size: {tamanho_input}
                    Alignment: {alinhamento_input}
                    Gender: {genero_input}"""
    def gerar_descricao(self):
        response=openai.Completion.create(
                                            model='text-davinci-003',
                                            prompt= self.prompt,
                                            max_tokens=2000
                    )
        resposta_raw = json.loads(str(response))['choices'][0]['text']
        resposta = max(re.findall("(.+?)(?:\n|\r|$)", resposta_raw), key=len) #Pegando o maior parágrafo, consertando o erro de completar respostas
        self.descricao = resposta.strip()
        return self.descricao
    def gerar_imagem(self):
        tldr = '\n\nTl;dr'
        response = openai.Image.create(
                                    prompt=f"""Monstro de RPG de mesa estilo portrait 2d medieval rpg anime black and white art.
                                    Aparência: {self.descricao+tldr}""",
                                    n=1,
                                    size="256x256"
                                    )
        image_url = response['data'][0]['url']
        self.imagem = f"""![Foo]({image_url})"""
        return self.imagem
    def gerar_resposta(self):
        self.gerar_descricao()
        self.gerar_imagem()
        return self.imagem + self.descricao
