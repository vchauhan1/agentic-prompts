from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import re


@dataclass(frozen=True)
class PromptAgent:
    """Represents one Markdown prompt as a runnable agent."""

    title: str
    category: str
    path: Path
    content: str
    prompt_body: str


def _extract_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback.replace("-", " ").replace("_", " ").title()


def _extract_prompt_body(markdown: str) -> str:
    """Extract content after the '## Prompt' heading, falling back to full content."""
    match = re.search(r"^##\s+Prompt\s*$", markdown, flags=re.MULTILINE | re.IGNORECASE)
    if not match:
        return markdown.strip()

    body = markdown[match.end():].strip()
    return body or markdown.strip()


def load_prompt_agents(prompts_dir: Path) -> list[PromptAgent]:
    """Load all Markdown prompt files from a prompts directory."""
    if not prompts_dir.exists():
        return []

    agents: list[PromptAgent] = []

    for md_file in sorted(prompts_dir.rglob("*.md")):
        category = md_file.parent.relative_to(prompts_dir).as_posix()
        content = md_file.read_text(encoding="utf-8")
        title = _extract_title(content, md_file.stem)
        prompt_body = _extract_prompt_body(content)

        agents.append(
            PromptAgent(
                title=title,
                category=category,
                path=md_file,
                content=content,
                prompt_body=prompt_body,
            )
        )

    return agents


def categories(agents: Iterable[PromptAgent]) -> list[str]:
    return sorted({agent.category for agent in agents})


def agents_for_category(agents: Iterable[PromptAgent], category: str) -> list[PromptAgent]:
    return [agent for agent in agents if agent.category == category]
