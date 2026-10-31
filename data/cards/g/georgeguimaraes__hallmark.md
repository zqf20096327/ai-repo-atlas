# georgeguimaraes/hallmark

⭐ 19 · Elixir · MIT · 推送 2026-10-20 · [GitHub](https://github.com/georgeguimaraes/hallmark) · 个人维护

**Elixir 幻觉检测库：本地运行 HHEM 模型评估文本一致性**

面向 Elixir 开发者的幻觉检测库，封装 Vectara 的 HHEM（基于 FLAN-T5-base，184M 参数）模型。输入前提与假设文本，输出 0-1 的一致性分数，用于检验 LLM 生成文本是否忠实于源材料。模型通过 Bumblebee 本地运行，首次下载约 440MB 后无需外部调用或 API key。需搭配 EXLA/EMLX 编译器，否则纯 Elixir 求值器单次评分耗时 10 分钟以上。检测的是逻辑蕴含而非事实准确性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HHEM 模型本地运行，无需 API key 与外部调用
- 输出 0-1 幻觉一致性分数
- 支持 EXLA（CPU/CUDA）与 EMLX（Apple Silicon Metal）加速
- 以 Mix deps 形式安装，模型下载后缓存

## 适用场景

- 检测 LLM 生成回答是否忠实于检索到的源文档
- 在 Elixir 应用中构建 RAG 输出的幻觉过滤
- 批量评估生成文本与前提材料的一致性

## 场景标签

 · 领域:LLM 可靠性/NLP

## 证据(README 行号)

> L5: Hallucination detection for Elixir, powered by Vectara's HHEM (Hallucination Evaluation Model).
> L7: Given a premise and a hypothesis, Hallmark scores how consistent the hypothesis is with the premise on a scale from 
> L9: HHEM is a fine-tuned FLAN-T5-base (184M params) that runs locally via Bumblebee. No API keys, no external calls afte

## 星数曲线

```mermaid
xychart-beta
    title "georgeguimaraes/hallmark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d1d815014c19` · [字段定义](../../DATASET.md)*
