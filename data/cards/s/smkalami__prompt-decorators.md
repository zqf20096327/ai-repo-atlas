# smkalami/prompt-decorators

⭐ 481 · MIT · 推送 2026-03-30 · [GitHub](https://github.com/smkalami/prompt-decorators) · 个人维护

**LLM 提示词装饰器框架：以 +++ 前缀声明式控制模型推理与输出**

受 Python 装饰器启发的提示工程框架：定义 +++Reasoning、+++StepByStep、+++Tone 等结构化前缀，分为认知生成类与表达系统类两大族，可组合、可设置作用域（消息级/会话级）并在对话中持久生效。使用方式面向终端用户：将定义文件 prompt-decorators.txt 粘贴进 ChatGPT、Gemini、Claude 或 Grok 的对话或系统指令后即可内联激活，无需改代码。另有 Agent Skill 封装版及 evo-search、tournament-search 等技能，附带 arXiv 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- +++ 前缀装饰器可组合、带参数与作用域控制
- 提供 prompt-decorators.txt 定义文件，粘贴即用于 ChatGPT/Gemini/Claude/Grok
- 提供 Agent Skill 版本接入 agent 流水线，含 evo-search 与 tournament-search 技能
- 附 arXiv 论文（arXiv:2510.19850）

## 适用场景

- 在 LLM 对话中用简短前缀控制推理方式、语气与输出格式
- 为 agent 工具集成可复用的提示控制技能
- 按论文了解装饰器的声明式组合语法

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L98: Detailed definitions for each decorator are provided in **`prompt-decorators.txt`**.
> L108: Prompt Decorators rely on the model’s memory of definitions.
> L190: **"Prompt Decorators: A Declarative and Composable Syntax for Reasoning, Formatting, and Control in LLMs"**

## 星数曲线

```mermaid
xychart-beta
    title "smkalami/prompt-decorators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 480 --> 482
    line [481, 481]
```

2026-10-18 481 → 2026-10-23 481（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ea04dfb11cda` · [字段定义](../../DATASET.md)*
