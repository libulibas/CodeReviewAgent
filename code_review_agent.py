import os, sys
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-4-20250514"

def claude(prompt, system="", max_tokens=2000):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY (copy .env.example to .env).")
    c = Anthropic(api_key=key)
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system:
        kw["system"] = system
    r = c.messages.create(**kw)
    return "".join(b.text for b in r.content if b.type == "text")



def review(path: str) -> str:
    src = open(path, encoding="utf-8", errors="ignore").read()
    sys_p = ("You are a senior code reviewer. Return markdown with sections: "
             "## Summary, ## Bugs, ## Security, ## Style, ## Suggested Fixes. "
             "Reference line numbers where possible.")
    return claude(f"Review this file ({path}):\n\n```\n{src}\n```",
                  system=sys_p, max_tokens=3000)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python code_review_agent.py <file>")
    print(review(sys.argv[1]))
