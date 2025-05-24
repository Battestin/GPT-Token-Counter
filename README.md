# GPT Token Counter

Simple script to estimate token count and cost of prompts for OpenAI models GPT-3.5-Turbo and GPT-4.

## ⚙️ What it Does

- Uses `tiktoken` to tokenize a sample prompt
- Calculates the number of tokens used
- Estimates cost based on official OpenAI pricing

## 💸 Cost Reference (as of 2024)

| Model          | Price per 1K tokens |
|----------------|---------------------|
| GPT-3.5-Turbo  | $0.002              |
| GPT-4          | $0.03               |

> GPT-4 is 15x more expensive per token than GPT-3.5-Turbo.

## 🧪 Example Output

```
Tokens list: [40, 389, 257, 1722, 23974, 13]
Number of tokens: 6
For the model gpt-3.5-turbo it costs $0.000012
...
```

## 📝 Notes

- Prompt is hardcoded, but can be replaced with dynamic input  
- Useful for budgeting token consumption before API calls

## 📄 License

MIT
