# CodeReviewAgent

Reviews a code file for bugs, style issues, and security vulnerabilities.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
```

## Usage

```bash
python code_review_agent.py path/to/file.py
```

## Model

`claude-sonnet-4-20250514` via the Anthropic Python SDK.

## License

MIT
