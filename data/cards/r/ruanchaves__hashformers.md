# ruanchaves/hashformers

⭐ 78 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/ruanchaves/hashformers) · 个人维护

**给 NLP 开发者：Transformer+beam search 的本地标签/标识符分词库**

使用 Hugging Face 语言模型与 beam search 对无空格文本（hashtag、标识符）做词切分，支持多语言、可选 reranker 与 RRF 集成融合。以 Python 库、spaCy 组件、本地 MCP server 与 Agent Skill 四种形式提供，可接入 Codex/Claude Code 做 agent 驱动的大文件批量切分（可断点续跑）。要求 Python 3.10+、Transformers 4.46.1–5.x；README 提及在单张 NVIDIA T4 上达 14.1 hashtags/秒。对简单领域建议用 CPU 启发式，对最高精度需求建议托管 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transformer beam search 分词，支持 Hugging Face Model Hub 模型
- 可选 reranker 与 RRF 集成融合（可自定义权重与 damping）
- 提供 MCP server 与 Agent Skill，支持 agent 驱动的可续跑批量文件处理
- spaCy pipeline 组件形式集成

## 适用场景

- 多语言社媒 hashtag 批量切分后再做情感/滥用语言分析
- 代码标识符或无空格文本的词级切分
- 让 Codex/Claude Code 通过 MCP 直接切分项目内 CSV/JSONL 文件

## 场景标签

 · 领域:自然语言处理

## 证据(README 行号)

> L10: **Fast, local, multilingual hashtag and identifier segmentation using
> L37: Hashformers uses language models and a beam search algorithm to segment text

## 星数曲线

```mermaid
xychart-beta
    title "ruanchaves/hashformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `546ef0181794` · [字段定义](../../DATASET.md)*
