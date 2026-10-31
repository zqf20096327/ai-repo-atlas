# Moshe-ship/artok

⭐ 14 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/Moshe-ship/artok) · [官网](https://moshe-ship.github.io/artok/) · 个人维护

**阿拉伯语 Token 税计算器：对比 18 种 LLM 分词器的成本差异**

Python CLI 工具，面向构建阿拉伯语 AI 产品的开发者：对同一段文本在 18 种 LLM 分词器（10 家提供商）上计数 token，量化阿拉伯语相对英语 2-5 倍的 token 开销并折算成本。后端使用 tiktoken、transformers 与 tokenizer.json 直接加载。支持阿拉伯语友好度基准评分（0-100）、方言对比、变音符号膨胀分析、批处理 JSONL/CSV、图表与 SVG 导出；价格数据从 GitHub 拉取并带 24 小时缓存，离线时回退内置默认值。需 Python 3.9+，从源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 种分词器（10 家提供商）的 token 计数与成本估算
- 阿拉伯语友好度基准评分 0-100 与排行榜
- 方言对比（MSA/埃及/海湾/黎凡特/摩洛哥）与变音符号膨胀分析
- 价格从 GitHub 自动更新，24h 缓存，离线回退内置默认

## 适用场景

- 估算阿拉伯语产品在不同模型上的 token 成本
- 按预算挑选阿拉伯语更友好的分词器/模型
- 对比切换提供商可节省的开销
- 批量分析 JSONL/CSV 文件的阿拉伯语 token 开销

## 场景标签

 · 领域:NLP/LLM 成本分析

## 证据(README 行号)

> L5: See how much more Arabic costs across **18 LLM tokenizers**.
> L45: ## Supported Tokenizers (18)
> L84: |`--recommend`|Best tokenizer for a budget|

## 星数曲线

```mermaid
xychart-beta
    title "Moshe-ship/artok 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5f375d180425` · [字段定义](../../DATASET.md)*
