# -*- coding: utf-8 -*-
"""把 state/s8_cards 剥到公开边界:去 raw_verdicts(内部裁决)与 trust.xcheck。

导出与断点续跑均不依赖这两项(sha 索引独立于卡片内容),剥掉符合公开仓设计边界。
每次批跑后执行,幂等。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "state" / "s8_cards"

n = stripped = 0
for f in CARDS.glob("*/*.json"):
    c = json.loads(f.read_text(encoding="utf-8"))
    n += 1
    if "raw_verdicts" in c or "xcheck" in (c.get("trust") or {}):
        c.pop("raw_verdicts", None)
        (c.get("trust") or {}).pop("xcheck", None)
        tmp = f.with_suffix(".tmp")
        tmp.write_text(json.dumps(c, ensure_ascii=False), encoding="utf-8")
        tmp.replace(f)
        stripped += 1
print(f"strip: {n} 卡,剥离 {stripped} 张的内部字段")
sys.exit(0)
