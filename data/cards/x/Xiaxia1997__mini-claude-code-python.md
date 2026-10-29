# Xiaxia1997/mini-claude-code-python

⭐ 25 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/Xiaxia1997/mini-claude-code-python) · 个人维护 · 中文 README

**给开发者：逐模块拆解并独立实现 Coding Agent 的 11 个核心机制**

教学向的 build-your-own-x 项目：不依赖 LangChain/LangGraph 等框架，用 Python 独立实现 Coding Agent 的 11 个核心模块（Agent Loop、Tool Use、Context Engineering、Sub-Agent 等），每个模块配套设计分析文档，并对比 Claude Code / Kimi Code / Codex 在各层的架构差异。代码使用 Anthropic Python SDK，通过 DeepSeek 的 Anthropic 兼容接口运行，无需购买 Claude API；API Key 经环境变量读取。共 11,000+ 行代码与 7,500+ 行文档，MCP 模块为计划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个模块独立可运行，配套设计分析文档
- 对比 Claude Code / Kimi Code / Codex 各层架构差异
- 通过 DeepSeek 的 Anthropic 兼容接口运行，无需 Claude API
- 13 个版本 tag，每个模块一个可回溯里程碑

## 适用场景

- 使用 Claude Code/Cursor 的开发者想理解底层机制
- 从零搭建 Coding Agent 且不依赖框架抽象
- 准备 AI Agent 岗位面试，深入理解 Agent Loop/Tool Use/Context Engineering

## 场景标签

`教程课程` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **逐模块拆解 Coding Agent 核心机制，独立实现，逐层对比。**
> L20: 不依赖 LangChain / LangGraph 等框架，用 Python 独立实现 Coding Agent 的 11 个核心模块，每个模块配套设计分析文档：
> L29: 1. **生产级 Coding Agent 为什么需要这一层**：缺少它时，长任务会在哪里失效？

## 星数曲线

```mermaid
xychart-beta
    title "Xiaxia1997/mini-claude-code-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `66577ec607fd` · [字段定义](../../DATASET.md)*
