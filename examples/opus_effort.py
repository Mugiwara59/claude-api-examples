import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Effort parameter — GA, no beta header needed
response = client.messages.create(
    model="claude-opus-4-6-20250205",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Analyze trade-offs..."}],
    output_config={"effort": "medium"}  # "low", "medium", "high", "max" (Opus 4.6 only)
)

# Adaptive thinking — Opus 4.6 exclusive
response = client.messages.create(
    model="claude-opus-4-6-20250205",
    max_tokens=16384,
    messages=[{"role": "user", "content": "Design a distributed caching architecture"}],
    thinking={"type": "adaptive"}  # Auto-calibrates thinking depth
)
