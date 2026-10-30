# outsourc-e/qwen36-4090-recipes

⭐ 24 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/outsourc-e/qwen36-4090-recipes) · 个人维护

**在单卡 RTX 4090 上运行 Qwen3.6-27B 的可复现 llama.cpp 配置与质量基准**

面向本地 LLM 部署者的实验记录仓库：给出单张 RTX 4090 (24 GB) 运行 Qwen3.6-27B-Q4_K_M 的 llama.cpp 启动配置矩阵（投机解码、不同上下文长度与 KV 量化），并配 bench-split.py 按 6 类任务（列表/代码/JSON/推理/工具调用/长文）做每类质量校验，而非只报聚合 tok/s。关键发现：ik_llama.cpp 跨词表投机解码会静默破坏 JSON 与列表等结构化输出，修复路径是主线 llama.cpp + 同词表 Qwen3.5-4B draft。也记录了 vLLM/DFlash 等在 24 GB 上的失败配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐配置的速度/显存/6 类质量通过率结果矩阵
- bench-split.py 按任务类别输出 tps 与自动质量检查
- 记录跨词表投机解码静默破坏 JSON/列表输出的问题
- 收录 DFlash/vLLM/TurboQuant 等在 24 GB 显存上的失败配置

## 适用场景

- 在单张 RTX 4090 上选可用的 Qwen3.6-27B 推理配置
- 验证投机解码是否破坏结构化输出
- 复现或对比本机的每类别吞吐与质量结果

## 场景标签

`推理引擎` `模型量化` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Reproducible llama.cpp configs for **Qwen3.6-27B-Q4_K_M** on a single **RTX 4090 (24 GB)**, with **per-category qual
> L11: All numbers are RTX 4090, Qwen3.6-27B-Q4_K_M, benched with `bench/bench-split.py` — 6 task categories with automate

## 星数曲线

```mermaid
xychart-beta
    title "outsourc-e/qwen36-4090-recipes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `dfbfd42c4c92` · [字段定义](../../DATASET.md)*
