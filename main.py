"""Minimal LangChain chat-model smoke test (OpenAI + Anthropic)."""
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Optional Anthropic import — only if key present
claude_instant = None
if os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY"):
    try:
        from langchain_community.chat_models import ChatAnthropic
        claude_instant = ChatAnthropic(model="claude-instant-v1", temperature=0.7)
    except Exception as exc:
        print(f"Anthropic model not initialized: {exc}")

gpt4o = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=1000)

if __name__ == "__main__":
    print(gpt4o.invoke("Say hello in one short sentence.").content)
