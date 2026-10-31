# BerriAI/litespeed

⭐ 29 · TypeScript · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/BerriAI/litespeed) · 组织维护

**本地多模型协作编程 agent，覆盖终端、Mac 桌面与浏览器**

Litespeed 是运行在本地的 coding agent，提供终端 CLI、Apple silicon Mac 桌面应用和浏览器界面（localhost:3210），三者共享会话与模型设置。核心机制是多模型工作流：单模型、Sidekick Fusion（强模型规划+廉价模型执行）、Team Fusion（并行 workers）、Expert Fusion、实验性 LiteFusion 等，由强模型规划、便宜模型处理常规任务。模型接入通过 LiteLLM、OpenAI 兼容 API、原生 Anthropic 或 ChatGPT 设备登录；项目文件留在本机，提示词发送至所选 provider。支持 MCP、Claude/Codex 技能导入、权限控制与上下文压缩。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种多模型编排模式（单模型/Sidekick/Team/Expert/LiteFusion）
- 终端、Mac 桌面应用、浏览器三客户端共享会话
- 通过 LiteLLM、OpenAI 兼容 API、原生 Anthropic、ChatGPT 设备登录接入模型
- 可导入 Claude Code / Codex 技能，支持 MCP 连接

## 适用场景

- 在终端或桌面用多模型组合完成编码任务
- 用便宜模型做常规工作、强模型做规划以降低成本
- 在浏览器中继续管理本地项目的 agent 会话

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A local coding agent for your Mac, terminal, and browser, built around **multi-model workflows**. Use one model or c
> L38: 1. On your first launch, connect your **LiteLLM gateway base URL** and **API key**, then review your ready-to-use *

## 星数曲线

```mermaid
xychart-beta
    title "BerriAI/litespeed 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a14c1ebca40b` · [字段定义](../../DATASET.md)*
