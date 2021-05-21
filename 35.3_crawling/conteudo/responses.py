"""Faz as requisições pras urls e retorna as respostas"""
import time
import requests
from requests.exceptions import HTTPError, ReadTimeout

def make_requests(urls):
    # Faz as requisições, se possível, e retorna as respostas bem sucedidas
    # time.sleep pra esperar 1 segundo entre cada requisição, não atrapalha o site, educação
    time.sleep(1)
    responses = []
    
    for url in urls:
        # e se der erro na requisição? try...except...
    
        # se demorar pra receber resposta, se der um ReadTimeout, passa pro próximo, 
        # "desiste dessa url e segue adiante"
        try:
            response = requests.get(url, timeout=3)
        except ReadTimeout:
            continue
        
        # caso dê um erro de http, ou seja, status 400, 500, etc
        try:
            # raise_for_status traz o erro, sem ele o requests só retorna <Erro 404> como se fosse ok
            response.raise_for_status()
        except HTTPError:
            continue # para aqui e vai pra próxima iteração, não faz mais nada
            
        responses.append(response)
    return responses

# pra cada url tenta dar um get. 
# Se não conseguir, vai pra pŕoxima.
# se conseguir, testa o status
# se for 400, 500, passa pra próxima
# se for 200, joga a url no responses[]
