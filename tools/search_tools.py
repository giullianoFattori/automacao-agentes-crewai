import requests
import json
import os
from langchain.tools import tool


class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """Útil para pesquisar na Internet sobre um determinado tópico e retornar resultados relevantes"""
        top_result_to_return = 4
        url = "https://google.serper.dev//search"
        payload = json.dumps({"q": query})
        header = { 'x-api-key': os.environ['SERPER_API_KEY'], 'content-type': 'application/json'}
        response = requests.request("POST", url, headers=header, data=payload)
        if 'organic' not in response.json():
            return 'Desculpe, não consegui encontrar nada sobre isso. Pode haver um erro com sua chave de API do Serper'
        else:
            result = response.json()['organic']
            string = []
            for result in result[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n----------------"
                    ]))
                except KeyError:
                    next
            return '\n'.join(string)