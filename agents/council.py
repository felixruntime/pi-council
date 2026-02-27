import requests
import json
import time
import datetime
import pyfiglet
import os
from .config import OLLAMA_URL, MODEL, TEMPERATURE, NUM_CTX
from .prompts import AGENTS, MODERATOR_PROMPT
from .context import FIAP_CURRICULUM, PI5_SPECS

def query_ollama(system_prompt, user_message):
    """Envia uma requisição para a API do Ollama e retorna a resposta processada."""
    # Integração dos contextos estruturados e instruções do sistema 
    full_prompt = (
        f"SYSTEM: {system_prompt}\n\n"
        f"CONTEXTO - CURRÍCULO FIAP:\n{FIAP_CURRICULUM}\n\n"
        f"CONTEXTO - HARDWARE:\n{PI5_SPECS}\n\n"
        f"PERGUNTA: {user_message}"
    )
    
    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "num_ctx": NUM_CTX,
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=1200)
        return response.json()["response"]
    except Exception as e:
        return f"[ERRO DE CONEXÃO: {e}]"

def run_council(question=None):
    """Executa a sessão completa: debate entre 6 agentes e síntese do moderador."""
    if question is None:
        question = (
            "Baseado no currículo da FIAP e nas capacidades do Raspberry Pi 5, "
            "qual deveria ser o próximo projeto para maximizar aprendizado e portfólio? "
            "Defenda sua posição com base na sua área de expertise."
        )

    responses = {}
    separator = "=" * 60

    banner = pyfiglet.figlet_format("PI COUNCIL", font="slant")
    
    print("\033[96m" + banner + "\033[0m")
    print("\033[92m" + "  Base de Conhecimento: Currículo FIAP | Hardware: Pi 5 16GB" + "\033[0m")
    print("-" * 65)
    print(f"\033[1mPergunta:\033[0m {question}\n")

    # Fase 1: Cada agente se pronuncia sequencialmente
    for key, agent in AGENTS.items():
        print(f"🤖 {agent['name'].upper()} ({agent['area']}) analisando...")
        start = time.time()
        
        response = query_ollama(agent["prompt"], question)
        
        elapsed = time.time() - start
        responses[key] = response
        
        print(f"{response}")
        print(f"[{elapsed:.1f}s]\n")

    # Fase 2: O Moderador sintetiza os argumentos e decide
    print(f"{separator}")
    print("⚖️  MODERADOR — DECISÃO FINAL")
    print(f"{separator}\n")

    synthesis_context = "Argumentos dos 6 especialistas da FIAP:\n\n"
    for key, agent in AGENTS.items():
        synthesis_context += f"{agent['name']} ({agent['area']}):\n{responses[key]}\n\n"

    start = time.time()
    final_decision = query_ollama(MODERATOR_PROMPT, synthesis_context)
    elapsed = time.time() - start

    print(final_decision)
    print(f"\n[{elapsed:.1f}s]")
    print(f"\n{separator}")
    print("  SESSÃO ENCERRADA")
    print(separator)

    output_dir = "benchmarks"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model_name = MODEL.replace(":", "-") 
    filename = f"{output_dir}/{model_name}_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"PERGUNTA: {question}\n")
        f.write("="*60 + "\n")
        for key, resp in responses.items():
            f.write(f"AGENTE: {key}\nRESPOSTA: {resp}\n\n")
        f.write("="*60 + "\n")
        f.write(f"DECISÃO FINAL:\n{final_decision}")
    
    print(f"\n✅ Benchmark salvo em: {filename}")