# tolitius/cupel

⭐ 64 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/tolitius/cupel) · [官网](https://cupel.run) · 个人维护

**本地与云端 LLM 评分排行榜工具，带可配置裁判模型**

面向开发者的 LLM 评测工具：用自定义 prompt 对本地与云端模型采集回答，由可配置的裁判模型按 0–3 评分标准打分并给出理由，生成评分与速度（tok/s）的排行榜和各类别雷达图。支持多轮对话与工具调用评测、thinking 模型自动分离 think 块、按已知端口自动发现本地推理服务器（oMLX/Ollama/LM Studio/SGLang/llama.cpp）。提供浏览器 UI 与 CLI，首次启动附带示例数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可配置裁判模型，0–3 评分标准含裁判理由
- 支持本地（oMLX/Ollama/LM Studio/SGLang/llama.cpp）与云端（Anthropic/OpenRouter/OpenAI）模型
- LLM 辅助起草测试 prompt 与评分标准
- 自动发现本地推理服务器，结果保存为 JSON 可排序、打标签

## 适用场景

- 对比多个本地或云端模型在我的自定义任务上的表现
- 生成评分与速度对比的模型排行榜
- 为多轮对话和工具调用场景做模型评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: score local and cloud LLMs with custom prompts and a configurable judge
> L37: - **local + cloud** — oMLX, Ollama, LM Studio, SGLang, OpenRouter, Anthropic, OpenAI
> L125: cloud providers can be added from presets (Anthropic, OpenRouter, OpenAI) or as custom endpoints. the settings pag

## 星数曲线

```mermaid
xychart-beta
    title "tolitius/cupel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-29 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bc6a5952e914` · [字段定义](../../DATASET.md)*
