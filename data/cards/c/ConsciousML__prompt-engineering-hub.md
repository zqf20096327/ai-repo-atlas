# ConsciousML/prompt-engineering-hub

⭐ 27 · Shell · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/ConsciousML/prompt-engineering-hub) · 组织维护

**提示词集合与生成器：帮用户为各 LLM 创建优化提示词**

提示词工程资源库，包含两部分：Prompt Generator 助手（遵循 Anthropic、OpenAI、Gemini 的提示词工程实践生成优化提示词）与现成提示词集合（分为对话用 assistants 和供 Claude Code 等工具自主使用的 agents，含 Mermaid 图表设计、README 撰写等条目，状态分 Stable/Beta/Experimental）。提示词以 system.xml、user_facing_prompts 等文件组织，可复制到 LLM 网页界面或 API 使用。基于 Claude 优化，用于其他平台可能需小幅调整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Prompt Generator 按链式思考、提示词链、XML 格式等技巧生成优化提示词
- 现成提示词分 assistants（对话）与 agents（Claude Code 子代理）两类
- 提示词遵循 Anthropic/OpenAI/Gemini 的提示词工程实践
- 提供迭代式高级提示词生成指南

## 适用场景

- 为 LLM 网页界面或 Claude Code 搭建自定义助手或子代理
- 直接复用现成提示词完成图表设计、README 撰写等任务
- 学习提示词工程示例并贡献自己的提示词

## 场景标签

`提示工程` `精选清单` · 领域:Agent 开发

## 证据(README 行号)

> L13: ### The Prompt Generator
> L16: ### Ready-Made Prompts
> L17: A collection of prompts for a variety of tasks, including both **assistants** (for conversational use in LLM web in

## 星数曲线

```mermaid
xychart-beta
    title "ConsciousML/prompt-engineering-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `96e1cb9d2701` · [字段定义](../../DATASET.md)*
