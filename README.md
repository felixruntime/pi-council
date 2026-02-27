# 🥧 Pi 5 Council: Agent Debate

> **6 AI Agents. 3 Open-Source Models. 1 Raspberry Pi 5. No Consensus.**

This project is a multi-agent debate system running 100% locally on a **Raspberry Pi 5 (16GB RAM)**. The goal? To pit six AI specialists against each other to analyze the **FIAP**  curriculum and decide which "end-to-end" practical project should be built first on this specific hardware.

---

## 🔬 The Experiment
We fed the same strategic question to 6 specialized agents across 3 different LLM models, all running via **Ollama**. No cloud, no API keys, no external dependencies.

**The Question:**
> *"Based on the FIAP AI curriculum, what should be the first practical end-to-end project to be developed on a Raspberry Pi 5 16GB?"*

### 🤖 The Agents
Each agent brings a unique technical perspective to the debate:

| Agent | Focus | Expertise |
| :--- | :--- | :--- |
| **ML Engineer** | Machine Learning & Data Science | Pipelines, statistical models, and data integrity |
| **Deep Learning Architect** | Neural Networks & GenAI | Model architectures, Fine-tuning, and TFLite |
| **NLP Specialist** | Natural Language & Agents | Chatbots, RAG, and language processing |
| **Vision Engineer** | Computer Vision | Object detection, OpenCV, and real-time processing |
| **Edge AI Specialist** | IoT & Embedded Systems | Hardware optimization, sensors, and GPIO |
| **AI Strategist** | Security & Governance | Business value, ethical AI, and deployment |

---

## 🧬 Models Benchmark
We tested the limits of the Raspberry Pi 5 using the most relevant "Edge-class" models:

| Model | Parameters | Quantization | Size |
| :--- | :--- | :--- | :--- |
| **Llama 3.2** | 3B | Q4_K_M | ~2.0 GB |
| **Qwen 2.5** | 3B | Q4_K_M | ~1.9 GB |
| **Phi 3.5** | 3.8B | Q4_K_M | ~2.4 GB |

---

## 📊 Results & Key Findings

### 1. Llama 3.2 — The Conservative
* **Behavior:** 5 out of 6 agents reached an "echo chamber" consensus (Computer Vision).
* **Verdict:** Safe, predictable, and technically sound.
* **Moderator Decision:** Image Classification.
* **Total Time:** 511 seconds.

### 2. Qwen 2.5 — The Creative
* **Behavior:** High diversity of ideas, but prone to "technical hallucinations" (e.g., suggested YOLO for reading text hashtags and GANs for NLP).
* **Verdict:** Visionary but requires human auditing.
* **Moderator Decision:** AI Social Assistant.
* **Total Time:** **342 seconds** (The fastest).

### 3. Phi 3.5 — The Academic
* **Behavior:** Extremely dense and structured responses (+400 words per agent).
* **Critical Failure:** The Moderator suffered a **TIMEOUT** (+1200s) trying to synthesize the massive context.
* **Total Time:** 1200s+ (Crashed during synthesis).

> **💡 Insight:** Running a model is not intelligence. Knowing how to evaluate the output is. Llama played it safe, Qwen was unreliable, and Phi was too verbose for edge hardware. **The strategic decision-making remains human.**

---

## 🛠️ Hardware & Stack

* **Device:** Raspberry Pi 5 (16GB LPDDR4X)
* **Processor:** Broadcom BCM2712, ARM Cortex-A76 @ 2.4GHz
* **OS:** Raspberry Pi OS 64-bit (Bookworm)
* **Inference Engine:** Ollama (Local)

### Project Structure
```text
pi-council/
├── main.py                # Main orchestrator (entry point)
├── requirements.txt       # Dependencies (requests, pyfiglet, etc.)
├── .gitignore             # Ignore __pycache__ and local logs
├── agents/
│   ├── __init__.py        # Makes agents a Python package
│   ├── config.py          # Model selection, Timeouts, and API URLs
│   ├── context.py         # FIAP Curriculum and Pi5 hardware data
│   ├── prompts.py         # System prompts for the 6 specialized personas
│   └── council.py         # Logic for API calls and debate flow
└── benchmarks/            # Raw .txt logs for model comparison
    ├── llama3.2-3b.txt
    ├── qwen2.5-3b.txt
    └── phi3.5.txt
````

## 🚀 Quick Start

### 1. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Pull the Models
```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull phi3.5
```

### 3. Clone and Run
```bash
git clone https://github.com/felixruntime/pi-council.git
cd pi-council
pip install -r requirements.txt
python3 main.py "Your question"
```

---

## 🎯 Conclusion

This experiment demonstrates that while multi-agent systems are powerful for analysis, technical curation and strategic direction are still the "human-in-the-loop" differentiator.

> **Insight:** Running a model is not intelligence; knowing how to evaluate and orchestrate the output is.

---

## 🛠️ Built With

- **Python** — Orchestration & Logic
- **Ollama** — Local LLM Runtime
- **Raspberry Pi 5** — Edge Computing Hardware

---