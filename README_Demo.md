# Agentic Prompts Local Demo

A Streamlit demo application that turns every Markdown prompt in the `prompts/` folder into a selectable AI agent.

It is designed for local OpenAI-compatible endpoints such as:

- LM Studio: `http://localhost:1234/v1`
- vLLM: `http://localhost:8000/v1`
- Ollama OpenAI compatibility: `http://localhost:11434/v1`
- Any OpenAI-compatible gateway or proxy

---

## What This Demo Does

This app lets you:

- Select a prompt-agent from your curated prompt catalog
- Run it against your local OpenAI-compatible endpoint
- Provide code, logs, requirements, architecture notes, or any text input
- Generate structured Markdown output
- Download the result as a Markdown file
- Reuse the same UI for debugging, refactoring, code review, security review, DevOps, MLOps, documentation, and testing agents

---

## Project Structure

```text
agentic-prompts-local-demo/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── __init__.py
│   ├── agent_factory.py
│   ├── prompt_loader.py
│   └── sample_inputs.py
└── prompts/
    ├── application-development/
    ├── architecture/
    ├── refactoring/
    ├── code-review/
    ├── debugging/
    ├── security/
    ├── devops/
    ├── mlops/
    ├── documentation/
    ├── testing/
    └── agents/
```

---

## Quick Start

### 1. Create Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_API_KEY=local-demo-key
OPENAI_MODEL=your-local-model-name
```

For LM Studio, the model name must match the served model name shown in the LM Studio server UI.

For vLLM, use the model name exposed by your vLLM server.

### 4. Run the App

```bash
streamlit run app.py
```

---

## How to Use

1. Open the Streamlit UI.
2. Configure:
   - Base URL
   - API key
   - Model ID
3. Select a prompt category.
4. Select an agent prompt.
5. Paste your input.
6. Click **Run Agent**.
7. Download the generated Markdown result if needed.

---

## Example Local Endpoints

### LM Studio

```env
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_API_KEY=lm-studio
OPENAI_MODEL=local-model
```

### vLLM

```env
OPENAI_BASE_URL=http://localhost:8000/v1
OPENAI_API_KEY=vllm-local
OPENAI_MODEL=Qwen/Qwen3-32B
```

### Ollama OpenAI-Compatible API

```env
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_API_KEY=ollama
OPENAI_MODEL=qwen2.5-coder:latest
```

---

## Notes

- Some local models may not follow large prompts perfectly.
- For best results, use instruction-tuned models.
- For codebase work, paste focused context or connect this app later with repository readers.
- This demo intentionally keeps tools disabled by default so it works in offline/local environments.
- You can add MCP tools later using the same pattern from your travel-planner example.

---

## Next Suggested Improvements

- Add file upload support for code/logs
- Add repository scanner
- Add MCP tools for filesystem, Git, GitHub, and web search
- Add prompt result history
- Add multi-agent workflows
- Add structured output validation
- Add export to GitHub issue or pull request comment
