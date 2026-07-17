# LLM Price / Performance Dataset (2026)

An open, hand-verified dataset of **30+ AI models (LLMs)** — specs, API pricing (USD per 1M tokens), licenses, context windows, and a composite **intelligence score** — plus a derived **price/performance** ranking.

Maintained by **[Convly](https://convly.ai)** and updated as new models ship.

---

## 💡 Why this exists

Choosing an AI model means juggling scattered specs, prices, and benchmarks across a dozen tabs. This puts the essentials in one machine-readable place.

A headline finding from this data: **intelligence-per-dollar varies ~62× across the scored models.** DeepSeek V4-Flash delivers about **192 intelligence-points per dollar** versus roughly **3** for the priciest frontier tier (GPT-5.5) — see [`price-performance.csv`](price-performance.csv). Open-weight models like DeepSeek V4-Flash and GLM 5.2 give a large fraction of frontier intelligence at a fraction of the price. Our broader cost-per-intelligence study (more models, cost weighted differently) puts the full spread at ~114×: **https://convly.ai/ai-price-performance-index-2026/**

**Update — July 2026:** the highest-scoring model in this dataset is now itself **open-weight**. Moonshot's **Kimi K3** (2.8T parameters, 16 of 896 experts active) scores **57**, edging past Claude Opus 4.8 (55.7) — while costing $3/$15 per 1M tokens against Opus's $5/$25, i.e. **~1.7× more intelligence per dollar**. It is not the value leader, though: GLM 5.2 still returns ~2.8× more capability per dollar than K3, and DeepSeek V4-Flash ~30× more. Background: [Kimi K3 explained](https://convly.ai/kimi-k3-explained-2026/).

## 📁 Files

| file | what it is |
|------|------------|
| [`ai-models.json`](ai-models.json) | Full dataset, one object per model |
| [`ai-models.csv`](ai-models.csv) | Same data as CSV (pandas/Excel-friendly) |
| [`price-performance.csv`](price-performance.csv) | Derived: blended price, intelligence, and **intelligence-per-dollar**, ranked best-value first |
| [`build_dataset.py`](build_dataset.py) | Regenerates the CSVs from the JSON |

## 🧾 Columns

| column | meaning |
|--------|---------|
| `name`, `slug` | model name and URL slug |
| `developer` | who built it (OpenAI, Anthropic, DeepSeek, Alibaba, Meta, Google, …) |
| `model_type` | dense / MoE / reasoning / multimodal |
| `modality` | input → output modalities |
| `parameters` | total / active params (MoE noted) |
| `context_window`, `max_output` | token limits |
| `license`, `open_weights` | license and whether weights are open (`yes`/`no`) |
| `release_date` | ship date |
| `input_price`, `output_price` | API price, **USD per 1M tokens** |
| `api_providers` | where you can call it |
| `intelligence` | composite 0–100 benchmark score (empty = not yet scored) |

## 🛠️ Interactive tools built on this data

- 🏆 **LLM Leaderboard** — rank models by intelligence, price & context: https://convly.ai/llm-leaderboard/
- 📊 **AI Models Database** — full spec sheets: https://convly.ai/models/
- 💸 **AI API Cost Calculator** — what each model costs you per month: https://convly.ai/ai-api-cost-calculator/
- 🎮 **LLM VRAM Calculator** — can your GPU run it locally: https://convly.ai/llm-vram-calculator/
- ⚖️ **Self-Hosting vs API** break-even: https://convly.ai/self-hosting-vs-api-calculator/

## 🔄 Regenerate the CSVs

```bash
python build_dataset.py
```

## 🤝 Contributing

Spotted an error, a stale price, or a missing model? **Open an issue or a pull request** — corrections welcome.

## 📜 License

**CC-BY-4.0.** Free to use, share, and adapt — including commercially — with attribution to **Convly (https://convly.ai)**. See [`LICENSE`](LICENSE).

## ⚠️ Disclaimer

Prices, specs, and availability change frequently. Intelligence scores are a composite of public benchmarks and are estimates. Verify anything important against the provider before relying on it.
