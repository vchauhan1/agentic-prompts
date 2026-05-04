from __future__ import annotations

from datetime import datetime
from pathlib import Path
import os
import traceback

import streamlit as st
from dotenv import load_dotenv

from src.agent_factory import build_user_task, create_prompt_agent
from src.prompt_loader import agents_for_category, categories, load_prompt_agents
from src.sample_inputs import SAMPLE_INPUTS


load_dotenv()

APP_ROOT = Path(__file__).parent
PROMPTS_DIR = APP_ROOT / "prompts"


def init_state() -> None:
    defaults = {
        "result": "",
        "last_agent": "",
        "last_input": "",
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def render_sidebar():
    st.sidebar.header("🔌 Local LLM Endpoint")

    base_url = st.sidebar.text_input(
        "OpenAI-Compatible Base URL",
        value=os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1"),
        help="Examples: LM Studio http://localhost:1234/v1, vLLM http://localhost:8000/v1, Ollama http://localhost:11434/v1",
    )

    api_key = st.sidebar.text_input(
        "API Key",
        value=os.getenv("OPENAI_API_KEY", "local-demo-key"),
        type="password",
        help="Many local endpoints accept any non-empty value.",
    )

    model_id = st.sidebar.text_input(
        "Model ID",
        value=os.getenv("OPENAI_MODEL", "local-model"),
        help="Use the model name exposed by your local server.",
    )

    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.5,
        value=0.2,
        step=0.1,
    )

    debug_mode = st.sidebar.toggle("Agno debug mode", value=False)

    st.sidebar.divider()
    st.sidebar.caption("Common local endpoints:")
    st.sidebar.code(
        "LM Studio: http://localhost:1234/v1\n"
        "vLLM:      http://localhost:8000/v1\n"
        "Ollama:    http://localhost:11434/v1",
        language="text",
    )

    return base_url, api_key, model_id, temperature, debug_mode


def main() -> None:
    init_state()

    st.set_page_config(
        page_title=os.getenv("APP_TITLE", "Agentic Prompts Local Demo"),
        page_icon="🤖",
        layout="wide",
    )

    st.title("🤖 Agentic Prompts Local Demo")
    st.caption("Run your curated prompt-agents against a local OpenAI-compatible endpoint.")

    base_url, api_key, model_id, temperature, debug_mode = render_sidebar()

    all_agents = load_prompt_agents(PROMPTS_DIR)

    if not all_agents:
        st.error("No prompt files found in the prompts/ directory.")
        return

    category_list = categories(all_agents)

    left, right = st.columns([0.32, 0.68], gap="large")

    with left:
        st.subheader("🧠 Select Agent")

        selected_category = st.selectbox(
            "Category",
            options=category_list,
            index=0,
        )

        category_agents = agents_for_category(all_agents, selected_category)
        selected_title = st.selectbox(
            "Prompt Agent",
            options=[agent.title for agent in category_agents],
        )

        selected_agent = next(agent for agent in category_agents if agent.title == selected_title)

        with st.expander("Preview selected prompt", expanded=False):
            st.caption(str(selected_agent.path.relative_to(APP_ROOT)))
            st.markdown(selected_agent.content)

        st.info(
            f"Loaded **{len(all_agents)}** prompt agents from `{PROMPTS_DIR.name}/`."
        )

    with right:
        st.subheader("📥 Task Input")

        default_sample = SAMPLE_INPUTS.get(selected_category, "Paste your task, code, logs, architecture, or requirement here.")

        user_input = st.text_area(
            "What should this agent work on?",
            value=default_sample,
            height=240,
        )

        extra_context = st.text_area(
            "Additional context, code, logs, or constraints",
            value="",
            height=160,
            placeholder="Optional: paste code snippets, logs, stack traces, PR notes, architecture details, etc.",
        )

        uploaded_files = st.file_uploader(
            "Optional: upload text/code files",
            accept_multiple_files=True,
            type=None,
        )

        uploaded_context_parts = []
        for uploaded_file in uploaded_files:
            try:
                content = uploaded_file.read().decode("utf-8", errors="replace")
                uploaded_context_parts.append(
                    f"## Uploaded File: {uploaded_file.name}\n\n```text\n{content}\n```"
                )
            except Exception as exc:
                uploaded_context_parts.append(
                    f"## Uploaded File: {uploaded_file.name}\n\nCould not read file: {exc}"
                )

        combined_extra_context = "\n\n".join(
            part for part in [extra_context, *uploaded_context_parts] if part
        )

        col_run, col_clear = st.columns([0.22, 0.78])

        with col_run:
            run_clicked = st.button("🚀 Run Agent", type="primary")

        with col_clear:
            if st.button("🧹 Clear Result"):
                st.session_state.result = ""
                st.session_state.last_agent = ""
                st.session_state.last_input = ""
                st.rerun()

        if run_clicked:
            if not base_url.strip():
                st.error("Please provide a local OpenAI-compatible base URL.")
                return

            if not model_id.strip():
                st.error("Please provide a model ID.")
                return

            if not user_input.strip():
                st.error("Please provide a task input.")
                return

            with st.spinner(f"Running {selected_agent.title} using {model_id}..."):
                try:
                    agent = create_prompt_agent(
                        name=selected_agent.title,
                        role=f"{selected_agent.category} specialist",
                        prompt_body=selected_agent.prompt_body,
                        model_id=model_id.strip(),
                        base_url=base_url.strip(),
                        api_key=api_key.strip(),
                        temperature=temperature,
                        debug_mode=debug_mode,
                    )

                    task = build_user_task(
                        user_input=user_input,
                        extra_context=combined_extra_context,
                    )

                    response = agent.run(task)
                    content = getattr(response, "content", response)

                    st.session_state.result = str(content)
                    st.session_state.last_agent = selected_agent.title
                    st.session_state.last_input = user_input

                except Exception as exc:
                    st.error(f"Agent execution failed: {exc}")
                    with st.expander("Debug traceback"):
                        st.code(traceback.format_exc(), language="text")

    if st.session_state.result:
        st.divider()
        st.subheader(f"📋 Result: {st.session_state.last_agent}")
        st.markdown(st.session_state.result)

        download_name = (
            f"{st.session_state.last_agent.lower().replace(' ', '-')}-"
            f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        )

        st.download_button(
            label="⬇️ Download Result as Markdown",
            data=st.session_state.result,
            file_name=download_name,
            mime="text/markdown",
        )


if __name__ == "__main__":
    main()
