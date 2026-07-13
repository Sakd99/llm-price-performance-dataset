# -*- coding: utf-8 -*-
"""Build ai-models.csv and price-performance.csv from ai-models.json, and re-emit clean JSON."""
import json, csv

with open("ai-models.json", encoding="utf-8") as f:
    models = json.load(f)

FIELDS = ["name", "slug", "developer", "model_type", "modality", "parameters",
          "context_window", "max_output", "license", "open_weights", "release_date",
          "input_price", "output_price", "api_providers", "intelligence"]

# normalize: ensure all fields present
for m in models:
    for k in FIELDS:
        m.setdefault(k, "")

models.sort(key=lambda m: m["name"].lower())

# re-emit clean, pretty JSON
with open("ai-models.json", "w", encoding="utf-8") as f:
    json.dump(models, f, indent=2, ensure_ascii=False)

# full CSV
with open("ai-models.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for m in models:
        w.writerow({k: m.get(k, "") for k in FIELDS})

# derived price/performance table (models that have both a price and an intelligence score)
def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None

pp = []
for m in models:
    ip, op, intel = num(m["input_price"]), num(m["output_price"]), num(m["intelligence"])
    if ip is None or op is None or intel is None or intel <= 0:
        continue
    blended = round(ip * 0.5 + op * 0.5, 3)          # simple 50/50 input:output blend, USD / 1M tokens
    ipd = round(intel / blended, 1) if blended > 0 else None   # intelligence per dollar
    pp.append({
        "name": m["name"], "developer": m["developer"], "open_weights": m["open_weights"],
        "intelligence": intel, "input_price_usd_per_1m": ip, "output_price_usd_per_1m": op,
        "blended_price_usd_per_1m": blended, "intelligence_per_dollar": ipd,
    })

pp.sort(key=lambda r: r["intelligence_per_dollar"], reverse=True)  # best value first

with open("price-performance.csv", "w", newline="", encoding="utf-8") as f:
    cols = ["rank", "name", "developer", "open_weights", "intelligence",
            "input_price_usd_per_1m", "output_price_usd_per_1m",
            "blended_price_usd_per_1m", "intelligence_per_dollar"]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for i, r in enumerate(pp, 1):
        r["rank"] = i
        w.writerow(r)

# report the spread (the "114x" headline)
vals = [r["intelligence_per_dollar"] for r in pp if r["intelligence_per_dollar"]]
if vals:
    spread = round(max(vals) / min(vals), 1)
    print("models:", len(models), "| price-perf rows:", len(pp),
          "| value spread (best/worst intelligence-per-$):", str(spread) + "x")
    print("best value:", pp[0]["name"], "(", pp[0]["intelligence_per_dollar"], "intel/$ )")
    print("worst value:", pp[-1]["name"], "(", pp[-1]["intelligence_per_dollar"], "intel/$ )")
