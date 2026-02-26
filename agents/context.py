import json

FIAP_CURRICULUM_DATA = {
    "curso": "Tecnólogo em Inteligência Artificial - FIAP",
    "ano_1": {
        "sistemas": "AI Computer Systems & Sensors, Raspberry Pi, ESP32",
        "dados": "Cognitive Data Science, Statistical Computing (R & Python)",
        "modelagem": "Machine Learning & Modelling, Redes Neurais & Deep Learning",
        "seguranca_cloud": "Cognitive Cybersecurity, Cloud Computing"
    },
    "ano_2": {
        "ia_avancada": "Generative AI & Advanced Nets, NLP & Chatbots",
        "visao_robotica": "Visão Computacional, IoT & Robotics",
        "automacao_negocios": "AI for RPA, Governança em IA & Business Analytics"
    }
}

PI5_HARDWARE_DATA = {
    "modelo": "Raspberry Pi 5",
    "cpu": "Quad-core ARM Cortex-A76 @ 2.4GHz",
    "memoria": "16GB LPDDR4X",
    "ia_local": {
        "engine": "Ollama",
        "modelo": "Qwen 2.5 3B",
        "capacidade_max": "Modelos até 7B (Quantização Q4)"
    },
    "perifericos": ["Câmera", "Microfone", "Sensores", "GPIO"]
}

FIAP_CURRICULUM = json.dumps(FIAP_CURRICULUM_DATA, indent=2, ensure_ascii=False)
PI5_SPECS = json.dumps(PI5_HARDWARE_DATA, indent=2, ensure_ascii=False)