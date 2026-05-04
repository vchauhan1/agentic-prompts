from __future__ import annotations

from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat


def create_prompt_agent(
    *,
    name: str,
    role: str,
    prompt_body: str,
    model_id: str,
    base_url: str,
    api_key: str,
    temperature: float = 0.2,
    debug_mode: bool = False,
) -> Agent:
    """
    Create an Agno Agent backed by a local OpenAI-compatible endpoint.

    Notes:
    - LM Studio usually runs on http://localhost:1234/v1
    - vLLM usually runs on http://localhost:8000/v1
    - Ollama OpenAI compatibility usually runs on http://localhost:11434/v1
    """

    safe_api_key = api_key.strip() or "local-demo-key"

    model = OpenAIChat(
        id=model_id,
        api_key=safe_api_key,
        base_url=base_url,
        temperature=temperature,
    )

    return Agent(
        name=name,
        role=role,
        model=model,
        description=dedent(
            f"""
            You are running as a specialized AI agent selected from a curated engineering prompt catalog.

            Use the following agent prompt as your primary operating instructions:

            {prompt_body}
            """
        ).strip(),
        instructions=[
            "Follow the selected prompt instructions carefully.",
            "Return a clear, structured Markdown response.",
            "State assumptions explicitly.",
            "Do not claim that tests, commands, or repository checks were run unless the user provided evidence or tool output.",
            "If the user input is incomplete, make reasonable assumptions and clearly label them.",
            "For code, prefer production-ready, maintainable, secure, and testable output.",
        ],
        markdown=True,
        debug_mode=debug_mode,
    )


def build_user_task(*, user_input: str, extra_context: Optional[str] = None) -> str:
    extra = extra_context.strip() if extra_context else ""
    return dedent(
        f"""
        ## User Task

        {user_input.strip()}

        {"## Additional Context\\n\\n" + extra if extra else ""}

        ## Response Requirements

        - Use the selected agent behavior.
        - Produce a practical engineering response.
        - Use Markdown headings, tables, and checklists where useful.
        - Include code blocks when code is needed.
        - Be clear about assumptions, limitations, and validation steps.
        """
    ).strip()
