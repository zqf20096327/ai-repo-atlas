# structuredllm/syncode

⭐ 341 · Python · MIT · 推送 2026-01-19 · [GitHub](https://github.com/structuredllm/syncode) · [官网](https://structuredllm.com) · 组织维护

**面向开发者的 LLM 语法约束解码框架，保证输出符合给定文法**

SynCode 是一个上下文文法（CFG）引导的 LLM 生成框架，通过增量解析器与离线构建的 DFA mask store 对每步生成的 token 施加掩码，保证输出在语法上有效，并具有可靠性与完备性保证。内置 Python/Go/Java/SQL/JSON 等文法，也支持以 EBNF 语法定义自定义文法。以 pip 包、Python API（logits processor 或 SynCode 推理类）与 CLI 三种方式使用，依赖 HuggingFace transformers（不支持 Python 3.13）。适用于需要模型输出合法代码或结构化格式的开发者。

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

- 基于增量解析与 DFA mask store 的文法约束解码
- 内置 Python/Go/Java/SQL/JSON 等文法，支持 EBNF 自定义文法
- 可配合任意 HuggingFace 模型与既有解码策略（greedy/beam/采样）
- 提供 logits processor、推理类与 CLI 三种使用方式

## 适用场景

- 让 LLM 输出保证合法的 JSON 结构化数据
- 生成无缩进错误的 Python 代码补全
- 用自定义 EBNF 文法约束模型回复格式

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L13: * **SynCode** is a novel framework for the grammar-guided generation of Large Language Models (LLMs) that is scalab
> L33: |🤖 Seamlessly work with any HuggingFace Language Model, including Code, Chat, and Instruct models|
> L68: from syncode import SyncodeLogitsProcessor

## 星数曲线

```mermaid
xychart-beta
    title "structuredllm/syncode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 340 --> 342
    line [341, 341]
```

2026-10-18 341 → 2026-10-23 341（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a41f61ca8de3` · [字段定义](../../DATASET.md)*
